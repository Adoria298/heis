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

channel = grpc.insecure_channel("localhost:50051")
stub = uno_pb2_grpc.UnoStub(channel)
me = Player(hand=[Card(colour=5, action=6, value=50) for i in range(7)], # ideal hand
            name="Test Player",
            uno_declared=False,
            score=0)
me = stub.AddPlayer(me) # should ruin my dreams/hand


print("Getting state.")
state = stub.RequestStateOfPlay(me)
pprint(stub)

print("Playing a green skip.")
new_state = stub.PlayCard(Card(colour=3, action=4, value=20))
pprint(new_state)

print("Drawing card.")
new_card = stub.DrawCard(Player(hand=[
    Card(colour=5, action=5, value=50), # an undecided (black) wild
    Card(colour=1, action=1, value=1)], # a red 1
    name="Test Player",
    uno_declared=False,
    score=72))
pprint(new_card)