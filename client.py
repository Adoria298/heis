"""
Client code for UNO's GRPC server.
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

#TODO: manage invalid cards
#TODO: improve output formatting

name = input("Identify yourself! ")

with grpc.insecure_channel("localhost:50051") as channel:
    stub = uno_pb2_grpc.UnoStub(channel)
    me = Player(hand=[Card(colour=5, action=6, value=50) for i in range(7)], # ideal hand
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
                card_index = int(input("Please input the index of the card you would like to play: "))
                state = stub.PlayCard(me.hand.pop(card_index))
            else:
                print("Someone else is playing right now.")
                time.sleep(30)
                state = stub.RequestStateOfPlay(me)
    except KeyboardInterrupt:
        print("Ctrl+C pressed. Terminating")
    finally:
        # game over
        stub.RemovePlayer(me)

