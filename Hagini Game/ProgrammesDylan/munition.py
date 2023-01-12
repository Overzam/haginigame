import pygame as pyg

pyg.init()
width, height = 1920, 1080
screen = pyg.display.set_mode((width, height))

munition_sprite = pyg.image.load('img/papier.png').convert_alpha()
munition_sprite = pyg.transform.scale(munition_sprite, (100, 100))

pos1, pos2, pos3, pos4, pos5 = 600, 800, 1000, 1200, 1400
pos = [pos1, pos2, pos3, pos4, pos5]


class Munition:
    def __init__(self): 
        pass

    def draw(self, screen, nb_munition):
        if nb_munition ==  5:
            screen.blit(munition_sprite, (pos1, 900))
            screen.blit(munition_sprite, (pos2, 900))
            screen.blit(munition_sprite, (pos3, 900))
            screen.blit(munition_sprite, (pos4, 900))
            screen.blit(munition_sprite, (pos5, 900))
        elif nb_munition == 4:
            screen.blit(munition_sprite, (pos1, 900))
            screen.blit(munition_sprite, (pos2, 900))
            screen.blit(munition_sprite, (pos3, 900))
            screen.blit(munition_sprite, (pos4, 900))
        elif nb_munition == 3:
            screen.blit(munition_sprite, (pos1, 900))
            screen.blit(munition_sprite, (pos2, 900))
            screen.blit(munition_sprite, (pos3, 900))
        elif nb_munition == 2:
            screen.blit(munition_sprite, (pos1, 900))
            screen.blit(munition_sprite, (pos2, 900))
        elif nb_munition == 1:
            screen.blit(munition_sprite, (pos1, 900))