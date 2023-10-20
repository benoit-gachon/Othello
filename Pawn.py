class Pawn:
    def __init__(self,couleur: str, coord: tuple):
       self.couleur=couleur
       self.coord = coord

    def position(self,liste_ligne,liste_colonne):
        for i in range(0, len(liste_ligne)):
            for j in range(0, len(liste_colonne)):
                self.position= (liste_ligne[i], liste_colonne[j])
                print(self.position)
        
    def tourner(self):
        if self.couleur=='N':
            self.couleur='B'
        else:
            self.couleur='N'

    def test_case(self,tuple):
        self.tuple=tuple
        if self.position==():
            return False
        else:
            return True  

pion=Pawn('noir')
pion.position([1,2,3],(1,2,3))
tuple=(1,1)
print(pion.test_case(tuple))








