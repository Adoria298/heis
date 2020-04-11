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

#TODO: manage turns
#TODO: manage invalid cards
#TODO: improve output formatting
#TODO: allow players to leave

with grpc.insecure_channel("localhost:50051") as channel:
    stub = uno_pb2_grpc.UnoStub(channel)
    me = Player(hand=[Card(colour=5, action=6, value=50) for i in range(7)], # ideal hand
                name="Test Player",
                uno_declared=False,
                score=0)
    me = stub.AddPlayer(me) # should ruin my dreams/hand
    state = stub.RequestStateOfPlay(me) # initial state
    print(f"Welcome, {me.name}.")
    while len(me.hand) > 0:
        print("The Discard Pile:"); pprint(state.discard_pile)
        print("Your Hand:"); pprint(me.hand)
        card_index = int(input("Please input the index of the card you would like to play: "))
        state = stub.PlayCard(me.hand.pop(card_index))

    # game over
    stub.RemovePlayer(me)

