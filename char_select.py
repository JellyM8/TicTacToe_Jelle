from tkinter import Button
from tkinter import Label
from tkinter import Tk
from board import draw_board
root = Tk()
# player char is leeg zodat deze later gevuld kan worden
player_char = ""

# functie om player x aan te maken
def x_select():
    global player_char
    global ai_char
    player_char = "X"
    ai_char = "O"
    player_label = Label(root, text=f"You have selected {player_char}").grid(row=3, column=0, columnspan=3)
    start_button = Button(root, text="Start the game", command=draw_board).grid(row=4, column=0, columnspan=3)


# functie om player o aan te maken
def o_select():
    global player_char
    global ai_char
    player_char = "O"
    ai_char = "X"
    player_label = Label(root, text=f"You have selected {player_char}").grid(row=3, column=0, columnspan=3)
    start_button = Button(root, text="Start the game", command=draw_board).grid(row=4, column=0, columnspan=3)