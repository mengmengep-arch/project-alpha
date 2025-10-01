# เกม Tic-Tac-Toe (โอเอกซ์) ด้วย tkinter
import tkinter as tk
from tkinter import messagebox

current_player = 'X'
board = ['' for _ in range(9)]

def check_winner():
    win_conditions = [
        (0,1,2), (3,4,5), (6,7,8), # rows
        (0,3,6), (1,4,7), (2,5,8), # columns
        (0,4,8), (2,4,6)           # diagonals
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] != '':
            return board[a]
    if '' not in board:
        return 'Draw'
    return None

def on_click(idx):
    global current_player
    if board[idx] == '' and not check_winner():
        board[idx] = current_player
        buttons[idx].config(text=current_player)
        winner = check_winner()
        if winner:
            if winner == 'Draw':
                messagebox.showinfo('ผลลัพธ์', 'เสมอ!')
            else:
                messagebox.showinfo('ผลลัพธ์', f'ผู้ชนะคือ {winner}!')
            reset_game()
        else:
            current_player = 'O' if current_player == 'X' else 'X'
            label_turn.config(text=f'ถึงตา: {current_player}')

def reset_game():
    global board, current_player
    board = ['' for _ in range(9)]
    for btn in buttons:
        btn.config(text='')
    current_player = 'X'
    label_turn.config(text=f'ถึงตา: {current_player}')

root = tk.Tk()
root.title('Tic-Tac-Toe (โอเอกซ์)')
root.geometry('300x350')

label_turn = tk.Label(root, text=f'ถึงตา: {current_player}', font=('Arial', 14))
label_turn.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

buttons = []
for i in range(9):
    btn = tk.Button(frame, text='', width=6, height=3, font=('Arial', 18), command=lambda idx=i: on_click(idx))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

btn_reset = tk.Button(root, text='รีเซ็ตเกม', command=reset_game)
btn_reset.pack(pady=15)

root.mainloop()
