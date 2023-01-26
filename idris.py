# Importations des bibliothèques
import sys
from win32api import GetSystemMetrics
import pygame as pyg
import random

# Initialisation des instances de pygame
pyg.init()
pyg.font.init()
clock = pyg.time.Clock()

# Définition des variables
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
screen = pyg.display.set_mode((width, height), 0, 32)

# Définition des polices
font = pyg.font.Font("Pixellari.ttf", width // 40)
font1 = pyg.font.Font("Pixellari.ttf", width // 80)

# Définition des images
img1 = screen.fill((0, 0, 0))
img1 = pyg.Surface((width, height))

pp = pyg.image.load("sprites/pp/pp.png")
pp = pyg.transform.scale(pp, (width // 21.3, height // 12))

faux1 = pyg.image.load("sprites/pp/faux1.png")
faux1 = pyg.transform.scale(faux1, (width//21.3, height//12))

faux2 = pyg.image.load("sprites/pp/faux2.png")
faux2 = pyg.transform.scale(faux2, (width//21.3, height//12))

faux3 = pyg.image.load("sprites/pp/faux3.png")
faux3 = pyg.transform.scale(faux3, (width//21.3, height//12))

faux4 = pyg.image.load("sprites/pp/faux4.png")
faux4 = pyg.transform.scale(faux4, (width//21.3, height//12))

coeurvide = pyg.image.load("sprites/assets/coeurvide.png")
coeurplein = pyg.image.load("sprites/assets/coeurplein.png")

amongusvide = pyg.image.load("sprites/assets/amongus.png")
amongusplein = pyg.image.load("sprites/assets/amogusplein.png")

view = pyg.image.load("sprites/assets/views.png")

comments = pyg.image.load("sprites/assets/comments.png")

background = pyg.image.load("switter.png")
background = pyg.transform.scale(background, (width, height))
fond = background.convert()
screen.blit(fond, (0, 0))

fauxpseudo = ["@Pirdi_Z", "@Sir_Deez", "@Tire_liz", "@Zirdi_S", "@Terrodi_Z", "@Liredi_Z", "@Zizi_Z", "@Pi_Z"]
fauxpp = [faux1, faux2, faux3, faux4]
tweets = ["Eh jsp si vous avez remarqué mais les mecs en général ils aiment trop vanner ceux en STMG", "Yass Encore / Yass en crop", "1 tweet sur 3 va te plaire, c'est mathématiques", "Quand je mange un poulet tikka masala devant le chicken spot", "J'ai décidé de sécher les cours ajd", "J'ai étranglé un vieux mais c'est pour l'économie"]
fauxtweets = ["Vous avez remarqué mais les mecs en STMG aiment trop vanner ceux en général", "Yass Encore / Skibididop dop dop dop yass yass yass", "1 tweet sur 4 va te plaire, c'est philosophique", "Quand je mange un kebab devant gare du nord à 8h03", "J'ai décidé de mouiller les cours ajd", "J'ai sauvé un vieux pour l'économie"]
def tweetidris(tweet, photo):
    screen.blit(photo, (width / 5.5, height / 3.15))
    screen.blit(font.render("@Sirdi_Z", True, (120, 120, 120)), (width / 4, height / 2.9))
    screen.blit(font1.render(tweet, True, (255, 255, 255)), (width / 4.5, height / 2.4))

    def like():
        screen.blit(coeurvide, (width // 2, height // 1.9))
        screen.blit(font1.render("12.9k", True, (120, 120, 120)), (width // 1.9, height // 1.9))
        if pyg.mouse.get_pressed()[0] and (width // 1.95 >= posmouse[0] >= width // 2) and (
                height // 1.85 >= posmouse[1] >= height // 2):
            screen.blit(coeurplein, (width // 2, height // 1.9))
        pyg.display.update()
        pyg.display.flip()

    def imposter():
        screen.blit(amongusvide, (width // 2.5, height // 1.9))
        screen.blit(font1.render("2.4k", True, (120, 120, 120)), (width // 2.35, height // 1.9))
        if pyg.mouse.get_pressed()[0] and (width // 2.35 >= posmouse[0] >= width // 2.5) and (
                height // 1.85 >= posmouse[1] >= height // 2):
            screen.blit(amongusplein, (width // 2.5, height // 1.9))
        pyg.display.update()
        pyg.display.flip()

    def views():
        screen.blit(view, (width // 1.5, height // 1.9))
        screen.blit(font1.render("5.3M", True, (120, 120, 120)), (width // 1.44, height // 1.9))

    def commentaires():
        screen.blit(comments, (width // 4, height // 1.9))
        screen.blit(font1.render("253", True, (120, 120, 120)), (width // 3.6, height // 1.9))

    like()
    views()
    commentaires()
    imposter()


def fauxtweet(tweet, photo):
    screen.blit(photo, (width / 5.5, height / 1.75))

    screen.blit(font.render(fauxpseudo[random.randint(0, 7)], True, (120, 120, 120)), (width / 4, height / 1.67))
    screen.blit(font1.render(tweet, True, (255, 255, 255)), (width / 4.5, height / 1.48))

    def like():
        screen.blit(coeurvide, (width // 2, height // 1.3))
        screen.blit(font1.render("1.2M", True, (120, 120, 120)), (width // 1.9, height // 1.3))
        if pyg.mouse.get_pressed()[0] and (width // 1.95 >= posmouse[0] >= width // 2) and (
                height // 1.2 >= posmouse[1] >= height // 1.3) :
            screen.blit(coeurplein, (width // 2, height // 1.3))
        pyg.display.update()
        pyg.display.flip()

    def imposter():
        screen.blit(amongusvide, (width // 2.5, height // 1.3))
        screen.blit(font1.render("365k", True, (120, 120, 120)), (width // 2.35, height // 1.3))
        if pyg.mouse.get_pressed()[0] and (width // 2.35 >= posmouse[0] >= width // 2.5) and (
                height // 1.2 >= posmouse[1] >= height // 1.3):
            screen.blit(amongusplein, (width // 2.5, height // 1.3))
        pyg.display.update()
        pyg.display.flip()

    def views():
        screen.blit(view, (width // 1.5, height // 1.3))
        screen.blit(font1.render("121.3M", True, (120, 120, 120)), (width // 1.44, height // 1.3))

    def commentaires():
        screen.blit(comments, (width // 4, height // 1.3))
        screen.blit(font1.render("218k", True, (120, 120, 120)), (width // 3.6, height // 1.3))

    like()
    views()
    commentaires()
    imposter()


while True:
    posmouse = pyg.mouse.get_pos()

    pyg.display.flip()
    for event in pyg.event.get():

        if event.type == pyg.KEYDOWN:

            if event.key == pyg.K_ESCAPE:
                pyg.quit()

            if event.key == pyg.K_a :
                tweetidris(tweets[random.randint(0, 5)],
                           pp)
                fauxtweet(fauxtweets[random.randint(0, 5)], fauxpp[random.randint(0, 3)])
        pyg.display.update()
        clock.tick(60)

        if event.type == pyg.QUIT:
            pyg.quit()
            sys.exit()
