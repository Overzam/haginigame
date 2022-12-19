#importation des bibliotheques
import pygame as pyg, random
from hit_animation import hit
from class_prof import Prof
from moins_5_animation import moins_5
from win_and_loose import loose, win

#definition de l'ecran et du titre du jeu
width, height = 1920, 1080
screen = pyg.display.set_mode((width, height))
titre = "Jeu Dylan"
pyg.display.set_caption(titre)

#initialisation des modules
pyg.init()

#timer du jeu 
clock = pyg.time.Clock()
start_ticks = pyg.time.get_ticks()
seconds = 0



#definition des variables
prof_affiche = True
peut_taper_prof = True
x_prof, y_prof = 200, 200
hit_anim = pyg.sprite.Group()
degat = hit(x_prof - 100, y_prof + 150)
hit_anim.add(degat)
prof = Prof(200, 200, 100)

moins_5_animation = pyg.sprite.Group()
anim_degat = moins_5(x_prof + 120, y_prof - 40)
moins_5_animation.add(anim_degat)

#classe pour les timings ou il faut reagir
class Timing:
    premier = random.randint(1,2)
    deuxieme = random.randint(3,4)


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
        if event.type == pyg.MOUSEBUTTONDOWN and pyg.mouse.get_pressed()[0]:
            if peut_taper_prof:
                degat.animate()
                prof.prend_degat(5)
                anim_degat.animate()

    #timer du jeu
    seconds = ((pyg.time.get_ticks() - start_ticks) / 1000)

    screen.fill((12,24,36))

    prof.barre_de_vie()
    
    if Timing.deuxieme > seconds > Timing.premier :
        prof.update(1)

    if Timing.deuxieme + 3 > seconds > Timing.deuxieme :
        prof.update(2)

    if prof.sprite_actuel == 2:
        peut_taper_prof = False


    #si il est affiche, l'affiche
    if prof_affiche:
        prof.draw(screen)
    

    hit_anim.draw(screen)
    hit_anim.update(0.5)

    moins_5_animation.draw(screen)
    moins_5_animation.update(0.5)

    if seconds > Timing.deuxieme + 1:
        if prof.pv > 0:
            loose()
    if prof.pv <= 0:
        win()



    #actualiser l'affichage du jeu
    pyg.display.flip()

    
    clock.tick(60)