#importation des bibliotheques
import pygame as pyg
from hit_animation import hit
from class_prof import Prof
from voisin import Voisin
from moins_5_animation import moins_5
from plus_5_animation import plus_5
from random import randint
from boullette import Boulette
from munition import Munition
from viseur import Viseur

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
prof_touche_mechant = False
prof_hitbox = [[500, 300], [800, 300], [500, 800], [800, 800]]
prof_enorme = pyg.image.load('img/prof_mechant.png')
prof_enorme = pyg.transform.scale(prof_enorme, (5000, 5000))

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
boulette_a_touche = False
boulette_x, boulette_y = 960, 700
boulette = Boulette(boulette_x, boulette_y)
nb_boulette = 5
nb_boulette_touche = 0

#definition des variables du viseur
x_viseur = 200
y_viseur = 200
viseur = Viseur(x_viseur, y_viseur)
bouge_horizontal = False
bouge_vertical = False
bouge_droite = False
bouge_gauche = False
bouge_haut = False
bouge_bas = False
nb_touche = 0
viseur_affiche = False

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


#definbition de la victoire ou defaite

font = pyg.font.Font('freesansbold.ttf', 64)
txt_perdant = "BOO la  honte 😹😹"
txt_gagnant = "Squid game 🔥🔥"
bleu = (255,255,0)
rouge = (100, 200, 0)

def loose():
    fin = True
    while fin:
        for event in pyg.event.get():
        #terminer la boucle quand le joueur quitte le jeu 
            if event.type == pyg.QUIT:
                fin  = False
            #si une touche est pressé
            if event.type == pyg.KEYDOWN:
                #si echap quitte le jeu
                if event.key == pyg.K_ESCAPE:
                    fin  = False        
        screen.fill((0, 0, 0))
        screen.blit(prof_enorme, (0, 0))
        afficher_texte_perdant = font.render(str(txt_perdant), True, bleu, rouge)
        screen.blit(afficher_texte_perdant, (width//3, height//3))
        pyg.display.flip()


def win():
    screen.fill((0,0,0))
    afficher_texte_gagnant = font.render(str(txt_gagnant), True, bleu, rouge)
    screen.blit(afficher_texte_gagnant, (width//3, height//3))
    pyg.display.flip()



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
            if not boulette_lance:
                if event.key == pyg.K_SPACE:
                    if nb_touche == 2:
                        bouge_horizontal = False
                        bouge_vertical = False
                        bouge_droite = False
                        bouge_gauche = False
                        bouge_haut = False
                        bouge_bas = False
                        nb_touche += 1
                    if nb_touche == 1:
                        bouge_horizontal = False
                        bouge_vertical = True
                        bouge_haut = True
                        nb_touche += 1
                    if nb_touche == 0:
                        viseur_affiche = True
                        bouge_horizontal = True
                        bouge_droite = True
                        nb_touche += 1
                    if nb_touche == 3:
                        if not boulette_lance:
                            if nb_boulette > 0:
                                boulette_affiche = True
                                boulette_lance = True
                                boulette_a_atteint = False
                                nb_boulette -= 1
                                nb_touche = 0
                                viseur_affiche = False
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

    if prof_affiche:
        prof.draw(screen)

    if boulette_affiche:
        if not boulette_a_atteint:
            boulette.draw(screen)

    if boulette_lance:
        if not boulette_a_atteint:
            boulette.lance(viseur.x, viseur.y, 10)

    if prof.sprite_actuel == 2:
        if boulette_lance:
            perdu = True


    if boulette.x <= viseur.x:
        boulette_a_atteint = True
        boulette_lance = False
        viseur.x = x_viseur
        viseur.y = y_viseur

    if boulette_a_atteint:
        if prof_hitbox[0][0] < boulette.x < prof_hitbox[1][0] and prof_hitbox[0][1] < boulette.y < prof_hitbox[3][1]:
            boulette_a_touche = True
            nb_boulette_touche +=1
            

    if boulette_a_touche:
        prof_shake = 7 
        boulette_a_touche = False
    
    
    if prof_touche_mechant:
        perdu = True

    if nb_boulette_touche >= 3:
        gagne = True

    if boulette_a_atteint:
        boulette.x = boulette_x
        boulette.y = boulette_y
        boulette_affiche = False
        boulette_a_atteint = False
        if prof.sprite_actuel:
            prof_touche_mechant = True


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
            
            
    chance  = randint(0, 100)
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





    if viseur_affiche:
        viseur.draw(screen)

    if bouge_horizontal:
        if bouge_droite:
            if viseur.x < width - 1000:
                viseur.update('droite')
            else:
                bouge_gauche = True
                bouge_droite = False
        else:
            if viseur.x > 0:
                viseur.update('gauche')
            else:
                bouge_droite = True
                bouge_gauche = False
    
    if bouge_vertical:
        if bouge_haut:
            if viseur.y < height - 200:
                viseur.update('bas')
            else:
                bouge_bas = True
                bouge_haut = False
        else:
            if viseur.y > 0:
                viseur.update('haut')
            else:
                bouge_haut = True
                bouge_bas = False




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
    

    if voisin_peut_gagner_vie:
        if not voisin_a_gagner_vie:
            voisin.pv += 50
            anim_vie.animate()
            voisin_a_gagner_vie = True
            if voisin.pv > voisin.max_pv:
                voisin.pv = voisin.max_pv

    if not perdu:
        if voisin.pv <= 0:
            gagne = True

    if not gagne:
        if 30 - seconds <= 0:
            perdu = True


    if gagne:
        win()
    if perdu:
        loose()
        run = False

    #actualiser l'affichage du jeu
    pyg.display.flip()

    
    clock.tick(60)