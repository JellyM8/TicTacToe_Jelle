# importing van tkinter
from tkinter import Tk
from char_select import Char_select
from gamestate import Gamestate
from screen import Mainscreen_en_widgets
from turn_board import Turn_board
root = Tk()

# bovenstaande werkte niet dus probeerde daarna alle aangemaakte functies op te roepen
Mainscreen_en_widgets.restart()
Mainscreen_en_widgets.quit()
Char_select.x_select()
Char_select.o_select()
Turn_board.draw_board()
Gamestate.Check_game_over()
Turn_board.player_positie()
Turn_board.Ai_turn()


root.mainloop()