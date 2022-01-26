from game_of_life2.simulation import *
from game_of_life2.initialization import *

def main():
    #Lance une animation du jeu de la vie avec des paramètres définis par l'utilisateur
    animation((int(input("Largeur de l'univers : ")),int(input("Hauteur de l'univers : "))), seeds[input("Entrez le nom d'un seed : ")],
    (int(input("x_seed_départ : ")),int(input("y_seed_départ : "))), input("Choisissez une colormap : "), int(input("Nombre_générations : ")),
    int(input("interval en millisecondes : ")), bool(input("Sauvegarder en gif ? (True or False) : ")))


if __name__ == '__main__':
    main()
#Empêche un appel de la fonction lorsqu'elle est importée


