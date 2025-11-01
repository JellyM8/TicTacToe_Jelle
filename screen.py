from tkinter import Tk
from tkinter import Label
from tkinter import Button
import os
from neutral_importfile import player_char, ai_char
root = Tk()
Tk.Grid.rowconfigure(root, 5, weight=1)
Tk.Grid.rowconfigure(root, 6, weight=1)
Tk.Grid.rowconfigure(root, 7, weight=1)
Tk.Grid.columnconfigure(root, 0, weight=1)
Tk.Grid.columnconfigure(root, 1, weight=1)
Tk.Grid.columnconfigure(root, 2, weight=1)

class Mainscreen_en_widgets:
    def call_x_select():
        from char_select import x_select
        x_select()

    def call_o_select():
        from char_select import o_select
        o_select()




    # button functies op het scherm
    def __init__(self, master):
        self.master = master

    # scherm zelf aanmaken aanmaken
        self.main_label = Label(root, text="Welcome to Tic Tac Toe!")  # Welkom scherm
        self.player_select_label = Label(text="Select a player to play as")  # Kies een speler
        self.x_button = Button(root, text="player X", command=Mainscreen_en_widgets.call_x_select)# button om x te zijn
        self.o_button = Button(root, text="player O", command=Mainscreen_en_widgets.call_o_select)# button om O te zijn
        self.main_label.grid(row=0, column=0, columnspan=3)
        self.player_select_label.grid(row=1, column=0, columnspan=3)
        self.x_button.grid(row=2, column=0, sticky="ew")
        self.o_button.grid(row=2, column=1, sticky="ew")

        # Quit and Restart inside __init__
        self.restart_button = Button(master, text="Restart", command=self.restart)
        self.quit_button = Button(master, text="Quit", command=self.quit)
        self.restart_button.grid(row=10, column=1, columnspan=3)
        self.quit_button.grid(row=10, column=0, columnspan=3)



    def quit(self):
        self.master.destroy()

    # functie om een restart button aan te maken
    def restart(self):
        self.master.destroy()
        os.system(f'python "{__file__}"')



window = Mainscreen_en_widgets(root)
root.mainloop()
