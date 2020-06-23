"""
utility.py - Code shared between both the client and the server.
Copyright (C) <2020>  <Adoria298>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from rich.style import Style
from uno_pb2 import CardAction, CardColour

# utility functions
def card_str(card):
    """
    Takes a `card` (uno_pb2.Card) and returns a string and a rich.style.Style.
    Uses colorama to make ASCII escape sequences work on Windows.
    The colour is the card's colour, and the string is either the card's action 
    or the card's value, depending on whether the card is an action card or not.
    """
    colours_style  = { # rich.console.Console styles
            "RED": Style(color="black", bgcolor="red"),
            "BLUE": Style(color="black", bgcolor="blue"),
            "GREEN": Style(color="black", bgcolor="green"),
            "YELLOW": Style(color="black", bgcolor="yellow"),
            "BLACK": Style(color="white", bgcolor="black"),
            "WHITE": Style(color="black", bgcolor="white")
    } # provides background colours for the cards.

    action_symbols = {
        "REVERSE": "<->",
        "SKIP": "!X!",
        "DRAW2": "+2",
        "WILD": "??",
        "WILD_DRAW4": "??+4"
    }

    card_string = ""
    
    if (card.action != CardAction.Value("NUMBER") 
        and card.action != CardAction.Value("NONE")):
            card_string += action_symbols[CardAction.Name(card.action)]
    else:
        card_string += str(card.value)

    return card_string, colours_style[CardColour.Name(card.colour)]

def print_card(card, console, end="\n"):
    """Calls card_str() to print and format a card."""
    card_out = card_str(card) # returns a string and a style 
    console.print(card_out[0], end=end, style=card_out[1])

BUG_REPORT_STRING = "If you think this is an issue, please submit a bug report at https://www.github.com/Adoria298/Heis/issues. Ensure you include your entire game up to this point, including the method used to start this program."

INTRO_TO_HEIS_STRING = """
HEIS
A Python implementation of the classic card game UNO.

In UNO, everyone starts with seven cards. There are three main types of cards:
numeric cards, that display a number and a colour and nothing more, action 
cards, that generally force the next player to take an action, and wild cards, 
which change the colour to the player's desire. There are four colours, which 
affect what cards can be player: red, green, blue and yellow. In each colour 
there are the numbers 0 to 9, 2 of each action card, a wild card, and a special 
wild card that forces the following player to pick up four cards. There are 
three types of action card as well: the reverse, which changes the direction of 
play so that the previous player plays next; the skip, which skips the next 
player; and the draw 2, which forces the next player to draw 2 cards (and skip 
their turn). The cards are shuffled before being dealt.

HEIS represents the cards textually, using colours to represent the colours, 
and numbers to represent the value of numeric cards. The following symbols are 
used for the remaining cards:

    <-> REVERSE  ??   WILD
    !X! SKIP     ??+4 WILD DRAW 4
    +2  DRAW2 

Where HEIS requires an 'index', it would like a number. This number can be 
obtained by counting through your hand (as represented on the screen) to the 
card you would like, then subtracting one from it. More advanced users may use 
-1 for the final card in your hand, and may proceed from there (e.g. the index 
-2 indicates the second to last card, -3 the third to last). Programmers may 
recognise this as Python's zero indexing system.

Please report any bugs you may have found at https://www.github.com/Adoria298/Heis/issues.
"""
