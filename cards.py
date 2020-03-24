#! /usr/bib/env python3
"""
UnoPy - The Card Game brought to life by Python.

cards.py contains the code for all types of card used in Uno.
"""

COLOURS = ("Red", "Blue", "Green", "Yellow")
ACTIONS = ("Number", "Reverse", "Draw Two", "Skip", "Wild", "Wild Draw 4")

class Card:
    def __init__(self, colour, action=None):
        self.colour = colour
        self.action = action
        self.score = 0 # amount added to score
        self.cards_drawn = 0 # how many cards to draw

    def __repr__(self):
        return f"{self.colour} {self.action} Card worth {self.score} points."

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
        super().__init__(colour, action=None)
        self.score = value

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
        super().__init__(colour, action="Draw Two")
        self.score = 20 # constant
        self.cards_drawn = 2

class ReverseCard(Card):

    def __init__(self, colour):
        super().__init__(colour, action="Reverse")
        self.score = 20

class SkipCard(Card):

    def __init__(self, colour):
        super().__init__(colour, action="Reverse")
        self.score = 20
    
class WildCard(Card):

    def __init__(self):
        super().__init__(colour="Black", action="Wild")
        self.score = 50

class WildDraw4Card(Card):

    def __init__(self):
        super().__init__(colour="Black", action="Wild Draw 4")
        self.score = 50
        self.cards_drawn = 4
