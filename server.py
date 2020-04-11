"""
Uses code based on protocol buffers file `uno.proto` to create a GRPC server.
Implements uno_pb2_grpc.UnoServicer and a serve() method, which is then called.
"""
# imports
## stdlib
from concurrent import futures
import random
## pip modules
import grpc
## proto3 generated code
import uno_pb2
import uno_pb2_grpc
## homemade code
from deck import Deck

class UnoServicer(uno_pb2_grpc.UnoServicer):
    def __init__(self):
        super().__init__() # just in case
        self.draw_pile = Deck().cards
        random.shuffle(self.draw_pile)
        self.players = []
        self.discard_pile = self.draw_pile[-1]
        self.round_num = 0
        self.round_over = False
        self.game_over = False
        self.current_player = 0

    def get_state_of_play(self):
        return {"round_num": self.round_num,
                "players": self.players,
                "current_player": self.current_player,
                "discard_pile": self.discard_pile,
                "draw_pile": self.draw_pile,
                "round_over": self.round_over,
                "game_over": self.game_over}

    def RequestStateOfPlay(self, request, context):
        print(f"State of Play requested by {request.name}")
        return uno_pb2.StateOfPlay(**self.get_state_of_play())
    
    def PlayCard(self, request, context):
        print(f"{request} played.")
        return uno_pb2.StateOfPlay(round_num = 3,
            players = [uno_pb2.Player(
                    hand = Deck().cards[:6],
                    name="Test",
                    uno_declared = False,
                    score = 0),
                uno_pb2.Player(
                    hand = Deck().cards[7:9],
                    name="Test 2",
                    uno_declared = False,
                    score = 0)],
            current_player = 1,
            discard_pile = Deck().cards[8:53],
            draw_pile = Deck().cards[54:89],
            round_over = False,
            game_over = False)

    def DrawCard(self, request, context):
        print(f"{request.name} wants to draw a card!")
        return uno_pb2.Card(colour=3,# green
            action=4, # skip
            value=20)

    def AddPlayer(self, request, context): # request is a new player
        print(f"Adding player {request.name}.")
        if len(self.players) <= 10:
            hand = []
            for i in range(7):
                hand.append(self.draw_pile.pop(i))
            new_player = uno_pb2.Player(hand=hand,
                                        name=request.name,
                                        uno_declared=False,
                                        score=0)
            self.players.append(new_player)
            return new_player
        else:
            return uno_pb2.Player(hand=[], name="TOO MANY PLAYERS", uno_declared=True, score=-1)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    uno_pb2_grpc.add_UnoServicer_to_server(UnoServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("Ctrl+C pressed. Terminating.")

if __name__ == "__main__":
    serve()
    # test code
    #s = UnoServicer()
    #print(s.PlayCard(uno_pb2.Card(colour=3, action=5, value=50), "")) # a wild that changes the colour to green