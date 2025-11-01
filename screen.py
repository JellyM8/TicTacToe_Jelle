from tkinter import Tk
from tkinter import Label
from tkinter import Button
import os
# from char_select import Char_select
root = Tk()

class Mainscreen_en_widgets:
    # button functies op het scherm
    def __init__(self, master):
        self.grid(sticky= "nsew")
        # self.x_button
        # self.o_button
    # scherm zelf aanmaken aanmaken
        main_label.grid(row=0, column=0, columnspan=3)
        player_select_label.grid(row=1, column=0, columnspan=3)
        x_button.grid(row=2, column=0, sticky="ew")
        o_button.grid(row=2, column=1, sticky="ew")
        main_label = Label(root, text="Welcome to Tic Tac Toe!")  # Welkom scherm
        player_select_label = Label(text="Select a player to play as")  # Kies een speler
        x_button = Button(root, text="player X")# button om X te zijn
        o_button = Button(root, text="player O")# button om O te zijn



    def quit():
        root.destroy()

    # functie om een restart button aan te maken
    def restart():
        root.destroy()
        os.system(f'python "{__file__}"')

    Button(root, text="Restart", command=restart).grid(row=10, column=1, columnspan=3)
    Button(root, text="Quit", command=quit).grid(row=10, column=0, columnspan=3)


