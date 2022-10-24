from win32api import GetSystemMetrics
import pygame as pyg

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
pyg.init()
pyg.font.init()
pyg.display.set_caption('hagini game')
screen = pyg.display.set_mode((width, height))
clock = pyg.time.Clock()
background = pyg.image.load("image/backroom.jpg")
fond = background.convert()
screen.blit(fond, (0, 0))
pyg.font.init()
font = pyg.font.Font("../../Pixellari.ttf", 72)
text = font.render("Tibaka", True, (0, 128, 0))
xtext = height/5

def quit():
    if event.type == pyg.KEYDOWN :
        if event.type == pyg.K_ESCAPE :
            pyg.quit()
            exit()


while True:
    for event in pyg.event.get():
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_z :
                screen.blit(text, (xtext, width / 5))
                xtext += height/100
                print(4)
                screen.blit(fond, (0, 0))
            if event.key == pyg.K_ESCAPE :
                pyg.quit()
                exit()
    screen.blit(text, (xtext, width / 5))
    pyg.display.flip()
    pyg.display.update()