import sys

import pygame
import random

from pygame import *
pygame.init()
pygame.display.set_caption('whack-a-mole')
screen = pygame.display.set_mode((500,500), 0, 32)
clock = pygame.time.Clock()

random.seed()

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

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

while True:
    screen.fill((0,0,0))

    pygame.draw.circle(screen, (255, 0, 0), (150,235),40, 2)
    pygame.draw.circle(screen, (255, 0, 0), (235,150),40, 2)
    pygame.draw.circle(screen, (255, 0, 0), (315,235),40, 2)
    pygame.draw.circle(screen, (255, 0, 0), (235,315),40, 2)

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

    for event in pygame.event.get():

        # bouton A B X Y
        if event.type == JOYBUTTONDOWN:
            #print(event)
            # start button
            if event.button == 7: # demarrer la partie
                bout_OK = 1
                s = secondes
                game_start = 1

            # A button ( genere une nouvelle valeur, change la couleur, reset le timer, +1 point )
            if event.button == 0:
                # vérifie si le bouton appyuer est le bon
                if bas == 1:
                    bout_OK = 1
                    bas = 0
                    color_switch = (color_switch + 1) % len(colors)
                    s = secondes
                    points += 1
                else:
                    points -= 1
            # B button ( genere une nouvelle valeur, change la couleur, reset le timer, +1 point )
            if event.button == 1:
                # vérifie si le bouton appyuer est le bon
                if droite == 1:
                    bout_OK = 1
                    droite = 0
                    color_switch = (color_switch + 1) % len(colors)
                    s = secondes
                    points += 1
                else:
                    points -= 1
            # X button ( genere une nouvelle valeur, change la couleur, reset le timer, +1 point )
            if event.button == 2:
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
            if event.button == 3:
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