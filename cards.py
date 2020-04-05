#! /usr/bib/env python3
"""
UnoPy - The Card Game brought to life by Python.

cards.py contains the code for all types of card used in Uno.
"""
from dataclasses import dataclass

COLOURS = ("Red", "Blue", "Green", "Yellow")
ACTIONS = ("Number", "Reverse", "Draw Two", "Skip", "Wild", "Wild Draw 4")

@dataclass()
class Card:
    colour: str
    action: str
    score: int # amount added to score
    cards_drawn: int # cards to draw when this card is played

    @property
    def colour(self):
        "Returns self._colour."
        return self._colour
    
    @colour.setter
    def colour(self, value):
        "Checks that value is in COLOURS before setting self._colour. If not, raises an UnoException."
        if value not in COLOURS:
            self._colour = "Black"
        else:
            self._colour = value

    @property
    def action(self):
        "Returns self._action."
        return self._action
    
    @action.setter
    def action(self, value):
        "Checks that value is in ACTIONS before setting self._actiob. If not, raises an UnoException."
        if value == None:
            self._action = "Number"
        elif value not in ACTIONS:
            raise ValueError(f"Invalid Action: {value}. Actions must be one of: {ACTIONS}.")
        else:
            self._action = value

class NumCard(Card):

    def __init__(self, colour, value):
        super().__init__(colour, action=None, score=value, cards_drawn=0)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if value < 0 or value > 9:
            raise ValueError("Score of a NumCard must be between 0 and 9.")
        else:
            self._score = value

class Draw2Card(Card):

    def __init__(self, colour):
        super().__init__(colour, action="Draw Two", score=20, cards_drawn=2)
        
class ReverseCard(Card):

    def __init__(self, colour):
        super().__init__(colour, action="Reverse", score=20, cards_drawn=0)

class SkipCard(Card):

    def __init__(self, colour):
        super().__init__(colour, action="Reverse", score=20, cards_drawn=0)

class WildCard(Card):

    def __init__(self):
        super().__init__(colour="Black", action="Wild", score=50, card_drawn=0)


class WildDraw4Card(Card):

    def __init__(self):
        super().__init__(colour="Black", action="Wild Draw 4", score=50, cards_drawn=4)
