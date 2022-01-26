from game_of_life2.game_of_life_pygame import *


def test_generate_universe():
    L = generate_universe()
    for y in range(hauteur):
        for x in range(largeur):
            assert L[x][y] == 1 or L[x][y] == 0
