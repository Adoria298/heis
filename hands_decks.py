#! /usr/bin/env python
"""
Code for managing hands and decks of cards.
"""
from cards import NumCard, Draw2Card, ReverseCard, SkipCard, WildCard, WildDraw4Card, COLOURS
import random
from pprint import pprint

class Pile:

    def __init__(self):
        self.cards = []

class Deck(Pile):
    """
    A Deck contains 108 cards:
     - 19 Blue
     - 19 Green
     - 19 Red
     - 19 Yellow
     - 8 Draw Two - 2 of each colour
     - 8 Reverse - 2 of each colour
     - 8 Skip - 2 of each colour
     - 4 Wild
     - 4 Wild Draw Four

    This class manages all 108 cards.
    """
    def __init__(self):
        super().__init__(self)
        for colour in COLOURS:
            for i in range(19):
                self.cards.append(NumCard(colour, random.randint(0,9)))
            for i in range(2):
                self.cards.append(Draw2Card(colour))
                self.cards.append(ReverseCard(colour))
                self.cards.append(SkipCard(colour))
        for i in range(4):
            self.cards.append(WildCard())
            self.cards.append(WildDraw4Card())
        pprint(self.cards)
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)  

if __name__ == "__main__":
    d = Deck()