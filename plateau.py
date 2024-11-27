

class Plateau:
    def __init__(self):

        grille=[]
        for row in range(8):
            d=[]
            for col in range (8):
                d.append(' ')
            grille.append(d)

        grille[3][3]= 'O'
        grille[4][4]= 'O'
        grille[3][4]= 'X'
        grille[4][3]= 'X'
        print(grille)

 

        
        















p=Plateau()








