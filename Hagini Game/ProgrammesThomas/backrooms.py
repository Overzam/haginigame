from win32api import GetSystemMetrics
import pygame as pyg

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
pyg.init()
pyg.font.init()
pyg.display.set_caption('hagini game')
screen = pyg.display.set_mode((width, height))
clock = pyg.time.Clock()
fond = pyg.image.load('image/backroom.png')
fond = pyg.transform.scale(fond, (height, width))


while True:
    screen.blit(fond, (0, 0))
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            pyg.quit()
            exit()
