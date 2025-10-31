from tkinter import Button
from tkinter import Label
from tkinter import Tk
from char_select import player_char, ai_char
from gamestate import Check_game_over
from board import posities
from random import randint
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