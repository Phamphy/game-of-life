from tkinter import *
import numpy as np
from game_of_life2.evolution import *
from game_of_life2.initialization import *
from game_of_life2.generate_universe import *
import time

gameoflife1 = Tk()

hauteur=500
largeur=500
#taille du canvas

def seed_chosen():
    """fonction appelee a chaque fois qu'on choisit un seed dans l'interface graphique, il faut alors s'assurer que l'univers est assez grand pour accueillir la seed"""
    seed_name = selected_seed.get()
    seed = seeds[seed_name]
    seed_array = np.array(seed)
    x_dimension=seed_array.shape[0]
    #taille de la seed suivant x
    y_dimension=seed_array.shape[1]
    #taille de la seed suivant y
    if x_dimension>int(universe_x.get()):
        #si le seed est plus grand que l'univers suivant x
        var_universe_x.set(x_dimension)
    universe_x["from_"]=x_dimension
    #on empeche l'utilisateur de pouvoir creer un univers plus petit que le seed suivant x
    if y_dimension>int(universe_y.get()):
        #si le seed est plus grand que l'univers suivant x
        var_universe_y.set(y_dimension)
    universe_y["from_"]=y_dimension
    #on empeche l'utilisateur de pouvoir creer un univers plus petit que le seed suivant x
    var_seed_x.set(0)
    var_seed_y.set(0)
    #on reset la position du seed a chaque changement de type de seed


def prepared_simulation():
    """fonction appeler lorsque l'on clique sur le bouton pour lancer l'animation"""
    seed_array=np.array(seeds[selected_seed.get()])
    #recuperer le seed voulu
    grid_game = add_seed_to_universe(seed_array,generate_universe((int(universe_x.get()),int(universe_y.get()))),x_start=int(var_seed_x.get()), y_start=int(var_seed_y.get()))
    #generer l'univers sopuhaite avec le seed incorpore
    seed_x["state"]=DISABLED
    seed_y["state"]=DISABLED
    universe_x["state"]=DISABLED
    universe_y["state"]=DISABLED
    button_start["state"]=DISABLED
    nbr_etape_box["state"]=DISABLED
    refresh_box["state"]=DISABLED
    #On desactive les widgets pour éviter que l'utilisateur ne perturbe la simulation
    simuler(grid_game,int(nbr_etape.get()))
    #lancer la simulation
    seed_x["state"]="readonly"
    seed_y["state"]="readonly"
    universe_x["state"]="readonly"
    universe_y["state"]="readonly"
    button_start["state"]=NORMAL
    nbr_etape_box["state"]="readonly"
    refresh_box["state"]="readonly"
    #On reactive les widgets


def change_seed_x():
    """fonction appelee a chaque fois que l'on change la position du seed suivant x, on verifie que le seed est bien contenu dans l'univers suivant x"""
    seed_x_position=int(var_seed_x.get())
    #position suivant x du seed
    universe_x_dimension=int(universe_x.get())
    #taille suivant x de l'univers
    seed_x_dimension=np.array(seeds[selected_seed.get()]).shape[0]
    #taille suivant x du seed
    if seed_x_position+seed_x_dimension>universe_x_dimension:
        #si le seed depasse de l'univers suivant x
        var_seed_x.set(universe_x_dimension-seed_x_dimension)


def change_seed_y():
    """fonction appelee a chaque fois que l'on change la position du seed suivant y, on verifie que le seed est bien contenu dans l'univers suivant y"""
    seed_y_position=int(var_seed_y.get())
    #position suivant y du seed
    universe_y_dimension=int(universe_y.get())
    #taille suivant y de l'univers
    seed_y_dimension=np.array(seeds[selected_seed.get()]).shape[1]
    #taille suivant y du seed
    if seed_y_position+seed_y_dimension>universe_y_dimension:
        #si le seed depasse de l'univers suivant y
        var_seed_y.set(universe_y_dimension-seed_y_dimension)


def increase_step():
    """fonction appelee a chaque etape de la simulation, elle permet de mettre a jour l'affichage indiquant a quelle etape on se situe"""
    step=int(current_step.get())
    step+=1
    current_step.set(str(step))
    #on met a jour le IntVar


def reset_step():
    """fonction appelee a la fin de la simulation pour remettre a zero l'affichage de l'etape actuelle"""
    current_step.set("0")
    #on met a jour le IntVar



gameoflife = Toplevel(gameoflife1)
gameoflife.grid()
#creation des fenetres
graphical_grid = Canvas(gameoflife,bg='white',height=hauteur,width=largeur)
graphical_grid.pack()
#creation et placement du canvas


param_universe = LabelFrame(gameoflife1, text="Paramètres de l'univers")
param_universe.pack()
#creation d'une frame contenant les widgets relatifs a la creation de l'univers

var_universe_x = IntVar()
universe_x = Spinbox(param_universe, from_=4, to=100,state="readonly",textvariable=var_universe_x)
universe_x.grid(row=0,column=1)
var_universe_y = IntVar()
universe_y = Spinbox(param_universe, from_=4, to=100,state="readonly",textvariable=var_universe_y)
universe_y.grid(row=1,column=1)
label_x = Label(param_universe,text="hauteur")
label_x.grid(row=0,column=0)
label_y = Label(param_universe,text="largeur")
label_y.grid(row=1,column=0)
#creation des spinboxs permettants de recuperer les dimmensions de l'univers


