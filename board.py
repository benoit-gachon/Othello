##########################
###       Board        ###
##########################

# class Board:
#     def __init__(self, affichage):
#         self.affichage = affichage

#     def affichage(self):
#         for row in range(1, 18):
#             for i in range(1, 33) : 
#                 if row % 2 ==0:
#                     if i == 1:
#                         print("|", end="")
#                     if i % 4 == 0 :
#                         print("|", end="")
#                     else:
#                         print(" ", end="")
#                 if row % 2 !=0:
#                     if i == 1:
#                         print("+", end="")
#                     if i % 4 == 0:
#                         print("+", end="")
#                     else:
#                         print("-", end="")
#             print(" ")

###################################### test 2
# for row in range(1, 19):
#     if row == 1:
#         print("   A   B   C   D   E   F   G   H")
#     for i in range(1, 34) : 
#         if i == 1:
#             print(1,2,3,4,5,6,7,8, sep="\n")
#         if row % 2 + 1 ==1:
#             if i == 2:
#                 print("|", end="")
#             if i % 4 +1 == 1 :
#                 print("|", end="")
#             else:
#                 print(" ", end="")
#         if row % 2 ==0:
#             if i == 2:
#                 print("+", end="")
#             if i % 4 +1 == 1:
#                 print("+", end="")
#             else:
#                 print("-", end="")
#     print(" ")



def init_board():
    board = [[' ' for _ in range(8)] for _ in range(8)]
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'
    return board



def display_board(board):
    for element in board[0][0]:
        print("A   B   C   D   E   F   G   H")
    for element in board[0][1]:
    for row in board:
        print(" | ".join(row))
        print("-" * 30)


print(display_board(init_board()))
