import sys

import pygame
import random

from pygame import *
pygame.init()
pygame.display.set_caption('tel sans se faire choper')
screen = pygame.display.set_mode((500,500), 0, 32)
clock = pygame.time.Clock()

random.seed()

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

colors = [(0, 255, 0),(255, 0, 0)]
color_switch = 0

i = 50 # compteur pour le cercle ( laisse du temps au joueur pou arréter d'appuyer )
x = random.randrange(1,100,1) # compteur pour que le carré reste

attention = 0 # fait apparaitre le cercle
carré_up = 0 # vérifie si le carré est présent

button_pressed = 0 # vérifie si le bouton est préssé

jauge = 0 # jauge de victoire (doit arriver a 1000)
victoire = 1000 # objectif pour gagner

while True:
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, colors[color_switch], (200,200,50,50))

    # temps que le cercle n'apparait pas ( que pop n'est pas egal a 1 ), génère des valeurs
    if attention == 0:
        pop = random.randrange(1,100,1)

    # vérifie quand la valeur 1 arrive, bloque la génération d'autre valeurs, fait apparaitre un cercle, et commence un décompte pour faire apparaitre le carré
    if pop == 1:
        attention = 1
        pygame.draw.circle(screen,(255,0,0),(375,125),50,2)
        pygame.display.update()
        if i > 0:
            i -= 1

     # une fois décompte du carré fait, le fait apparaitre, et commence un autre décompte pour le faire disparaitre
    if i == 0:
        pygame.draw.rect(screen, (0, 0, 255), (350, 100, 50, 50))
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
            pygame.quit()
            sys.exit()

    # augmente la jauge de victoire
    if button_pressed == 1:
        if carré_up == 0:
            jauge += 1

    # condition de victoire
    if jauge == victoire:
        print("victoire")
        pygame.quit()
        sys.exit()

    print(jauge)

    for event in pygame.event.get():

        if event.type == JOYBUTTONDOWN:
            # A button
            if event.button == 0:
                button_pressed = 1
                # change la couleur du bouton (a terme, changer le sprite de l'élève)
                color_switch = 1

        if event.type == JOYBUTTONUP:
            if event.button == 0:
                color_switch = 0
                button_pressed = 0

        # affiche quand la manette se connecte et déconnecte
        if event.type == JOYDEVICEADDED:
            joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
            print("manette connecté")
        if event.type == JOYDEVICEREMOVED:
            joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
            print("manette déconnecté")

        # fermer le jeu
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)