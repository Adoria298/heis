#! /usr/bin/env python
"""
Code for managing hands and decks of cards.
"""
from card import Card, COLOURS, ACTIONS

class Deck:
    """
    A Deck contains 108 cards:
     - 19 Blue
     - 19 Green
     - 19 Red
     - 19 Yellow
     - 8 Draw Two
     - 8 Reverse
     - 8 Skip
     - 4 Wild
     - 4 Wild Draw Four

    This class manages all 108 cards.
    """