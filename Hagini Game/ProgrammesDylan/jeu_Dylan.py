#importation des bibliotheques
import pygame as pyg, random
from hit_animation import hit
from class_prof import Prof
from voisin import Voisin
from moins_5_animation import moins_5
from plus_5_animation import plus_5
from win_and_loose import loose, win
from random import randint


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
prof_se_retourne = False
prof_va_se_retourne = False
voisin_affiche = True
peut_taper_voisin = True
voisin_peut_gagner_vie = False
voisin_a_gagner_vie = False
x_prof, y_prof = 200, 200
x_voisin, y_voisin = 1000, 700
prof = Prof(x_prof, y_prof)
voisin = Voisin(x_voisin, y_voisin, 350)
perdu = False
gagne = False
font = pyg.font.Font('freesansbold.ttf', 64)
save_seconds = seconds


hit_anim = pyg.sprite.Group()
degat = hit(x_voisin - 150, y_voisin - 100)
hit_anim.add(degat)

moins_5_animation = pyg.sprite.Group()
anim_degat = moins_5(x_voisin + 120, y_voisin - 200)
moins_5_animation.add(anim_degat)

plus_5_animation = pyg.sprite.Group()
anim_vie = plus_5(x_voisin + 120, y_voisin - 200)
plus_5_animation.add(anim_vie)

#classe pour les timings ou il faut reagir
class Timing:
    premier = randint(3,4)
    deuxieme = premier + 0.5
    troisieme = deuxieme + 2


#debut de la boucle du jeu
run = True
while run:
    countdown = font.render(str(round(30-seconds)), True, (255, 0, 0), (0, 255, 0))
    

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
            if peut_taper_voisin:
                degat.animate()
                anim_degat.animate()
                voisin.pv -= 5
            if not peut_taper_voisin:
                voisin_affiche = False
                perdu = True
        if event.type == pyg.MOUSEBUTTONDOWN and pyg.mouse.get_pressed()[2]:
            if peut_taper_voisin:
                degat.animate()
                anim_vie.animate()
                voisin.pv += 5
            

    #timer du jeu
    seconds = ((pyg.time.get_ticks() - start_ticks) / 1000)

    screen.fill((12,24,36))

    screen.blit(countdown, (width - 90, 100))

    if prof_affiche:
        prof.draw(screen)

    if voisin_affiche:
        voisin.draw(screen)
        voisin.barre_de_vie(x_voisin + 150, y_voisin + 230) 
    
    hit_anim.draw(screen)
    hit_anim.update(0.5)

    moins_5_animation.draw(screen)
    moins_5_animation.update(0.40)

    plus_5_animation.draw(screen)
    plus_5_animation.update(0.40)


    chance  = randint(1, 200)
    if not prof_va_se_retourne:
        if chance == 1:
            prof_se_retourne = True
            prof_va_se_retourne = True
            save_seconds = seconds


    
    if prof_se_retourne:
        prof.update(1) 

    if prof_se_retourne:
        if seconds - save_seconds >= 0.5:
            prof.update(2)
            voisin_peut_gagner_vie = False

    if prof_se_retourne:
        if seconds - save_seconds > 2.5:
            prof.update(0)
            voisin_a_gagner_vie = False
            voisin_peut_gagner_vie = False
            save_seconds = 0
            prof_va_se_retourne = False
            prof_se_retourne = True




    if prof.sprite_actuel == 2:
        peut_taper_voisin = False
        voisin_peut_gagner_vie = True
    else:
        peut_taper_voisin = True

    if voisin_peut_gagner_vie:
        if not voisin_a_gagner_vie:
            voisin.pv += 50
            voisin_a_gagner_vie = True
            if voisin.pv > voisin.max_pv:
                voisin.pv = voisin.max_pv

    if voisin.pv <= 0:
        gagne = True
    if 30 - seconds <= 0:
        perdu = True


    if gagne:
        win()
    if perdu:
        loose()

    #actualiser l'affichage du jeu
    pyg.display.flip()

    
    clock.tick(60)