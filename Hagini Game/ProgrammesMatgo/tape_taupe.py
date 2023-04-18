import sys

import pygame as pyg
import random

from pygame import *
pyg.init()
pyg.font.init()
pyg.display.set_caption('whack-a-mole')

width = 1920
height = 1080
screen = pyg.display.set_mode((width,height), 0, 32)

clock = pyg.time.Clock()

random.seed()

colors = [(255, 0, 0),(0, 255, 0),(0, 0, 255)]

# condition qui permet de générer une nouveau carré
bout_OK = 0

gauche = 0
droite = 0
haut = 0
bas = 0

HG = 0
HD = 0
BG = 0
BD = 0

mid = 0

color_switch = 0

points = 0

game_start = 0

show_hitbox = -1

viseur = pyg.image.load('Assets/Tape_Taupe/viseur.png')

marteau_normal = pyg.image.load('Assets/Tape_Taupe/marteau45.png')
marteau_frappe = pyg.image.load("Assets/Tape_Taupe/marteau90.png")

marteau = marteau_normal

facile = pyg.image.load('Assets/Tape_Taupe/facile.png')
difficile = pyg.image.load('Assets/Tape_Taupe/difficile.png')

trou_haut_x = 810      
trou_haut_y = 250      

trou_droite_x = 1700     
trou_droite_y = 540     

trou_gauche_x = 250      
trou_gauche_y = 540       

trou_bas_x = 810         
trou_bas_y = 800          

var_sortie = 0

offset_marteau_x = -70
offset_marteau_y = -160

font = pyg.font.Font('Assets/Tape_Taupe/Monocraft.otf', 100)

facile_coll = Rect(100,300,800,400)
difficile_coll = Rect(1000,300,800,400)

victoire = pyg.image.load('Assets/Tape_Taupe/win.png')
defaite = pyg.image.load('Assets/Tape_Taupe/defaite.png')

Run_menu = True
Run = False
Run_fin = False

while Run_menu:
    
    screen.fill((0,0,0))
    
    pos_souris = pyg.mouse.get_pos()
    
    screen.blit(facile, (100,300))
    screen.blit(difficile, (1000, 300))

    pyg.draw.rect(screen, (255, 0, 0), facile_coll, -1)
    pyg.draw.rect(screen, (255, 0, 0), facile_coll, -1)
    
    for event in pyg.event.get():
        
        if event.type == QUIT:
            pyg.quit()
            sys.exit()
        
        if event.type == MOUSEBUTTONDOWN:
            if pyg.Rect.collidepoint(facile_coll, pos_souris): #mode facile

                secondes = 100000  # temps pour taper les taupes
                s = secondes
                timer_de_fin = 5100
                temps = 50

                taille_taupe = 120

                points_pour_win = 25

                fond = pyg.image.load('Assets/Tape_Taupe/tape_taupe_ez.png').convert()
                fond = pyg.transform.scale(fond, (1920,1080))

                trou_haut = Rect(770, 370, 380, 150)
                trou_droite = Rect(1225, 530, 460, 200)
                trou_gauche = Rect(240, 530, 460, 200)
                trou_bas = Rect(690, 745, 545, 280)

                trou_HG = Rect(350, 370, 380, 150)
                trou_HD = Rect(1190, 370, 380, 150)
                trou_BG = Rect(80, 745, 560, 280)
                trou_BD = Rect(1280, 745, 560, 280)

                trou_mid = Rect(730, 530, 460, 200)

                taupe_haut = (770 + 150, 370 + 30, 80, 80)
                taupe_droite = (1225 + 160, 530 + 50, 100, 100)
                taupe_gauche = (240 + 180, 530 + 60, 100, 100)
                taupe_bas = (690 + 190, 745 + 80, 140, 140)

                taupe_HG = (240 + 250, 370 + 30 , 80, 80)
                taupe_HD = (1225 + 120, 370 + 30 ,80 ,80)
                taupe_BG = (240 + 60, 745 + 70, 140, 140)
                taupe_BD = (1225 + 260, 745 + 70, 140, 140)
                
                taupe_mid = (770 + 135, 530 + 50, 100, 100)

                Run_menu = False
                Run = True

            if pyg.Rect.collidepoint(difficile_coll, pos_souris): # mode difficile

                secondes = 75  # temps pour taper les taupes
                s = secondes
                timer_de_fin = 2100
                temps = 20

                taille_taupe = 40

                points_pour_win = 50

                fond = pyg.image.load('Assets/Tape_Taupe/tape_taupe_hard.png').convert()
                fond = pyg.transform.scale(fond, (1920,1080))

                trou_haut = Rect(870, 375, 180, 110)
                trou_droite = Rect(1225, 560, 210, 125)
                trou_gauche = Rect(490, 560, 210, 125)
                trou_bas = Rect(845, 800, 240, 170)

                trou_HG = Rect(540, 370, 180, 110)
                trou_HD = Rect(1190, 375, 180, 110)
                trou_BG = Rect(420, 800, 240, 170)
                trou_BD = Rect(1280, 800, 235, 170)

                trou_mid = Rect(855, 565, 210, 125)

                taupe_haut = (870 + 70, 375 + 30, 40, 40)
                taupe_droite = (1225 + 75, 560 + 30, 60, 60)
                taupe_gauche = (490 + 75, 560 + 30, 60, 60)
                taupe_bas = (845 + 75, 800 + 30, 100, 100)

                taupe_HG = (540 + 70, 370 + 30, 40, 40)
                taupe_HD = (1190 + 70, 375 + 30, 40 ,40)
                taupe_BG = (420 + 75, 800 + 30, 100, 100)
                taupe_BD = (1280 + 75, 800 + 30, 100, 100)
                
                taupe_mid = (855 + 70, 565 + 30, 60, 60)

                Run_menu = False
                Run = True

    pyg.display.update()
    clock.tick(60)

