"""
Client code for UNO's GRPC server.
"""
# imports
## stdlib
from pprint import pprint
## pip modules
import grpc
## proto3 generated modules
from uno_pb2 import Card, Player
import uno_pb2_grpc

with grpc.insecure_channel("localhost:50051") as channel:
    stub = uno_pb2_grpc.UnoStub(channel)
    me = Player(hand=[Card(colour=5, action=6, value=50) for i in range(7)], # ideal hand
                name="Test Player",
                uno_declared=False,
                score=0)
    me = stub.AddPlayer(me) # should ruin my dreams/hand
    print(f"Welcome, {me.name}.")
    state = stub.RequestStateOfPlay(me)
    print("The Discard Pile:", state.discard_pile)
    print("Your Hand:", me.hand)
    card_index = int(input("Please input the index of the card you would like to play: "))
    state = stub.PlayCard(me.hand[card_index])
    print("The Game:", state)

