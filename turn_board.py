# turn_board.py
# ---------------------
# Bevat de spel-logica en het bord zelf.
# Gebruikt 1 root (meegegeven door char_select/start).

from tkinter import Button, Label
from random import randint
from gamestate import Gamestate
import neutral_importfile as n  # gebruikt player_char en ai_char

class Turn_board:
    def __init__(self):
        self.posities = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
        self.turn = 1
        self.turns = 0
        self.game_over = False
        self.gamestate = Gamestate()

    def player_positie(self, positie, root):
        if self.posities[positie] == "-" and not self.game_over:
            self.posities[positie] = n.player_char

            # rij/kolom berekenen zoals jij deed
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

            Button(root, text=n.player_char).grid(row=r, column=c, sticky="nesw")
            self.game_over = self.gamestate.Check_game_over(self.posities, root)
            self.turns += 1
            if not self.game_over and self.turns < 9:
                self.Ai_turn(root)

    def Ai_turn(self, root):
        while True:
            ai_select = randint(0, 8)
            if self.posities[ai_select] == "-":
                self.posities[ai_select] = n.ai_char

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

                Button(root, text=n.ai_char).grid(row=r, column=c, sticky="nesw")
                self.game_over = self.gamestate.Check_game_over(self.posities, root)
                self.turns += 1
                break

    def draw_board(self,root):
        
        self.posities = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
        self.turn = 1
        self.turns = 0
        self.game_over = False
        
            # 🔹 Voeg dit toe om sticky te laten werken
        for r in range(5, 8):
            root.rowconfigure(r, weight=1)
        for c in range(3):
            root.columnconfigure(c, weight=1)

        # ✅ Hier gebruiken we jouw originele knoppenaanmaak (niet met for-loop)
        Button(root, text=self.posities[0], command=lambda: self.player_positie(0, root)).grid(row=5, column=0, sticky="nesw")
        Button(root, text=self.posities[1], command=lambda: self.player_positie(1, root)).grid(row=5, column=1, sticky="nesw")
        Button(root, text=self.posities[2], command=lambda: self.player_positie(2, root)).grid(row=5, column=2, sticky="nesw")
        Button(root, text=self.posities[3], command=lambda: self.player_positie(3, root)).grid(row=6, column=0, sticky="nesw")
        Button(root, text=self.posities[4], command=lambda: self.player_positie(4, root)).grid(row=6, column=1, sticky="nesw")
        Button(root, text=self.posities[5], command=lambda: self.player_positie(5, root)).grid(row=6, column=2, sticky="nesw")
        Button(root, text=self.posities[6], command=lambda: self.player_positie(6, root)).grid(row=7, column=0, sticky="nesw")
        Button(root, text=self.posities[7], command=lambda: self.player_positie(7, root)).grid(row=7, column=1, sticky="nesw")
        Button(root, text=self.posities[8], command=lambda: self.player_positie(8, root)).grid(row=7, column=2, sticky="nesw")
        
        # restart button nog toegevoegd
        Button(root, text="Restart", command=lambda: self.draw_board(root)).grid(row=9, column=0, columnspan=3)

        Label(root, text=" ").grid(row=8, column=0, columnspan=3)
