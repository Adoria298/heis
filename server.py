"""
Uses code based on protocol buffers file `uno.proto` to create a GRPC server.
"""
import uno_pb2 as uno_pb2
import uno_pb2_grpc as uno_pb2_grpc

# manually check files compiled correctly
#print(help(uno_pb2))
#print(help(uno_pb2_grpc))

def create_deck():
    """
    Returns a list of cards to form an UNO deck.

    A Deck contains 108 cards:
     - 19 Blue
     - 19 Green
     - 19 Red
     - 19 Yellow
     - 8 Draw Two - 2 of each colour
     - 8 Reverse - 2 of each colour
     - 8 Skip - 2 of each colour
     - 4 Wild
     - 4 Wild Draw Four

    The number cards have the numbers 0-9, with 1-9 repeated (i.e. they have two of every number
    between 0 and 9 except 0, which they only have one of.)
    """
    # card generators
    def NumCard(colour, value):
        card = uno_pb2.Card()
        card.colour = colour
        card.action = uno_pb2.Value("NUMBER")
        card.value = value
        return card
    def ActionCard(colour, action):
        card = uno_pb2.Card()
        card.colour = colour
        card.action = uno_pb2.Value(action)
        card.value = 20
        return card
    def WildCard(isWildDraw4Card = False):
        card = uno_pb2.Card()
        card.colour = uno_pb2.Value("BLACK")
        card.value = 50
        if isWildDraw4Card:
            card.action = uno_pb2.Value("WILD_DRAW4")
        else:
            card.action = uno_pb2.Value("WILD")
        return card
 
    cards = []
    for colour in (uno_pb2_grpc.Value("RED"), uno_pb2_grpc.Value("BLUE"), uno_pb2_grpc.Value("GREEN"), uno_pb2_grpc.Value("YELLOW")):
        for i in range(0, 10): # stop point is exclusive
            cards.append(NumCard(colour, value=i))
        for i in range(1, 10): # start point is inclusive    
            cards.append(NumCard(colour, value=i))
        for i in range(2):
            cards.append(ActionCard(colour, "DRAW2"))
            cards.append(ActionCard(colour, "REVERSE"))
            cards.append(ActionCard(colour, "SKIP"))        
    for i in range(4):
        cards.append(WildCard())
        cards.append(WildCard(isWildDraw4Card=True))
    return cards

if __name__ == "__main__":
    from pprint import pprint
    pprint(create_deck())