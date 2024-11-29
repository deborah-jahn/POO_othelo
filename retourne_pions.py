from  plateau_d import Plateau 
# class Plateau:
#     def affiche_grille(self):
#         pass



def retourne_pions_encadres(self, x, y, joueur, CV):
    directions = {'N': (0, -1), 'NE': (1, -1), 'E': (1, 0), 'SE': (1, 1), 'S': (0, 1), 'SW': (-1, 1), 'W': (-1, 0), 'NW': (-1, -1)}
    #adversaire = 'O' if joueur == 'X' else 'X'
    adversaire = 'O'
    joueur = 'X'

    for direction, (dx, dy) in directions.items():
        i, j = x + dx, y + dy
        pions_a_retourner = []

        while 0 <= i < 8 and 0 <= j < 8 and self.grille[i][j] == adversaire:
            pions_a_retourner.append((i, j))
            i += dx
            j += dy

        if 0 <= i < 8 and 0 <= j < 8 and self.grille[i][j] == joueur:
            for pi, pj in pions_a_retourner:
                self.grille[pi][pj] = joueur
            CV[direction] = len(pions_a_retourner)

    return CV


# def retourne(nombre,list en string avec les coordonees x e y de chaque pion dans le plateau, joueu_actif et le plateau)

def retourne_pions (n_pion_tourner, list_str_x_y_pions, joueur_actif,Plateau):
    for coord in list_str_x_y_pions [:n_pion_tourner]:
            x, y = map(int, coord.split(','))
            self.grille[x][y] = joueur_actif

        self.affichage_grille ()


if __name__=="__main__" :   
     
plateau = Plateau()
plateau.retourner_pions(nb_pions=3,liste_coord=["3,4", "4,4", "5,5"],joueur_actif="X")
