##########################
###       Board        ###
##########################

from pawn import Pawn
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

        pawn1 = Pawn("N", (4, 4))
        self.add_pawn(pawn1)
        pawn2 = Pawn("N", (5, 5))
        self.add_pawn(pawn2)
        pawn3 = Pawn("B", (4, 5))
        self.add_pawn(pawn3)
        pawn4 = Pawn("B", (5, 4))
        self.add_pawn(pawn4)

    # Méthode qui permet d'afficher le tableau
    def display_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 35)
        return self.board
    
    #Méthode qui permet d'ajouter un pion sur le board en faisant appel à la classe Pawn
    def add_pawn(self, pawn: Pawn):
        if pawn.couleur == 'N':
            self.board[pawn.coord[0]][pawn.coord[1]] = 'X' #Dans la classe Pawn on donne la couleur et les coordonnées sous forme de tuple
        elif pawn.couleur == 'B':
            self.board[pawn.coord[0]][pawn.coord[1]] = 'O'
        self.display_board()
