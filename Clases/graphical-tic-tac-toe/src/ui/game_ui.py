from customtkinter import CTk, CTkButton, CTkLabel, CTkFrame
import tkinter as tk

class GameUI:
    def __init__(self, master, game_logic):
        self.master = master
        self.game_logic = game_logic
        self.master.title("Tic-Tac-Toe")
        self.master.geometry("400x400")
        
        self.board_frame = CTkFrame(self.master)
        self.board_frame.pack(pady=20)

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = CTkButton(self.board_frame, text="", width=10, height=3,
                                                command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)

        self.status_label = CTkLabel(self.master, text="Turn: Player X")
        self.status_label.pack(pady=10)

    def make_move(self, row, col):
        if self.game_logic.make_move(row, col, self.current_player):
            self.buttons[row][col].configure(text=self.current_player)
            if self.game_logic.check_winner(self.current_player):
                self.status_label.configure(text=f"Player {self.current_player} wins!")
                self.disable_buttons()
            elif self.game_logic.is_board_full():
                self.status_label.configure(text="It's a tie!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.configure(text=f"Turn: Player {self.current_player}")

    def disable_buttons(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].configure(state=tk.DISABLED)