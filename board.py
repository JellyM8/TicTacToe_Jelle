from turn import player_positie
from tkinter import Button
from tkinter import Label
from tkinter import Tk
root = Tk()

# board locaties aanmaken
posities = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

def draw_board():
    global posities
    global turn
    global turns
    global game_over
    turn = 1
    turns = 0
    game_over = False
    posities = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

#  we moeten lambda gebruiken want als we variabelen door player posititie halen accepteert die het niet, 
# lambda zorgt ervoor dat het geaccepteert wordt en dat we niet elke keer een nieuwe functie hoeven aan te maken voor elke button
# sticky zorgt ervoor dat de buttons mee scalen met de groote van het scherm
    button1 = Button(text=posities[0], command=lambda: player_positie(0)).grid(row=5, column=0, sticky="nesw")
    button2 = Button(text=posities[1], command=lambda: player_positie(1)).grid(row=5, column=1, sticky="nesw")
    button3 = Button(text=posities[2], command=lambda: player_positie(2)).grid(row=5, column=2, sticky="nesw")
    button4 = Button(text=posities[3], command=lambda: player_positie(3)).grid(row=6, column=0, sticky="nesw")
    button5 = Button(text=posities[4], command=lambda: player_positie(4)).grid(row=6, column=1, sticky="nesw")
    button6 = Button(text=posities[5], command=lambda: player_positie(5)).grid(row=6, column=2, sticky="nesw")
    button7 = Button(text=posities[6], command=lambda: player_positie(6)).grid(row=7, column=0, sticky="nesw")
    button8 = Button(text=posities[7], command=lambda: player_positie(7)).grid(row=7, column=1, sticky="nesw")
    button9 = Button(text=posities[8], command=lambda: player_positie(8)).grid(row=7, column=2, sticky="nesw")


    Label(root, text=" ").grid(row=8, column=0, columnspan=3)