"""
Client code for UNO's GRPC server.
"""
# imports
## stdlib
from pprint import pprint
## pip modules
import grpc
## proto3 generated modules
import uno_pb2
import uno_pb2_grpc

channel = grpc.insecure_channel("localhost:50051")
stub = uno_pb2_grpc.UnoStub(channel)

print("Getting state.")
state = stub.RequestStateOfPlay(uno_pb2.Player(hand=[
        uno_pb2.Card(colour=3, action=4, value=20), # a green skip
        uno_pb2.Card(colour=5, action=5, value=50), # an undecided wild
        uno_pb2.Card(colour=1, action=1, value=1)], # a red 1
    name="Test Player",
    uno_declared=False,
    score=72))
pprint(stub)

print("Playing a green skip.")
new_state = stub.PlayCard(uno_pb2.Card(colour=3, action=4, value=20))
pprint(new_state)

print("Drawing card.")
new_card = stub.DrawCard(uno_pb2.Player(hand=[
    uno_pb2.Card(colour=5, action=5, value=50), # an undecided (black) wild
    uno_pb2.Card(colour=1, action=1, value=1)], # a red 1
    name="Test Player",
    uno_declared=False,
    score=72))
pprint(new_card)