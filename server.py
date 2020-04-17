"""
server.py - GRPC server for UNO.
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

This uses code based on protocol buffers file `uno.proto` to create a GRPC 
server.
It implements uno_pb2_grpc.UnoServicer and a serve() method, which is then 
called.
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
        print("Server started. Waiting for players.")

    # helper funcs
    def get_state_of_play(self):
        "Returns a dictionary with the format defined in `uno.proto`."
        return {"round_num": self.round_num,
                "players": self.players,
                "current_player": self.current_player,
                "discard_pile": self.discard_pile,
                "draw_pile": self.draw_pile,
                "round_over": self.round_over,
                "game_over": self.game_over}

    def increment_current_player(self):
        "Increments self.current_player or resets it to 0 if it equals len(self.player)-1."
        if self.current_player == len(self.players)-1:
            self.current_player = 0
        else:
            self.current_player += 1

    def RequestStateOfPlay(self, request, context):
        print(f"State of Play requested by {request.name}")
        return uno_pb2.StateOfPlay(**self.get_state_of_play())
    
    def PlayCard(self, request, context):
        """
        Plays card `request`. Returns a StateOfPlay message.

        1. Checks if the card shares a colour, action or value with the previously 
        played card. If not, checks for a WILD_DRAW4 action, and allows this to 
        be played. If neither check passes, checks for a WHITE NONE card with a 
        negative value, and changes the current player and plays this card 
        (used when all cards that need to be drawn have been drawn). NB when a 
        WHITE NONE card has been played, it should be omitted in a client's 
        output. If still no check has passed, raises a ValueError.

        It is the responsibilty of the client to remove the card from the player's hand.

        2. If the card is a SKIP card, then skips the next player by 
        incrementing self.current_player twice. If the card is a REVERSE card, reverses self.players. If the card is WILD* card, randomises its colour.
        
        It is the responsibility of the client to draw the necessary cards on 
        DRAW* cards.

        3. Once a card has been played, self.current_player is incremented, or 
        set to 0 if already at len(self.players)-1. 
        """
        last_card = self.discard_pile[-1]
        if (request.colour == last_card.colour
            or request.action == last_card.action
            or request.value == last_card.value):
                self.discard_pile.append(request) 
        elif (request.action == uno_pb2.CardAction.Value("WILD_DRAW4")
            or request.action == uno_pb2.CardAction.Value("WILD")):
                # TODO: implement checks on if this can be played
                request.colour = random.choice(uno_pb2.CardColour.values())
                self.discard_pile.append(request)
        elif (request.colour == 0 # default colour value - not used in game
            and request.action == 0 # same as above
            and request.value == -1): # unplayable card
                self.discard_pile.append(request)
                # used to make the game advance, for example when all 
                # cards needed to be drawn have been drawn.
                # still played so clients don't enter an infinite loop of card 
                # drawing.
        else: # if reached here, card can't be played.
            raise ValueError(f"{request} is not a valid card.")
        self.increment_current_player()
        if request.action == uno_pb2.CardAction.Value("SKIP"):
            self.increment_current_player() # an extra increment to skip the next player
        if request.action == uno_pb2.CardAction.Value("REVERSE"):
            self.players = self.players[::-1] # reverses order of players
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
            print(f"Added player {new_player.name}")
            return new_player
        else:
            return uno_pb2.Player(hand=[], name="TOO MANY PLAYERS", uno_declared=True, score=-1)

    def RemovePlayer(self, request, context):
        for i, player in enumerate(self.players):
            if request == player:
                print(f"{request.name} has left.")
                return self.players.pop(i)


def serve():
    """
    Creates a GRPC server and adds UnoServicer to the server.
    Starts the server on [::]:500051.
    Catches KeyboardInterrupt to gracefully exit.
    """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    uno_pb2_grpc.add_UnoServicer_to_server(UnoServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("Ctrl+C pressed. Terminating.")

if __name__ == "__main__":
    print("Starting server.")
    serve()
    # test code - used when client.py returns an _IncativeRpcError, which is overly verbose
    #s = UnoServicer()
    #print(s.RequestStateOfPlay(uno_pb2.Player(hand=[], name="", uno_declared=1, score=1), "")) # an empty Player