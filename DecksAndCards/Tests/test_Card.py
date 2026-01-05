import unittest
import sys
import os

# Add project root directory to path to import from DecksAndCards package
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from DecksAndCards.Card import Card, Suits, Values

def get_suit_name(suit):
    """Helper function to get suit name, handling both nested and non-nested tuple formats"""
    suit_data = suit.value[0] if isinstance(suit.value[0], tuple) else suit.value
    return suit_data[1]

class TestCard(unittest.TestCase):
    
    def test_short_print_ace_of_hearts(self):
        """Test short_print for Ace of Hearts"""
        card = Card(Values.ACE, Suits.HEARTS)
        self.assertEqual(card.short_print(), "AH")
    
    def test_full_print_ace_of_hearts(self):
        """Test full_print for Ace of Hearts"""
        card = Card(Values.ACE, Suits.HEARTS)
        self.assertEqual(card.full_print(), "Ace of Hearts")
    
    def test_short_print_ten_of_diamonds(self):
        """Test short_print for Ten of Diamonds"""
        card = Card(Values.TEN, Suits.DIAMONDS)
        self.assertEqual(card.short_print(), "10D")
    
    def test_full_print_ten_of_diamonds(self):
        """Test full_print for Ten of Diamonds"""
        card = Card(Values.TEN, Suits.DIAMONDS)
        self.assertEqual(card.full_print(), "Ten of Diamonds")
    
    def test_short_print_all_suits(self):
        """Test short_print for all suits with Ace"""
        expected = {
            Suits.HEARTS: "AH",
            Suits.DIAMONDS: "AD",
            Suits.CLUBS: "AC",
            Suits.SPADES: "AS"
        }
        for suit, expected_output in expected.items():
            card = Card(Values.ACE, suit)
            self.assertEqual(card.short_print(), expected_output, 
                           f"Failed for Ace of {get_suit_name(suit)}")
    
    def test_full_print_all_suits(self):
        """Test full_print for all suits with Ace"""
        expected = {
            Suits.HEARTS: "Ace of Hearts",
            Suits.DIAMONDS: "Ace of Diamonds",
            Suits.CLUBS: "Ace of Clubs",
            Suits.SPADES: "Ace of Spades"
        }
        for suit, expected_output in expected.items():
            card = Card(Values.ACE, suit)
            self.assertEqual(card.full_print(), expected_output,
                           f"Failed for Ace of {get_suit_name(suit)}")
    
    def test_short_print_face_cards(self):
        """Test short_print for face cards"""
        test_cases = [
            (Values.JACK, Suits.HEARTS, "JH"),
            (Values.QUEEN, Suits.DIAMONDS, "QD"),
            (Values.KING, Suits.CLUBS, "KC"),
        ]
        for value, suit, expected in test_cases:
            card = Card(value, suit)
            self.assertEqual(card.short_print(), expected,
                           f"Failed for {value.value[1]} of {get_suit_name(suit)}")
    
    def test_full_print_face_cards(self):
        """Test full_print for face cards"""
        test_cases = [
            (Values.JACK, Suits.HEARTS, "Jack of Hearts"),
            (Values.QUEEN, Suits.DIAMONDS, "Queen of Diamonds"),
            (Values.KING, Suits.CLUBS, "King of Clubs"),
        ]
        for value, suit, expected in test_cases:
            card = Card(value, suit)
            self.assertEqual(card.full_print(), expected,
                           f"Failed for {value.value[1]} of {get_suit_name(suit)}")
    
    def test_short_print_number_cards(self):
        """Test short_print for number cards (2-10)"""
        test_cases = [
            (Values.TWO, Suits.HEARTS, "2H"),
            (Values.FIVE, Suits.DIAMONDS, "5D"),
            (Values.NINE, Suits.CLUBS, "9C"),
            (Values.TEN, Suits.SPADES, "10S"),
        ]
        for value, suit, expected in test_cases:
            card = Card(value, suit)
            self.assertEqual(card.short_print(), expected,
                           f"Failed for {value.value[1]} of {get_suit_name(suit)}")

if __name__ == '__main__':
    unittest.main()

