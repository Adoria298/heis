"""
client.py - Basic client code for UNO's GRPC server.
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

----

This is not designed to be used by an end user as it is intended for testing the GRPC server itself. As such it is used on the same device as the server.
It should be a playable game.
"""
# imports
## stdlib
from pprint import pprint
import time
## pip modules
import grpc
import colorama as c
## proto3 generated modules
from uno_pb2 import Card, Player, CardColour, CardAction
import uno_pb2_grpc
# homemade
import client_cmds

def card_str(card):
    """
    Takes a `card` (uno_pb2.Card) and returns a string with a background colour.
    Uses colorama to make ASCII escape sequences work on Windows.
    The colour is the card's colour, and the string is either the card's action 
    or the card's value, depending on whether the card is an action card or not.
    """
    back_colours = {
            "RED": c.Back.RED,
            "BLUE": c.Back.BLUE,
            "GREEN": c.Back.GREEN,
            "YELLOW": c.Back.YELLOW,
            "BLACK": c.Back.BLACK,
            "WHITE": c.Back.WHITE
    } # background colours for the cards.

    fmt_string = back_colours[CardColour.Name(card.colour)]
    
    if (card.action != CardAction.Value("NUMBER") 
        and card.action != CardAction.Value("NONE")):
            fmt_string += CardAction.Name(card.action)
    else:
        fmt_string += str(card.value)

    fmt_string += c.Style.RESET_ALL

    return fmt_string

name = input("Identify yourself! ")

with grpc.insecure_channel("localhost:50051") as channel:
    stub = uno_pb2_grpc.UnoStub(channel)
    me = Player(hand=[Card(colour=5, action=6, value=50) for i in range(7)], # ideal hand - 7 black WILD_DRAW4s
                name=name,
                uno_declared=False,
                score=0)
    me = stub.AddPlayer(me) # should ruin my dreams/hand
    state = stub.RequestStateOfPlay(me) # initial state
    print(f"Welcome, {me.name}. I'm sorry I didn't recognise you.")
    try:
        # main game loop
        while len(me.hand) > 0:
            if state.players[state.current_player].name == me.name:
                # presentation
                print("Your turn!")
                print("The Last Card Played:")
                if state.discard_pile[-1] == Card(colour=0, action=0, value=-1):
                    # if cards have just been drawn
                    last_card = state.discard_pile[-2]
                else:
                    last_card = state.discard_pile[-1]
                print(card_str(last_card))
                print("Your Hand:") 
                for card in me.hand: 
                    print(card_str(card), end=" ")
                print()

                # player (in)action
                last_player = state.players[-1]
                if (last_card.action == CardAction.Value("DRAW2")
                    and state.discard_pile[-1] != Card(colour=0, action=0, value=-1)): # checks to prevent +2 infinite loop
                        print(f"You draw two cards because {last_player.name} played a +2 card.")
                        state = client_cmds.draw(stub, me, 2)
                elif (last_card.action == CardAction.Value("WILD_DRAW4")
                    and state.discard_pile[-1] != Card(colour=0, action=0, value=-1)): # checks to prevent +4 infinite loop
                        print(f"You draw four cards because {last_player.name} played a Wild +4 card.")
                        state = client_cmds.draw(stub, me, 4)
                else: # player can play!
                    try:
                        cmd, args = input("> ").split()
                        state = client_cmds.cmds[cmd.upper()](stub, me, args)
                    except Exception as e:
                        print(f"An error has occured with the input {cmd} {args}.")
                        print("Details:", e)
                        print("Please try again.")
            else: # check again in 30s
                print(f"{state.players[0].name} is playing right now.")
                time.sleep(30) # 30 seconds feels right - 10 too quick; 60 too slow
                state = stub.RequestStateOfPlay(me)
    except KeyboardInterrupt:
        print("Ctrl+C pressed.")
    finally:
        # game over
        print("Terminating.")
        stub.RemovePlayer(me)
        input("Press enter to exit. ")

