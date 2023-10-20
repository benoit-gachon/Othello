###################################################################
##                    Création du jeu Othello                    ##
###################################################################

from pawn import Pawn
from board import Board
    

# if __name__ == '__main__': # pour tester
board = Board()
board.display_board()
pawn1 = Pawn("B", (1, 1))
board.add_pawn(pawn1)





