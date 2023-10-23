class Joueur:
    def __init__(self, joeur_blanc, joueur_noir):
        self.joueur_blanc=joeur_blanc
        self.joueur_noir=joueur_noir

#7 0 1
#6 . 2
#5 4 3 
def increment(direction, position:tuple):
    if direction ==0:
        return(position[0]-1,position[1])
    if direction == 1:
        return(position[0]-1, position[1]+1)
    if direction == 2:
        return (position[0], position[1]+1)
    if direction == 3:
        return(position[0]+1, position[1]+1)
    if direction == 4:
        return (position[0]+1,position[1])
    if direction ==5:
        return (position[0]+1, position[1]-1)
    if direction ==6:
        return (position[0], position[1]-1)
    if direction ==7:
        return(position[0]-1,position[1]-1)

# if __name__ == '__main__':

pos = increment(2, (2,2))
print(pos)
