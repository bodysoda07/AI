
import tkinter as tk
from tkinter import messagebox

player = "X"
board = [" "] * 9
buttons = []

def check_win():

    win = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for w in win:
        if board[w[0]] == board[w[1]] == board[w[2]] != " ":
            return True

    return False


def click(i):

    global player

    if board[i] == " ":

        board[i] = player
        buttons[i].config(text=player, state="disabled")

        if check_win():
            messagebox.showinfo("Result", "Player " + player + " Wins!")
            reset()
            return

        if " " not in board:
            messagebox.showinfo("Result", "Match Draw!")
            reset()
            return

        if player == "X":
            player = "O"
        else:
            player = "X"

        label.config(text="Player " + player + "'s Turn")


def reset():

    global player

    player = "X"
    board[:] = [" "] * 9

    for button in buttons:
        button.config(text=" ", state="normal")

    label.config(text="Player X's Turn")


root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("350x450")

label = tk.Label(root, text="Player X's Turn",
                 font=("Arial", 18))
label.pack(pady=15)

frame = tk.Frame(root)
frame.pack()

for i in range(9):

    btn = tk.Button(frame, text=" ", font=("Arial", 25),
                    width=5, height=2,
                    command=lambda i=i: click(i))

    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

restart = tk.Button(root, text="Restart Game",
                    font=("Arial", 14), command=reset)
restart.pack(pady=20)

root.mainloop()
