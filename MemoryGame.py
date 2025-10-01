# เกมจับคู่ภาพ (Memory Game) ด้วย tkinter
import tkinter as tk
import random
from tkinter import messagebox

NUM_PAIRS = 8
CARD_SIZE = 60
PADDING = 10

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title('เกมจับคู่ภาพ (Memory Game)')
        self.cards = list(range(1, NUM_PAIRS+1)) * 2
        random.shuffle(self.cards)
        self.buttons = []
        self.flipped = []
        self.matched = set()
        self.create_board()

    def create_board(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)
        for i in range(4):
            row = []
            for j in range(4):
                idx = i*4 + j
                btn = tk.Button(frame, text='', width=6, height=3, font=('Arial', 16),
                                command=lambda idx=idx: self.flip_card(idx))
                btn.grid(row=i, column=j, padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)

    def flip_card(self, idx):
        if idx in self.matched or idx in [i for i, _ in self.flipped]:
            return
        i, j = divmod(idx, 4)
        self.buttons[i][j].config(text=str(self.cards[idx]), state='disabled')
        self.flipped.append((idx, self.cards[idx]))
        if len(self.flipped) == 2:
            self.root.after(700, self.check_match)

    def check_match(self):
        (idx1, val1), (idx2, val2) = self.flipped
        if val1 == val2:
            self.matched.add(idx1)
            self.matched.add(idx2)
            if len(self.matched) == 16:
                messagebox.showinfo('ยินดีด้วย!', 'คุณจับคู่ครบทุกคู่แล้ว!')
        else:
            for idx, _ in self.flipped:
                i, j = divmod(idx, 4)
                self.buttons[i][j].config(text='', state='normal')
        self.flipped = []

def main():
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()

if __name__ == '__main__':
    main()
