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
        self.discard_pile = [self.draw_pile[-1]]
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
        """
        Plays card `request`. Returns a StateOfPlay message.

        1. Removes card `request` from the current player's hand.

        2. Checks if the card shares a colour, action or value with the previously 
        played card. If not, checks for a WILD_DRAW4 action, and allows this to 
        be played. If neither check passes, checks for a WHITE NONE card with a 
        negative value, and changes the current player without playing a card 
        (used when all cards that need to be drawn have been drawn). If still 
        no check has passes, raises a ValueError.

        3. Once a card has been played, self.current_player is incremented, or set to 0 if already at len(self.players)-1. 
        """
        print(f"{request} played.")
        last_card = self.discard_pile[-1]
        #current_hand = self.players[self.current_player].hand # not needed yet
        #current_hand.remove(request)
        if (request.colour == last_card.colour
            or request.action == last_card.action
            or request.value == last_card.value):
                self.discard_pile.append(request) 
        elif request.action == uno_pb2.CardAction.Value("WILD_DRAW4"):
            # TODO: implement checks on if this can be played
            self.discard_pile.append(request)
        elif (request.colour == 0 # default colour value - not used in game
            and request.action == 0 # same as above
            and request.value < 0): # unplayable card
                pass # used to make the game advance, for example when all 
                    # cards needed to be drawn have been drawn.
        else: # if reached here, card can't be played.
            raise ValueError(f"{request} is not a valid card.")
        if self.current_player == len(self.players)-1:
            self.current_player = 0
        else:
            self.current_player += 1
        print(f"{request} played.")
        return uno_pb2.StateOfPlay(**self.get_state_of_play())

    def DrawCard(self, request, context):
        print(f"{request.name} wants to draw a card!")
        return self.draw_pile.pop(-1)

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
    #print(s.RequestStateOfPlay(uno_pb2.Player(hand=[], name="", uno_declared=1, score=1), "")) # an empty Player