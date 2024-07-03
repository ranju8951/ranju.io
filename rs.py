import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.player = 'X'
        self.board = [['' for i in range(3)] for i in range(3)]
        self.buttons = [[None for i in range(3)] for i in range(3)]
        self.create_buttons()

    def create_buttons(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text='',bg="#303F9F",fg="#FFFFFF", font=('Arial', 24,"bold"), width=5, height=2,
                                   command=lambda r=row, c=col: self.click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def click(self, row, col):
        if self.board[row][col] == '' and not self.check_winner():
            self.board[row][col] = self.player
            self.buttons[row][col].config(text=self.player)
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.player} wins!")
                self.reset_game()
            elif all(all(cell != '' for cell in row) for row in self.board):
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_game()
            else:
                self.player = 'O' if self.player == 'X' else 'X'

    def check_winner(self):
        for i in range(3):
            if all(self.board[i][j] == self.player for j in range(3)):
                return True
            if all(self.board[j][i] == self.player for j in range(3)):
                return True
        if all(self.board[i][i] == self.player for i in range(3)):
            return True
        if all(self.board[i][2-i] == self.player for i in range(3)):
            return True
        return False

    def reset_game(self):
        self.board = [['' for i in range(3)] for i in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text='')
        self.player = 'X'

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
