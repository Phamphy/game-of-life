from game_of_life2.simulation import *
import numpy as np


def test_game_life_simulate():
    """test de la fonction game_life_simulate"""
    assert np.array_equal(game_life_simulate(np.array([[0,0,0],[1,1,1],[0,0,0]]),3),np.array([[0,0,0],[0,0,0],[0,0,0]]))
