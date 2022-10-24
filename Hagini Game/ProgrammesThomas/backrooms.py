from win32api import GetSystemMetrics
import pygame as pyg

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
pyg.init()
pyg.font.init()
pyg.display.set_caption('hagini game')
screen = pyg.display.set_mode((width, height))
clock = pyg.time.Clock()
background = pyg.image.load("image/backroom.png")
background = pyg.transform.scale(background, (height, width))
fond = background.convert()
screen.blit(fond, (0, 0))
pyg.display.flip()

def quit():
    if event.type == pyg.KEYDOWN :
        if event.type == pyg.K_ESCAPE :
            pyg.quit()
            exit()

while True:
    for event in pyg.event.get():
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_a :
                print("sus")
            if event.key == pyg.K_ESCAPE :
                pyg.quit()
                exit()
