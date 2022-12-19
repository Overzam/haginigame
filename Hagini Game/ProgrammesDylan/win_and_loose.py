import pygame as pyg

width, height = 1920, 1080
screen = pyg.display.set_mode((width, height))

pyg.init()
pyg.font.init()

font = pyg.font.Font('freesansbold.ttf', 64)
txt_perdant = "ratio looser"
txt_gagnant = "gg bb"
bleu = (255,255,0)
rouge = (100, 200, 0)

def loose():
    screen.fill((0,0,0))
    afficher_texte_perdant = font.render(str(txt_perdant), True, bleu, rouge)
    screen.blit(afficher_texte_perdant, (width//3, height//3))
    pyg.display.flip()


def win():
    screen.fill((0,0,0))
    afficher_texte_gagnant = font.render(str(txt_gagnant), True, bleu, rouge)
    screen.blit(afficher_texte_gagnant, (width//3, height//3))
    pyg.display.flip()
