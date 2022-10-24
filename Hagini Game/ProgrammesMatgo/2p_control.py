import sys

import pygame

pygame.init()
pygame.display.set_caption('hagini game')
screen = pygame.display.set_mode((500,500), 0, 32)
clock = pygame.time.Clock()

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

colors = [(255, 0, 0),(0, 255, 0),(0, 0, 255)]

my_square = pygame.Rect(50, 50, 50, 50)
my_square_color = 0
motion = [0, 0]

my_square_clavier = pygame.Rect(400,50,50,50)
my_square_clavier_color = 0
motion_clavier = [0, 0]

while True:
    screen.fill((0,0,0))

    pygame.draw.rect(screen, colors[my_square_color], my_square)
    pygame.draw.rect(screen, colors[my_square_clavier_color], my_square_clavier)

    #dead zone joystick
    '''if abs(motion[0]) < 0.1:
        motion[0] = 0
    if abs(motion[1]) < 0.1:
        motion[1] = 0'''

    my_square.x += motion[0] * 10
    my_square.y += motion[1] * -10

    my_square_clavier.x += motion_clavier[0] * 10
    my_square_clavier.y += motion_clavier[1] * -10

    for event in pygame.event.get():
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
            joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
            print("manette connecté")
        if event.type == JOYDEVICEREMOVED:
            joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
            print("manette déconnecté")

        # support clavier
        if event.type == pygame.KEYDOWN:
            print(event)
            if pygame.key.get_pressed()[K_z]:
                print("haut")
                motion_clavier[1] = 1
            if pygame.key.get_pressed()[K_s]:
                print("bas")
                motion_clavier[1] = -1
            if pygame.key.get_pressed()[K_q]:
                print("gauche")
                motion_clavier[0] = -1
            if pygame.key.get_pressed()[K_d]:
                print("droite")
                motion_clavier[0] = 1
            if pygame.key.get_pressed()[K_j]:
                my_square_clavier_color = (my_square_clavier_color + 1) % len(colors)

        if event.type == pygame.KEYUP:

            print(event)

            xd = pygame.key.get_pressed()[K_d]
            xz = pygame.key.get_pressed()[K_z]
            xs = pygame.key.get_pressed()[K_s]
            xq = pygame.key.get_pressed()[K_q]

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
            pygame.quit()
            sys.exit()

    #print(motion)
    pygame.display.update()
    clock.tick(60)