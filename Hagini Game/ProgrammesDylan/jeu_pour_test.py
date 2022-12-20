import pygame as pyg, sys


width, height = 500, 500
titre = "Jeu Dylan"

pyg.init()
screen = pyg.display.set_mode((width, height))
pyg.display.set_caption(titre)
clock = pyg.time.Clock()

tank = pyg.image.load('img/voisin.png').convert_alpha()
tank = pyg.transform.scale(tank,(500,500))


class Player:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.rect = pyg.Rect(self.x, self.y, 32, 32)
        self.color = (250, 120, 60)
        self.velx = 0
        self.vely = 0
        self.up_pressed = False
        self.right_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.speed = 4

    def draw(self, screen):
        screen.blit(tank, (self.x, self.y))
    
    def update(self):
        self.velx = 0
        self.vely = 0
        if self.left_pressed and not self.right_pressed:
            self.velx = - self.speed
        if self.right_pressed and not self.left_pressed:
            self.velx = self.speed
        if self.up_pressed and not self.down_pressed:
            self.vely = - self.speed
        if self.down_pressed and not self.up_pressed:
            self.vely = self.speed

        self.x += self.velx
        self.y += self.vely

        self.rect = pyg.Rect(int(self.x), int(self.y), 32, 32)


player = Player(width//4, height//4)

while True:

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            pyg.quit()
            sys.exit()
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_LEFT:
                player.left_pressed = True
            if event.key == pyg.K_RIGHT:
                player.right_pressed = True
            if event.key == pyg.K_UP:
                player.up_pressed = True
            if event.key == pyg.K_DOWN:
                player.down_pressed = True
        if event.type == pyg.KEYUP:
            if event.key == pyg.K_LEFT:
                player.left_pressed = False
            if event.key == pyg.K_RIGHT:
                player.right_pressed = False
            if event.key == pyg.K_UP:
                player.up_pressed = False
            if event.key == pyg.K_DOWN:
                player.down_pressed = False
        
    screen.fill((12,24,36))
    player.draw(screen)

    player.update()
    pyg.display.flip()

    clock.tick(60)