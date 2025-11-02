# gamestate.py
# ---------------------
# Deze class controleert na elke zet of iemand gewonnen heeft.
# Let op: de functie krijgt 'root' mee, zodat we niet een tweede Tk() aanmaken.

from tkinter import Label


class Gamestate:
    def Check_game_over(self, pos, root):
        if (
            pos[0] + pos[1] + pos[2] == "XXX"
            or pos[3] + pos[4] + pos[5] == "XXX"
            or pos[6] + pos[7] + pos[8] == "XXX"
            or pos[0] + pos[3] + pos[6] == "XXX"
            or pos[1] + pos[4] + pos[7] == "XXX"
            or pos[2] + pos[5] + pos[8] == "XXX"
            or pos[0] + pos[4] + pos[8] == "XXX"
            or pos[2] + pos[4] + pos[6] == "XXX"
        ):
            Label(root, text="Player X wins!").grid(row=8, column=0, columnspan=3)
            return True
        elif (
            pos[0] + pos[1] + pos[2] == "OOO"
            or pos[3] + pos[4] + pos[5] == "OOO"
            or pos[6] + pos[7] + pos[8] == "OOO"
            or pos[0] + pos[3] + pos[6] == "OOO"
            or pos[1] + pos[4] + pos[7] == "OOO"
            or pos[2] + pos[5] + pos[8] == "OOO"
            or pos[0] + pos[4] + pos[8] == "OOO"
            or pos[2] + pos[4] + pos[6] == "OOO"
        ):
            Label(root, text="Player O wins!").grid(row=8, column=0, columnspan=3)
            return True
        else:
            return False