while Run:
    screen.blit(fond, (0,0))

    aff_points = font.render(str(points), True, (255, 255, 255))
    
    pyg.mouse.set_visible(False)
    
    pos_souris = pyg.mouse.get_pos()
    pos_viseur = list(pos_souris)
    pos_viseur[0] -= 50
    pos_viseur[1] -= 50

    pos_marteau = list(pos_souris)
    pos_marteau[1] = pos_souris[1] + offset_marteau_y
    pos_marteau[0] = pos_souris[0] + offset_marteau_x

    screen.blit(aff_points,(500,90))

    pyg.draw.rect(screen, (255, 0, 0), trou_haut, show_hitbox)
    pyg.draw.rect(screen, (255, 0, 0), trou_gauche, show_hitbox)
    pyg.draw.rect(screen, (255, 0, 0), trou_droite, show_hitbox)
    pyg.draw.rect(screen, (255, 0, 0), trou_bas, show_hitbox)
    
    pyg.draw.rect(screen, (255, 0, 0), trou_HG, show_hitbox)
    pyg.draw.rect(screen, (255, 0, 0), trou_HD, show_hitbox)
    pyg.draw.rect(screen, (255, 0, 0), trou_BG, show_hitbox)
    pyg.draw.rect(screen, (255, 0, 0), trou_BD, show_hitbox)
    
    pyg.draw.rect(screen, (255, 0, 0), trou_mid, show_hitbox)

    if timer_de_fin == temps * 100:
        temps -= 1

    aff_temps = font.render(str(temps), True, (255, 255, 255))
    screen.blit(aff_temps,(1300,90))

    # généré une nouvelle valeur, un nouveau carré
    if bout_OK == 1:

        prev_var_sortie = var_sortie
        var_sortie = random.randrange(1, 10, 1)

        if var_sortie == 1 and prev_var_sortie == 1:
            var_sortie += 1
        if var_sortie == 2 and prev_var_sortie == 2:
            var_sortie += 1
        if var_sortie == 3 and prev_var_sortie == 3:
            var_sortie += 1
        if var_sortie == 4 and prev_var_sortie == 4:
            var_sortie += 1
        if var_sortie == 5 and prev_var_sortie == 5:
            var_sortie += 1
        if var_sortie == 6 and prev_var_sortie == 6:
            var_sortie += 1
        if var_sortie == 7 and prev_var_sortie == 7:
            var_sortie += 1
        if var_sortie == 8 and prev_var_sortie == 8:
            var_sortie += 1
        if var_sortie == 9 and prev_var_sortie == 9:
            var_sortie -= 1

        # applique la carré au bon endroit
        if var_sortie == 1:
            gauche = 1
        if var_sortie == 2:
            haut = 1
        if var_sortie == 3:
            droite = 1
        if var_sortie == 4:
            bas = 1
        if var_sortie == 5:
            mid = 1
        if var_sortie == 6:
            HG = 1
        if var_sortie == 7:
            HD = 1
        if var_sortie == 8:
            BG = 1
        if var_sortie == 9:
            BD = 1
        

    # dessine le carré / empêche la création d'une nouvelle valeur
    if gauche == 1:
        pyg.draw.rect(screen, colors[color_switch], taupe_gauche)
        bout_OK = 0

    if droite == 1:
        pyg.draw.rect(screen, colors[color_switch], taupe_droite)
        bout_OK = 0

    if haut == 1:
        pyg.draw.rect(screen, colors[color_switch], taupe_haut)
        bout_OK = 0

    if bas == 1:
        pyg.draw.rect(screen, colors[color_switch], taupe_bas)
        bout_OK = 0
        
    if mid == 1:
        pyg.draw.rect(screen, colors[color_switch], taupe_mid)
        bout_OK = 0
    
    if HD == 1:
        pyg.draw.rect(screen, colors[color_switch], taupe_HD)
        bout_OK = 0
    
    if HG == 1:
        pyg.draw.rect(screen, colors[color_switch], taupe_HG)
        bout_OK = 0
    
    if BD == 1:
        pyg.draw.rect(screen, colors[color_switch], taupe_BD)
        bout_OK = 0
    
    if BG == 1:
        pyg.draw.rect(screen, colors[color_switch], taupe_BG)
        bout_OK = 0

    # compteur qui fait disparaitre le carré et crée une nouvelle valeur (-1 point)
    if game_start == 1:
        if s > 0:
            #print(s)
            s -= 1
        else:
            bout_OK = 1
            droite = 0
            gauche = 0
            haut = 0
            bas = 0
            mid = 0
            HG = 0
            HD = 0
            BG = 0
            BD = 0
            s = secondes
            color_switch = (color_switch + 1) % len(colors)
            points -= 1

    # limite les points a 0
    if points < 0:
        points = 0

    #print(points)
    # victoire a 50 points
    if points == points_pour_win:
        print("victoire")
        Run = False
        Run_fin = True

    if game_start == 1:
        if timer_de_fin > 0:
            timer_de_fin -= 1
        else:
            print("défaite")
            Run = False
            Run_fin = True

    #print(timer_de_fin)
    
    for event in pyg.event.get():

        if event.type == KEYDOWN:
            # demarrer la partie
            if event.key == pyg.K_SPACE:
                if game_start == 0:
                    bout_OK = 1
                    s = secondes
                    game_start = 1

        if event.type == pyg.MOUSEBUTTONDOWN:

            marteau = marteau_frappe
            
            offset_marteau_x = - 118
            offset_marteau_y = - 180
            pos_marteau = list(pos_souris)
            pos_marteau[1] = pos_souris[1] + offset_marteau_y
            pos_marteau[0] = pos_souris[0] + offset_marteau_x

            # bas ( genere une nouvelle valeur, change la couleur, reset le timer, +1 point )
            if pyg.Rect.collidepoint(trou_bas, pos_souris):
                #print("ratio")
                # vérifie si le bouton appyuer est le bon
                if bas == 1:
                    bout_OK = 1
                    bas = 0
                    color_switch = (color_switch + 1) % len(colors)
                    s = secondes
                    points += 1
                else:
                    points -= 1
                    bas = 0
                    
            # droite ( genere une nouvelle valeur, change la couleur, reset le timer, +1 point )
            if pyg.Rect.collidepoint(trou_droite, pos_souris):
                # vérifie si le bouton appyuer est le bon
                if droite == 1:
                    bout_OK = 1
                    droite = 0
                    color_switch = (color_switch + 1) % len(colors)
                    s = secondes
                    points += 1
                else:
                    points -= 1
                    droite = 0
                    
            # gauche ( genere une nouvelle valeur, change la couleur, reset le timer, +1 point )
            if pyg.Rect.collidepoint(trou_gauche, pos_souris):
                # vérifie si le bouton appyuer est le bon
                if gauche == 1:
                    bout_OK = 1
                    gauche = 0
                    color_switch = (color_switch + 1) % len(colors)
                    s = secondes
                    points += 1
                else:
                    points -= 1
                    gauche = 0
                    
            # haut ( genere une nouvelle valeur, change la couleur, reset le timer, +1 point )
            if pyg.Rect.collidepoint(trou_haut, pos_souris):
                # vérifie si le bouton appyuer est le bon
                if haut == 1:
                    bout_OK = 1
                    haut = 0
                    color_switch = (color_switch + 1) % len(colors)
                    s = secondes
                    points += 1
                else:
                    points -= 1
                    droite = 0
                    
            # mid ( genere une nouvelle valeur, change la couleur, reset le timer, +1 point )
            if pyg.Rect.collidepoint(trou_mid, pos_souris):
                # vérifie si le bouton appyuer est le bon
                if mid == 1:
                    bout_OK = 1
                    mid = 0
                    color_switch = (color_switch + 1) % len(colors)
                    s = secondes
                    points += 1
                else:
                    points -= 1
                    mid = 0
                    
            # HG ( genere une nouvelle valeur, change la couleur, reset le timer, +1 point )
            if pyg.Rect.collidepoint(trou_HG, pos_souris):
                # vérifie si le bouton appyuer est le bon
                if HG == 1:
                    bout_OK = 1
                    HG = 0
                    color_switch = (color_switch + 1) % len(colors)
                    s = secondes
                    points += 1
                else:
                    points -= 1
                    HG = 0
                    
            # HD ( genere une nouvelle valeur, change la couleur, reset le timer, +1 point )
            if pyg.Rect.collidepoint(trou_HD, pos_souris):
                # vérifie si le bouton appyuer est le bon
                if HD == 1:
                    bout_OK = 1
                    HD = 0
                    color_switch = (color_switch + 1) % len(colors)
                    s = secondes
                    points += 1
                else:
                    points -= 1
                    HD = 0
                    
            # BG ( genere une nouvelle valeur, change la couleur, reset le timer, +1 point )
            if pyg.Rect.collidepoint(trou_BG, pos_souris):
                # vérifie si le bouton appyuer est le bon
                if BG == 1:
                    bout_OK = 1
                    BG = 0
                    color_switch = (color_switch + 1) % len(colors)
                    s = secondes
                    points += 1
                else:
                    points -= 1
                    BG = 0
                    
            # BD ( genere une nouvelle valeur, change la couleur, reset le timer, +1 point )
            if pyg.Rect.collidepoint(trou_BD, pos_souris):
                # vérifie si le bouton appyuer est le bon
                if BD == 1:
                    bout_OK = 1
                    BD = 0
                    color_switch = (color_switch + 1) % len(colors)
                    s = secondes
                    points += 1
                else:
                    points -= 1
                    BD = 0

        if event.type == MOUSEBUTTONUP:
            marteau = marteau_normal
            offset_marteau_x = -60
            offset_marteau_y = -160
            pos_marteau = list(pos_souris)
            pos_marteau[1] = pos_souris[1] + offset_marteau_y
            pos_marteau[0] = pos_souris[0] + offset_marteau_x

        # fermer le jeu
        if event.type == QUIT:
            pyg.quit()
            sys.exit()

    screen.blit(viseur, pos_viseur) #affiche le viseur
    screen.blit(marteau, pos_marteau) #affiche le marteau

    pyg.display.update()
    clock.tick(60)

while Run_fin:

    screen.fill((0, 0, 0))

    if points == points_pour_win:
        screen.blit(victoire, (0, 0))
        victoire = pyg.transform.scale(victoire, (1920,1080))
    else:
        screen.blit(defaite, (0, 0))
        defaite = pyg.transform.scale(defaite, (1920,1080))

    for event in pyg.event.get():

        if event.type == QUIT:
            pyg.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            pyg.quit()
            sys.exit()

    pyg.display.update()
    clock.tick(60)