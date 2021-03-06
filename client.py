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
# stdlib
from pprint import pprint
import time
from sys import argv
# pip modules
import grpc
# rich - terminal support
from rich.traceback import install  # improved traceback formatting
from rich.console import Console  # improved terminal management
from rich.style import Style  # text styles
# proto3 generated modules
from uno_pb2 import Card, Player, CardColour, CardAction, StateOfPlay
import uno_pb2_grpc
# homemade
import client_cmds
from utility import print_card, BUG_REPORT_STRING

# TODO: Implement multidevice play (LAN)

# setup
install()  # adds rich formatting for errors
console = Console()
DEBUG_MODE = False
HOST_IP = "localhost:50051"

if len(argv) > 1:
    if argv[1] == "--debug":
        DEBUG_MODE = True
        HOST_IP = argv[2]
    else:
        print("Usage: python3 client.py [--debug HOST_IP]")
        input("Press enter to exit.")
        quit()

# main game
name = input("Identify yourself! ")

with grpc.insecure_channel(HOST_IP) as channel:
    stub = uno_pb2_grpc.UnoStub(channel)
    me = Player(hand=[Card(colour=5, action=6, value=50) for i in range(7)],  # ideal hand - 7 black WILD_DRAW4s
                name=name,
                uno_declared=False,
                score=0)
    try:
        me = stub.AddPlayer(me)  # should ruin my dreams/hand
    except grpc.RpcError as e:  # just in case name already taken
        print("There were so many problems with that name that I'm giving up.")
        if DEBUG_MODE:
            print(e.code())
            print(e.details)
        quit()
    state = stub.RequestStateOfPlay(me)  # initial state
    print(f"Welcome, {me.name}, to HEIS. I'm sorry I didn't recognise you.")
    try:
        # main game loop
        while len(me.hand) > 0:  # every run of this loop must end with an updated state
            for player in state.players:
                if player.uno_declared:
                    print(f"{player.name} declared UNO!")
            if state.players[0].name == me.name:
                # presentation
                print("Your turn!")
                print("The Last Card Played:")
                # when multiple cards are drawn by multiple players, two cards back is a WHITE NONE -1.
                index = -1
                try:  # find the correct index for last_card
                    while state.discard_pile[index] == Card(colour=0, action=0, value=-1):
                        # if cards have just been drawn
                        index -= 1
                except IndexError:
                    index += 1
                last_card = state.discard_pile[index]
                print_card(last_card, console)
                print("Your Hand:")
                for card in me.hand:
                    print_card(card, console, end=" ")
                print()

                # player (in)action
                last_player = state.players[-1]
                if (last_card.action == CardAction.Value("DRAW2")
                        and state.discard_pile[-1] != Card(colour=0, action=0, value=-1)):  # checks to prevent +2 infinite loop
                    print(
                        f"You draw two cards because {last_player.name} played a +2 card.")
                    state = client_cmds.draw(stub, me, 2)
                elif (last_card.action == CardAction.Value("WILD_DRAW4")
                      and state.discard_pile[-1] != Card(colour=0, action=0, value=-1)):  # checks to prevent +4 infinite loop
                    print(
                        f"You draw four cards because {last_player.name} played a Wild +4 card.")
                    state = client_cmds.draw(stub, me, 4)
                else:  # player can play!
                    try:
                        cmd, args = input("> ").split()
                        state = client_cmds.cmds[cmd.upper()](stub, me, args)
                    except grpc.RpcError as e:
                        if e.details() == "CARD_UNPLAYABLE":
                            print("You can't play that card.")
                        else:
                            print(
                                f"The following error occured with the input '{cmd} {args}'.")
                            print(f"Details: \n{e.details()}")
                            if DEBUG_MODE:
                                print(f"Status code name: {e.code().name}")
                                print(f"Status code value: {e.code().value}")
                            print(BUG_REPORT_STRING)
                        print("Please try again.")
                    except Exception as e:
                        print(
                            f"An error has occured with the input '{cmd} {args}'.")
                        print("Details:", e)
                        print(BUG_REPORT_STRING)
                        print("Please try again.")
            else:  # check again in 30s
                print(f"{state.players[0].name} is playing right now.")
                # save calls on the server
                if not DEBUG_MODE:  # waiting code
                    # 30 seconds feels right - 10 too quick; 60 too slow
                    time.sleep(30)
                else:  # make debugging quicker
                    time.sleep(10)
                state = stub.RequestStateOfPlay(me)
    except KeyboardInterrupt:
        print("Ctrl+C pressed.")
    finally:
        state = stub.RequestStateOfPlay(me)
        if state.win_info.game_over:  # see who won
            winner = state.win_info.ranked_players[0]
            if winner.name == me.name:
                print("You won!")
            else:
                print(f"{winner.name} won!")
        # game over
        print("Terminating.")
        stub.RemovePlayer(me)
        input("Press enter to exit. ")
