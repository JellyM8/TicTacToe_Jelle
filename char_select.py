# screen.py
# ---------------------
# Bouwt het welkomstscherm en knoppen voor spelerskeuze.
from tkinter import Label, Button
from char_select import Char_select

class Mainscreen_en_widgets:
    def __init__(self, root):
        self.root = root
        self.build_screen()

    def build_screen(self):
        Label(self.root, text="Welcome to Tic Tac Toe!").grid(row=0, column=0, columnspan=3)
        Label(self.root, text="Select your character").grid(row=1, column=0, columnspan=3)

        char = Char_select(self.root)
        Button(self.root, text="Play as X", command=char.x_select).grid(row=2, column=0, sticky="ew")
        Button(self.root, text="Play as O", command=char.o_select).grid(row=2, column=1, sticky="ew")

        Button(self.root, text="Quit", command=self.root.destroy).grid(row=10, column=0, columnspan=3)
