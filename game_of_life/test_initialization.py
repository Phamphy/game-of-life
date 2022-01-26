from game_of_life2.initialization import *
import numpy as np


def test_initiate():
    """test de la fonction initiate"""
    assert np.array_equal(initiate("infinite",(5,5)),np.array([
        [1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1],
    ]))
