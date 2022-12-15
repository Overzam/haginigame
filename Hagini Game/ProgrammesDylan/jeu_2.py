import pygame as pyg, sys, random

width, height = 1920, 1080
titre = "Jeu Dylan"

pyg.init()
pyg.font.init()

pyg.display.set_caption(titre)

screen = pyg.display.set_mode((width, height))

background = pyg.image.load("fond2.png").convert()
background = pyg.transform.scale(background, (width, height))

clock = pyg.time.Clock()
start_ticks = pyg.time.get_ticks()


tank = pyg.image.load('Tank.png').convert_alpha()
tank_affiche = False
tank_tue = False


seconds = 0
font = pyg.font.Font('freesansbold.ttf', 64)
orange = (250, 120, 60)
bleu_fonce = (12,24,36)


class Timing:
    x = random.randint(3,4)


while True:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            pyg.quit()
            sys.exit()
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_ESCAPE:
                pyg.quit()
                sys.exit()
            if event.key == pyg.K_SPACE:
                if tank_affiche:
                    tank_affiche = False
                    tank_tue = True
                    
    seconds = ((pyg.time.get_ticks() - start_ticks) / 1000)
    screen.blit(background,(0,0))
    if not tank_tue:
        if Timing.x + 1 >= seconds >= Timing.x :
            tank_affiche = True
    if tank_affiche:
        screen.blit(tank, (width//2, height//2))
    pyg.display.flip()