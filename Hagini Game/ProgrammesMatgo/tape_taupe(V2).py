import sys

import pygame as pyg
import random

from pygame import *
pyg.init()
pyg.display.set_caption('whack-a-mole')

width = 1920
height = 1080
screen = pyg.display.set_mode((width,height), 0, 32)

clock = pyg.time.Clock()

random.seed()

colors = [(255, 0, 0),(0, 255, 0),(0, 0, 255)]

# condition qui permet de générer une nouveau carré
bout_OK = 0

gauche = 0
droite = 0
haut = 0
bas = 0

color_switch = 0

secondes = 75 # temps pour taper les taupes
s = secondes

points = 0

game_start = 0

timer_de_fin = 2000

viseur = pyg.image.load('viseur.png')

trou_haut_x = width/2.03
trou_haut_y = height/2.59

trou_droite_x = width/1.826
trou_droite_y = height/2.05

trou_gauche_x = width/2.32
trou_gauche_y = height/2.05

trou_bas_x = width/2.03
trou_bas_y = height/1.69

trou_haut = Rect(trou_haut_x, trou_haut_y, 80, 80)
trou_droite = Rect(trou_droite_x,trou_droite_y, 80, 80)
trou_gauche = Rect(trou_gauche_x, trou_gauche_y, 80, 80)
trou_bas = Rect(trou_bas_x, trou_bas_y, 80, 80)

taupe_haut = (trou_haut_x + 20, trou_haut_y + 20,40,40)
taupe_droite = (trou_droite_x + 20,trou_droite_y + 20,40,40)
taupe_gauche = (trou_gauche_x + 20, trou_gauche_y + 20, 40, 40)
taupe_bas = (trou_bas_x + 20, trou_bas_y + 20,40,40)

var_sortie = 0

while True:
    screen.fill((0,0,0))
    
    pyg.mouse.set_visible(False)
    
    pos_souris = pyg.mouse.get_pos()
    pos_viseur = list(pos_souris)
    pos_viseur[0] -= 50
    pos_viseur[1] -= 50

    pyg.draw.rect(screen, (255, 0, 0), trou_haut, 1)
    pyg.draw.rect(screen, (255, 0, 0), trou_gauche, 1)
    pyg.draw.rect(screen, (255, 0, 0), trou_droite, 1)
    pyg.draw.rect(screen, (255, 0, 0), trou_bas, 1)

    # généré une nouvelle valeur, un nouveau carré
    if bout_OK == 1:

        prev_var_sortie = var_sortie
        var_sortie = random.randrange(1, 5, 1)

        if var_sortie == 1 and prev_var_sortie == 1:
            var_sortie += 1
        if var_sortie == 2 and prev_var_sortie == 2:
            var_sortie += 1
        if var_sortie == 3 and prev_var_sortie == 3:
            var_sortie += 1
        if var_sortie == 4 and prev_var_sortie == 4:
            var_sortie -= 1

        # applique la carré au bon endroit
        if var_sortie == 1:
            gauche = 1
        if var_sortie == 2:
            haut = 1
        if var_sortie == 3:
            droite = 1
        if var_sortie == 4:
            bas = 1

    # dessine le carré / empêche la création d'une nouvelle valeur
    if gauche == 1:
        pyg.draw.rect(screen, colors[color_switch], taupe_gauche)
        bout_OK = 0

    if droite == 1:
        pyg.draw.rect(screen, colors[color_switch], taupe_droite)
        bout_OK = 0

    if haut == 1:
        pyg.draw.rect(screen, colors[color_switch], taupe_haut)
        bout_OK = 0

    if bas == 1:
        pyg.draw.rect(screen, colors[color_switch], taupe_bas)
        bout_OK = 0

    # compteur qui fait disparaitre le carré et crée une nouvelle valeur (-1 point)
    if game_start == 1:
        if s > 0:
            #print(s)
            s -= 1
        else:
            bout_OK = 1
            droite = 0
            gauche = 0
            haut = 0
            bas = 0
            s = secondes
            color_switch = (color_switch + 1) % len(colors)
            points -= 1

    # limite les points a 0
    if points < 0:
        points = 0

    print(points)
    # victoire a 50 points
    if points == 50:
        print("victoire")
        pyg.quit()
        sys.exit()

    if game_start == 1:
        if timer_de_fin > 0:
            timer_de_fin -= 1
        else:
            print("défaite")
            pyg.quit()
            sys.exit()

    print(timer_de_fin)
    
    for event in pyg.event.get():

        if event.type == KEYDOWN:
            # demarrer la partie
            if event.key == pyg.K_SPACE:
                if game_start == 0:
                    bout_OK = 1
                    s = secondes
                    game_start = 1

        if event.type == pyg.MOUSEBUTTONDOWN:

            # bas ( genere une nouvelle valeur, change la couleur, reset le timer, +1 point )
            if pyg.Rect.collidepoint(trou_bas, pos_souris):
                print("ratio")
                # vérifie si le bouton appyuer est le bon
                if bas == 1:
                    bout_OK = 1
                    bas = 0
                    color_switch = (color_switch + 1) % len(colors)
                    s = secondes
                    points += 1
                else:
                    points -= 1
            # droite ( genere une nouvelle valeur, change la couleur, reset le timer, +1 point )
            if pyg.Rect.collidepoint(trou_droite, pos_souris):
                # vérifie si le bouton appyuer est le bon
                if droite == 1:
                    bout_OK = 1
                    droite = 0
                    color_switch = (color_switch + 1) % len(colors)
                    s = secondes
                    points += 1
                else:
                    points -= 1
            # gauche ( genere une nouvelle valeur, change la couleur, reset le timer, +1 point )
            if pyg.Rect.collidepoint(trou_gauche, pos_souris):
                # vérifie si le bouton appyuer est le bon
                if gauche == 1:
                    bout_OK = 1
                    gauche = 0
                    color_switch = (color_switch + 1) % len(colors)
                    s = secondes
                    points += 1
                else:
                    points -= 1
            # haut ( genere une nouvelle valeur, change la couleur, reset le timer, +1 point )
            if pyg.Rect.collidepoint(trou_haut, pos_souris):
                # vérifie si le bouton appyuer est le bon
                if haut == 1:
                    bout_OK = 1
                    haut = 0
                    color_switch = (color_switch + 1) % len(colors)
                    s = secondes
                    points += 1
                else:
                    points -= 1

        # fermer le jeu
        if event.type == QUIT:
            pyg.quit()
            sys.exit()

    screen.blit(viseur, pos_viseur) #affiche le viseur

    pyg.display.update()
    clock.tick(60)