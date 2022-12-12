# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 15:54:27 2022

@author: dbarros
"""

import pygame as pyg

pyg.init()
pyg.font.init()

height = 500
width = 500

pyg.init()
pyg.mixer.init()
pyg.font.init()

screen = pyg.display.set_mode((height, width))

clock = pyg.time.Clock()
start_ticks = pyg.time.get_ticks()
black = (0, 0, 0)
grey = (100,100,100)
seconds = 0
tank = pyg.image.load("Tank.png")
tank = pyg.transform.scale(tank, (200, 260)).convert_alpha()
font = pyg.font.Font('freesansbold.ttf', 64)
texte_est_affiche = False
run = True
while run:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            run = False
            pyg.quit()
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_d:
                if texte_est_affiche:
                    print("5")
    countdown = font.render(str(seconds), True, grey, black)
    texte = font.render("TAP", True, grey, black)
    # definition et affichage du compte a rebourd avant la fin du jeu
    seconds = round(((pyg.time.get_ticks() - start_ticks) / 1000))
    screen.blit(countdown, (200, height/10))
    screen.blit(tank, (200, 200))
    if seconds > 5:
        texte_est_affiche = True
    if texte_est_affiche:
        screen.blit(texte, (100,100))
    
    pyg.display.flip()