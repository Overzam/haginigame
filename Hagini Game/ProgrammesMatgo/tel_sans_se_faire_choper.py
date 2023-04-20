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

perso = pyg.image.load('Assets/tel_sans_se_faire_choper/perso_tel_non.png')

classe = pyg.image.load('Assets/tel_sans_se_faire_choper/classe.png')
classe_attention = pyg.image.load('Assets/tel_sans_se_faire_choper/prof_approche.png')
classe_prof = pyg.image.load('Assets/tel_sans_se_faire_choper/prof_la.png')

classe = pyg.transform.scale(classe, (1920, 1080))
classe_attention = pyg.transform.scale(classe_attention, (1920, 1080))
classe_prof = pyg.transform.scale(classe_prof, (1920, 1080))

classe_etat = 0  # 0 = chill, 1 = attention, 2 = prof

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

warn = 1

run = True
run_fin = True

while run:

    if classe_etat == 0:
        screen.blit(classe, (0, 0))
    if classe_etat == 1:
        screen.blit(classe_attention, (0, 0))
    if classe_etat == 2:
        screen.blit(classe_prof, (0, 0))

    screen.blit(jauge_visu, (20, 60))
    jauge_visu = pyg.transform.scale(jauge_visu, (jauge, 10))

    screen.blit(end, (470, 20))
    end = pyg.transform.scale(end, (100, 100))

    screen.blit(perso, (50, 50))
    perso = pyg.transform.scale(perso, (120,200))

    classe_etat = 0

    if warn == 1:
        perso = pyg.image.load('Assets/tel_sans_se_faire_choper/perso_tel_non.png')
    print(warn)

    # temps que le cercle n'apparait pas ( que pop n'est pas egal a 1 ), génère des valeurs
    if attention == 0:
        pop = random.randrange(1,100,1)

    # vérifie quand la valeur 1 arrive, bloque la génération d'autre valeurs, fait apparaitre un cercle, et commence un décompte pour faire apparaitre le carré
    if pop == 1:
        attention = 1
        classe_etat = 1
        if i > 0:
            i -= 1

     # une fois décompte du carré fait, le fait apparaitre, et commence un autre décompte pour le faire disparaitre
    if i == 0:
        classe_etat = 2
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
                perso = pyg.image.load('Assets/tel_sans_se_faire_choper/perso_tel.png')
                warn = 0

        if event.type == KEYUP:
            if event.key == pyg.K_SPACE:
                color_switch = 0
                button_pressed = 0  
                warn = 1

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