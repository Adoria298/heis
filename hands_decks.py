#! /usr/bin/env python
"""
Code for managing hands and decks of cards.
"""
from cards import *
import random
from pprint import pprint

class Deck:
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
        self.deck = []
        for colour in COLOURS:
            for i in range(19):
                self.deck.append(NumCard(colour, random.randint(0,9)))
            for i in range(2):
                self.deck.append(Draw2Card(colour))
                self.deck.append(ReverseCard(colour))
                self.deck.append(SkipCard(colour))
        for i in range(4):
            self.deck.append(WildCard())
            self.deck.append(WildDraw4Card())
        pprint(self.deck)
        self.shuffle()

    def shuffle(self):
        self.deck = random.shuffle(self.deck)  

if __name__ == "__main__":
    d = Deck()