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
## proto3 generated modules
from uno_pb2 import Card, Player
import uno_pb2_grpc
# homemade
import client_cmds

#TODO: manage invalid cards
#TODO: improve output formatting
#TODO: implement drawing cards - mini DSL?

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
        while len(me.hand) > 0:
            if state.players[state.current_player].name == me.name:
                print("Your turn!")
                print("The Discard Pile:"); pprint(state.discard_pile)
                print("Your Hand:"); pprint(me.hand)
                #card_index = int(input("Please input the index of the card you would like to play: "))
                #card = me.hand.pop(card_index)
                #state = stub.PlayCard(card)
                try:
                    cmd, args = input("> ").split()
                    state = client_cmds.cmds[cmd.upper()](stub, me, args)
                except Exception as e:
                    print(f"An error has occured with the input {cmd} {args}.")
                    print("Details:", e)
                    print("Please try again.")
            else:
                print("Someone else is playing right now.")
                time.sleep(30) # 30 seconds feels right - 10 too quick; 60 too slow
                state = stub.RequestStateOfPlay(me)
    except KeyboardInterrupt:
        print("Ctrl+C pressed. Terminating")
    finally:
        # game over
        stub.RemovePlayer(me)

