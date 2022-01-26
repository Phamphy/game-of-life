import numpy as np

def voisinage(x,y,universe):
    """retourne une liste des coordonnées des voisins de la cellule (x,y)"""
    voisins_bruts=[[x-1,y-1],[x,y-1],[x+1,y-1],[x+1,y],[x+1,y+1],[x,y+1],[x-1,y+1],[x-1,y]]
    #liste des voisins sans soucis de si l'on sort de l'univers
    voisins_cleans=[]
    #liste des voisins en considérant l'univers comme un tore
    taille=universe.shape
    for cell in voisins_bruts:
        position=[]
        if cell[0]>=taille[0]:
            position.append(cell[0]-taille[0])
        else :
            position.append(cell[0])
        if cell[1]>=taille[1]:
            position.append(cell[1]-taille[1])
        else :
            position.append(cell[1])
        voisins_cleans.append(position)
    return voisins_cleans


def somme(liste,universe):
    """retourne le nombre de cellules vivantes en considérant une liste de coordonnée de cellules"""
    S=0
    for position in liste:
        S+=universe[position[0],position[1]]
    return S



def survival(x,y,universe):
    """retourne l'état d'une cellule en fonction des cellules voisines"""
    voisins=voisinage(x,y,universe)
    #les voisins de la cellule
    vivants=somme(voisins,universe)
    #le nombre de voisins vivants
    if universe[x,y]==0:
        if vivants==3:
            return 1
        else :
            return 0
        #si la cellule etait morte
    else :
        if vivants==2 or vivants==3:
            return 1
        else :
            return 0
        #si la cellule etait vivante


def generation(universe):
    """retourne le prochain univers en mettant a jour l'etat de toutes les cellules"""
    new_universe=np.zeros(universe.shape)
    #creation d'un nouvel univers
    for x in range(universe.shape[0]):
        for y in range(universe.shape[1]):
            new_universe[x,y]=survival(x,y,universe)
            #on met a jour l'etat de chaque cellule en fonction de l'ancien univers
    return new_universe

