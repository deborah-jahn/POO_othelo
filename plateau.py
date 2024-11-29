

class Plateau:
    def __init__(self,taille = int):

        self.taille=taille
        self.grille=[]
        for row in range(self.taille):
            d=[]
            for col in range (self.taille):
                d.append(' ')
            self.grille.append(d)

        self.grille[int(self.taille/2)-1][int(self.taille/2)-1]= 'O'
        self.grille[int(self.taille/2)][int(self.taille/2)]= 'O'
        self.grille[int(self.taille/2)-1][int(self.taille/2)]= 'X'
        self.grille[int(self.taille/2)][int(self.taille/2)-1]= 'X'
        self.affichage_grille() 

     
    def affichage_grille (self):

        
        #print (self.grille)
#        print('    0   1   2   3   4   5   6   7 ')

        header = "   "
        operator = "+---"
        for i in range(self.taille):
            header += f" {i}"
        header = "   " + "  ".join(f" {i}" if len(str(i)) == 1 else f"{i}" for i in range(self.taille))### pour créére une liste de string espacée 
        ligne  = "  "+"".join([operator] * self.taille)
        print(header)
        print (ligne)

        for i in range(self.taille):
            ligne=""
            # ligne=str(i)+" "
            ligne = f" {i}" if len(str(i)) == 1 else f"{i}"
            texte=0
            for k in range (self.taille):
                texte="| "+str(self.grille[k][i])+" "
                ligne=ligne+texte
            ligne=ligne +"|" 
            print(ligne)
            # print("   ----------------------------------------------------------------")
        ligne  = "  "+"".join([operator] * self.taille) + "+"
        print(ligne)






if __name__=="__main__":


    p=Plateau(4)









