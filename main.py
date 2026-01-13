from DecksAndCards.Deck import Deck
from DecksAndCards.Card import Card, Suits, Values
import Cribbage

def main():
    # Create a new deck
    deck = Deck()

    # Shuffle the deck
    deck.shuffle()

    # Create a list to serve as our hand of cards
    hand = []
    # Draw 6 cards from the deck and add them to the hand
    hand.extend(deck.draw(6))

    # Print the hand, prompting the user to choose 2 cards to "discard" into the crib
    print_hand(hand)
    print("Choose 2 cards to discard into the crib:")
    crib = []
    for i in range(2):
        choose_discard(hand, crib)

    # "Draw" the cut card.
    cut_card = deck.draw()[0]

    # Score the hand
    score = Cribbage.score_hand(hand, cut_card)
    print_hand_and_cut_card(hand, cut_card)
    print(f"Your score is: {score}")

def choose_discard(hand, crib):
    print("Choose card to discard into the crib:")
    for i in range(len(hand)):
        print(f"{i}: {hand[i].full_print()}")
    choice = input(f"Enter the index of card to discard: ")
    crib.append(hand.pop(int(choice)))

def print_hand(hand):
    print(f"Your hand: {[card.full_print() for card in hand]}")

def print_hand_and_cut_card(hand, cut_card):
    print_hand(hand)
    print(f"Cut Card: {cut_card.full_print()}")

if __name__ == "__main__":
    main()