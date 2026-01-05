from .Card import Card, Suits, Values

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

    def draw(self):
        return self.cards.pop()

    
        