import pygame
import random
from game_of_life2.evolution import*
import numpy as np

white = (255, 255, 255)
black = (0, 0, 0)
red = (225,0,0)

largeur = int(input("Entrez la largeur de l'univers : "))
hauteur = int(input("Entrez la hauteur de l'univers : "))
universe = np.zeros((largeur, hauteur))

def generate_universe():
    """fonction générant un univers au hasard"""
    for y in range(hauteur):
        for x in range(largeur):
            universe[x][y] = random.randint(0,1)
    return universe

def play():
    """permet de lancer le jeu de la vie avec un nombre de case choisi par l'utilisateur et affichage du nombre d'étape"""
    compteur = 0
    x_screen_size = largeur*10
    y_screen_size = hauteur*10
    pygame.init()
    universe = generate_universe()
    ecran = pygame.display.set_mode((x_screen_size,y_screen_size))
    #création de la fenêtre
    surface = pygame.Surface((x_screen_size,y_screen_size))
    #création de la surface représentant le jeu
    pygame.display.set_caption("Random game of life")
    continuer = True
    while continuer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #quitte le jeu de la vie si on appuie sur la croix rouge
                continuer = False
                pygame.quit()
        for y in range(hauteur):
            for x in range(largeur):
                if universe[x][y] == 1:
                    #Couleur du jeu de la vie
                    pygame.draw.rect(surface, black, (x * 10, y * 10, 10, 10))
                else:
                    pygame.draw.rect(surface, white, (x * 10, y * 10, 10, 10))
        font = pygame.font.Font(None, 24)
        text = font.render("Nombre de générations : " + str(compteur), 1, red)
        #affichage d'un compteur d'étape
        ecran.blit(text, (x_screen_size//2,0))
        pygame.display.flip()
        compteur += 1
        universe = generation(universe)
        #On met à jour l'univers avec les règles du jeu de la vie
        ecran.blit(surface, (0,0))
        pygame.display.flip()
        #On affiche l'univers mis à jour

if __name__ == '__main__':
    play()

"""import copy
import pygame
from pygame import *
import random

#constants
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
#neighbour coordinates
neighbours = [[-1,-1],[-1,0],[-1,+1],
              [0,-1],        [0,+1],
              [+1,-1],[+1,0],[+1,+1],]

class cell(object):
        def __init__(self, ngb, state):
                self.state = state
                self.ngb = 0

#2d array for storing cells
cells = [[i for i in range(50)] for i in range(50)]

#random field generation
def generate():
        print("Generating")
        for y in range(50):
                for x in range(50):
                        cells[x][y] = cell(0, random.randint(0, 1))
        print("DoneGen")

#neighbour processing
def update():
        global cells2
        #saving this turn's state
        cells2=copy.deepcopy(cells)
        for y in range(50):
                for x in range(50):
                        cellv2=cells2[x][y]
                        cellv2.ngb=0
                        cellv = cells[x][y]
                        #processing
                        for i in neighbours:
                                #offsetting neighbour coordinates
                                dy=i[0]+y
                                dx=i[1]+x
                                if dy < 0:
                                        dy = 49
                                if dy > 49:
                                        dy = 0
                                if dx < 0:
                                        dx = 49
                                if dx > 49:
                                        dx = 0
                                if cells2[dx][dy].state==1:
                                        cellv2.ngb+=1
                        #updating field
                        if cellv2.state==1 and 2<=cellv2.ngb<=3:
                                cellv.state=1
                        else:
                                cellv.state=0
                        if cellv2.state==0 and cellv2.ngb==3:
                                cellv.state=1

#main game function
def play():
        #initialization
        pygame.init()
        scrn = pygame.display.set_mode((500, 500))
        mainsrf = pygame.Surface((500, 500))
        mainsrf.fill(white)
        generate()
        #game cycle
        while 1:
                #tracking quitting
                for event in pygame.event.get():
                        if event.type == QUIT:
                                pygame.quit()
                                sys.exit()
                #drawing
                for y in range(50):
                        for x in range(50):
                                if cells[x][y].state==1:
                                        pygame.draw.rect(mainsrf, black, (x*10, y*10, 10, 10))
                                else:
                                        pygame.draw.rect(mainsrf, white, (x*10, y*10, 10, 10))
                                if cells[x][y].ngb==3:
                                        pygame.draw.rect(mainsrf, red, (x*10, y*10, 10, 10))
                update()
                scrn.blit(mainsrf, (0, 0))
                pygame.display.update()



#running the game
if __name__ == "__main__":
    play()"""


