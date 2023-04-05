import pygame
from pygame.draw import *
from random import randint

pygame.init()
start_ticks = pygame.time.get_ticks()
width = 1920//2
height = 1080//2

screen = pygame.display.set_mode((width, height))
pygame.mouse.set_visible(0)
black = (0, 0, 0)

screen.fill(black)

pygame.display.update()
clock = pygame.time.Clock()
ancien_tempo = 0
finished = False
def contour(valeur):  # entre 0 et 100
    Pas_x = width // 100
    Pas_y = height // 100
    rouge = (255, 0, 0)
    if valeur <= 50:
        pygame.draw.rect(screen, rouge, (width/2 - a * Pas_x, height - Pas_y,2 * a * Pas_x ,Pas_y))
        pygame.draw.rect(screen, rouge, (width/2 - a * Pas_x,0 ,2 * a * Pas_x ,Pas_y))
    else:
        pygame.draw.rect(screen, rouge, (0, height - Pas_y,width ,Pas_y))
        pygame.draw.rect(screen, rouge, (0,0 ,width ,Pas_y))

        pygame.draw.rect(screen, rouge, (0, height -(a-50)*Pas_y, Pas_x, (a-50) * Pas_y ))
        pygame.draw.rect(screen, rouge, (width - Pas_x, height -(a-50)*Pas_y, Pas_x, (a-50) * Pas_y ))
        
        pygame.draw.rect(screen, rouge, (0, 0, Pas_x, (a-50) * Pas_y ))
        pygame.draw.rect(screen, rouge, (width - Pas_x, 0, Pas_x, (a-50) * Pas_y ))


a=0
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                finished = True
    a+=0.01
    contour(round(a))
    print(a)
    pygame.display.flip()


pygame.quit()