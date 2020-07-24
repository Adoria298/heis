"""
gui.py - A Tkinter-based GUI for HEIS.
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

---

Creates a client for HEIS, relying on backend.py, and represents it to the user as a tkinter GUI.
"""
# imports
## stdlib
from tkinter import *
from tkinter.ttk import *
## pip
import grpc
## homemade
from client_pkg.backend import Backend
### protoc generated
from uno_pb2 import Card, CardColour, CardAction

class CardDisplay(LabelFrame):
    """
    tkinter.ttk.Frame that draws a player's hand.
    """
    def __init__(self, master, label, hand, **kw):
        super().__init__(master, text=label, **kw)
        self.hand = hand
        self.card_btns = []
        self.draw_widgets()
        self.pack()
    
    def draw_widgets(self):
        s = Style(self)
        s.configure("Red.TButton", background="red")
        s.configure("Green.TButton", background="green")
        s.configure("Yellow.TButton", background="yellow")
        s.configure("Blue.TButton", background="blue")
        s.configure("Black.TButton", background="black")
        s.configure("White.TButton", background="white")
        for card in self.hand:
            btn = Button(master=self)
            # colours - changes the default style
            if card.colour == CardColour.Value("RED"):
                btn["style"] = "Red.TButton"
            elif card.colour == CardColour.Value("GREEN"):
                btn["style"] = "Green.TButton"
            elif card.colour == CardColour.Value("YELLOW"):
                btn["style"] = "Yellow.TButton"
            elif card.colour == CardColour.Value("BLUE"):
                btn["style"] = "Blue.TButton"
            elif card.colour == CardColour.Value("BLACK"):
                btn["style"] = "Black.TButton"
            elif card.colour == CardColour.Value("WHITE"):
                btn["style"] = "White.TButton"

            # actions
            if card.action == CardAction.Value("NUMBER") or card.action == CardAction.Value("NONE"):
                btn["text"] = str(card.value)
            elif card.action == CardAction.Value("REVERSE"):
                btn["text"] = "<->"
            elif card.action == CardAction.Value("DRAW2"):
                btn["text"] = "+2"
            elif card.action == CardAction.Value("SKIP"):
                btn["text"] = "!X!"
            elif card.action == CardAction.Value("WILD"):
                btn["text"] = "??"
            elif card.action == CardAction.Value("WILD_DRAW4"):
                btn["text"] = "??+4"
            else:
                btn["text"] = str(card)

            btn.pack()
            self.card_btns.append(btn)

class MainWindow(Tk):

    def __init__(self, host):
        super().__init__()
        self.title("HEIS Client")
        name = input("What's your name? ")
        with grpc.insecure_channel(host) as channel:
            self.backend = Backend(channel, name)
        self.player = self.backend.get_player()
        self.draw_widgets()

    def draw_widgets(self):
        self.player_name_lbl = Label(self, text=f"Player: {self.player.name}")
        self.cd = CardDisplay(self, "Your Hand", hand=self.backend.get_hand())

if __name__ == "__main__":
    # testing code
    ## CardDisplay
    #cd1_root = Tk()
    #cd1_root.title("Test 1: CardDisplay")
    #cd = CardDisplay(cd1_root, label="Your Hand:", hand=[Card(colour=4, action=3, value=20), Card(colour=1, action=6, value=50), Card(colour=5, action=2, value=20)])
    #cd1_root.mainloop()
    ## MainFrame
    root = MainWindow(host="localhost:50051")
    root.mainloop(0)