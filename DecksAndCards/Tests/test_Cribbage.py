import unittest
import sys
import os

# Add project root directory to path to import from DecksAndCards package
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from DecksAndCards.Card import Card, Suits, Values
from Cribbage import check_pairs, check_runs, check_flushes, check_nibs_and_nobs, check_15s

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

    def test_check_flushes_hand_four_plus_cut_same_suit(self):
        """Test check_flushes with hand [H,H,H,H] and cut [H] = 5 points"""
        hand = [
            Card(Values.ACE, Suits.HEARTS),
            Card(Values.TWO, Suits.HEARTS),
            Card(Values.THREE, Suits.HEARTS),
            Card(Values.FOUR, Suits.HEARTS)
        ]
        cut = Card(Values.FIVE, Suits.HEARTS)
        score = check_flushes(hand, cut, 0, is_crib=False)
        self.assertEqual(score, 5)
    
    def test_check_flushes_hand_four_different_cut(self):
        """Test check_flushes with hand [H,H,H,H] and cut [D] = 4 points"""
        hand = [
            Card(Values.ACE, Suits.HEARTS),
            Card(Values.TWO, Suits.HEARTS),
            Card(Values.THREE, Suits.HEARTS),
            Card(Values.FOUR, Suits.HEARTS)
        ]
        cut = Card(Values.FIVE, Suits.DIAMONDS)
        score = check_flushes(hand, cut, 0, is_crib=False)
        self.assertEqual(score, 4)
    
    def test_check_flushes_hand_mixed_suits_same_cut(self):
        """Test check_flushes with hand [H,H,D,H] and cut [H] = 0 points"""
        hand = [
            Card(Values.ACE, Suits.HEARTS),
            Card(Values.TWO, Suits.HEARTS),
            Card(Values.THREE, Suits.DIAMONDS),
            Card(Values.FOUR, Suits.HEARTS)
        ]
        cut = Card(Values.FIVE, Suits.HEARTS)
        score = check_flushes(hand, cut, 0, is_crib=False)
        self.assertEqual(score, 0)
    
    def test_check_flushes_hand_all_different_suits(self):
        """Test check_flushes with hand [S,C,D,H] and cut [D] = 0 points"""
        hand = [
            Card(Values.ACE, Suits.SPADES),
            Card(Values.TWO, Suits.CLUBS),
            Card(Values.THREE, Suits.DIAMONDS),
            Card(Values.FOUR, Suits.HEARTS)
        ]
        cut = Card(Values.FIVE, Suits.DIAMONDS)
        score = check_flushes(hand, cut, 0, is_crib=False)
        self.assertEqual(score, 0)
    
    def test_check_flushes_crib_five_card_flush(self):
        """Test check_flushes with crib [S,S,S,S] and cut [S] = 5 points"""
        hand = [
            Card(Values.ACE, Suits.SPADES),
            Card(Values.TWO, Suits.SPADES),
            Card(Values.THREE, Suits.SPADES),
            Card(Values.FOUR, Suits.SPADES)
        ]
        cut = Card(Values.FIVE, Suits.SPADES)
        score = check_flushes(hand, cut, 0, is_crib=True)
        self.assertEqual(score, 5)
    
    def test_check_flushes_crib_four_card_flush_different_cut(self):
        """Test check_flushes with crib [S,S,S,S] and cut [C] = 0 points"""
        hand = [
            Card(Values.ACE, Suits.SPADES),
            Card(Values.TWO, Suits.SPADES),
            Card(Values.THREE, Suits.SPADES),
            Card(Values.FOUR, Suits.SPADES)
        ]
        cut = Card(Values.FIVE, Suits.CLUBS)
        score = check_flushes(hand, cut, 0, is_crib=True)
        self.assertEqual(score, 0)
    
    def test_check_flushes_crib_mixed_suits_same_cut(self):
        """Test check_flushes with crib [S,S,S,C] and cut [S] = 0 points"""
        hand = [
            Card(Values.ACE, Suits.SPADES),
            Card(Values.TWO, Suits.SPADES),
            Card(Values.THREE, Suits.SPADES),
            Card(Values.FOUR, Suits.CLUBS)
        ]
        cut = Card(Values.FIVE, Suits.SPADES)
        score = check_flushes(hand, cut, 0, is_crib=True)
        self.assertEqual(score, 0)
    
    def test_check_flushes_crib_all_different_suits(self):
        """Test check_flushes with crib [H,D,C,S] and cut [H] = 0 points"""
        hand = [
            Card(Values.ACE, Suits.HEARTS),
            Card(Values.TWO, Suits.DIAMONDS),
            Card(Values.THREE, Suits.CLUBS),
            Card(Values.FOUR, Suits.SPADES)
        ]
        cut = Card(Values.FIVE, Suits.HEARTS)
        score = check_flushes(hand, cut, 0, is_crib=True)
        self.assertEqual(score, 0)
    
    def test_check_nibs_and_nobs_nibs_only(self):
        """Test check_nibs_and_nobs with [JH,4D,3S,10C] and cut [JD] = 2 points (nibs only)"""
        hand = [
            Card(Values.JACK, Suits.HEARTS),
            Card(Values.FOUR, Suits.DIAMONDS),
            Card(Values.THREE, Suits.SPADES),
            Card(Values.TEN, Suits.CLUBS)
        ]
        cut = Card(Values.JACK, Suits.DIAMONDS)
        score = check_nibs_and_nobs(hand, cut, 0)
        self.assertEqual(score, 2)
    
    def test_check_nibs_and_nobs_nibs_and_nobs(self):
        """Test check_nibs_and_nobs with [JD, AH, 2H, 3H] and cut [JD] = 3 points (nibs + nobs)"""
        hand = [
            Card(Values.JACK, Suits.DIAMONDS),
            Card(Values.ACE, Suits.HEARTS),
            Card(Values.TWO, Suits.HEARTS),
            Card(Values.THREE, Suits.HEARTS)
        ]
        cut = Card(Values.JACK, Suits.DIAMONDS)
        score = check_nibs_and_nobs(hand, cut, 0)
        self.assertEqual(score, 3)
    
    def test_check_nibs_and_nobs_nobs_only(self):
        """Test check_nibs_and_nobs with [AH, JS, 2C, 3C] and cut [4S] = 1 point (nobs only)"""
        hand = [
            Card(Values.ACE, Suits.HEARTS),
            Card(Values.JACK, Suits.SPADES),
            Card(Values.TWO, Suits.CLUBS),
            Card(Values.THREE, Suits.CLUBS)
        ]
        cut = Card(Values.FOUR, Suits.SPADES)
        score = check_nibs_and_nobs(hand, cut, 0)
        self.assertEqual(score, 1)
    
    def test_check_nibs_and_nobs_no_nibs_or_nobs(self):
        """Test check_nibs_and_nobs with [AD, 2S, 3C, 4H] and cut [5S] = 0 points"""
        hand = [
            Card(Values.ACE, Suits.DIAMONDS),
            Card(Values.TWO, Suits.SPADES),
            Card(Values.THREE, Suits.CLUBS),
            Card(Values.FOUR, Suits.HEARTS)
        ]
        cut = Card(Values.FIVE, Suits.SPADES)
        score = check_nibs_and_nobs(hand, cut, 0)
        self.assertEqual(score, 0)
    
    def test_check_15s_no_15s(self):
        """Test check_15s with [A, A, 2, 3] and cut [4] = 0 points (tests no 15s)"""
        hand = [
            Card(Values.ACE, Suits.HEARTS),
            Card(Values.ACE, Suits.DIAMONDS),
            Card(Values.TWO, Suits.CLUBS),
            Card(Values.THREE, Suits.SPADES)
        ]
        cut = Card(Values.FOUR, Suits.HEARTS)
        score = check_15s(hand, cut, 0)
        self.assertEqual(score, 0)
    
    def test_check_15s_fives_and_tens(self):
        """Test check_15s with [5, 5, J, Q] and cut [K] = 12 points (tests 5s and multiple different 10 value cards)"""
        hand = [
            Card(Values.FIVE, Suits.HEARTS),
            Card(Values.FIVE, Suits.DIAMONDS),
            Card(Values.JACK, Suits.CLUBS),
            Card(Values.QUEEN, Suits.SPADES)
        ]
        cut = Card(Values.KING, Suits.HEARTS)
        score = check_15s(hand, cut, 0)
        self.assertEqual(score, 12)
    
    def test_check_15s_five_and_multiple_tens(self):
        """Test check_15s with [5, 10, J, Q] and cut [K] = 8 points (tests 5 and multiple different 10 value cards)"""
        hand = [
            Card(Values.FIVE, Suits.HEARTS),
            Card(Values.TEN, Suits.DIAMONDS),
            Card(Values.JACK, Suits.CLUBS),
            Card(Values.QUEEN, Suits.SPADES)
        ]
        cut = Card(Values.KING, Suits.HEARTS)
        score = check_15s(hand, cut, 0)
        self.assertEqual(score, 8)
    
    def test_check_15s_three_card_15s(self):
        """Test check_15s with [6, 7, 7, 8] and cut [2] = 8 points (tests 15s made from 3 cards)"""
        hand = [
            Card(Values.SIX, Suits.HEARTS),
            Card(Values.SEVEN, Suits.DIAMONDS),
            Card(Values.SEVEN, Suits.CLUBS),
            Card(Values.EIGHT, Suits.SPADES)
        ]
        cut = Card(Values.TWO, Suits.HEARTS)
        score = check_15s(hand, cut, 0)
        self.assertEqual(score, 8)
    
    def test_check_15s_four_card_and_mixed_15s(self):
        """Test check_15s with [4, 4, 6, A] and cut [9] = 4 points (tests 15 made from 4 cards and mixed length 15s)"""
        hand = [
            Card(Values.FOUR, Suits.HEARTS),
            Card(Values.FOUR, Suits.DIAMONDS),
            Card(Values.SIX, Suits.CLUBS),
            Card(Values.ACE, Suits.SPADES)
        ]
        cut = Card(Values.NINE, Suits.HEARTS)
        score = check_15s(hand, cut, 0)
        self.assertEqual(score, 4)
    
    def test_check_15s_five_card_15s(self):
        """Test check_15s with [4, 3, 3, 3] and cut [2] = 2 points (Tests 15s made from 5 cards)"""
        hand = [
            Card(Values.FOUR, Suits.HEARTS),
            Card(Values.THREE, Suits.DIAMONDS),
            Card(Values.THREE, Suits.CLUBS),
            Card(Values.THREE, Suits.SPADES)
        ]
        cut = Card(Values.TWO, Suits.HEARTS)
        score = check_15s(hand, cut, 0)
        self.assertEqual(score, 2)
    
    def test_check_15s_wild_hand(self):
        """Test check_15s with [5, 5, 5, 5] and cut [10] = 16 points (just a wild hand)"""
        hand = [
            Card(Values.FIVE, Suits.HEARTS),
            Card(Values.FIVE, Suits.DIAMONDS),
            Card(Values.FIVE, Suits.CLUBS),
            Card(Values.FIVE, Suits.SPADES)
        ]
        cut = Card(Values.TEN, Suits.HEARTS)
        score = check_15s(hand, cut, 0)
        self.assertEqual(score, 16)