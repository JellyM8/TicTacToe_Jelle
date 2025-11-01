# main.py
# ---------------------
# Startpunt van het programma. Maakt één Tk() venster aan en laadt het hoofdscherm.
from tkinter import Tk
from screen import Mainscreen_en_widgets

root = Tk()
root.title("Tic Tac Toe")

# Maak hoofdscherm
Mainscreen_en_widgets(root)

# Start mainloop
root.mainloop()
