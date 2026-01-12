# This file contains functions for scoring, and other cribbage-related functions

from DecksAndCards.Card import Card, Suits, Values
import itertools

def score_hand(hand, cut_card):
    """Scores a hand of cards"""
    score = 0

    # Check for 15s
    score = check_15s(hand, cut_card, score)
    # Check for pairs, returns incremented score
    score = check_pairs(hand, cut_card, score)
    # Check for runs
    score = check_runs(hand, cut_card, score)
    # Check for flushes
    score = check_flushes(hand, cut_card, score)
    # Check for nibs and nobs
    score = check_nibs_and_nobs(hand, cut_card, score)

    return score

# Checks for 15s in the hand, rewarding 2 points for each 15
def check_15s(hand, cut_card, score):
    """
    Finds all combinations of cards that sum to exactly 15.
    Each combination of 2, 3, 4, or 5 cards that sums to 15 is worth 2 points.
    """
    def get_card_value(card):
        """Get the numeric value of a card for 15s scoring (ACE=1, 2-10=2-10, J/Q/K=10)"""
        if card.value == Values.ACE:
            return 1
        elif card.value in [Values.JACK, Values.QUEEN, Values.KING]:
            return 10
        else:
            # For 2-10, use the numeric value from the enum
            return card.value.value[0]
    
    # Combine hand and cut_card into a list of all cards
    all_cards = hand.copy()
    if cut_card is not None:
        all_cards.append(cut_card)
    
    # Count how many combinations sum to 15
    # We need to check all subsets of size 2, 3, 4, and 5
    combinations_that_sum_to_15 = 0
    
    # Check all possible combinations of 2, 3, 4, and 5 cards
    for r in range(2, len(all_cards) + 1):
        for combo in itertools.combinations(all_cards, r):
            # Calculate the sum of this combination
            total = sum(get_card_value(card) for card in combo)
            if total == 15:
                combinations_that_sum_to_15 += 1
    
    # Each combination that sums to 15 is worth 2 points
    score += combinations_that_sum_to_15 * 2
    
    return score

# Checks for pairs in the hand, rewarding 2 points for each pair
def check_pairs(hand, cut_card, score):
    cards = hand.copy()
    if cut_card is not None:
        cards.append(cut_card)

    # Check for unique pairs
    # Group cards by their value
    value_counts = {}
    for card in cards:
        card_value = card.value
        value_counts[card_value] = value_counts.get(card_value, 0) + 1
    
    # For each value with n cards, calculate pairs = n*(n-1)/2
    # Each pair is worth 2 points
    for count in value_counts.values():
        if count >= 2:
            # Number of pairs = C(n,2) = n*(n-1)/2
            num_pairs = count * (count - 1) // 2
            score += num_pairs * 2

    return score

def check_runs(hand, cut_card, score):
    cards = hand.copy()
    if cut_card is not None:
        cards.append(cut_card)
    
    # Check for runs
    # First, convert card values to run values (J=11, Q=12, K=13)
    def get_run_value(card):
        """Convert card value to numeric value for run checking"""
        if card.value == Values.JACK:
            return 11
        elif card.value == Values.QUEEN:
            return 12
        elif card.value == Values.KING:
            return 13
        else:
            # For ACE through TEN, use the numeric value from the enum
            return card.value.value[0]
    
    # Group cards by their run value, keeping track of counts
    value_counts = {}
    for card in cards:
        run_value = get_run_value(card)
        value_counts[run_value] = value_counts.get(run_value, 0) + 1
    
    # Find all runs of length 3 or more
    # A run is a sequence of consecutive values
    unique_values = sorted(value_counts.keys())
    
    # Find the longest run(s) and score them
    # In cribbage, we score the longest run only, but duplicates multiply the score
    max_run_length = 0
    best_runs = []
    
    # Check all possible starting points for runs
    for start_idx in range(len(unique_values)):
        run_length = 1
        current_value = unique_values[start_idx]
        
        # Try to extend the run forward
        for next_idx in range(start_idx + 1, len(unique_values)):
            if unique_values[next_idx] == current_value + run_length:
                run_length += 1
            else:
                break
        
        # If this is a valid run (length >= 3), check if it's the longest
        if run_length >= 3:
            if run_length > max_run_length:
                max_run_length = run_length
                best_runs = [(start_idx, run_length)]
            elif run_length == max_run_length:
                best_runs.append((start_idx, run_length))
    
    # Score the longest run(s)
    if max_run_length >= 3:
        for start_idx, run_length in best_runs:
            # Calculate multiplier based on duplicates
            multiplier = 1
            for i in range(start_idx, start_idx + run_length):
                value = unique_values[i]
                multiplier *= value_counts[value]
            
            # Score is run_length points * multiplier
            score += run_length * multiplier
    
    return score

def check_flushes(hand, cut_card, score, is_crib=False):
        flush_points = 0
        # If the hand is the crib, we can only score a full 5 card flush
        if is_crib:
            cards = hand.copy()
            if cut_card is not None:
                cards.append(cut_card)
            # Check for a flush of 5 cards
            if len(cards) == 5:
                # Check if all cards are the same suit
                if all(card.suit == cards[0].suit for card in cards):
                    return score + 5
            return score
        else:
            # We are scoring a hand, not a crib.
            # We can score a flush of 4 or 5 cards
            # A flush of 4 can only happen if it's all four cards in the hand
            # A flush of 5 can happen with all 4 hand cards and the cut card

            # Check for a flush of 4 cards
            if all(card.suit == hand[0].suit for card in hand):
                flush_points = 4
            # Check for a flush of 5 cards
            if all(card.suit == hand[0].suit for card in hand) and cut_card is not None and cut_card.suit == hand[0].suit:
                flush_points = 5
            return score + flush_points
    
# A simple nibs and nobs check
# Will be expanded to only score nibs for the dealer
def check_nibs_and_nobs(hand, cut_card, score):
    # Check for nibs (the cut card is any Jack)
    if cut_card is not None and cut_card.value == Values.JACK:
        score += 2
    # Check for nobs (the cut card matches the suit of any Jack in the hand)
    if cut_card is not None and any(card.value == Values.JACK and card.suit == cut_card.suit for card in hand):
        score += 1
    return score
