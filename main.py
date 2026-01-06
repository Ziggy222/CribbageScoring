from DecksAndCards.Deck import Deck
from DecksAndCards.Card import Card, Suits, Values

def main():
    # Create a new deck
    deck = Deck()

    # Shuffle the deck
    deck.shuffle()

    # Create a list to serve as our hand of cards
    hand = []
    # Draw 4 cards from the deck and add them to the hand
    hand.extend(deck.draw(4))

    # "Draw" the cut card.
    cut_card = deck.draw()[0]

    # Temporary debug print of the hand and cut card
    debug_print_hand_and_cut_card(hand, cut_card)

# Temporary debug function to print the hand and cut card
def debug_print_hand_and_cut_card(hand, cut_card):
    print(f"Hand: {[card.full_print() for card in hand]}")
    print(f"Cut Card: {cut_card.full_print()}")

if __name__ == "__main__":
    main()