from  plateau import Plateau 
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
