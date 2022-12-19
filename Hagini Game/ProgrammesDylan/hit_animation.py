import pygame as pyg
class hit(pyg.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        vide = pyg.image.load('img/Hit_animation/transpar.png')
        hit_0 = pyg.image.load('img/Hit_animation/sprite_0.png')
        hit_0 = pyg.transform.scale(hit_0, (100, 100))
        hit_1 = pyg.image.load('img/Hit_animation/sprite_1.png')
        hit_1 = pyg.transform.scale(hit_1, (100, 100))
        hit_2 = pyg.image.load('img/Hit_animation/sprite_2.png')
        hit_2 = pyg.transform.scale(hit_2, (100, 100))
        hit_3 = pyg.image.load('img/Hit_animation/sprite_3.png')
        hit_3 = pyg.transform.scale(hit_3, (100, 100))
        hit_4 = pyg.image.load('img/Hit_animation/sprite_4.png')
        hit_4 = pyg.transform.scale(hit_4, (100, 100))
        hit_5 = pyg.image.load('img/Hit_animation/sprite_5.png')
        hit_5 = pyg.transform.scale(hit_5, (100, 100))
        hit_6 = pyg.image.load('img/Hit_animation/sprite_6.png')
        hit_6 = pyg.transform.scale(hit_6, (100, 100))
        self.sprites.append(vide)
        self.sprites.append(hit_0)
        self.sprites.append(hit_1)
        self.sprites.append(hit_2)
        self.sprites.append(hit_3)
        self.sprites.append(hit_4)
        self.sprites.append(hit_5)
        self.sprites.append(hit_6)
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
