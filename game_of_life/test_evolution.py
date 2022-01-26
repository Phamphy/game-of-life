from game_of_life2.evolution import *
import numpy as np


def test_survival():
    """test de la fonction survival"""
    assert survival(1,1,np.array([[1,1,1],[0,0,0],[0,0,0]]))==1
    assert survival(1,1,np.array([[1,1,0],[0,0,0],[0,0,0]]))==0
    assert survival(1,1,np.array([[1,1,1],[0,1,0],[0,0,0]]))==1
    assert survival(1,1,np.array([[1,1,1],[0,1,1],[0,0,0]]))==0


def test_generation():
    """test de la fonction generation"""
    assert np.array_equal(generation(np.array([[1,1,1],[1,1,1],[1,1,1]])),np.zeros((3,3)))
