from .Card import Card, Suits, Values
import random

class Deck:
    def __init__(self, cards=None):
        # If we do not pass in a list of cards we create a default deck
        if cards is None:
            self.cards = []
            for suit in Suits:
                for value in Values:
                    self.cards.append(Card(value, suit))
        else:
            self.cards = cards

    # Returns a list of cards drawn from the deck of length num_cards (default is 1)
    def draw(self, num_cards=1):
        return [self.cards.pop() for _ in range(num_cards)]

    def shuffle(self):
        """Shuffles the deck in place"""
        random.shuffle(self.cards)