"Code entirely for making a deck"
import uno_pb2
from dataclasses import dataclass
@dataclass
class Deck():
    """
    Creates a full deck, as described in __init__.
    Used like this:
    ````py 
    deck = Deck().cards
    print(deck)
    ````
    """
    def __init__(self):
        """
        Returns a list of cards to form an UNO deck.

        A Deck contains 108 cards:
        - 19 Blue
        - 19 Green
        - 19 Red
        - 19 Yellow
        - 8 Draw Two - 2 of each colour (i.e. RGBY)
        - 8 Reverse - 2 of each colour
        - 8 Skip - 2 of each colour
        - 4 Wild
        - 4 Wild Draw Four

        The number cards have the numbers 0-9, with 1-9 repeated (i.e. they have two of every number
        between 0 and 9 except 0, which they only have one of.) NB due to using `proto3` as a backend format, cards with a value of 0, of which there are four (one in each colour), do not have a value created in python.
        """
        self.cards = []
        for colour in (uno_pb2.CardColour.Value("RED"), uno_pb2.CardColour.Value("BLUE"), uno_pb2.CardColour.Value("GREEN"), uno_pb2.CardColour.Value("YELLOW")):
            for i in range(0, 10): # stop point is exclusive
                self.cards.append(self.NumCard(colour, value=i))
            for i in range(1, 10): # start point is inclusive    
                self.cards.append(self.NumCard(colour, value=i))
            for i in range(2):
                self.cards.append(self.ActionCard(colour, "DRAW2"))
                self.cards.append(self.ActionCard(colour, "REVERSE"))
                self.cards.append(self.ActionCard(colour, "SKIP"))        
        for i in range(4):
            self.cards.append(self.WildCard())
            self.cards.append(self.WildCard(isWildDraw4Card=True))

    def __len__(self):
        return len(self.cards)

    # card generators
    def NumCard(self, colour, value):
        card = uno_pb2.Card()
        card.colour = colour
        card.action = uno_pb2.CardAction.Value("NUMBER")
        card.value = value
        return card
    def ActionCard(self, colour, action):
        card = uno_pb2.Card()
        card.colour = colour
        card.action = uno_pb2.CardAction.Value(action)
        card.value = 20
        return card
    def WildCard(self, isWildDraw4Card = False):
        card = uno_pb2.Card()
        card.colour = uno_pb2.CardColour.Value("BLACK")
        card.value = 50
        if isWildDraw4Card:
            card.action = uno_pb2.CardAction.Value("WILD_DRAW4")
        else:
            card.action = uno_pb2.CardAction.Value("WILD")
        return card

if __name__ == "__main__":
    from pprint import pprint
    pprint(Deck().cards)