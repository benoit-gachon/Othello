##########################
###       Board        ###
##########################
class Board:
    def __init__(self, affichage):
        self.affichage = affichage

    def affichage(self):
        for row in range(1, 18):
            for i in range(1, 33) : 
                if row % 2 ==0:
                    if i == 1:
                        print("|", end="")
                    if i % 4 == 0 :
                        print("|", end="")
                    else:
                        print(" ", end="")
                if row % 2 !=0:
                    if i == 1:
                        print("+", end="")
                    if i % 4 == 0:
                        print("+", end="")
                    else:
                        print("-", end="")
            print(" ")

# for row in range(1, 19):
#     if row == 1:
#         print("   A   B   C   D   E   F   G   H")
#     for i in range(1, 34) : 
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
