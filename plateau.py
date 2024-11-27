

class Plateau:
    def __init__(self):

        self.grille=[]
        for row in range(8):
            d=[]
            for col in range (8):
                d.append(' ')
            self.grille.append(d)

        self.grille[3][3]= 'O'
        self.grille[4][4]= 'O'
        self.grille[3][4]= 'X'
        self.grille[4][3]= 'X'
        self.affichage_grille() 

 

        
        

    def affichage_grille (self):
        print (self.grille)

        print('+---+---+')
        print(f'| {self.grille[0][0]} | {self.grille[3][3]} |')
        print('+---+---+')






if __name__=="__main__":


    p=Plateau()









