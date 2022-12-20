import pygame as pyg


width, height = 1920, 1080
screen = pyg.display.set_mode((width, height))
pyg.init()


#definition des images
prof_gentil = pyg.image.load('img/prof_gentil.png').convert_alpha()
prof_moitie =pyg.image.load('img/prof_moitie.png').convert_alpha()
prof_mechant = pyg.image.load('img/prof_mechant.png').convert_alpha()

prof_gentil = pyg.transform.scale(prof_gentil, (300, 500))
prof_moitie =pyg.transform.scale(prof_moitie, (300, 500))
prof_mechant = pyg.transform.scale(prof_mechant, (500, 500))

etat_prof = [prof_gentil, prof_moitie, prof_mechant]



class Prof:
    def __init__(self, pos_x, pos_y):
        self.x = int(pos_x)
        self.y = int(pos_y)
        self.rect = pyg.Rect(self.x, self.y, 32, 32)
        self.sprite_actuel = 0

    def draw(self, screen):
        screen.blit(etat_prof[self.sprite_actuel], (self.x, self.y))

    def update(self, sprite_a_afficher):
        self.sprite_actuel = sprite_a_afficher
        self.rect = pyg.Rect(int(self.x), int(self.y), 32, 32)