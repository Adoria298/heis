"""
Uses code based on protocol buffers file `uno.proto` to create a GRPC server.
"""
# proto3 generated code
import uno_pb2
import uno_pb2_grpc
# homemade code
from deck import Deck

class UnoServicer(uno_pb2_grpc.UnoServicer):
    """
    Runs the game.
    """

    def RequestStateOfPlay(self, request, context):
        print(f"State of Play requested by {request.name}")
        return uno_pb2.StateOfPlay(round_num = 3,
            players = [uno_pb2.Player(
                    hand = Deck().cards[:6],
                    name="Test",
                    uno_declared = False,
                    score = 0),
                uno_pb2.Player(
                    hand = Deck().cards[7],
                    name="Test 2",
                    uno_declared = True,
                    score = 0)],
            current_player = 1,
            discard_pile = Deck().cards[8:53],
            draw_pile = Deck().cards[54:89],
            round_over = False,
            game_over = False)
    
    def PlayCard(self, request, context):
        print(f"{request} played.")
        return uno_pb2.StateOfPlay(round_num = 3,
            players = [uno_pb2.Player(
                    hand = Deck().cards[:6],
                    name="Test",
                    uno_declared = False,
                    score = 0),
                uno_pb2.Player(
                    hand = Deck().cards[7],
                    name="Test 2",
                    uno_declared = True,
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
if __name__ == "__main__":
    from pprint import pprint
    pprint(Deck().cards)