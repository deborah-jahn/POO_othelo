from  plateau import Plateau 
# class Plateau:
#     def affiche_grille(self):
#         pass

def saisie_position():
    x=input("saisir X:")
    y=input("saisir Y:")
    return x,y
def coup_valide():
    pass
def retourne_pions_encadres():
    pass
def detecte_fin_du_jeu():
    pass

class Jeu():
    def __init__(self):
        
        plateau = Plateau()
        #self.positionne_depart(plateau)
        #plateau.affichage_grille()
        self.run_the_game(plateau)
        self.affiche_scores(plateau)

    def positionne_depart(self, board:Plateau):   #place les 4 premiers pions
        pass

    def run_the_game(self, board:Plateau):
        fin=False
        compt=0
        while not fin :
            #verifie_si_coup_impossible()   avoir un marqueur joueur en cours2
            x,y = saisie_position()
            board.grille[int(x)][int(y)]="X"
            coup_valide= True             #coup_valide=coup_valide()
            if coup_valide :
                retourne_pions_encadres()
                board.affichage_grille()
                if detecte_fin_du_jeu() :
                    fin=True
                else :
                    compt+=1   #arret du jeu au bout de 3 fois car detecte_fin_du_jeu non ecrite
            else :
                print("coup non valide !")
            if compt>1 : fin=True

    def affiche_scores(self, board:Plateau):
        print("le jeu est fini")
 

if __name__=="__main__" :   
    Jeu()
