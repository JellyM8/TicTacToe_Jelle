from tkinter import Tk
from tkinter import Label
root = Tk()
# een check om te kijken of er iemand heeft gewonnen, deze check wordt elke beurt op nieuw gedaan (zie turn)
class Gamestate:
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

    #  voor als je met 4 op een rij wil spelen
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