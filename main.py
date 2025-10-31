# importing van tkinter
from tkinter import *
from char_select import *
from gamestate import *
from screen import *
from turn_board import *
root = Tk()

# bovenstaande werkte niet dus probeerde daarna alle aangemaakte functies op te roepen
x_select()
o_select()
draw_board()
Check_game_over()
restart()
Quit()
player_positie()
Ai_turn()
root.mainloop()