param_seed = LabelFrame(gameoflife1, text="Paramètres du seed")
param_seed.pack()
#creation d'une frame contenant les widgets relatifs a la gestion du seed

selected_seed = StringVar()
selected_seed.set("boat")
for name in seeds.keys():
    Radiobutton(param_seed,variable=selected_seed,text=name, value=name,command=seed_chosen).pack()
#creation de radiobuttons pour selectionner le seed souhaite

param_seed2 = LabelFrame(param_seed, text="Position du seed")
param_seed2.pack(side=RIGHT)
#creation d'une frame contenant les widgets relatifs au positionnement du seed

labelS_x = Label(param_seed2,text="hauteur")
labelS_x.grid(row=0,column=0)
labelS_y = Label(param_seed2,text="largeur")
labelS_y.grid(row=1,column=0)
var_seed_x = IntVar()
seed_x = Spinbox(param_seed2, from_=0, to=99,state="readonly",textvariable=var_seed_x,command=change_seed_x)
seed_x.grid(row=0,column=1)
var_seed_y = IntVar()
seed_y = Spinbox(param_seed2, from_=0, to=99,state="readonly",textvariable=var_seed_y,command=change_seed_y)
seed_y.grid(row=1,column=1)
#creation des spinboxs permettants de recuperer la position du seed


button_start = Button(gameoflife1,text="Lancer la simulation",command=prepared_simulation)
button_start.pack()
#creation du bouton pour lancer la simulation


param_simulation = LabelFrame(gameoflife1, text="Paramètres de la simulation")
param_simulation.pack()
#creation d'une frame contenant les widgets relatifs aux parametres de la simulation

label_nbr_etape = Label(param_simulation,text="Nombre d'étape souhaité :")
label_nbr_etape.grid(row=0,column=0)
nbr_etape = IntVar()
nbr_etape.set(20)
nbr_etape_box = Spinbox(param_simulation, from_=1, to=100,state="readonly",textvariable=nbr_etape)
nbr_etape_box.grid(row=0,column=1)
step_label = Label(param_simulation,text="etape :")
step_label.grid(row=1,column=0)
current_step=StringVar()
current_step.set("0")
current_step_label = Label(param_simulation,textvariable=current_step)
current_step_label.grid(row=1,column=1)
#creation d'une spinbox et d'un label pour choisir le nombre d'etape voulue et afficher quelle est l'etape courante lors d'une simulation

refresh_label = Label(param_simulation,text="rapidité")
refresh_label.grid(row=2,column=0)
refresh_rate=IntVar()
refresh_rate.set(7)
refresh_box = Spinbox(param_simulation, from_=1, to=10,state="readonly",textvariable=refresh_rate)
refresh_box.grid(row=2,column=1)
#creation d'une spinbox pour regler la rapidite d'execution entre deux etapes (10 vitesse max)



def config_display(grid_game, max):
    """retourne la taille que doit avoir une cellule en pixel par rapport à la taille de l'univers et du canvas"""
    nbr_case_x=grid_game.shape[0]
    nbr_case_y=grid_game.shape[1]
    graphical_grid["height"]=max
    graphical_grid["width"]=max
    #on initialise la taille du canvas à un carre de max*max pixels
    if nbr_case_x>nbr_case_y :
        graphical_grid["width"]=nbr_case_y*max/nbr_case_x
        #on redimensionne le canvas
        return max/nbr_case_x
    else :
        graphical_grid["height"]=nbr_case_x*max/nbr_case_y
        #on redimensionne le canvas
        return max/nbr_case_y



def draw_universe(grid_game, taille_pixel):
    """dessine l'univers dans le canvas"""
    for x in range(grid_game.shape[0]):
        for y in range(grid_game.shape[1]):
            #on parcourt chaque cellule de l'univers
            if grid_game[x, y]==1:
                draw_cell(x,y,"black",taille_pixel)
                #si la cellule est vivante, elle apparait noire
            else:
                draw_cell(x,y,"white",taille_pixel)
                #si la cellule est morte, elle apparait blanche


def draw_cell(x,y,couleur,taille_pixel):
    """dessine la cellule correspondant à la position (x,y) de l'univers"""
    graphical_grid.create_rectangle(y*taille_pixel,x*taille_pixel,(y+1)*taille_pixel,(x+1)*taille_pixel,fill=couleur)


def simuler(grid_game, n):
    """simule le jeu de la vie pour un univers de depart donne, pour n etapes"""
    taille_pixel=config_display(grid_game, 500)
    #on recupere la taille des cellule a afficher
    temps_mort=1/int(refresh_rate.get())
    #temps d'attente entre deux etapes
    for etape in range(n):
        increase_step()
        draw_universe(grid_game, taille_pixel)
        #on dessine l'univers
        grid_game=generation(grid_game)
        #on stocke le prochain univers
        time.sleep(temps_mort)
        #on patiente un peu pour que l'animation soit visible
        graphical_grid.update()
        #on s'assure que le canvas se mette bien a jour
    reset_step()


gameoflife.mainloop()
