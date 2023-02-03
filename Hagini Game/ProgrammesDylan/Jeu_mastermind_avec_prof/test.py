import pygame
pygame.init()
transpar = pygame.image.load('img/transpar.png')



stockage_quatre_couleur = [[[transpar], [transpar], [transpar], [transpar]],
[[transpar], [transpar], [transpar], [transpar]],
[[transpar], [transpar], [transpar], [transpar]],
[[transpar], [transpar], [transpar], [transpar]],
[[transpar], [transpar], [transpar], [transpar]],
[[transpar], [transpar], [transpar], [transpar]],
[[transpar], [transpar], [transpar], [transpar]]]

ligne_actuel = 6
colonne_actuel = 0

print(stockage_quatre_couleur[6][0])