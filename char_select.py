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
        Label(self.root, text=f"You are X").grid(row=3, column=0, columnspan=3)
        Button(self.root, text="Start Game", command=self.start_game).grid(row=4, column=0, columnspan=3)


    # functie om player o aan te maken
    def o_select():
        global player_char
        global ai_char
        player_char = "O"
        ai_char = "X"
        player_label = Label(root, text=f"You have selected {player_char}").grid(row=3, column=0, columnspan=3)
        start_button = Button(root, text="Start the game", command=Turn_board.draw_board).grid(row=4, column=0, columnspan=3)