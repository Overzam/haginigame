#importatio
import pygame as pyg, sys, random

#definition de l'ecran et du titre du jeu
width, height = 1920, 1080
screen = pyg.display.set_mode((width, height))
titre = "Jeu Dylan"
pyg.display.set_caption(titre)

#initialisation des modules
pyg.init()

#definition du fond du jeu
background = pyg.image.load("fond2.png").convert()
background = pyg.transform.scale(background, (width, height))

#timer du jeu 
clock = pyg.time.Clock()
start_ticks = pyg.time.get_ticks()
seconds = 0

#definition des images
tank = pyg.image.load('Tank.png').convert_alpha()

#definition des variables
tank_affiche = False
tank_tue = False


#classe pour les timings ou il faut reagir
class Timing:
    premier = random.randint(3,4)
    deuxieme = random.randint(6,7)


#debut de la boucle du jeu
run = True
while run:
    for event in pyg.event.get():
        #terminer la boucle quand le joueur quitte le jeu 
        if event.type == pyg.QUIT:
            run  = False
        #si une touche est pressé
        if event.type == pyg.KEYDOWN:
            #si echap quitte le jeu
            if event.key == pyg.K_ESCAPE:
                run  = False
            #si espace pour terminer le tank
            if event.key == pyg.K_SPACE:
                if tank_affiche:
                    tank_affiche = False
                    tank_tue = True
                    
    
    #timer du jeu
    seconds = ((pyg.time.get_ticks() - start_ticks) / 1000)

    #reaffichage du fond du jeu
    screen.blit(background,(0,0))

    #si le tank est vivant, check les conditions pour le faire apparaitre,
    #sinon ne pas le faire apparaitre
    if not tank_tue:
        if Timing.premier + 1 >= seconds >= Timing.premier :
            tank_affiche = True
        elif Timing.deuxieme + 1 >= seconds >= Timing.deuxieme :
            tank_affiche = True
        else:
            tank_affiche = False
    
    #si il est affiche, l'affiche
    if tank_affiche:
        screen.blit(tank, (width//2, height//2))
    
    #le faire revivre si il est entre les deux timing
    if Timing.deuxieme - 1 > seconds > Timing.premier + 1:
        tank_tue = False

    #actualiser l'affichage du jeu
    pyg.display.flip()
