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
        """Test that draw() returns a Card instance"""
        deck = Deck()
        initial_count = len(deck.cards)
        
        card = deck.draw()
        
        # Verify it's a Card instance
        self.assertIsInstance(card, Card, "draw() should return a Card instance")
        # Verify the deck has one fewer card
        self.assertEqual(len(deck.cards), initial_count - 1,
                        "Deck should have one fewer card after drawing")
    
    def test_draw_removes_card_from_deck(self):
        """Test that draw() removes the card from the deck"""
        deck = Deck()
        initial_count = len(deck.cards)
        
        drawn_card = deck.draw()
        
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
        
        drawn_cards = []
        for _ in range(num_draws):
            card = deck.draw()
            drawn_cards.append(card)
        
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
        
        drawn_cards = []
        for _ in range(expected_count):
            card = deck.draw()
            drawn_cards.append(card)
        
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
        
        # Draw all cards
        drawn_cards = []
        while len(deck.cards) > 0:
            drawn_cards.append(deck.draw())
        
        # Verify we got all the cards we put in
        self.assertEqual(len(drawn_cards), len(custom_cards),
                        "Should have drawn all custom cards")
        
        # Verify the cards match (order may be reversed due to pop())
        self.assertEqual(set(drawn_cards), set(custom_cards),
                        "Drawn cards should match the custom cards")

if __name__ == '__main__':
    unittest.main()

