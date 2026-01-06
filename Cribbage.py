# This file contains functions for scoring, and other cribbage-related functions

from DecksAndCards.Card import Card, Suits, Values

def score_hand(hand, cut_card):
    """Scores a hand of cards"""
    score = 0

    # Check for 15s
    # Check for pairs, returns incremented score
    score = check_pairs(hand, cut_card, score)
    # Check for runs
    # Check for flushes
    # Check for nibs and nobs

    return score

# Checks for pairs in the hand, rewarding 2 points for each pair
def check_pairs(hand, cut_card, score):
    cards = hand.copy()
    if cut_card is not None:
        cards.append(cut_card)

    # Check for unique pairs
    # Group cards by their value
    value_counts = {}
    for card in hand:
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
    for card in hand:
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
    
