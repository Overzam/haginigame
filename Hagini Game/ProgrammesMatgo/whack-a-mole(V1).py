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

while True:
    screen.fill((0,0,0))

    pyg.draw.circle(screen, (255, 0, 0), (width/2.28, height/2),40, 2) # gauche
    pyg.draw.circle(screen, (255, 0, 0), (width/2, height/2.5),40, 2) # haut
    pyg.draw.circle(screen, (255, 0, 0), (width/1.8,height/2),40, 2) # droite
    pyg.draw.circle(screen, (255, 0, 0), (width/2, height/1.65),40, 2) # bas

    # généré une nouvelle valeur, un nouveau carré
    if bout_OK == 1:
        var_sortie = random.randrange(1, 5, 1)

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
        pyg.draw.rect(screen, colors[color_switch], (width/2.32, height/2.05, 30, 30)) # + 0.04 / + 0.05
        bout_OK = 0

    if droite == 1:
        pyg.draw.rect(screen, colors[color_switch], (width/1.826,height/2.05,30,30))
        bout_OK = 0

    if haut == 1:
        pyg.draw.rect(screen, colors[color_switch], (width/2.03, height/2.59,30,30))
        bout_OK = 0

    if bas == 1:
        pyg.draw.rect(screen, colors[color_switch], (width/2.03, height/1.69,30,30))
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
            #print(event)
            # start button
            if event.key == pyg.K_SPACE: # demarrer la partie
                if game_start == 0:
                    bout_OK = 1
                    s = secondes
                    game_start = 1

            # bas ( genere une nouvelle valeur, change la couleur, reset le timer, +1 point )
            if event.key == K_DOWN:
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
            if event.key == K_RIGHT:
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
            if event.key == K_LEFT:
                # vérifie si le bouton appyuer est le bon
                if gauche == 1:
                    bout_OK = 1
                    gauche = 0
                    color_switch = (color_switch + 1) % len(colors)
                    s = secondes
                    points += 1
                else:
                    points -= 1
            # Y button ( genere une nouvelle valeur, change la couleur, reset le timer, +1 point )
            if event.key == K_UP:
                # vérifie si le bouton appyuer est le bon
                if haut == 1:
                    bout_OK = 1
                    haut = 0
                    color_switch = (color_switch + 1) % len(colors)
                    s = secondes
                    points += 1
                else:
                    points -= 1

        # affiche quand la manette se connecte et déconnecte
        if event.type == JOYDEVICEADDED:
            joysticks = [pyg.joystick.Joystick(i) for i in range(pyg.joystick.get_count())]
            print("manette connecté")
        if event.type == JOYDEVICEREMOVED:
            joysticks = [pyg.joystick.Joystick(i) for i in range(pyg.joystick.get_count())]
            print("manette déconnecté")

        # fermer le jeu
        if event.type == QUIT:
            pyg.quit()
            sys.exit()

    pyg.display.update()
    clock.tick(60)