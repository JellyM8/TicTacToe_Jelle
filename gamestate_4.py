from tkinter import Tk
from tkinter import Label
root = Tk()
# een check om te kijken of er iemand heeft gewonnen, deze check wordt elke beurt op nieuw gedaan (zie turn)

#  nu moet ik checken voor elke combinatie mogelijk op 6 x 7 veld, dit heb ik aan chat gevraagd die eerste regel zelf gedaan om te voorkomen dat ik te lang bezig ben
def Check_game_over(pos):
    global game_over
     
    if pos[0] + pos[1] + pos[2] + pos[3] == "XXXX" or \
    pos[1] + pos[2] + pos[3] + pos[4] == "XXXX" or \
    pos[2] + pos[3] + pos[4] + pos[5] == "XXXX" or \
    pos[3] + pos[4] + pos[5] + pos[6] == "XXXX" or \
    pos[7] + pos[8] + pos[9] + pos[10] == "XXXX" or \
    pos[8] + pos[9] + pos[10] + pos[11] == "XXXX" or \
    pos[9] + pos[10] + pos[11] + pos[12] == "XXXX" or \
    pos[10] + pos[11] + pos[12] + pos[13] == "XXXX" or \
    pos[14] + pos[15] + pos[16] + pos[17] == "XXXX" or \
    pos[15] + pos[16] + pos[17] + pos[18] == "XXXX" or \
    pos[16] + pos[17] + pos[18] + pos[19] == "XXXX" or \
    pos[17] + pos[18] + pos[19] + pos[20] == "XXXX" or \
    pos[21] + pos[22] + pos[23] + pos[24] == "XXXX" or \
    pos[22] + pos[23] + pos[24] + pos[25] == "XXXX" or \
    pos[23] + pos[24] + pos[25] + pos[26] == "XXXX" or \
    pos[24] + pos[25] + pos[26] + pos[27] == "XXXX" or \
    pos[28] + pos[29] + pos[30] + pos[31] == "XXXX" or \
    pos[29] + pos[30] + pos[31] + pos[32] == "XXXX" or \
    pos[30] + pos[31] + pos[32] + pos[33] == "XXXX" or \
    pos[31] + pos[32] + pos[33] + pos[34] == "XXXX" or \
    pos[35] + pos[36] + pos[37] + pos[38] == "XXXX" or \
    pos[36] + pos[37] + pos[38] + pos[39] == "XXXX" or \
    pos[37] + pos[38] + pos[39] + pos[40] == "XXXX" or \
    pos[38] + pos[39] + pos[40] + pos[41] == "XXXX" or \
    pos[0] + pos[7] + pos[14] + pos[21] == "XXXX" or \
    pos[7] + pos[14] + pos[21] + pos[28] == "XXXX" or \
    pos[14] + pos[21] + pos[28] + pos[35] == "XXXX" or \
    pos[1] + pos[8] + pos[15] + pos[22] == "XXXX" or \
    pos[8] + pos[15] + pos[22] + pos[29] == "XXXX" or \
    pos[15] + pos[22] + pos[29] + pos[36] == "XXXX" or \
    pos[2] + pos[9] + pos[16] + pos[23] == "XXXX" or \
    pos[9] + pos[16] + pos[23] + pos[30] == "XXXX" or \
    pos[16] + pos[23] + pos[30] + pos[37] == "XXXX" or \
    pos[3] + pos[10] + pos[17] + pos[24] == "XXXX" or \
    pos[10] + pos[17] + pos[24] + pos[31] == "XXXX" or \
    pos[17] + pos[24] + pos[31] + pos[38] == "XXXX" or \
    pos[4] + pos[11] + pos[18] + pos[25] == "XXXX" or \
    pos[11] + pos[18] + pos[25] + pos[32] == "XXXX" or \
    pos[18] + pos[25] + pos[32] + pos[39] == "XXXX" or \
    pos[5] + pos[12] + pos[19] + pos[26] == "XXXX" or \
    pos[12] + pos[19] + pos[26] + pos[33] == "XXXX" or \
    pos[19] + pos[26] + pos[33] + pos[40] == "XXXX" or \
    pos[6] + pos[13] + pos[20] + pos[27] == "XXXX" or \
    pos[13] + pos[20] + pos[27] + pos[34] == "XXXX" or \
    pos[20] + pos[27] + pos[34] + pos[41] == "XXXX" or \
    pos[0] + pos[8] + pos[16] + pos[24] == "XXXX" or \
    pos[1] + pos[9] + pos[17] + pos[25] == "XXXX" or \
    pos[2] + pos[10] + pos[18] + pos[26] == "XXXX" or \
    pos[3] + pos[11] + pos[19] + pos[27] == "XXXX" or \
    pos[7] + pos[15] + pos[23] + pos[31] == "XXXX" or \
    pos[8] + pos[16] + pos[24] + pos[32] == "XXXX" or \
    pos[9] + pos[17] + pos[25] + pos[33] == "XXXX" or \
    pos[10] + pos[18] + pos[26] + pos[34] == "XXXX" or \
    pos[14] + pos[22] + pos[30] + pos[38] == "XXXX" or \
    pos[15] + pos[23] + pos[31] + pos[39] == "XXXX" or \
    pos[16] + pos[24] + pos[32] + pos[40] == "XXXX" or \
    pos[17] + pos[25] + pos[33] + pos[41] == "XXXX" or \
    pos[3] + pos[9] + pos[15] + pos[21] == "XXXX" or \
    pos[4] + pos[10] + pos[16] + pos[22] == "XXXX" or \
    pos[5] + pos[11] + pos[17] + pos[23] == "XXXX" or \
    pos[6] + pos[12] + pos[18] + pos[24] == "XXXX" or \
    pos[10] + pos[16] + pos[22] + pos[28] == "XXXX" or \
    pos[11] + pos[17] + pos[23] + pos[29] == "XXXX" or \
    pos[12] + pos[18] + pos[24] + pos[30] == "XXXX" or \
    pos[13] + pos[19] + pos[25] + pos[31] == "XXXX" or \
    pos[17] + pos[23] + pos[29] + pos[35] == "XXXX" or \
    pos[18] + pos[24] + pos[30] + pos[36] == "XXXX" or \
    pos[19] + pos[25] + pos[31] + pos[37] == "XXXX" or \
    pos[20] + pos[26] + pos[32] + pos[38] == "XXXX":

        game_over = True
        win_label = Label(root, text="player X wins").grid(row=8, column=0, columnspan=3)
        print(win_label)
        
    elif pos[0] + pos[1] + pos[2] + pos[3] == "OOOO" or \
        pos[1] + pos[2] + pos[3] + pos[4] == "OOOO" or \
        pos[2] + pos[3] + pos[4] + pos[5] == "OOOO" or \
        pos[3] + pos[4] + pos[5] + pos[6] == "OOOO" or \
        pos[7] + pos[8] + pos[9] + pos[10] == "OOOO" or \
        pos[8] + pos[9] + pos[10] + pos[11] == "OOOO" or \
        pos[9] + pos[10] + pos[11] + pos[12] == "OOOO" or \
        pos[10] + pos[11] + pos[12] + pos[13] == "OOOO" or \
        pos[14] + pos[15] + pos[16] + pos[17] == "OOOO" or \
        pos[15] + pos[16] + pos[17] + pos[18] == "OOOO" or \
        pos[16] + pos[17] + pos[18] + pos[19] == "OOOO" or \
        pos[17] + pos[18] + pos[19] + pos[20] == "OOOO" or \
        pos[21] + pos[22] + pos[23] + pos[24] == "OOOO" or \
        pos[22] + pos[23] + pos[24] + pos[25] == "OOOO" or \
        pos[23] + pos[24] + pos[25] + pos[26] == "OOOO" or \
        pos[24] + pos[25] + pos[26] + pos[27] == "OOOO" or \
        pos[28] + pos[29] + pos[30] + pos[31] == "OOOO" or \
        pos[29] + pos[30] + pos[31] + pos[32] == "OOOO" or \
        pos[30] + pos[31] + pos[32] + pos[33] == "OOOO" or \
        pos[31] + pos[32] + pos[33] + pos[34] == "OOOO" or \
        pos[35] + pos[36] + pos[37] + pos[38] == "OOOO" or \
        pos[36] + pos[37] + pos[38] + pos[39] == "OOOO" or \
        pos[37] + pos[38] + pos[39] + pos[40] == "OOOO" or \
        pos[38] + pos[39] + pos[40] + pos[41] == "OOOO" or \
        pos[0] + pos[7] + pos[14] + pos[21] == "OOOO" or \
        pos[7] + pos[14] + pos[21] + pos[28] == "OOOO" or \
        pos[14] + pos[21] + pos[28] + pos[35] == "OOOO" or \
        pos[1] + pos[8] + pos[15] + pos[22] == "OOOO" or \
        pos[8] + pos[15] + pos[22] + pos[29] == "OOOO" or \
        pos[15] + pos[22] + pos[29] + pos[36] == "OOOO" or \
        pos[2] + pos[9] + pos[16] + pos[23] == "OOOO" or \
        pos[9] + pos[16] + pos[23] + pos[30] == "OOOO" or \
        pos[16] + pos[23] + pos[30] + pos[37] == "OOOO" or \
        pos[3] + pos[10] + pos[17] + pos[24] == "OOOO" or \
        pos[10] + pos[17] + pos[24] + pos[31] == "OOOO" or \
        pos[17] + pos[24] + pos[31] + pos[38] == "OOOO" or \
        pos[4] + pos[11] + pos[18] + pos[25] == "OOOO" or \
        pos[11] + pos[18] + pos[25] + pos[32] == "OOOO" or \
        pos[18] + pos[25] + pos[32] + pos[39] == "OOOO" or \
        pos[5] + pos[12] + pos[19] + pos[26] == "OOOO" or \
        pos[12] + pos[19] + pos[26] + pos[33] == "OOOO" or \
        pos[19] + pos[26] + pos[33] + pos[40] == "OOOO" or \
        pos[6] + pos[13] + pos[20] + pos[27] == "OOOO" or \
        pos[13] + pos[20] + pos[27] + pos[34] == "OOOO" or \
        pos[20] + pos[27] + pos[34] + pos[41] == "OOOO" or \
        pos[0] + pos[8] + pos[16] + pos[24] == "OOOO" or \
        pos[1] + pos[9] + pos[17] + pos[25] == "OOOO" or \
        pos[2] + pos[10] + pos[18] + pos[26] == "OOOO" or \
        pos[3] + pos[11] + pos[19] + pos[27] == "OOOO" or \
        pos[7] + pos[15] + pos[23] + pos[31] == "OOOO" or \
        pos[8] + pos[16] + pos[24] + pos[32] == "OOOO" or \
        pos[9] + pos[17] + pos[25] + pos[33] == "OOOO" or \
        pos[10] + pos[18] + pos[26] + pos[34] == "OOOO" or \
        pos[14] + pos[22] + pos[30] + pos[38] == "OOOO" or \
        pos[15] + pos[23] + pos[31] + pos[39] == "OOOO" or \
        pos[16] + pos[24] + pos[32] + pos[40] == "OOOO" or \
        pos[17] + pos[25] + pos[33] + pos[41] == "OOOO" or \
        pos[3] + pos[9] + pos[15] + pos[21] == "OOOO" or \
        pos[4] + pos[10] + pos[16] + pos[22] == "OOOO" or \
        pos[5] + pos[11] + pos[17] + pos[23] == "OOOO" or \
        pos[6] + pos[12] + pos[18] + pos[24] == "OOOO" or \
        pos[10] + pos[16] + pos[22] + pos[28] == "OOOO" or \
        pos[11] + pos[17] + pos[23] + pos[29] == "OOOO" or \
        pos[12] + pos[18] + pos[24] + pos[30] == "OOOO" or \
        pos[13] + pos[19] + pos[25] + pos[31] == "OOOO" or \
        pos[17] + pos[23] + pos[29] + pos[35] == "OOOO" or \
        pos[18] + pos[24] + pos[30] + pos[36] == "OOOO" or \
        pos[19] + pos[25] + pos[31] + pos[37] == "OOOO" or \
        pos[20] + pos[26] + pos[32] + pos[38] == "OOOO":

        game_over = True
        win_label = Label(root, text="player O wins")
        win_label.grid(row=8, column=0, columnspan=3)
        print("player O wins")

    else:
        game_over = False
    return game_over
