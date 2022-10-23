import sys

import pygame
import random
import time

from pygame import *
pygame.init()
pygame.display.set_caption('whack-a-mole')
screen = pygame.display.set_mode((500,500), 0, 32)
clock = pygame.time.Clock()

random.seed()

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

colors = [(255, 0, 0),(0, 255, 0),(0, 0, 255)]

bout_OK = 0

gauche = 0
droite = 0
haut = 0
bas = 0

color_switch = 0

while True:
    screen.fill((0,0,0))

    pygame.draw.circle(screen, (255, 0, 0), (150,235),40, 2)
    pygame.draw.circle(screen, (255, 0, 0), (235,150),40, 2)
    pygame.draw.circle(screen, (255, 0, 0), (315,235),40, 2)
    pygame.draw.circle(screen, (255, 0, 0), (235,315),40, 2)

    if bout_OK == 1:
        var_sortie = random.randrange(1, 5, 1)

        if var_sortie == 1:
            gauche = 1
        if var_sortie == 2:
            haut = 1
        if var_sortie == 3:
            droite = 1
        if var_sortie == 4:
            bas = 1

    if gauche == 1:
        pygame.draw.rect(screen, colors[color_switch], (135, 220, 30, 30))
        bout_OK = 0
    if droite == 1:
        pygame.draw.rect(screen, colors[color_switch], (300,220,30,30))
        bout_OK = 0
    if haut == 1:
        pygame.draw.rect(screen, colors[color_switch], (220,135,30,30))
        bout_OK = 0
    if bas == 1:
        pygame.draw.rect(screen, colors[color_switch], (220,300,30,30))
        bout_OK = 0

    for event in pygame.event.get():

        # bouton A B X Y
        if event.type == JOYBUTTONDOWN:
            #print(event)
            # start button
            if event.button == 7: # demarrer la partie
                bout_OK = 1

            # A button
            if event.button == 0:
                if bas == 1:
                    bout_OK = 1
                    bas = 0
                    color_switch = (color_switch + 1) % len(colors)
            # B button
            if event.button == 1:
                if droite == 1:
                    bout_OK = 1
                    droite = 0
                    color_switch = (color_switch + 1) % len(colors)
            # X button
            if event.button == 2:
                if gauche == 1:
                    bout_OK = 1
                    gauche = 0
                    color_switch = (color_switch + 1) % len(colors)
            # Y button
            if event.button == 3:
                if haut == 1:
                    bout_OK = 1
                    haut = 0
                    color_switch = (color_switch + 1) % len(colors)

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