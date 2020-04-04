import piles, cards

# setup
deck = piles.Deck()
discard_pile = piles.DiscardPile()
draw_pile = piles.DrawPile()
num_players = int(input("How many players (please input an integer)? "))
if num_players < 2:
    print("Not enough players.")
elif num_players > 10:
    print("Too many players")
players = []
for i in range(num_players):
    players.append(Player(deck=deck, draw_pile=draw_pile, discard_pile=discard_pile))
deck.shuffle()
