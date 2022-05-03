from abc import ABC, abstractmethod
from Game import Game

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        pass

    def run(self):
        pass

class Terminal(Ui):
    def __init__(self):
        pass

    def run(self):
        game = Game()
        while True:
            print(f"it is player {game.turn} turn")
            for row in range(len(game.board)):
                print(f"{game.board[row][0]}|{game.board[row][1]}|{game.board[row][2]}")
                if row != 2:
                    print("-+-+-")
            break
