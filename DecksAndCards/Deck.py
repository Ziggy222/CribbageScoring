from .Card import Card, Suits, Values
import random
import csv

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

    def deck_from_file(self, file_path):
        """
        Loads a deck from a CSV file. The CSV should have two columns: value and suit.
        Supports multiple formats:
        - Enum names: "ACE", "HEARTS"
        - Symbols: "A", "H"
        - Case-insensitive matching
        
        Args:
            file_path (str): Path to the CSV file
            
        Raises:
            FileNotFoundError: If the file doesn't exist
            ValueError: If a row cannot be parsed or contains invalid data
        """
        # Clear existing deck
        self.cards = []
        
        # Helper function to find enum by name or symbol
        def find_value(value_str):
            value_str = value_str.strip().upper()
            # Try by enum name first
            for value in Values:
                if value.name == value_str or value.value[2].upper() == value_str:
                    return value
            raise ValueError(f"Invalid value: {value_str}")
        
        def find_suit(suit_str):
            suit_str = suit_str.strip().upper()
            # Try by enum name first
            for suit in Suits:
                if suit.name == suit_str or suit.value[2].upper() == suit_str:
                    return suit
            raise ValueError(f"Invalid suit: {suit_str}")
        
        try:
            with open(file_path, 'r', newline='') as file:
                reader = csv.reader(file)
                for row_num, row in enumerate(reader, start=1):
                    # Skip empty rows
                    if not row or (len(row) >= 2 and not row[0].strip() and not row[1].strip()):
                        continue
                    
                    # Skip header row if it looks like a header (contains non-enum values)
                    if row_num == 1:
                        # Check if first row looks like a header
                        if len(row) >= 2:
                            first_col = row[0].strip().upper()
                            second_col = row[1].strip().upper()
                            # Common header patterns
                            if first_col in ['VALUE', 'VALUES', 'CARD_VALUE', 'RANK'] or \
                               second_col in ['SUIT', 'SUITS', 'CARD_SUIT']:
                                continue
                    
                    if len(row) < 2:
                        raise ValueError(f"Row {row_num}: Expected 2 columns (value, suit), got {len(row)}")
                    
                    try:
                        value = find_value(row[0])
                        suit = find_suit(row[1])
                        self.cards.append(Card(value, suit))
                    except ValueError as e:
                        raise ValueError(f"Row {row_num}: {str(e)}")
        except FileNotFoundError:
            raise FileNotFoundError(f"Deck file not found: {file_path}")
        except Exception as e:
            if isinstance(e, (FileNotFoundError, ValueError)):
                raise
            raise ValueError(f"Error reading deck file: {str(e)}")

    # Returns a list of cards drawn from the deck of length num_cards (default is 1)
    def draw(self, num_cards=1):
        return [self.cards.pop() for _ in range(num_cards)]

    def shuffle(self):
        """Shuffles the deck in place"""
        random.shuffle(self.cards)
    
    @classmethod
    def from_file(cls, file_path):
        """
        Creates a new Deck instance from a CSV file.
        
        Args:
            file_path (str): Path to the CSV file
            
        Returns:
            Deck: A new Deck instance loaded from the CSV file
        """
        deck = cls(cards=[])
        deck.deck_from_file(file_path)
        return deck