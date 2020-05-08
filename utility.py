"""
utility.py - Utility code for UNO's GRPC serve, mainly related to presentation.
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
