#! /usr/bin/env python
"""
Code for managing hands and decks of cards.
"""
from cards import NumCard, Draw2Card, ReverseCard, SkipCard, WildCard, WildDraw4Card, COLOURS
import random
from pprint import pprint

class Pile:
    """
    Superclass for a group of cards.
    """

    def __init__(self):
        self.cards = []

    def draw_cards(self, cards):
        self.cards += cards

    def discard_cards(self, amount):
        try:
            for i in range(amount):
                yield self.cards.pop(i)
        except IndexError:
            print("Run out of cards.")

class DiscardPile(Pile):
    """
    Where cards are discarded to.
    """
    pass

class DrawPile(Pile):
    """
    Where cards are drawn from.
    """
    pass

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

     The number cards have the numbers 0-9, with 1-9 repeated (i.e. they have two of every number
     between 0 and 9 except 0, which they only have one of.)

    This class manages all 108 cards.
    """
    def __init__(self):
        super().__init__()
        for colour in COLOURS:
            for i in range(0, 10): # stop point is exclusive
                self.cards.append(NumCard(colour, value=i))
            for i in range(1, 10): # start point is inclusive
                self.cards.append(NumCard(colour, value=i))
            for i in range(2):
                self.cards.append(Draw2Card(colour))
                self.cards.append(ReverseCard(colour))
                self.cards.append(SkipCard(colour))
        for i in range(4):
            self.cards.append(WildCard())
            self.cards.append(WildDraw4Card())
        pprint(self.cards)
        #self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)  

class Hand(Pile):
    """
    A single player's hand.
    """
    pass

if __name__ == "__main__":
    d = Deck()