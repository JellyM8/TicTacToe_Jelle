# char_select.py
# ---------------------
# Laat de speler kiezen tussen X of O, en start daarna het bord.
from tkinter import Button, Label
import neutral_importfile as n
from turn_board import Turn_board

class Char_select:
    def __init__(self, root):
        self.root = root

    def x_select(self):
        n.player_char = "X"
        n.ai_char = "O"
        Label(self.root, text="You are X").grid(row=3, column=0, columnspan=3)
        Button(self.root, text="Start Game", command=self.start_game).grid(row=4, column=0, columnspan=3)

    def o_select(self):
        n.player_char = "O"
        n.ai_char = "X"
        Label(self.root, text="You are O").grid(row=3, column=0, columnspan=3)
        Button(self.root, text="Start Game", command=self.start_game).grid(row=4, column=0, columnspan=3)

    def start_game(self):
        board = Turn_board()
        board.draw_board(self.root)
