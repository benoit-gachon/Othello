##########################
###       Board        ###
##########################

class Board:
    def __init__(self): 
        self.board = []
        for _ in range(9):
            row = [' '] * 9
            self.board.append(row)
    
        self.board[0][1] = "1"
        self.board[0][2] = "2"
        self.board[0][3] = "3"
        self.board[0][4] = "4"
        self.board[0][5] = "5"
        self.board[0][6] = "6"
        self.board[0][7] = "7"
        self.board[0][8] = "8"

        self.board[1][0] = "1"
        self.board[2][0] = "2"
        self.board[3][0] = "3"
        self.board[4][0] = "4"
        self.board[5][0] = "5"
        self.board[6][0] = "6"
        self.board[7][0] = "7"
        self.board[8][0] = "8"


        self.board[4][4] = 'X'
        self.board[4][5] = 'O'
        self.board[5][4] = 'O'
        self.board[5][5] = 'X'
    
    def display_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 35)
        return self.board

