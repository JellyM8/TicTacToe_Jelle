from tkinter import Button
from tkinter import Label
from tkinter import Tk
from char_select import player_char, ai_char
from gamestate import Check_game_over
from board import posities
from random import randint
from turn import player_positie

# ik moet dit van bestand een class gaan maken
# variabelen aanmaken zodat we een turn cycle kunnen maken
root = Tk()
turn = 1
turns = 0

def player_positie(positie):
    global turn
    global turns
    global posities
    global game_over
    if 0 <= positie <= 2:
        r = 5
    elif 3 <= positie <= 5:
        r = 6
    else:
        r = 7

    if positie == 0 or positie == 3 or positie == 6:
        c = 0
    elif positie == 1 or positie == 4 or positie == 7:
        c = 1
    else:
        c = 2

    if turn == 1 and turns < 9 and game_over is False:
        if posities[positie] == "-":
            posities[positie] = player_char
            new_button = Button(root, text=posities[positie]).grid(row=r, column=c, sticky="nesw")
            game_over = Check_game_over(posities)
            turn = 0
            turns += 1
            print(posities)
            Ai_turn()
# functie om ai turn aan te maken
def Ai_turn():
    global turn
    global turns
    global game_over
    while turn == 0 and turns < 9:
        ai_select = randint(0, 8)
        if posities[ai_select] == "-":
            posities[ai_select] = ai_char
            if 0 <= ai_select <= 2:
                r = 5
            elif 3 <= ai_select <= 5:
                r = 6
            else:
                r = 7
            if ai_select == 0 or ai_select == 3 or ai_select == 6:
                c = 0
            elif ai_select == 1 or ai_select == 4 or ai_select == 7:
                c = 1
            else:
                c = 2
            new_button = Button(root, text=posities[ai_select]).grid(row=r, column=c, sticky="nesw")
            game_over = Check_game_over(posities)
            turn = 1
            turns += 1
            print(posities)



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





# def player2_positie(positie):
#     global turn
#     global turns
#     global posities
#     global game_over
#     global player_char
#     if 0 <= positie <= 2:
#         r = 5
#     elif 3 <= positie <= 5:
#         r = 6
#     else:
#         r = 7
#     if positie == 0 or positie == 3 or positie == 6:
#         c = 0
#     elif positie == 1 or positie == 4 or positie == 7:
#         c = 1
#     else:
#         c = 2
#     if turn == 1 and turns < 9 and game_over == False:
#         if posities[positie] == "-": 
#             posities[positie] = ai_select
#             player_char = ai_select
#             new_button =Button(root, text=posities[positie]).grid(row=r, column =c, sticky="nesw")
#             game_over = Check_game_over(posities)
#             turn = 1
#             turns += 1
#             print(posities)
#             player1_positie()