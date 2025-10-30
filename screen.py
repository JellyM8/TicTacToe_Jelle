# button functies op het scherm
main_label = Label(root, text="Welcome to Tic Tac Toe!")  # Welkom scherm
player_select_label = Label(text="Select a player to play as")  # Kies een speler
x_button = Button(root, text="player X", command=x_select)  # button om X te zijn
o_button = Button(root, text="player O", command=o_select)  # button om O te zijn

# button om een quit functie te maken
Button(root, text="Quit", command=root.destroy).grid(row=10, column=0, columnspan=3)

# button om een restart functie aan te maken
def restart():
    root.destroy()
    os.system(f'python "{__file__}"')

Button(root, text="Restart", command=restart).grid(row=10, column=1, columnspan=3)

# scherm zelf aanmaken aanmaken
main_label.grid(row=0, column=0, columnspan=3)
player_select_label.grid(row=1, column=0, columnspan=3)
x_button.grid(row=2, column=0, sticky="ew")
o_button.grid(row=2, column=1, sticky="ew")