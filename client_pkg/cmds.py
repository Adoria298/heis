"""
client_cmds.py - Stores available commands for client.py
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

---

All functions in this file have two mandatory parameters (stub and player), 
which are always the same, then have *args specific to themselves. They also 
all return the StateOfPlay. 

The _help variable in each function provides a helpful message for the user. 
The docstring of each function is intended for the programmer.
"""
import uno_pb2, grpc
from utility import INTRO_TO_HEIS_STRING

def play(stub, player, *args):
    """
    Plays a card by taking the card at the 0-index `index` of `hand`.
    Returns the StateOfPlay.
    Parameters:
        - stub: instance of uno_pb2_grpc.UnoStub.
        - player: instance of uno_pb2.Player
        - *args:  
            - 1st arg is a valid index of hand.
    Returns a StateOfPlay object.
    """
    card = player.hand.pop(int(args[0]))
    if len(player.hand) == 1:
        player.uno_declared = True
        print("You Declared Uno!")
    try:
        return stub.PlayCard(card)
    except grpc.RpcError as e: # put the card back in your hand then let the client deal with the problem
        player.hand.append(card)
        raise e

def draw(stub, player, *args):
    """
    Draws cards and appends them to a player's hand. Returns the StateOfPlay.
    Plays WHITE NONE -1 Card to advance play and get the StateOfPlay.
    Parameters:
        - stub: instance of uno_pb2_grpc.UnoStub.
        - player: instance of uno_pb2.Player
        - *args: 
            - 1st arg is the number of cards to be drawn.
    Returns a StateOfPlay object.
    """
    num = int(args[0])
    for i in range(num):
        player.hand.append(stub.DrawCard(player))
    return stub.PlayCard(uno_pb2.Card(colour=0, action=0, value=-1))

def heis_help(stub, player, *args):
    """
    Prints out help messages.
    Parameters:
        - stub: instance of uno_pb2_grpc.UnoStub.
        - player: instance of uno_pb2.Player
        - *args: List of strings that help is needed with.
            - "heis": prints out all help messages with a general introduction to the game
            - "play": prints out help for command play
            - "draw": prints out help for command draw
    Returns the StateOfPlay.
    """
    args = [arg.lower() for arg in args]
    play_help = "PLAY\nUsage: PLAY {index}, eg 'PLAY 2' plays the 3rd card in your hand. This is probably the most common command."
    draw_help = "DRAW\nUsage: DRAW {number}, eg 'DRAW 2' draws two cards. This is used for tactical reasons or when you have no cards that can be played in your hand."
    if "heis" in args:
        print(INTRO_TO_HEIS_STRING)
        print("Available commands: ")
        print(play_help)
        print(draw_help)
    else:
        if "play" in args:
            print(play_help)
        elif "draw" in args:
            print(draw_help)
        else:
            print(f"Arguments to 'HELP' not recognised: {args}")
    # returning anything but a State of Play causes the client to exit.
    return stub.RequestStateOfPlay(player)

cmds = {
    "PLAY": play,
    "DRAW": draw,
    "HELP": heis_help
}