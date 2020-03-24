#! /usr/bib/env python3
"""
UnoPy - The Card Game brought to life by Python.

card.py contains the code for class Card and tests.
"""

COLOURS = ("Red", "Blue", "Green", "Yellow", "Black")
ACTIONS = ("None", "Reverse", "Draw Two", "Skip", "Wild", "Wild Draw 4")

class Card:
    def __init__(self, colour, action=None):
        self.colour = colour
        self.action = action
        self.score = 0 # amount added to score

    @property
    def colour(self):
        "Returns self._colour."
        return self._colour
    
    @colour.setter
    def colour(self, value):
        "Checks that value is in COLOURS before setting self._colour. If not, raises an UnoException."
        print("Colour setter called.")
        if value not in COLOURS:
            raise ValueError(f"Invalid Colour: {value}. Colours must be one of: {COLOURS}.")
        else:
            self._colour = value

    @property
    def action(self):
        "Returns self._action."
        return self._action
    
    @action.setter
    def action(self, value):
        "Checks that value is in ACTIONS before setting self._actiob. If not, raises an UnoException."
        if value not in ACTIONS:
            raise ValueError(f"Invalid Action: {value}. Actions must be one of: {ACTIONS}.")
        elif value == None:
            self._action = None
        else:
            self._action = value

class NumCard(Card):

    def __init__(self, colour, value):
        

if __name__ == "__main__":
    # tests
    r = Card("Red", "None")
    print(r.colour)
    print(r.action)
    p = Card("Pink", "Skip")