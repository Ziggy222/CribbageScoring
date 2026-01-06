import unittest
import sys
import os

# Add project root directory to path to import from DecksAndCards package
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from DecksAndCards.Card import Card, Suits, Values
from Cribbage import check_pairs, check_runs

class TestCribbage(unittest.TestCase):
    def test_score_pairs_one_pair(self):
        hand = [Card(Values.ACE, Suits.HEARTS), Card(Values.ACE, Suits.DIAMONDS)]
        cut = Card(Values.TEN, Suits.HEARTS)
        score = check_pairs(hand, cut, 0)
        self.assertEqual(score, 2)
    
    def test_check_pairs_no_pairs(self):
        """Test check_pairs with no pairs - cards = [AH, 2D, 3C, 4S]; expected result = 0"""
        hand = [
            Card(Values.ACE, Suits.HEARTS),
            Card(Values.TWO, Suits.DIAMONDS),
            Card(Values.THREE, Suits.CLUBS),
            Card(Values.FOUR, Suits.SPADES)
        ]
        cut = None
        score = check_pairs(hand, cut, 0)
        self.assertEqual(score, 0)
    
    def test_check_pairs_three_of_a_kind(self):
        """Test check_pairs with three of a kind - cards = [2D, 2C, 2S]; expected result = 6"""
        hand = [
            Card(Values.TWO, Suits.DIAMONDS),
            Card(Values.TWO, Suits.CLUBS),
            Card(Values.TWO, Suits.SPADES)
        ]
        cut = None
        score = check_pairs(hand, cut, 0)
        self.assertEqual(score, 6)
    
    def test_check_pairs_two_pairs(self):
        """Test check_pairs with two pairs - cards = [3H, 3S, 4S, 4C]; expected result = 4"""
        hand = [
            Card(Values.THREE, Suits.HEARTS),
            Card(Values.THREE, Suits.SPADES),
            Card(Values.FOUR, Suits.SPADES),
            Card(Values.FOUR, Suits.CLUBS)
        ]
        cut = None
        score = check_pairs(hand, cut, 0)
        self.assertEqual(score, 4)
    
    def test_check_pairs_three_of_a_kind_and_pair(self):
        """Test check_pairs with three of a kind and a pair - cards = [AH, AS, AC, 7H, 7D]; expected result = 8"""
        hand = [
            Card(Values.ACE, Suits.HEARTS),
            Card(Values.ACE, Suits.SPADES),
            Card(Values.ACE, Suits.CLUBS),
            Card(Values.SEVEN, Suits.HEARTS),
            Card(Values.SEVEN, Suits.DIAMONDS)
        ]
        cut = None
        score = check_pairs(hand, cut, 0)
        self.assertEqual(score, 8)
    
    def test_check_pairs_four_of_a_kind(self):
        """Test check_pairs with four of a kind - cards = [6D, 6S, 6C, 6H]; expected result = 12"""
        hand = [
            Card(Values.SIX, Suits.DIAMONDS),
            Card(Values.SIX, Suits.SPADES),
            Card(Values.SIX, Suits.CLUBS),
            Card(Values.SIX, Suits.HEARTS)
        ]
        cut = None
        score = check_pairs(hand, cut, 0)
        self.assertEqual(score, 12)
    
    def test_check_runs_run_of_three(self):
        """Test check_runs with a run of 3 - A, 2, 3, 7, 10 = 3 points"""
        hand = [
            Card(Values.ACE, Suits.HEARTS),
            Card(Values.TWO, Suits.DIAMONDS),
            Card(Values.THREE, Suits.CLUBS),
            Card(Values.SEVEN, Suits.SPADES),
            Card(Values.TEN, Suits.HEARTS)
        ]
        cut = None
        score = check_runs(hand, cut, 0)
        self.assertEqual(score, 3)
    
    def test_check_runs_run_of_four(self):
        """Test check_runs with a run of 4 - 4, 5, 7, 6 = 4 points"""
        hand = [
            Card(Values.FOUR, Suits.HEARTS),
            Card(Values.FIVE, Suits.DIAMONDS),
            Card(Values.SEVEN, Suits.CLUBS),
            Card(Values.SIX, Suits.SPADES)
        ]
        cut = None
        score = check_runs(hand, cut, 0)
        self.assertEqual(score, 4)
    
    def test_check_runs_run_of_five(self):
        """Test check_runs with a run of 5 - 9, 10, J, Q, K = 5 points"""
        hand = [
            Card(Values.NINE, Suits.HEARTS),
            Card(Values.TEN, Suits.DIAMONDS),
            Card(Values.JACK, Suits.CLUBS),
            Card(Values.QUEEN, Suits.SPADES),
            Card(Values.KING, Suits.HEARTS)
        ]
        cut = None
        score = check_runs(hand, cut, 0)
        self.assertEqual(score, 5)
    
    def test_check_runs_run_of_three_with_duplicate(self):
        """Test check_runs with a run of 3 and duplicate - 9, 9, 10, J = 6 points"""
        hand = [
            Card(Values.NINE, Suits.HEARTS),
            Card(Values.NINE, Suits.DIAMONDS),
            Card(Values.TEN, Suits.CLUBS),
            Card(Values.JACK, Suits.SPADES)
        ]
        cut = None
        score = check_runs(hand, cut, 0)
        self.assertEqual(score, 6)
    
    def test_check_runs_no_run(self):
        """Test check_runs with no run - A, 3, 5, 8 = 0 points"""
        hand = [
            Card(Values.ACE, Suits.HEARTS),
            Card(Values.THREE, Suits.DIAMONDS),
            Card(Values.FIVE, Suits.CLUBS),
            Card(Values.EIGHT, Suits.SPADES)
        ]
        cut = None
        score = check_runs(hand, cut, 0)
        self.assertEqual(score, 0)
    
    def test_check_runs_run_of_four_with_extra_card(self):
        """Test check_runs with a run of 4 and extra card - 4, 5, 6, 7, Q = 4 points"""
        hand = [
            Card(Values.FOUR, Suits.HEARTS),
            Card(Values.FIVE, Suits.DIAMONDS),
            Card(Values.SIX, Suits.CLUBS),
            Card(Values.SEVEN, Suits.SPADES),
            Card(Values.QUEEN, Suits.HEARTS)
        ]
        cut = None
        score = check_runs(hand, cut, 0)
        self.assertEqual(score, 4)