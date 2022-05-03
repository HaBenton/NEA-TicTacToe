class Game:

    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.turn = 1

    def __repr__(self):
        pass

    def play(self,row,col):
        if 0 <= row and row <= 2 and 0 <= col and col <= 2:
            if self.board[row][col] == " ":
                if self.turn == 1:
                    self.board[row][col] = "X"
                else:
                    self.board[row][col] = "O"
            return True
        return False
        
    
    @property
    def winner(self):
        for row in self.board:
            ...


if __name__ == "__main__":
    pass
