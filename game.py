import piles, cards

class Game:
    def setup (self)
    self.deck = piles.Deck()
    self.discard_pile = piles.DiscardPile()
    self.draw_pile = piles.DrawPile()
    self.num_players = int(input("How many players (please input an integer)? "))
    if num_players < 2:
        print("Not enough players.")
    elif num_players > 10:
        print("Too many players")
    self.players = []
    for i in range(num_players):
        self.players.append(Player(deck=deck, draw_pile=draw_pile, discard_pile=discard_pile))
    self.deck.shuffle()
