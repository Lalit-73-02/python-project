import tkinter as tk
from tkinter import messagebox

def check_winner():
    global game_over
    win_combinations = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for combo in win_combinations:
        if buttons[combo[0]]['text'] == buttons[combo[1]]['text'] == buttons[combo[2]]['text'] != "":
            for i in combo:
                buttons[i].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            game_over = True
            return

    # Draw condition
    if all(button['text'] != "" for button in buttons):
        messagebox.showinfo("Tic-Tac-Toe", "It's a Draw!")
        game_over = True


def button_click(index):
    if buttons[index]['text'] == "" and not game_over:
        buttons[index]['text'] = current_player
        check_winner()
        if not game_over:
            toggle_player()


def toggle_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"
    label.config(text=f"Player {current_player}'s turn")


# ---------- GUI ----------
root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = []
for i in range(9):
    btn = tk.Button(
        root,
        text="",
        font=('normal', 40),
        width=5,
        height=2,
        command=lambda i=i: button_click(i)
    )
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

current_player = "X"
game_over = False

label = tk.Label(root, text="Player X's turn", font=('normal', 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()
