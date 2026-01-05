from DecksAndCards.Deck import Deck
from DecksAndCards.Card import Card, Suits, Values

def main():
    deck = Deck()

    # Create a list to serve as our hand of cards
    hand = []
    # Draw 4 cards from the deck and add them to the hand
    for i in range(4):
        hand.append(deck.draw())

if __name__ == "__main__":
    main()