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
## homemade
### protoc generated
from uno_pb2 import Card

class CardDisplay(Frame):
    """
    tkinter.ttk.Frame that draws a player's hand.
    """
    def __init__(self, master, hand, **kw):
        super().__init__(master, **kw)
        self.hand = hand
        self.card_btns = []
        self.draw_widgets()
        self.pack()
    
    def draw_widgets(self):
        for card in self.hand:
            btn = Button(self, text=str(card))
            btn.pack()
            self.card_btns.append(btn)

if __name__ == "__main__":
    # testing code
    ## CardDisplay
    cd1_root = Tk()
    cd1_root.title("Test 1: CardDisplay")
    cd = CardDisplay(cd1_root, [Card(colour=4, action=3, value=20), Card(colour=1, action=6, value=50), Card(colour=5, action=2, value=20)])
    cd1_root.mainloop()