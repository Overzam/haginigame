import pygame as pyg

pyg.init()

class moins_5(pyg.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        vide = pyg.image.load('img/Hit_animation/transpar.png')
        moins_5_0 = pyg.image.load('img/-5_animation/sprite_0.png')
        moins_5_0 = pyg.transform.scale(moins_5_0, (300, 300))
        moins_5_1 = pyg.image.load('img/-5_animation/sprite_1.png')
        moins_5_1 = pyg.transform.scale(moins_5_1, (300, 300))
        moins_5_2 = pyg.image.load('img/-5_animation/sprite_2.png')
        moins_5_2 = pyg.transform.scale(moins_5_2, (300, 300))
        moins_5_3 = pyg.image.load('img/-5_animation/sprite_3.png')
        moins_5_3 = pyg.transform.scale(moins_5_3, (300, 300))
        self.sprites.append(vide)
        self.sprites.append(moins_5_0)
        self.sprites.append(moins_5_1)
        self.sprites.append(moins_5_2)
        self.sprites.append(moins_5_3)
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
