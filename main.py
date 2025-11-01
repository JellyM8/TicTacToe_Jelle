# main.py
# ---------------------
# Startpunt van het programma. Maakt één Tk() venster aan en laadt het hoofdscherm.
from tkinter import Tk
from screen import Mainscreen_en_widgets

def main():
    root = Tk()
    root.title("Tic Tac Toe")
    app = Mainscreen_en_widgets(root)
    root.mainloop()

if __name__ == "__main__":
    main()
