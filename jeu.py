from  plateau import Plateau 
# class Plateau:   def affiche_grille(self):   pass

def saisie_position(plat,joueur):
    fin = False
    while not fin :
        texte ="Joueur "+ joueur+"          saisir X:"
        x=input(texte)
        texte ="Joueur "+ joueur+"          saisir Y:"
        y=input(texte)
        if plat.grille[int(x)][int(y)]!=" ":
            print("case non valide, pion present")
        else : fin = True
    return x,y

def  valide (plat, taille_tab, joueur_actif, non_joueur, pion_valid:dict, x, y, movX, movY) :
    blanc=" "
    coord=""
    fin = False
    nb_pion_non_joueur=0
    while not fin and y>= 0 and y<= taille_tab and x>=0 and x<= taille_tab:
 #       print('fin',fin, "x ",x, "y ",y, "platxy :", plat.grille[x][y], ":")
        if plat.grille[x][y] == blanc :  # une case vide, pas de pion joueur non actif encadre
            nb_pion_non_joueur=0
            coord=""
            fin = True
        elif plat.grille[x][y] == non_joueur :  # c'est un pion du non_joueur, +1 sur le compteur des nb_pion_non_joueur 
            nb_pion_non_joueur+=1
            coord= coord+ str(x)+" "+str(y)+" "
            x+=movX
            y+=movY
        elif plat.grille[x][y] == joueur_actif :
            if nb_pion_non_joueur >0 :
                fin = True              #on a trouvé des pions encadrés :))
            else :
                nb_pion_non_joueur=0   # 2 pions du joueur actif cote a cote
                coord=""
                fin = True
    #pion_valid['N']=nb_pion_non_joueur
    return nb_pion_non_joueur,coord


def coup_valide(plat, taille_tab, joueur_actif, pion_valid:dict, x, y) :

    if joueur_actif == "X" : non_joueur= "O"
    else : non_joueur="X"
    blanc=" "
    list_coord=""
    nbtotal=0
    xori=x
    yori=y

# N                 -1 sur Y
    x=xori
    y=yori-1
    movX=0
    movY=-1
    l_N=""
    nb,l_N =valide(plat, taille_tab, joueur_actif, non_joueur, pion_valid, x, y, movX, movY)
    nbtotal+=nb
    print(nb,"N:",l_N,":")
# NE    +1 sur X,   -1 sur Y 
    x=xori+1
    y=yori-1
    movX=1
    movY=-1
    l_NE=""
    nb,l_NE =valide(plat, taille_tab, joueur_actif, non_joueur, pion_valid, x, y, movX, movY)
    nbtotal+=nb
    print(nb,"NE:",l_NE,":")
# E     +1 sur X
    x=xori+1
    y=yori
    movX=1
    movY=0
    l_E=""
    nb,l_E =valide(plat, taille_tab, joueur_actif, non_joueur, pion_valid, x, y, movX, movY)
    nbtotal+=nb
    print(nb,"E:",l_E,":")
# SE    +1 sur X,   +1 sur Y 
    x=xori+1
    y=yori+1
    movX=1
    movY=1
    l_SE=""
    nb,l_SE =valide(plat, taille_tab, joueur_actif, non_joueur, pion_valid, x, y, movX, movY)
    nbtotal+=nb
    print(nb,"SE:",l_SE,":")
# S                 +1 sur Y
    x=xori
    y=yori+1
    movX=0
    movY=1
    l_S=""
    nb,l_S =valide(plat, taille_tab, joueur_actif, non_joueur, pion_valid, x, y, movX, movY)
    nbtotal+=nb
    print(nb,"S:",l_S,":")
# SW    -1 sur X,   +1 sur Y 
    x=xori-1
    y=yori+1
    movX=-1
    movY=1
    l_SW=""
    nb,l_SW =valide(plat, taille_tab, joueur_actif, non_joueur, pion_valid, x, y, movX, movY)
    nbtotal+=nb
    print(nb,"SW:",l_SW,":")
# W     -1 sur X
    x=xori-1
    y=yori
    movX=-1
    movY=0
    l_W=""
    nb,l_W =valide(plat, taille_tab, joueur_actif, non_joueur, pion_valid, x, y, movX, movY)  
    nbtotal+=nb
    print(nb,"W:",l_W,":")
# NW     -1 sur X,   -1 sur Y 
    x=xori-1
    y=yori-1
    movX=-1
    movY=-1
    l_NW=""
    nb,l_NW =valide(plat, taille_tab, joueur_actif, non_joueur, pion_valid, x, y, movX, movY)  
    nbtotal+=nb
    print(nb,"NW:",l_NW,":")

    #nbtotal= pion_valid['N'] + pion_valid['NE'] +pion_valid['E'] + pion_valid['SE'] + pion_valid['S'] +pion_valid['SW'] + pion_valid['W'] +pion_valid['NW']
    list_coord= l_N+ l_NE+l_E+l_SE+ l_S+ l_SW+l_W+l_NW
    print(nbtotal, list_coord)
    return nbtotal, list_coord
    

def retourne_pions_encadres():
    pass
def detecte_fin_du_jeu():
    pass

class Jeu():
    def __init__(self):
        #taille_tab=input("saisir taille du tableau nombre pair:")
        taille_tab=8
        self.plateau = Plateau()  #initialise le plateau + 4 pions de depart
        self.run_the_game(taille_tab)
        self.affiche_scores()

         
    def run_the_game(self, taille):
        taille_tab= taille
        fin=False
        compt=0
        #init du dico CV avec 0 pion encadré pour chacune des directions
        CV= {'N': 0, 'NE': 0, 'E': 0, 'SE': 0, 'S': 0, 'SW': 0, 'W': 0, 'NW': 0}

        #nombre_coup=input("saisir nombre de coup a jouer:")
        nombre_coup=20
        joueur_actif="X"
        while not fin :
            #verifie_si_coup_impossible()   avoir un marqueur joueur en cours2
            x,y = saisie_position(self.plateau, joueur_actif)
            temp =self.plateau.grille[int(x)][int(y)]
            self.plateau.grille[int(x)][int(y)]=joueur_actif
            self.plateau.affichage_grille()
            nb_pion_a_retourner=0
            list_pions_a_retourner=""
            nb_pion_a_retourner, list_pions_a_retourner = coup_valide(self.plateau, taille_tab, joueur_actif, CV, int(x), int(y))
            if nb_pion_a_retourner>0 :    #il y a des coups valides car nb_pion_encadre >0
                #retourne_pions_encadres(self.plateau, nb_pion_a_retourner,list_pions_a_retourner, joueur_actif)
                self.plateau.affichage_grille()
                if detecte_fin_du_jeu() :
                    fin=True
                else :  #le jeu continu , on inverse le joueur actif
                    compt+=1   
                    tempjoueur = joueur_actif
                    if tempjoueur == "X" : joueur_actif= "O"
                    else : joueur_actif="X"
            else :
                print("coup non valide !")
                self.plateau.grille[int(x)][int(y)]=temp
                self.plateau.affichage_grille()
            if compt>nombre_coup : fin=True
    def affiche_scores(self):
        print("le jeu est fini")
 
if __name__=="__main__" :   
    Jeu()
