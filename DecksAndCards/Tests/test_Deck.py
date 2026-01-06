import unittest
import sys
import os

# Add project root directory to path to import from DecksAndCards package
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from DecksAndCards.Deck import Deck
from DecksAndCards.Card import Card, Suits, Values

class TestDeck(unittest.TestCase):
    
    def test_default_deck_has_one_of_each_suit_value_pair(self):
        """Test that default deck construction creates exactly one copy of each suit-value pair"""
        deck = Deck()
        
        # Calculate expected number of cards
        expected_count = len(Suits) * len(Values)
        self.assertEqual(len(deck.cards), expected_count, 
                        f"Deck should have {expected_count} cards (one for each suit-value pair)")
        
        # Count occurrences of each suit-value combination
        card_counts = {}
        for card in deck.cards:
            key = (card.suit, card.value)
            card_counts[key] = card_counts.get(key, 0) + 1
        
        # Verify each combination appears exactly once
        for suit in Suits:
            for value in Values:
                key = (suit, value)
                self.assertEqual(card_counts.get(key, 0), 1,
                               f"Card with suit {suit} and value {value} should appear exactly once, "
                               f"but appears {card_counts.get(key, 0)} times")
    
    def test_draw_returns_card(self):
        """Test that draw() returns a list with one Card instance"""
        deck = Deck()
        initial_count = len(deck.cards)
        
        cards = deck.draw()
        self.assertEqual(len(cards), 1, "draw() should return a list with one Card instance")
        card = cards[0]
        
        # Verify it's a Card instance
        self.assertIsInstance(card, Card, "draw() should return a Card instance")
        # Verify the deck has one fewer card
        self.assertEqual(len(deck.cards), initial_count - 1,
                        "Deck should have one fewer card after drawing")
    
    def test_draw_removes_card_from_deck(self):
        """Test that draw() removes the card from the deck"""
        deck = Deck()
        initial_count = len(deck.cards)
        
        drawn_cards = deck.draw()
        
        # Verify we got a list with one card
        self.assertEqual(len(drawn_cards), 1,
                        "draw() should return a list with one card")
        drawn_card = drawn_cards[0]
        
        # Verify the card is no longer in the deck
        self.assertNotIn(drawn_card, deck.cards,
                        "Drawn card should not be in the deck anymore")
        # Verify deck size decreased
        self.assertEqual(len(deck.cards), initial_count - 1,
                        "Deck size should decrease by 1 after drawing")
    
    def test_draw_multiple_cards_in_sequence(self):
        """Test that we can draw multiple cards in a row"""
        deck = Deck()
        initial_count = len(deck.cards)
        num_draws = 5
        
        drawn_cards = deck.draw(num_draws)
        
        # Verify we got the expected number of cards
        self.assertEqual(len(drawn_cards), num_draws,
                        f"Should have drawn {num_draws} cards")
        
        # Verify all drawn cards are Card instances
        for card in drawn_cards:
            self.assertIsInstance(card, Card,
                                "Each drawn card should be a Card instance")
        
        # Verify deck size decreased by the number of draws
        self.assertEqual(len(deck.cards), initial_count - num_draws,
                        f"Deck should have {initial_count - num_draws} cards after {num_draws} draws")
        
        # Verify no drawn card is still in the deck
        for card in drawn_cards:
            self.assertNotIn(card, deck.cards,
                            "Drawn cards should not be in the deck")
        
        # Verify all drawn cards are unique (no duplicates)
        self.assertEqual(len(drawn_cards), len(set(drawn_cards)),
                        "All drawn cards should be unique")
    
    def test_draw_all_cards_from_deck(self):
        """Test that we can draw all cards from a full deck"""
        deck = Deck()
        expected_count = len(Suits) * len(Values)
        
        # Draw all cards at once
        drawn_cards = deck.draw(expected_count)
        
        # Verify we drew all cards
        self.assertEqual(len(drawn_cards), expected_count,
                        f"Should have drawn all {expected_count} cards")
        
        # Verify deck is now empty
        self.assertEqual(len(deck.cards), 0,
                        "Deck should be empty after drawing all cards")
        
        # Verify we have one of each suit-value combination
        card_counts = {}
        for card in drawn_cards:
            key = (card.suit, card.value)
            card_counts[key] = card_counts.get(key, 0) + 1
        
        # Verify each combination appears exactly once
        for suit in Suits:
            for value in Values:
                key = (suit, value)
                self.assertEqual(card_counts.get(key, 0), 1,
                               f"Card with suit {suit} and value {value} should appear exactly once")
    
    def test_draw_from_custom_deck(self):
        """Test drawing from a custom deck with specific cards"""
        custom_cards = [
            Card(Values.ACE, Suits.HEARTS),
            Card(Values.TWO, Suits.DIAMONDS),
            Card(Values.THREE, Suits.CLUBS)
        ]
        deck = Deck(cards=custom_cards.copy())
        
        # Draw all cards at once
        drawn_cards = deck.draw(len(custom_cards))
        
        # Verify we got all the cards we put in
        self.assertEqual(len(drawn_cards), len(custom_cards),
                        "Should have drawn all custom cards")
        
        # Verify the cards match (order may be reversed due to pop())
        self.assertEqual(set(drawn_cards), set(custom_cards),
                        "Drawn cards should match the custom cards")
        
        # Verify deck is now empty
        self.assertEqual(len(deck.cards), 0,
                        "Deck should be empty after drawing all cards")
    
    def test_shuffle_preserves_all_cards(self):
        """Test that shuffle() preserves all cards (no cards lost or added)"""
        deck = Deck()
        original_cards = deck.cards.copy()
        original_count = len(deck.cards)
        
        deck.shuffle()
        
        # Verify deck size is unchanged
        self.assertEqual(len(deck.cards), original_count,
                        "Shuffle should not change the number of cards")
        
        # Verify all original cards are still present
        for card in original_cards:
            self.assertIn(card, deck.cards,
                         "All original cards should still be in the deck after shuffling")
        
        # Verify no new cards were added (check by counting unique cards)
        original_set = set(original_cards)
        shuffled_set = set(deck.cards)
        self.assertEqual(original_set, shuffled_set,
                        "The set of cards should be identical before and after shuffling")
    
    def test_shuffle_preserves_deck_size(self):
        """Test that shuffle() preserves the deck size"""
        deck = Deck()
        original_count = len(deck.cards)
        
        deck.shuffle()
        
        self.assertEqual(len(deck.cards), original_count,
                        "Deck size should remain the same after shuffling")
    
    def test_shuffle_changes_order(self):
        """Test that shuffle() actually changes the order of cards"""
        deck = Deck()
        original_order = deck.cards.copy()
        
        # Try shuffling multiple times to account for randomness
        # (It's theoretically possible but extremely unlikely that shuffle produces the same order)
        order_changed = False
        for _ in range(10):  # Try up to 10 times
            deck.shuffle()
            if deck.cards != original_order:
                order_changed = True
                break
        
        self.assertTrue(order_changed,
                       "Shuffle should change the order of cards (tried 10 times)")
    
    def test_shuffle_modifies_in_place(self):
        """Test that shuffle() modifies the deck in place (doesn't return a new deck)"""
        deck = Deck()
        deck_id = id(deck.cards)  # Get the memory address of the cards list
        
        result = deck.shuffle()
        
        # Verify shuffle returns None (in-place operation)
        self.assertIsNone(result, "shuffle() should return None (modifies in place)")
        
        # Verify we're still working with the same list object
        self.assertEqual(id(deck.cards), deck_id,
                        "shuffle() should modify the deck in place, not create a new list")
    
    def test_shuffle_empty_deck(self):
        """Test that shuffle() handles an empty deck gracefully"""
        deck = Deck(cards=[])
        
        # Should not raise an error
        deck.shuffle()
        
        self.assertEqual(len(deck.cards), 0,
                        "Empty deck should remain empty after shuffling")
    
    def test_shuffle_single_card_deck(self):
        """Test that shuffle() handles a deck with a single card"""
        single_card = Card(Values.ACE, Suits.HEARTS)
        deck = Deck(cards=[single_card])
        
        deck.shuffle()
        
        # Deck should still have one card
        self.assertEqual(len(deck.cards), 1,
                        "Single card deck should still have one card after shuffling")
        
        # The card should still be the same card
        self.assertEqual(deck.cards[0], single_card,
                        "Single card should remain in the deck after shuffling")
    
    def test_shuffle_multiple_times(self):
        """Test that shuffle() can be called multiple times without issues"""
        deck = Deck()
        original_count = len(deck.cards)
        
        # Shuffle multiple times
        for _ in range(5):
            deck.shuffle()
            self.assertEqual(len(deck.cards), original_count,
                           "Deck size should remain constant through multiple shuffles")
        
        # Verify all cards are still present
        expected_count = len(Suits) * len(Values)
        self.assertEqual(len(deck.cards), expected_count,
                        "All cards should still be present after multiple shuffles")

if __name__ == '__main__':
    unittest.main()

