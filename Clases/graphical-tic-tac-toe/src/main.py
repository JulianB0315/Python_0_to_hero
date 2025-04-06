from customtkinter import CTk, CTkButton, CTkLabel, CTkFrame
import game_logic

class TicTacToeApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.master.geometry("400x400")
        
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        
        self.create_widgets()
        
    def create_widgets(self):
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.frame = CTkFrame(self.master)
        self.frame.pack(pady=20)
        
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = CTkButton(self.frame, text=" ", width=60, height=60,
                                                    command=lambda r=row, c=col: self.make_move(r, c))
                self.buttons[row][col].grid(row=row, column=col, padx=5, pady=5)
        
        self.status_label = CTkLabel(self.master, text=f"Turno del jugador {self.current_player}")
        self.status_label.pack(pady=10)
        
    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].configure(text=self.current_player)
            
            if game_logic.verificar_ganador(self.board, self.current_player):
                self.status_label.configure(text=f"¡El jugador {self.current_player} ha ganado!")
                self.disable_buttons()
            elif game_logic.tablero_lleno(self.board):
                self.status_label.configure(text="¡Es un empate!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.configure(text=f"Turno del jugador {self.current_player}")
    
    def disable_buttons(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].configure(state="disabled")

if __name__ == "__main__":
    root = CTk()
    app = TicTacToeApp(root)
    root.mainloop()