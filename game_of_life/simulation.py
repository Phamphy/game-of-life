from game_of_life2.evolution import *
from game_of_life2.initialization import *
import matplotlib.animation as anim
import matplotlib.pyplot as plt
import os

#os.chdir("C:/Users/Stefferc/PycharmProjects/game_of_life_3")


def game_life_simulate(universe,n):
    """retourne l'univers au bout de n evolutions"""
    for etape in range(n):
        universe=generation(universe)
        #calcul successif des univers
    return universe


def animation(universe_size,seed,seed_position,cmap,n_generations=30,interval=300,save=False):
    """affiche l'animation du jeu de la vie et peut sauvegarder cette animation dans un fichier gif"""
    universe=add_seed_to_universe(seed, generate_universe(universe_size),x_start=seed_position[0], y_start=seed_position[1])
    #on cree un univers de taille demande, avec le seed demande, positionne a l'endroit demande
    fig = plt.figure()
    im=plt.imshow(universe,cmap=cmap,animated=True)

    def animate(i):
        """fonction pour gerer l'animation"""
        universe1=im.get_array()
        im.set_array(generation(universe1))
        return [im]
    anime = anim.FuncAnimation(fig, animate,frames=n_generations, interval=interval, blit=True)
    #creation de l'animation

    if save:
        anime.save('animation.gif',writer='imagemagick')
        #possibilite de sauvegarder un gif de l'animation
    plt.show()
    #afficher l'animation



def beacon():
    """affiche l'animation du beacon et la sauvegarde dans un gif"""
    universe1=np.array([[0,0,0,0,0,0],[0,1,1,0,0,0],[0,1,1,0,0,0],[0,0,0,1,1,0],[0,0,0,1,1,0],[0,0,0,0,0,0]])
    #univers avec un beacon
    fig = plt.figure()
    im=plt.imshow(universe1,cmap='Greys',animated=True)

    def animate(i):
        """fonction pour gerer l'animation"""
        universe1=im.get_array()
        im.set_array(generation(universe1))
        return [im]

    anime = anim.FuncAnimation(fig, animate,frames=10, interval=500, blit=True)
    #creation de l'animation
    #anime.save('beacon.gif',writer='imagemagick')
    #sauvegarde un gif de l'animation
    plt.show()
    #afficher l'animation
























