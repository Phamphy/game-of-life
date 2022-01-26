from game_of_life2.simulation import *

import argparse
from game_of_life2.simulation import *

parser = argparse.ArgumentParser()
parser.add_argument("universe_size", help = "choose the size of the universe", type = tuple)
parser.add_argument("seed", help = "pick a seed", type = list)
parser.add_argument("seed_position", help = "choose the position of the seed", type = tuple)
parser.add_argument("cmap", help = "pick a colormap")
parser.add_argument("--n_generations", help = "how many generations ?", type = int)
parser.add_argument("--interval", help = "which time interval ? (in milliseconds)", type = int)
parser.add_argument("--save", help = "Do you wish to save as a gif ?", type = bool)
args = parser.parse_args()
if not args.n_generations:
    args.n_generations = 30
if not args.interval:
    args.interval = 300
if not args.save:
    args.save = False
animation(args.universe_size,args.seed,args.seed_position,args.cmap,args.n_generations,args.interval,args.save)
