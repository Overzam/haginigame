import pygame as pyg

width, height = 1920, 1080
screen = pyg.display.set_mode((width, height))
pyg.init()

voisin_sprite = pyg.image.load('img/voisin.png')
voisin_sprite = pyg.transform.scale(voisin_sprite, (400, 200))
rouge = (255, 0, 0)
vert = (0, 255, 0)

class Voisin:
    def __init__(self, pos_x, pos_y, pv):
        self.x = int(pos_x)
        self.y = int(pos_y)
        self.pv = int(pv)
        self.max_pv = pv

    def draw(self, screen):
        screen.blit(voisin_sprite, (self.x, self.y))

    def update(self, sprite_a_afficher):
        self.sprite_actuel = sprite_a_afficher
        self.rect = pyg.Rect(int(self.x), int(self.y), 32, 32)

    def barre_de_vie(self, x, y):
        if self.pv > self.max_pv:
            self.pv = self.max_pv
        ratio_barre_de_vie = self.pv / self.max_pv
        pyg.draw.rect(screen, rouge, (x, y, 150, 20))
        pyg.draw.rect(screen, vert, (x, y, 150 * ratio_barre_de_vie, 20))
        