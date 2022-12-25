#importation des bibliotheques
import pygame as pyg
from hit_animation import hit
from class_prof import Prof
from voisin import Voisin
from moins_5_animation import moins_5
from plus_5_animation import plus_5
from win_and_loose import loose, win
from random import randint
from boullette import Boulette
from munition import Munition

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
save_seconds = seconds


#definition des variables du prof
prof_affiche = True
prof_se_retourne = False
prof_va_se_retourne = False
x_prof, y_prof = 500, 300
prof = Prof(x_prof, y_prof)

#definition des variables des munitions
munition_affiche = True
munition = Munition()

#definition des variables du voisin
voisin_affiche = True
peut_taper_voisin = True
voisin_peut_gagner_vie = False
voisin_a_gagner_vie = False
x_voisin, y_voisin = width-400, 600
voisin = Voisin(x_voisin, y_voisin, 350)

#definition des variables de la boulette de papier
boulette_lance = False
boulette_affiche = False
boulette_a_atteint = False
boulette_x, boulette_y = 960, 700
boulette = Boulette(boulette_x, boulette_y)
nb_boulette = 3

#definition des variables qui determine si on a gagné ou perdu
perdu = False
gagne = False

#definition font qui affichera les secondes
font = pyg.font.Font('freesansbold.ttf', 64)

#definition du fond du jeu
background = pyg.image.load('img/fond.png')
background = pyg.transform.scale(background, (width, height))

#definition du tremblement du voisin quand on clique
voisin_shake = 0
shake_saver = [0] * 2
voisin_shake_termine = False

#definition du tremblement du prof quand on clique
prof_shake = 0
prof_shake_termine = False

#definition des variables pour animer l'animation de degat, de +5 et -5
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
    
    
    for event in pyg.event.get():
        #terminer la boucle quand le joueur quitte le jeu 
        if event.type == pyg.QUIT:
            run  = False
        #si une touche est pressé
        if event.type == pyg.KEYDOWN:
            #si echap quitte le jeu
            if event.key == pyg.K_ESCAPE:
                run  = False
            #si espace pour lancer boulette
            if event.key == pyg.K_SPACE:
                if nb_boulette > 0:
                    boulette_affiche = True
                    boulette_lance = True
                    boulette_a_atteint = False
                    nb_boulette -= 1
        #si on clique tape le voisin -5hp
        if event.type == pyg.MOUSEBUTTONDOWN and pyg.mouse.get_pressed()[0]:
            if peut_taper_voisin:  
                degat.animate()
                anim_degat.animate()
                voisin.pv -= 5
                voisin_shake_termine = False
                voisin_shake = 7
            if not peut_taper_voisin:
                voisin_affiche = False
                perdu = True
            

    
    #affichage du fond du jeu
    screen.blit(background, (0, 0))

    #affichage du timer 
    seconds = ((pyg.time.get_ticks() - start_ticks) / 1000)
    countdown = font.render(str(round(30-seconds)), True, (255, 0, 0), (0, 255, 0))
    screen.blit(countdown, (width - 90, 100))

    if munition_affiche:
        munition.draw(screen, nb_boulette)


    if voisin_shake:
        if not voisin_shake_termine:
            voisin.x += randint(0, 8) - 4
            voisin.y += randint(0, 8) - 4
        
    if voisin_shake > 0:
        voisin_shake -= 1

    elif voisin_shake == 0:
        voisin_shake_termine = True

    if voisin_shake_termine:
        voisin.x, voisin.y =  x_voisin, y_voisin
    

    if prof_affiche:
        prof.draw(screen)

    if boulette_affiche:
        if not boulette_a_atteint:
            boulette.draw(screen)

    if boulette_lance:
        if not boulette_a_atteint:
            boulette.lance(x_prof + 100, y_prof + 200, 10)


    if boulette.x <= x_prof + 100:
        boulette_a_atteint = True
        boulette_lance = False

    if boulette_a_atteint:
        prof_shake = 7 
    
    if boulette_a_atteint:
        boulette.x = boulette_x
        boulette.y = boulette_y
        boulette_affiche = False
        boulette_a_atteint = False


    if prof_shake > 0:
        prof.x += randint(0, 10) - 5   
        prof.y += randint(0, 10) - 5
        prof_shake -= 1

    elif prof_shake == 0:
        prof_shake_termine = True
    
    if prof_shake_termine:
        prof.x, prof.y =  x_prof, y_prof
        prof_shake_termine = False

    if voisin_affiche:
        voisin.draw(screen)
        voisin.barre_de_vie(voisin.x + 150, voisin.y + 230) 
    
    hit_anim.draw(screen)
    hit_anim.update(0.5)

    moins_5_animation.draw(screen)
    moins_5_animation.update(0.40)

    plus_5_animation.draw(screen)
    plus_5_animation.update(0.40)
            
            
    chance  = randint(0, 250)
    if not prof_va_se_retourne:
        if not boulette_lance:
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
        if seconds - save_seconds > 1.5:
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
            anim_vie.animate()
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