from enum import Enum

# Enum of "SUIT" to tuple of (id, name, symbol)
class Suits(Enum):
    HEARTS = (0, "Hearts", "H")
    DIAMONDS = (1, "Diamonds", "D")
    CLUBS = (2, "Clubs", "C")
    SPADES = (3, "Spades", "S")

# Enum of "VALUE" to tuple of (value, name, symbol)
class Values(Enum):
    ACE = (1, "Ace", "A")
    TWO = (2, "Two", "2")
    THREE = (3, "Three", "3")
    FOUR = (4, "Four", "4")
    FIVE = (5, "Five", "5")
    SIX = (6, "Six", "6")
    SEVEN = (7, "Seven", "7")
    EIGHT = (8, "Eight", "8")
    NINE = (9, "Nine", "9")
    TEN = (10, "Ten", "10")
    JACK = (10, "Jack", "J")
    QUEEN = (10, "Queen", "Q")
    KING = (10, "King", "K")

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def short_print(self):
        """Returns a short string representation of the card (e.g., 'AH', '10D')"""
        # Values and Suits are stored as tuples: (id, name, symbol)
        value_symbol = self.value.value[2]
        suit_symbol = self.suit.value[2]
        return f"{value_symbol}{suit_symbol}"

    def full_print(self):
        """Returns a full string representation of the card (e.g., 'Ace of Hearts', 'Ten of Diamonds')"""
        # Values and Suits are stored as tuples: (id, name, symbol)
        value_name = self.value.value[1]
        suit_name = self.suit.value[1]
        return f"{value_name} of {suit_name}"