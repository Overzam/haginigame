import sys         

import pygame as pyg
import random

from pygame import *

pyg.init()
pyg.display.set_caption('tel sans se faire choper')

width = 1920
height = 1080

screen = pyg.display.set_mode((width, height), 0, 32)

jauge_visu = pyg.image.load('Assets/tel_sans_se_faire_choper/progress.png')
end = pyg.image.load('Assets/tel_sans_se_faire_choper/end.png')

victoire_screen = pyg.image.load('Assets/Tape_Taupe/win.png')
defaite = pyg.image.load('Assets/Tape_Taupe/defaite.png')

clock = pyg.time.Clock()

random.seed()

colors = [(0, 255, 0),(255, 0, 0)]
color_switch = 0

ending = -1

i = 50 # compteur pour le cercle ( laisse du temps au joueur pou arréter d'appuyer )
x = random.randrange(1,100,1) # compteur pour que le carré reste

attention = 0 # fait apparaitre le cercle
carré_up = 0 # vérifie si le carré est présent

button_pressed = 0 # vérifie si le bouton est préssé

jauge = 100 # jauge de victoire (doit arriver a 1000)
victoire = 500 # objectif pour gagner

run = True
run_fin = True

while run:
    screen.fill((0, 0, 0))

    screen.blit(jauge_visu, (20, 60))
    jauge_visu = pyg.transform.scale(jauge_visu, (jauge, 10))

    screen.blit(end, (470, 20))
    end = pyg.transform.scale(end, (100, 100))

    pyg.draw.rect(screen, colors[color_switch], (width/3,height/2,50,50))

    # temps que le cercle n'apparait pas ( que pop n'est pas egal a 1 ), génère des valeurs
    if attention == 0:
        pop = random.randrange(1,100,1)

    # vérifie quand la valeur 1 arrive, bloque la génération d'autre valeurs, fait apparaitre un cercle, et commence un décompte pour faire apparaitre le carré
    if pop == 1:
        attention = 1
        pyg.draw.circle(screen,(255,0,0),(width/2,height/3),50,2)
        if i > 0:
            i -= 1

     # une fois décompte du carré fait, le fait apparaitre, et commence un autre décompte pour le faire disparaitre
    if i == 0:
        pyg.draw.rect(screen, (0, 0, 255), (width/2.05,height/3.2, 50, 50))
        carré_up = 1
        if x > 0:
            x -= 1

    # une fois décompte pour faire disparaitre le carré fait, recommence a donné des valeurs,
    # réinitialise les timers, avec celui qui fait disparaitre le carré qui est aléatoire
    if x == 0:
        carré_up = 0
        attention = 0
        i = 100
        x = random.randrange(1,100,1)

    # condition de défaite
    if button_pressed == 1:
        if carré_up == 1:
            print("perdu")
            ending = 0
            run_fin = True
            run = False

    # augmente la jauge de victoire
    if button_pressed == 1:
        if carré_up == 0:
            jauge += 1

    # condition de victoire
    if jauge == victoire:
        ending = 1
        print("victoire")
        run_fin = True
        run = False

    print(jauge)

    for event in pyg.event.get():

        if event.type == KEYDOWN:
            if event.key == pyg.K_SPACE:
                button_pressed = 1
                # change la couleur du bouton (a terme, changer le sprite de l'élève)
                color_switch = 1

        if event.type == KEYUP:
            if event.key == pyg.K_SPACE:
                color_switch = 0
                button_pressed = 0  

        # fermer le jeu
        if event.type == QUIT:
            pyg.quit()
            sys.exit()

    pyg.display.update()
    clock.tick(60)

while run_fin:

    screen.fill((0, 0, 0))

    if ending == 1:
        screen.blit(victoire_screen, (0, 0))
        victoire_screen = pyg.transform.scale(victoire_screen, (1920,1080))
    else:
        screen.blit(defaite, (0, 0))
        defaite = pyg.transform.scale(defaite, (1920,1080))

    for event in pyg.event.get():

        if event.type == QUIT:
            pyg.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            pyg.quit()
            sys.exit()
    
    pyg.display.update()
    clock.tick(60)