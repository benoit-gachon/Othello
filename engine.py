def case():
    for i in range (0,8):
      for j in range(0,8):
           if board[i][j]=='':
               case='vide'

class Joueur:
    def __init__(self, joeur_blanc, joueur_noir):
        self.joueur_blanc=joeur_blanc
        self.joueur_noir=joueur_noir


def increment(direction, position):
    if direction ==0:
        position=