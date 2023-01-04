import pygame as pyg
from random import randint

pyg.init()
width, height = 1920, 1080
screen = pyg.display.set_mode((width, height))

boulette_sprite = pyg.image.load('img/papier.png')
boulette_sprite = pyg.transform.scale(boulette_sprite, (50, 50))
boulette_lance = False
boulette_affiche = False
boulette_a_atteint = False


class Boulette:
    def __init__(self, pos_x, pos_y) :
        self.x = int(pos_x)
        self.y = int(pos_y)

    def draw(self, screen):
        screen.blit(boulette_sprite, (self.x, self.y))

    def lance(self, x_vise, y_vise, vitesse):
        distance_max = max(x_vise, y_vise)
        if distance_max == x_vise:
            if self.x > x_vise:
                if self.y - y_vise != 0:
                    self.x -= (self.x - x_vise) * vitesse /(self.y - y_vise)
            if self.y > y_vise:
                self.y -= vitesse
        else:
            if self.x > x_vise:
                if self.x - x_vise != 0:
                    self.y -= (self.y - y_vise) * vitesse/(self.x - x_vise)
            if self.x > x_vise:
                self.x -= vitesse        