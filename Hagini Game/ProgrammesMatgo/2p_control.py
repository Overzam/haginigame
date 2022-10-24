import sys

import pygame as pyg

<<<<<<< HEAD
from pygame import *
pyg.init()
pyg.display.set_caption('hagini game')
=======
pygame.init()
pygame.display.set_caption('hagini game')
screen = pygame.display.set_mode((500,500), 0, 32)
clock = pygame.time.Clock()
>>>>>>> 1bb448a1585bafacc853a0b3c8639a54385ef352

width = 1920
height = 1080
screen = pyg.display.set_mode((width,height), 0, 32)

clock = pyg.time.Clock()

pyg.joystick.init()
joysticks = [pyg.joystick.Joystick(i) for i in range(pyg.joystick.get_count())]

colors = [(255, 0, 0),(0, 255, 0),(0, 0, 255)]

my_square = pyg.Rect(50, 50, 50, 50)
my_square_color = 0
motion = [0, 0]

my_square_clavier = pyg.Rect(400,50,50,50)
my_square_clavier_color = 0
motion_clavier = [0, 0]

while True:
    screen.fill((0,0,0))

    pyg.draw.rect(screen, colors[my_square_color], my_square)
    pyg.draw.rect(screen, colors[my_square_clavier_color], my_square_clavier)

    #dead zone joystick
    '''if abs(motion[0]) < 0.1:
        motion[0] = 0
    if abs(motion[1]) < 0.1:
        motion[1] = 0'''

    my_square.x += motion[0] * 10
    my_square.y += motion[1] * -10

    my_square_clavier.x += motion_clavier[0] * 10
    my_square_clavier.y += motion_clavier[1] * -10

    for event in pyg.event.get():
        # support manette

        # bouton A B X Y
        if event.type == JOYBUTTONDOWN:
            print(event)
            # bouton A
            if event.button == 0:
                my_square_color = (my_square_color + 1) % len(colors)
        # D-pad
        if event.type == JOYHATMOTION:
            #print(event)
            if event.value == (0,1):
                print("haut")
                motion = event.value
            if event.value == (0,-1):
                print("bas")
                motion = event.value
            if event.value == (-1,0):
                print("gauche")
                motion = event.value
            if event.value == (1,0):
                print("droite")
                motion = event.value
            motion = event.value

        # affiche quand la manette se connecte et déconnecte
        if event.type == JOYDEVICEADDED:
            joysticks = [pyg.joystick.Joystick(i) for i in range(pyg.joystick.get_count())]
            print("manette connecté")
        if event.type == JOYDEVICEREMOVED:
            joysticks = [pyg.joystick.Joystick(i) for i in range(pyg.joystick.get_count())]
            print("manette déconnecté")

        # support clavier
        if event.type == pyg.KEYDOWN:
            print(event)
            if pyg.key.get_pressed()[K_z]:
                print("haut")
                motion_clavier[1] = 1
            if pyg.key.get_pressed()[K_s]:
                print("bas")
                motion_clavier[1] = -1
            if pyg.key.get_pressed()[K_q]:
                print("gauche")
                motion_clavier[0] = -1
            if pyg.key.get_pressed()[K_d]:
                print("droite")
                motion_clavier[0] = 1
            if pyg.key.get_pressed()[K_j]:
                my_square_clavier_color = (my_square_clavier_color + 1) % len(colors)

        if event.type == pyg.KEYUP:

            print(event)

            xd = pyg.key.get_pressed()[K_d]
            xz = pyg.key.get_pressed()[K_z]
            xs = pyg.key.get_pressed()[K_s]
            xq = pyg.key.get_pressed()[K_q]

            if motion_clavier[1] == 1:
                if xz == False:
                    print("haut_UP")
                    motion_clavier[1] = 0
            if motion_clavier[1] == -1:
                if xs == False:
                    print("bas_UP")
                    motion_clavier[1] = 0
            if motion_clavier[0] == -1:
                if xq == False:
                    print("gauche_UP")
                    motion_clavier[0] = 0
            if motion_clavier[0] == 1:
                if xd == False:
                    print("droite_UP")
                    motion_clavier[0] = 0

        # fermer le jeu
        if event.type == QUIT:
            pyg.quit()
            sys.exit()

    #print(motion)
    pyg.display.update()
    clock.tick(60)