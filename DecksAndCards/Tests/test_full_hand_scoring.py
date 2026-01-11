import unittest
import sys
import os

# Add project root directory to path to import from DecksAndCards package
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from DecksAndCards.Card import Card, Suits, Values
from Cribbage import score_hand

def parse_card_string(card_str):
    """
    Parse a card string like '3C', 'KH', '10H', 'JC' into a Card object.
    
    Args:
        card_str: String like '3C' (Three of Clubs), 'KH' (King of Hearts), 
                  '10H' (Ten of Hearts), 'JC' (Jack of Clubs)
    
    Returns:
        Card object
    """
    # Handle 10 separately since it's two characters
    if card_str.startswith('10'):
        value_str = '10'
        suit_str = card_str[2]
    else:
        value_str = card_str[0]
        suit_str = card_str[1]
    
    # Map value string to Values enum
    value_map = {
        'A': Values.ACE,
        '2': Values.TWO,
        '3': Values.THREE,
        '4': Values.FOUR,
        '5': Values.FIVE,
        '6': Values.SIX,
        '7': Values.SEVEN,
        '8': Values.EIGHT,
        '9': Values.NINE,
        '10': Values.TEN,
        'J': Values.JACK,
        'Q': Values.QUEEN,
        'K': Values.KING
    }
    
    # Map suit string to Suits enum
    suit_map = {
        'H': Suits.HEARTS,
        'D': Suits.DIAMONDS,
        'C': Suits.CLUBS,
        'S': Suits.SPADES
    }
    
    return Card(value_map[value_str], suit_map[suit_str])

class TestFullHandScoring(unittest.TestCase):
    """
    Test cases for full hand scoring using score_hand function.
    These tests verify that all scoring components work together correctly.
    """
    
    def test_hand_1(self):
        """Hand: 3C 8D 2H KH, Cut: 4C, Expected: 7"""
        hand = [parse_card_string('3C'), parse_card_string('8D'), parse_card_string('2H'), parse_card_string('KH')]
        cut = parse_card_string('4C')
        score = score_hand(hand, cut)
        self.assertEqual(score, 7)
    
    def test_hand_2(self):
        """Hand: 4S 6D 4D 7C, Cut: 9S, Expected: 6"""
        hand = [parse_card_string('4S'), parse_card_string('6D'), parse_card_string('4D'), parse_card_string('7C')]
        cut = parse_card_string('9S')
        score = score_hand(hand, cut)
        self.assertEqual(score, 6)
    
    def test_hand_3(self):
        """Hand: 4S 6D 4D 7C, Cut: JC, Expected: 6"""
        hand = [parse_card_string('4S'), parse_card_string('6D'), parse_card_string('4D'), parse_card_string('7C')]
        cut = parse_card_string('JC')
        score = score_hand(hand, cut)
        self.assertEqual(score, 6)
    
    def test_hand_4(self):
        """Hand: 6H AC JH 7S, Cut: 6S, Expected: 2"""
        hand = [parse_card_string('6H'), parse_card_string('AC'), parse_card_string('JH'), parse_card_string('7S')]
        cut = parse_card_string('6S')
        score = score_hand(hand, cut)
        self.assertEqual(score, 2)
    
    def test_hand_5(self):
        """Hand: 6S AC JH 7S, Cut: 6H, Expected: 3"""
        hand = [parse_card_string('6S'), parse_card_string('AC'), parse_card_string('JH'), parse_card_string('7S')]
        cut = parse_card_string('6H')
        score = score_hand(hand, cut)
        self.assertEqual(score, 3)
    
    def test_hand_6(self):
        """Hand: 8D 8H 9S 10H, Cut: 4C, Expected: 8"""
        hand = [parse_card_string('8D'), parse_card_string('8H'), parse_card_string('9S'), parse_card_string('10H')]
        cut = parse_card_string('4C')
        score = score_hand(hand, cut)
        self.assertEqual(score, 8)
    
    def test_hand_7(self):
        """Hand: 8D 8H 9S 10H, Cut: 7H, Expected: 14"""
        hand = [parse_card_string('8D'), parse_card_string('8H'), parse_card_string('9S'), parse_card_string('10H')]
        cut = parse_card_string('7H')
        score = score_hand(hand, cut)
        self.assertEqual(score, 14)
    
    def test_hand_8(self):
        """Hand: 4C QC 2D 7D, Cut: 10S, Expected: 0"""
        hand = [parse_card_string('4C'), parse_card_string('QC'), parse_card_string('2D'), parse_card_string('7D')]
        cut = parse_card_string('10S')
        score = score_hand(hand, cut)
        self.assertEqual(score, 0)
    
    def test_hand_9(self):
        """Hand: 6H 7H 8H 9H, Cut: 10H, Expected: 14"""
        hand = [parse_card_string('6H'), parse_card_string('7H'), parse_card_string('8H'), parse_card_string('9H')]
        cut = parse_card_string('10H')
        score = score_hand(hand, cut)
        self.assertEqual(score, 14)
    
    def test_hand_10(self):
        """Hand: 6H 7H 8H 9H, Cut: 8D, Expected: 20"""
        hand = [parse_card_string('6H'), parse_card_string('7H'), parse_card_string('8H'), parse_card_string('9H')]
        cut = parse_card_string('8D')
        score = score_hand(hand, cut)
        self.assertEqual(score, 20)
    
    def test_hand_11(self):
        """Hand: 5H 5S 5D JC, Cut: 5C, Expected: 29"""
        hand = [parse_card_string('5H'), parse_card_string('5S'), parse_card_string('5D'), parse_card_string('JC')]
        cut = parse_card_string('5C')
        score = score_hand(hand, cut)
        self.assertEqual(score, 29)

if __name__ == '__main__':
    unittest.main()
