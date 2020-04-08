#! /usr/bin/env python
"""
Code for managing hands and decks of cards.
"""
from uno_pb2 import Card, CardColour
import random
from pprint import pprint
from dataclasses import dataclass
from typing import List

@dataclass
class Pile:
    """
    Superclass for a group of cards.
    """
    cards: List[Card]

    def __len__(self):
        return len(self.cards)

    def draw_cards(self, cards):
        """
        Appends cards to internal list.
        """
        self.cards += cards

    def discard_cards(self, amount):
        """
        Generator function that Pops {amount} of cards from self.cards and yields results.
        
        Catches IndexError and prints 'Run out of cards'.
        """
        try:
            for i in range(amount):
                yield self.cards.pop(i)
        except IndexError:
            print("Run out of cards.")

    def shuffle(self):
        """
        Uses random.shuffle() to shuffe self.cards.

        TODO: implement shuffling algorithm based on Spotify's playlist shuffle so that similar cards are far apart: https://codegolf.stackexchange.com/questions/198094/spotify-shuffle-music-playlist-shuffle-algorithm
        """
        random.shuffle(self.cards)  
