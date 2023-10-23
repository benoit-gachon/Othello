###################################################################
##                    Création du jeu Othello                    ##
###################################################################

from Pawn import Pawn
from board import Board
    

# if __name__ == '__main__': # pour tester
board = Board()
board.display_board()
running = True
i=1

while running:
    if i %2==0:
        Y = int(input("coordonnée X :"))
        X = int(input("coordonnée Y :"))
        if board.test(X,Y) == True:
            pawn1 = Pawn("B", (X,Y))
            board.add_pawn(pawn1)
            i=i+1
        
             
    else:
        Y = int(input("coordonnée X :"))
        X = int(input("coordonnée Y :"))
        if board.test(X,Y) == True:
            pawn2 = Pawn("N", (X,Y))
            board.add_pawn(pawn2)
            i=i+1
        
             
    





