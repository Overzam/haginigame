# importation des bibliotheque a utiliser
import pygame as pyg
from sys import exit

height = 1920
width = 1080

pyg.init()
pyg.mixer.init()
pyg.font.init()

x_explo = 100
y_explo = 100

screen = pyg.display.set_mode((height, width))

pyg.display.set_caption('boom')

background = pyg.image.load("img_dylan/fond2.png")
background = pyg.transform.scale(background, (height, width))
fond = background.convert()

    
class explo(pyg.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        vide = pyg.image.load('img_dylan/transpar.png')
        explo1 = pyg.image.load('img_dylan/explosion-frame-1.png')
        explo1 = pyg.transform.scale(explo1, (x_explo - 5, y_explo - 5))
        explo2 = pyg.image.load('img_dylan/explosion-frame-2.png')
        explo2 = pyg.transform.scale(explo2, (x_explo, y_explo))
        explo3 = pyg.image.load('img_dylan/explosion-frame-3.png')
        explo3 = pyg.transform.scale(explo3, (x_explo, y_explo))
        explo4 = pyg.image.load('img_dylan/explosion-frame-4.png')
        explo4 = pyg.transform.scale(explo4, (x_explo, y_explo))
        explo5 = pyg.image.load('img_dylan/explosion-frame-5.png')
        explo5 = pyg.transform.scale(explo5, (x_explo, y_explo))
        explo6 = pyg.image.load('img_dylan/explosion-frame-6.png')
        explo6 = pyg.transform.scale(explo6, (x_explo, y_explo))
        explo7 = pyg.image.load('img_dylan/explosion-frame-7.png')
        explo7 = pyg.transform.scale(explo7, (x_explo, y_explo))
        explo8 = pyg.image.load('img_dylan/explosion-frame-8.png')
        explo8 = pyg.transform.scale(explo8, (x_explo, y_explo))
        self.sprites.append(vide)
        self.sprites.append(explo1)
        self.sprites.append(explo2)
        self.sprites.append(explo3)
        self.sprites.append(explo4)
        self.sprites.append(explo5)
        self.sprites.append(explo6)
        self.sprites.append(explo7)
        self.sprites.append(explo8)
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def animate(self):
        self.is_animating = True

    def update(self, vitesse):
        if self.is_animating:
            self.current_sprite += vitesse

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[int(self.current_sprite)]



