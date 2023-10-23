##########################
###       Board        ###
##########################

from Pawn import Pawn
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

        pawn1 = Pawn("B", (4, 4))
        self.add_pawn(pawn1)
        pawn2 = Pawn("B", (5, 5))
        self.add_pawn(pawn2)
        pawn3 = Pawn("N", (4, 5))
        self.add_pawn(pawn3)
        pawn4 = Pawn("N", (5, 4))
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

    #Méthode qui test si une case est vide ou non
    def test(self,X:int,Y:int):
        if self.board[X][Y] == " ":
            return True
        else:
            return False


############################################################
##     Test pour créer méthode qui retourne les pions     ##
############################################################

    def retourner_pions(self, pawn:Pawn):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        if pawn.couleur == "N":
            opponent = "O"
            player = "X"
        else:
            opponent = "X" 
            player = "O"
        pions_retournes = []

        for dr, dc in directions:
            r = pawn.coord[1]
            c = pawn.coord[0]
            r += dr
            c += dc
            pions_a_retourner = []  # Liste pour stocker les pions de l'adversaire à retourner

            while 0 <= r < len(self.board) and 0 <= c < len(self.board[0]) and self.board[r][c] == opponent:
                pions_a_retourner.append((r, c))
                r += dr
                c += dc

            if 0 <= r < len(self.board) and 0 <= c < len(self.board[0]) and self.board[r][c] == player:
                pions_retournes.extend(pions_a_retourner)

        for r, c in pions_retournes:
            self.board[r][c] = player

        return self.board    

# if __name__ == '__main__':