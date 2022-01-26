import numpy as np
import matplotlib.pyplot as plt

def display_universe(universe):
    """affiche l'univers en niveau de gris : case noir = vivant / case blanche = mort"""
    plt.imshow(universe,cmap='Greys')
    plt.show()
