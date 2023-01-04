import pygame as pyg

pyg.init()

width, height = 1920, 1080
screen = pyg.display.set_mode((width, height))

viseur_sprite = pyg.image.load('img/viseur.png').convert_alpha()
viseur_sprite = pyg.transform.scale ( viseur_sprite, (100, 100))


class Viseur:
    def __init__(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y
    def draw(self, screen):
        screen.blit(viseur_sprite, (self.x, self. y))
    def update(self, direction):
        if direction == 'gauche':
            self.x -= 5
        elif direction == 'droite':
            self.x += 5
        if direction == 'haut':
            self.y -= 5
        elif direction == 'bas':
            self.y += 5
                
    pyg.display.flip()
