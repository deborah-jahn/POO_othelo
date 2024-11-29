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
        
        self.plateau = Plateau()
        #self.positionne_depart(plateau)
        #plateau.affichage_grille()
        self.run_the_game()
        self.affiche_scores()

    def positionne_depart(self, board:Plateau):   #place les 4 premiers pions
        pass

    def run_the_game(self):
        fin=False
        compt=0
        CV= {'N': 0, 'nb_pion': 0}, {'NE': 1, 'nb_pion': 0}, {'E': 2, 'nb_pion': 0}, {'dir': 'SE', 'nb_pion': 0}, {'dir': 'S', 'nb_pion': 0}, {'dir': 'SW', 'nb_pion': 0}, {'dir': 'W', 'nb_pion': 0},{'dir': 'NW', 'nb_pion': 0} ]
        listdir="N NE E SE S SW W NW"
        while not fin :
            #verifie_si_coup_impossible()   avoir un marqueur joueur en cours2
            x,y = saisie_position()
            self.plateau.grille[int(x)][int(y)]="X"
            coup_valide= True             #coup_valide=coup_valide()
            if coup_valide :
                CV= {'dir': 'N', 'nb_pion': 0}, {'dir': 'NE', 'nb_pion': 0}, {'dir': 'E', 'nb_pion': 0}, {'dir': 'SE', 'nb_pion': 0}, {'dir': 'S', 'nb_pion': 0}, {'dir': 'SW', 'nb_pion': 0}, {'dir': 'W', 'nb_pion': 0},{'dir': 'NW', 'nb_pion': 0} ]
                retourne_pions_encadres(CV:dict, listdir:str)
                self.plateau.affichage_grille()
                if detecte_fin_du_jeu() :
                    fin=True
                else :
                    compt+=1   #arret du jeu au bout de 3 fois car detecte_fin_du_jeu non ecrite
            else :
                print("coup non valide !")
            if compt>1 : fin=True

    def affiche_scores(self):
        print("le jeu est fini")
 

if __name__=="__main__" :   
    Jeu()
