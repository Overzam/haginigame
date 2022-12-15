# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 15:54:27 2022

@author: dbarros
"""

import pygame as pyg
from random import randint

height = 500
width = 500

pyg.init()
pyg.mixer.init()
pyg.font.init()

screen = pyg.display.set_mode((height, width))

background = pyg.image.load("fond2.png")
background = pyg.transform.scale(background, (height, width))
fond = background.convert()
screen.blit(fond, (0, 0))
pyg.display.flip()
    
clock = pyg.time.Clock()
start_ticks = pyg.time.get_ticks()
black = (0, 0, 0)
grey = (100,100,100)
seconds = 0
tank = pyg.image.load("Tank.png")
tank = pyg.transform.scale(tank, (200, 260)).convert_alpha()
font = pyg.font.Font('freesansbold.ttf', 64)
texte_est_affiche = False
txt_affichage = randint(4,7)
run = True
x_txt = 300
y_txt = 300
x_tank = 0
while run:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            run = False
            pyg.quit()
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_d:
                if texte_est_affiche:
                    x_tank += 10
    countdown = font.render(str(seconds), True, grey, black)
    texte = font.render("TAP", True, grey, black)
    # definition et affichage du compte a rebourd avant la fin du jeu
    seconds = round(((pyg.time.get_ticks() - start_ticks) / 1000))
    screen.blit(countdown, (200, height/10))
    screen.blit(tank, (x_tank, 200))
    if seconds >= txt_affichage and seconds < txt_affichage+1:
        texte_est_affiche = True
    elif seconds > txt_affichage + 1:
        texte_est_affiche = False
        x_txt = 0
        y_txt = 0
    if texte_est_affiche:
        screen.blit(texte, (x_txt,y_txt))
        
    pyg.display.update()
    pyg.display.flip()    
   
    screen.blit(background, (0, 0))