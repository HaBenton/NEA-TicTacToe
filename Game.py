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
        
    
    def winner(self):
        for row in self.board:
            if (row[0] == row[1] == row[2]) and self.token(row[1]):
                return True
        for item in range(3):
            if (self.board[0][item] == self.board[1][item] == self.board[2][item]) and self.token(self.board[0][item]):
                return True
        if (self.board[0][0] == self.board[1][1] == self.board[2][2]) and self.token(self.board[0][0]):
            return True
        elif (self.board[0][2] == self.board[1][1] == self.board[2][0]) and self.token(self.board[0][2]):
            return True
        else:
            return False


    def token(self, item):
        if item == "X" or item == "O":
            return True
        else:
            return False


if __name__ == "__main__":
    pass
