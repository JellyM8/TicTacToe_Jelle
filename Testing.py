# importing van tkinter
from random import randint
from tkinter import *
import os

root = Tk()

# player char is leeg zodat deze later gevuld kan worden
player_char = ""

# board locaties aanmaken
posities = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
turn = 1
turns = 0

# game state checken die checkt voor winst of verlies
game_over = False

Grid.rowconfigure(root, 5, weight=1)
Grid.rowconfigure(root, 6, weight=1)
Grid.rowconfigure(root, 7, weight=1)
Grid.columnconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 1, weight=1)
Grid.columnconfigure(root, 2, weight=1)

# button om destroy functie te maken
Button(root, text="Quit", command=root.destroy).grid(row=10, column=0, columnspan=3)

# restart functie aan te maken
def restart():
    root.destroy()
    os.system(f'python "{__file__}"')

Button(root, text="Restart", command=restart).grid(row=10, column=1, columnspan=3)


def Check_game_over(pos):
    global game_over
    if pos[0] + pos[1] + pos[2] == "XXX" or \
       pos[3] + pos[4] + pos[5] == "XXX" or \
       pos[6] + pos[7] + pos[8] == "XXX" or \
       pos[0] + pos[3] + pos[6] == "XXX" or \
       pos[1] + pos[4] + pos[7] == "XXX" or \
       pos[2] + pos[5] + pos[8] == "XXX" or \
       pos[0] + pos[4] + pos[8] == "XXX" or \
       pos[3] + pos[4] + pos[6] == "XXX":
        game_over = True
        win_label = Label(root, text="player X wins").grid(row=8, column=0, columnspan=3)
        print(win_label)
    elif pos[0] + pos[1] + pos[2] == "OOO" or \
         pos[3] + pos[4] + pos[5] == "OOO" or \
         pos[6] + pos[7] + pos[8] == "OOO" or \
         pos[0] + pos[3] + pos[6] == "OOO" or \
         pos[1] + pos[4] + pos[7] == "OOO" or \
         pos[2] + pos[5] + pos[8] == "OOO" or \
         pos[0] + pos[4] + pos[8] == "OOO" or \
         pos[3] + pos[4] + pos[6] == "OOO":
        game_over = True
        win_label = Label(root, text="player O wins").grid(row=8, column=0, columnspan=3)
        print(win_label)
    else:
        game_over = False
    return game_over


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

def draw_board():
    global posities
    global turn
    global turns
    global game_over
    turn = 1
    turns = 0
    game_over = False
    posities = ["-"] * 9

    Button(text=posities[0], command=lambda: player_positie(0)).grid(row=5, column=0, sticky="nesw")
    Button(text=posities[1], command=lambda: player_positie(1)).grid(row=5, column=1, sticky="nesw")
    Button(text=posities[2], command=lambda: player_positie(2)).grid(row=5, column=2, sticky="nesw")
    Button(text=posities[3], command=lambda: player_positie(3)).grid(row=6, column=0, sticky="nesw")
    Button(text=posities[4], command=lambda: player_positie(4)).grid(row=6, column=1, sticky="nesw")
    Button(text=posities[5], command=lambda: player_positie(5)).grid(row=6, column=2, sticky="nesw")
    Button(text=posities[6], command=lambda: player_positie(6)).grid(row=7, column=0, sticky="nesw")
    Button(text=posities[7], command=lambda: player_positie(7)).grid(row=7, column=1, sticky="nesw")
    Button(text=posities[8], command=lambda: player_positie(8)).grid(row=7, column=2, sticky="nesw")
    Label(root, text=" ").grid(row=8, column=0, columnspan=3)


# Widget definition
main_label = Label(root, text="Welcome to Tic Tac Toe!")  # Welkom scherm
player_select_label = Label(text="Select a player to play as")  # Kies een speler
x_button = Button(root, text="player X", command=x_select)  # button om X te zijn
o_button = Button(root, text="player O", command=o_select)  # button om O te zijn

# scherm aanmaken
main_label.grid(row=0, column=0, columnspan=3)
player_select_label.grid(row=1, column=0, columnspan=3)
x_button.grid(row=2, column=0, sticky="ew")
o_button.grid(row=2, column=1, sticky="ew")

root.mainloop()
