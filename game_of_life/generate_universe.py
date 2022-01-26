import numpy as np
import random


def generate_universe(size):
    """genere un univers avec uniquement des cellules mortes"""
    return np.zeros((size[0],size[1]))


def create_seed(type_seed):
    """renvoie la seed r_pentomino"""
    if type_seed=="r_pentomino":
        return [[0, 1, 1], [1, 1, 0], [0, 1, 0]]


def add_seed_to_universe(seed, universe,x_start=-1, y_start=-1):
    """ajoute un seed a l'univer de façons aleatoire si l'on ne renseigne pas de x_start et y_start"""
    if x_start==-1:
        x_start=random.randint(0,universe.shape[0]-len(seed[0]))
        #choix d'une position x aleatoire
    if y_start==-1:
        y_start=random.randint(0,universe.shape[1]-len(seed))
        #choix d'une position y aleatoire
    universe[y_start:y_start+len(seed),x_start:x_start+len(seed[0])]=seed
    #on place la seed dans l'univers
    return universe
