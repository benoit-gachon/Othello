###################################################################
##                    Création du jeu Othello                    ##
###################################################################

from Pawn import Pawn
from board import Board
board = Board()
board.display_board()
running = True
i=1

while running:
    if i %2==0:
        print("Au tour du joueur blanc")
        X = int(input("Numéro de ligne :"))
        Y = int(input("Numéro de colonne :"))
        if board.test(X,Y) == True:
            pawn1 = Pawn("B", (X,Y))
            board.retourner_pions(pawn1)
            board.add_pawn(pawn1)
            board.compteur()
            i=i+1
        else : 
            print("la case n'est pas disponible, essayez à nouveau")   
            
        
             
    else:
        print("Au tour du joueur noir")
        X = int(input("Numéro de ligne :"))
        Y = int(input("Numéro de colonne :"))

        if board.test(X,Y) == True:
            pawn2 = Pawn("N", (X,Y))
            board.retourner_pions(pawn2)
            board.add_pawn(pawn2)
            board.compteur()
            i=i+1
        else : 
            print("la case n'est pas disponible, essayez à nouveau") 
            
            

  
    





