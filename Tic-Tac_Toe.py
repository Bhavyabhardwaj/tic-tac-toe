
from tkinter import *
import random

# define a function to handle the next player's turn
def next_turn(row, column):

    global player

    # check if the selected shell is empty and game is not won or tied
    if buttons[row][column]['text'] == "" and check_winner() is False:

        # check which player turn it is
        if player == players[0]:

            buttons[row][column]['text'] = player

            # Check for a win, switch players, or declare a tie
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[0]+" wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

        else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[1]+" wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

# function to check if game is won 
def check_winner():

    # check horizontal wins
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
        
    # check vertical wins
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
    # check for diagonal wins
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    # if all the shells are filled the game is tied
    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False

# function to check if any empty spaces left
def empty_spaces():

    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

# func to start a new game
def new_game():

    global player

    # randomly choose the starting player
    player = random.choice(players)

    label.config(text=player+" turn")

    # reset the game board
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")

# main window
window = Tk()
window.title("Tic-Tac-Toe")

# define player symbol
players = ["x","o"]
player = random.choice(players)

# Initialize the game grid with empty buttons
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

# create a label to display curent player's turn
label = Label(text=player + " turn", font=('consolas',40))
label.pack(side="top")

# a reset btn to restart the game
reset_button = Button(text="restart", font=('consolas',20), command=new_game)
reset_button.pack(side="top")

# create a frame that contain's game grid
frame = Frame(window)
frame.pack()

# Create buttons for the game grid and assign the next_turn function to handle clicks
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2,
                                      command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)

window.mainloop()