# Importations des bibliothèques
import sys
from win32api import GetSystemMetrics
import pygame as pyg

# Initialisation des instances de pygame
pyg.init()
pyg.font.init()
clock = pyg.time.Clock()

# Définition des variables
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
screen = pyg.display.set_mode((width, height), 0, 32)
font = pyg.font.Font("Pixellari.ttf", width // 10)
text2 = font.render("Press Space", True, (0, 0, 0))
img1 = screen.fill((0, 0, 0))
img1 = pyg.Surface((width, height))

background = pyg.image.load("Landscape.png")

fond = background.convert()
screen.blit(fond, (0, 0))


# Définition des fonctions
def fade(SCREENWIDTH, SCREENHEIGHT):  # Fonction pour faire un fondu

    fade = pyg.Surface((width, height))
    fade = fond
    opacity = 0

    for r in range(0, 300):

        opacity += 1
        fade.set_alpha(opacity)
        screen.blit(text2, (width // 5, height // 2))
        screen.blit(fade, (0, 0))
        pyg.display.update()

    for r in range(0, 300):

        opacity -= 1
        fade.set_alpha(opacity)
        screen.blit(text2, (width // 5, height // 2))
        screen.blit(fade, (0, 0))
        pyg.display.update()


def trans(img1, img2):  # Fonction pour faire une transition vers le bas

    yimage1 = 0
    yimage2 = height

    for r in range(height):

        screen.blit(img1, (0, yimage1))
        yimage1 += 1
        screen.blit(img2, (0, yimage2))
        yimage2 -= 1
        pyg.display.update()


while True:

    pyg.display.flip()
    for event in pyg.event.get():

        if event.type == pyg.KEYDOWN:

            if event.key == pyg.K_SPACE:

                trans(fond, img1)

            if event.key == pyg.K_ESCAPE :
                fade(width, height)
        pyg.display.update()
        clock.tick(60)

        if event.type == pyg.QUIT:
            pyg.quit()
            sys.exit()
