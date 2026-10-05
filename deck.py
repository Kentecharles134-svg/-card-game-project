import random
from card import Card


class Deck:
    def __init__(self):
        self.cards = []
        self.build_deck()

    def build_deck(self):
        self.cards = []

        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

        ranks = [
            ("2", 2),
            ("3", 3),
            ("4", 4),
            ("5", 5),
            ("6", 6),
            ("7", 7),
            ("8", 8),
            ("9", 9),
            ("10", 10),
            ("Jack", 11),
            ("Queen", 12),
            ("King", 13),
            ("Ace", 14)
        ]

        for suit in suits:
            for rank, value in ranks:
                self.cards.append(Card(suit, rank, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        return None

    def cards_remaining(self):
        return len(self.cards)
