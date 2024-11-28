<<<<<<< HEAD
from  plateau import Plateau 
=======
2from  plateau import Plateau 
>>>>>>> e39569eb418ffbfad26c75422bc8da4f3b4fbac9
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
        
<<<<<<< HEAD
        plateau = Plateau()
        #self.positionne_depart(plateau)
        #plateau.affichage_grille()
        self.run_the_game(plateau)
        self.affiche_scores(plateau)
=======
        self.plateau = Plateau()
        #self.positionne_depart(plateau)
        #plateau.affichage_grille()
        self.run_the_game()
        self.affiche_scores()
>>>>>>> e39569eb418ffbfad26c75422bc8da4f3b4fbac9

    def positionne_depart(self, board:Plateau):   #place les 4 premiers pions
        pass

<<<<<<< HEAD
    def run_the_game(self, board:Plateau):
=======
    def run_the_game(self):
>>>>>>> e39569eb418ffbfad26c75422bc8da4f3b4fbac9
        fin=False
        compt=0
        while not fin :
            #verifie_si_coup_impossible()   avoir un marqueur joueur en cours2
            x,y = saisie_position()
<<<<<<< HEAD
            board.grille[int(x)][int(y)]="X"
            coup_valide= True             #coup_valide=coup_valide()
            if coup_valide :
                retourne_pions_encadres()
                board.affichage_grille()
=======
            self.plateau.grille[int(x)][int(y)]="X"
            coup_valide= True             #coup_valide=coup_valide()
            if coup_valide :
                retourne_pions_encadres()
                self.plateau.affichage_grille()
>>>>>>> e39569eb418ffbfad26c75422bc8da4f3b4fbac9
                if detecte_fin_du_jeu() :
                    fin=True
                else :
                    compt+=1   #arret du jeu au bout de 3 fois car detecte_fin_du_jeu non ecrite
            else :
                print("coup non valide !")
            if compt>1 : fin=True

<<<<<<< HEAD
    def affiche_scores(self, board:Plateau):
=======
    def affiche_scores(self):
>>>>>>> e39569eb418ffbfad26c75422bc8da4f3b4fbac9
        print("le jeu est fini")
 

if __name__=="__main__" :   
    Jeu()
