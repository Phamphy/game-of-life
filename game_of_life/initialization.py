from game_of_life2.generate_universe import *


seeds = {
    "boat": [[1, 1, 0], [1, 0, 1], [0, 1, 0]],
    "r_pentomino": [[0, 1, 1], [1, 1, 0], [0, 1, 0]],
    "beacon": [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]],
    "acorn": [[0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [1, 1, 0, 0, 1, 1, 1]],
    "block_switch_engine": [
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0],
    ],
    "infinite": [
        [1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1],
    ],
    "block": [[1,1],[1,1]],
    "beehive": [[0,1,1,0],[1,0,0,1],[0,1,1,0]],
    "loaf": [[0,1,1,0],[1,0,0,1],[0,1,0,1],[0,0,1,0]],
    "tub": [[0,1,0],[1,0,1],[0,1,0]],
    "blinker": [[1,1,1]],
    "toad": [[0,1,1,1],[1,1,1,0]],
    "pulsar": [
        [0,0,1,1,1,0,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,0,0,0,0,1,0,1,0,0,0,0,1],
        [1,0,0,0,0,1,0,1,0,0,0,0,1],
        [1,0,0,0,0,1,0,1,0,0,0,0,1],
        [0,0,1,1,1,0,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,1,0,0,0,1,1,1,0,0],
        [1,0,0,0,0,1,0,1,0,0,0,0,1],
        [1,0,0,0,0,1,0,1,0,0,0,0,1],
        [1,0,0,0,0,1,0,1,0,0,0,0,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,1,0,0,0,1,1,1,0,0]
    ],
    "pentadecathlon": [
        [0,1,0],
        [0,1,0],
        [1,0,1],
        [0,1,0],
        [0,1,0],
        [0,1,0],
        [0,1,0],
        [1,0,1],
        [0,1,0],
        [0,1,0],
    ],
    "glider": [[1,0,0],[0,1,1],[1,1,0]],
    "lightweight_spaceship": [
        [0,1,1,0,0],
        [1,1,1,1,0],
        [1,1,0,1,1],
        [0,0,1,1,0]
    ]
}
#dictionnaire contenant quelques seeds


def initiate(seed_name,size):
    """retourne un univers avec un seed choisit et positionne aleatoirement"""
    if seed_name not in seeds.keys():
        raise ValueError("Le seed n'est pas dans le dictionnaire !")
    #on verifie que la seed est bien dans l'univers

    seed=np.array(seeds[seed_name])

    if seed.shape[0]>size[0] or seed.shape[1]>size[1]:
        raise ValueError("Le seed est plus grand que l'univers !")
    #on verifie que le seed n'est pas plus grand que l'univers

    else :
        universe=generate_universe(size)
        #on genere un univers vide
        return add_seed_to_universe(seed, universe)
        #on retourne l'univer avec la seed choisie placee aleatoirement

