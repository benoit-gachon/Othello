class Pawn:
    def __init__(self,couleur: str, coord: tuple):
       self.couleur=couleur
       self.coord = coord


            
        # for i in range(0, len(liste_ligne)):
        #     for j in range(0, len(liste_colonne)):
        #         self.position= (liste_ligne[i], liste_colonne[j])
        #         print(self.position)
        
    def tourner(self):
        if self.couleur=='N':
            self.couleur='B'
        else:
            self.couleur='N'










