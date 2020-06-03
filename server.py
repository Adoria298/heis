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
from uno_pb2 import Card, CardAction, CardColour, Player, WinInfo, StateOfPlay, ErrorMessage
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
        self.win_info = {"game_over":False, "ranked_players":self.players}
        print("Server started. Waiting for players.")

    # helper funcs
    def get_state_of_play(self):
        "Returns a dictionary with the format defined in `uno.proto`."
        return {"round_num": self.round_num,
                "players": self.players,
                "discard_pile": self.discard_pile,
                "draw_pile": self.draw_pile,
                "win_info": WinInfo(**self.win_info)}

    def cycle_players(self):
        """"
        Cycles self.players, i.e. puts 1st at last, 2nd at 1st, 3rd at 2nd etc.
        """
        self.players.append(self.players.pop(0))

    def check_for_uno_and_win(self):
        """
        Checks if a player can declare uno and declares it if they can.
        At the same time checks if a player has won.
        If the player has won calls self.someone_won().
        No parameters, no return value.
        """
        for player in self.players:
            if len(player.hand) == 1:
                player.uno_declared = True
            elif len(player.hand) > 1:
                player.uno_declared = False
            else: # must be 0
                self.someone_won()

    def someone_won(self):
        """
        Ends the game. Totals players' scores.

        Game over occurs when a player has no cards left. The player
        with the least points is the winner. 
        """
        for player in self.players:
            for card in player.hand:
                player.score += card.value
        self.win_info["game_over"] = True

        sorted_players = sorted(self.players, key=lambda p: p.score)
        print(f"{sorted_players[0].name} has won.")
        self.win_info["ranked_players"] = sorted_players

    def is_valid_card(self, card, last_card):
        """Checks if `card` can be played on `last_card`.
        
        Both cards are instances of uno_pb2.Card. Returns True or False.

        The following checks are carried out:
            - If `card` shares a colour, action or value with `last_card`.
            - If `card` has a `WILD` or `WILD_DRAW4` action. The colour should be changed by the calling function.
            - If `card` is a `WHITE NONE -1` card, of any value. More action may still be required depending on the particular value.
        """
        def is_valid_wild(card, last_card):
            """Checks if a wild card `card` can be played on card `last_card`.

            Assumes that `card` is either a WILD or WILD_DRAW4.
            """
            if card.action == CardAction.Value("WILD"):
                return True # simple wilds can always be played
            elif card.action == CardAction.Value("WILD_DRAW4"):
                for player_card in self.players[0].hand:
                    if player_card.SerializeToString() != card.SerializeToString():
                        if self.is_valid_card(player_card, last_card):
                            return False # we only want it to return if another card can be played.
                    # no action if the player card is the card being tested.
                return True
            else:
                return False # not a WILD

        if (card.colour == last_card.colour
            or card.action == last_card.action
            or card.value == last_card.value):
                if card.action == CardAction.Value("NUMBER"): # check same colour or number
                    if (card.colour == last_card.colour
                        or card.value == last_card.value):
                            return True
                    else: # stops two number cards being played after each other when they're otherwise incompatible.
                        return False
                elif card.action in [CardAction.Value("REVERSE"), CardAction.Value("DRAW2"), CardAction.Value("SKIP")]:
                    if (card.colour == last_card.colour
                        or card.action == last_card.action):
                            return True
                    else: # stops two action cards being valid because they share the same value
                        return False
                else:
                    if card.action in [CardAction.Value("WILD"), CardAction.Value("WILD_DRAW4")]:
                        return is_valid_wild(card, last_card)
                    else: # special cards are always valid
                        return True
        elif (card.action == CardAction.Value("WILD_DRAW4")
            or card.action == CardAction.Value("WILD")):
                return is_valid_wild(card, last_card)
        elif (card.colour == 0 # default colour value - not used in game
            and card.action == 0 # same as above
            and card.value == -1): # unplayable card
                # used to make the game advance, for example when all 
                # cards needed to be drawn have been drawn.
                # still played so clients don't enter an infinite loop of card 
                # drawing.
                return True

    def raise_internal_error(self, message, context):
        """
        Calls context.set_details and context.set_code appropriately.
        Params:
            - message: An string of an ErrorMessage name, as defined as the enum ErrorMessage in uno.proto. NB it is converted into the enum here.
            - context: an RPC context parameter.
        No return value. The calling function *must* return an empty instance immediately after this is called.
        """
        if message in [ErrorMessage.Name(m) for m in ErrorMessage.values()]:
            context.set_details(message)
            context.set_code(grpc.StatusCode.INTERNAL)
            print(f"A {message} error occured.")
        else:
            raise ValueError(f"'{message}' is not a valid internal error message'")

    def RequestStateOfPlay(self, request, context):
        print(f"State of Play requested by {request.name}")
        for player in self.players:
            if player.name == request.name:
                player = request
        return StateOfPlay(**self.get_state_of_play())
    
    def PlayCard(self, request, context):
        """
        Plays card `request`. Returns a StateOfPlay message.

        1. Checks if the card shares a colour, action or value with the 
        previously played card. If not, checks for a WILD_DRAW4 action, and 
        allows this to be played. If neither check passes, checks for a WHITE 
        NONE card with a negative value, and changes the current player and 
        plays this card (used when all cards that need to be drawn have been 
        drawn). 
        NB when a WHITE NONE card has been played, it should be omitted in a 
        client's output. 
        
        If no check has yet passed, it returns an empty state of play and sets the error code to INTERNAL, with the details to "CARD_UNPLAYABLE".

        The server will then remove the card from the player's hand it the card can be played.

        2. If the card is a SKIP card, then skips the next player by 
        incrementing self.current_player twice. If the card is a REVERSE card, 
        reverses self.players. If the card is WILD* card, randomises its colour.
        
        It is the responsibility of the client to draw the necessary cards on 
        DRAW* cards.

        3. Once a card has been played, self.current_player is incremented, or 
        set to 0 if already at len(self.players)-1. 
        """
        index = -1
        try:
            while self.discard_pile[index] == Card(colour=0, action=0, value=-1):
                # if cards have just been drawn
                index -= 1
        except IndexError:
            index += 1
        last_card=self.discard_pile[index]
        if self.is_valid_card(request, last_card):
            self.discard_pile.append(request)
            # remove card played from the player's hand
            for index, card in enumerate(self.players[0].hand):
                if card == request:
                    self.players[0].hand.pop(index)
        else:
            self.raise_internal_error("CARD_UNPLAYABLE", context)
            return StateOfPlay()
        self.check_for_uno_and_win()
        self.cycle_players()
        if request.action == CardAction.Value("SKIP"):
            self.cycle_players() # an extra increment to skip the next player
        if request.action == CardAction.Value("REVERSE"):
            self.players = self.players[::-1] # reverses order of players
        if (request.action == CardAction.Value("WILD_DRAW4") # randomly change colour
            or request.action == CardAction.Value("WILD")): 
                while (request.colour == CardColour.Value("BLACK") # default WILD colour
                    or request.colour == CardColour.Value("WHITE")): # unplayable
                        request.colour = random.choice(CardColour.values())
        print(f"{request} played.")
        return StateOfPlay(**self.get_state_of_play())

    def DrawCard(self, request, context):
        print(f"{request.name} wants to draw a card!")
        return self.draw_pile.pop(-1)

    def AddPlayer(self, request, context): # request is a new player
        print(f"Adding player {request.name}.")
        for player in self.players:
            if player.name == request.name:
                self.raise_internal_error("NAME_TAKEN", context)
                return Player()
        if len(self.players) <= 10:
            hand = []
            for i in range(7):
                hand.append(self.draw_pile.pop(i))
            new_player = Player(hand=hand,
                                        name=request.name,
                                        uno_declared=False,
                                        score=0)
            self.players.append(new_player)
            print(f"Added player {new_player.name}")
            return new_player
        else:
            self.raise_internal_error("TOO_MANY_PLAYERS", context)
            return Player()

    def RemovePlayer(self, request, context):
        print(f"Removing {request.name} from the game.")
        for i, player in enumerate(self.players):
            if request.name == player.name:
                print(f"{request.name} has left.")
                return self.players.pop(i)
        self.raise_internal_error("PLAYER_NOT_FOUND", context)
        return Player()


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