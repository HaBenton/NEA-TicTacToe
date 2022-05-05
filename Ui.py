from abc import ABC, abstractmethod
from Game import Game
import tkinter as tk
from tkinter import N, W, E, S, ttk

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("tictactoe")
        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)


    def run(self):
        self.root.mainloop()
        

class Terminal(Ui):
    def __init__(self):
        pass

    def run(self):
        game = Game()
        turn = 0
        while True:
            print(f"it is player {game.turn} turn")
            for row in range(len(game.board)):
                print(f"{game.board[row][0]}|{game.board[row][1]}|{game.board[row][2]}")
                if row != 2:
                    print("-+-+-")
            play = False
            while not play:
                row = int(input("row: "))
                col = int(input("col: "))
                play = game.play(row-1, col-1)
            turn +=1
            if game.winner():
                print(f"player {game.turn} won the game")
                break
            if turn == 9:
                print("its a draw")
                for row in range(len(game.board)):
                    print(f"{game.board[row][0]}|{game.board[row][1]}|{game.board[row][2]}")
                    if row != 2:
                        print("-+-+-")
                break
            if game.turn == 1:
                game.turn = 2
            elif game.turn == 2:
                game.turn = 1
