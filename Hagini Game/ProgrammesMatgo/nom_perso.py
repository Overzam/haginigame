import sys

import pygame as pyg

from pygame import *

pyg.init()
pyg.display.set_caption('hagini game')

width = 500#1920
height = 500#1080

screen = pyg.display.set_mode((width, height), 0, 32)

clock = pyg.time.Clock()

green = (0, 255, 0)
blue = (0, 0, 128)

nom = ''
nom_du_perso = ''

font = pyg.font.Font('freesansbold.ttf', 32)
text = font.render('nom', True, green, blue)

textRect = text.get_rect()
textRect.center = (width // 2, height // 2)

while True:
    screen.fill((0, 0, 0))

    screen.blit(font.render(nom, True, green, blue), textRect)
    screen.blit(font.render(nom_du_perso, True, green, blue), text.get_rect())

    for event in pyg.event.get():

        if event.type == KEYDOWN:
            if event.key == pyg.K_RETURN:
                nom_du_perso = nom
                nom = ''
            if event.key == pyg.K_BACKSPACE:
                nom = nom[:-1]
            if event.key == pyg.K_a:
                nom += 'a'
            if event.key == pyg.K_b:
                nom += 'b'
            if event.key == pyg.K_c:
                nom += 'c'
            if event.key == pyg.K_d:
                nom += 'd'
            if event.key == pyg.K_e:
                nom += 'e'
            if event.key == pyg.K_f:
                nom += 'f'
            if event.key == pyg.K_g:
                nom += 'g'
            if event.key == pyg.K_h:
                nom += 'h'
            if event.key == pyg.K_i:
                nom += 'i'
            if event.key == pyg.K_j:
                nom += 'j'
            if event.key == pyg.K_k:
                nom += 'k'
            if event.key == pyg.K_l:
                nom += 'l'
            if event.key == pyg.K_m:
                nom += 'm'
            if event.key == pyg.K_n:
                nom += 'n'
            if event.key == pyg.K_o:
                nom += 'o'
            if event.key == pyg.K_p:
                nom += 'p'
            if event.key == pyg.K_q:
                nom += 'q'
            if event.key == pyg.K_r:
                nom += 'r'
            if event.key == pyg.K_s:
                nom += 's'
            if event.key == pyg.K_t:
                nom += 't'
            if event.key == pyg.K_u:
                nom += 'u'
            if event.key == pyg.K_v:
                nom += 'v'
            if event.key == pyg.K_w:
                nom += 'w'
            if event.key == pyg.K_x:
                nom += 'x'
            if event.key == pyg.K_y:
                nom += 'y'
            if event.key == pyg.K_z:
                nom += 'z'

        # fermer le jeu
        if event.type == QUIT:
            pyg.quit()
            sys.exit()

    if len(nom) > 10:
        nom = nom[:-1]

    pyg.display.update()
    clock.tick(60)