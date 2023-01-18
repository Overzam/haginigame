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

secondes = 75 # temps pour taper les taupes
s = secondes

points = 0

game_start = 0

timer_de_fin = 1900
temps = 0

viseur = pyg.image.load('viseur.png')

marteau_normal = pyg.image.load('marteau45.png')
marteau_frappe = pyg.image.load("marteau90.png")

marteau = marteau_normal

trou_haut_x = width/2.04
trou_haut_y = height/2.59

trou_droite_x = width/1.826
trou_droite_y = height/2.05

trou_gauche_x = width/2.32
trou_gauche_y = height/2.05

trou_bas_x = width/2.04
trou_bas_y = height/1.69

trou_haut = Rect(trou_haut_x, trou_haut_y, 80, 80)
trou_droite = Rect(trou_droite_x,trou_droite_y, 80, 80)
trou_gauche = Rect(trou_gauche_x, trou_gauche_y, 80, 80)
trou_bas = Rect(trou_bas_x, trou_bas_y, 80, 80)

trou_HG = Rect(trou_gauche_x, trou_haut_y, 80, 80)
trou_HD = Rect(trou_droite_x, trou_haut_y, 80, 80)
trou_BG = Rect(trou_gauche_x, trou_bas_y, 80, 80)
trou_BD = Rect(trou_droite_x, trou_bas_y, 80, 80)

trou_mid = Rect(trou_haut_x,trou_droite_y, 80, 80)

taupe_haut = (trou_haut_x + 20, trou_haut_y + 20,40,40)
taupe_droite = (trou_droite_x + 20,trou_droite_y + 20,40,40)
taupe_gauche = (trou_gauche_x + 20, trou_gauche_y + 20, 40, 40)
taupe_bas = (trou_bas_x + 20, trou_bas_y + 20,40,40)

taupe_HG = (trou_gauche_x + 20, trou_haut_y + 20,40,40)
taupe_HD = (trou_droite_x + 20, trou_haut_y + 20,40,40)
taupe_BG = (trou_gauche_x + 20, trou_bas_y + 20,40,40)
taupe_BD = (trou_droite_x + 20, trou_bas_y + 20,40,40)

taupe_mid = (trou_haut_x + 20, trou_droite_y + 20,40,40)

var_sortie = 0

offset_marteau_x = 0
offset_marteau_y = -130

font = pyg.font.Font('Monocraft.otf', 100)

Run = True

while Run:
    screen.fill((0,0,0))

    aff_points = font.render(str(points), True, (255, 255, 255))
    
    pyg.mouse.set_visible(False)
    
    pos_souris = pyg.mouse.get_pos()
    pos_viseur = list(pos_souris)
    pos_viseur[0] -= 50
    pos_viseur[1] -= 50

    pos_marteau = list(pos_souris)
    pos_marteau[1] = pos_souris[1] + offset_marteau_y
    pos_marteau[0] = pos_souris[0] + offset_marteau_x

    screen.blit(aff_points,(30,10))

    pyg.draw.rect(screen, (255, 0, 0), trou_haut, 1)
    pyg.draw.rect(screen, (255, 0, 0), trou_gauche, 1)
    pyg.draw.rect(screen, (255, 0, 0), trou_droite, 1)
    pyg.draw.rect(screen, (255, 0, 0), trou_bas, 1)
    
    pyg.draw.rect(screen, (255, 0, 0), trou_HG, 1)
    pyg.draw.rect(screen, (255, 0, 0), trou_HD, 1)
    pyg.draw.rect(screen, (255, 0, 0), trou_BG, 1)
    pyg.draw.rect(screen, (255, 0, 0), trou_BD, 1)
    
    pyg.draw.rect(screen, (255, 0, 0), trou_mid, 1)

    if timer_de_fin == 1900:
        temps = 20
    if timer_de_fin < 1900 and timer_de_fin > 1800:
        temps = 19
    if timer_de_fin < 1800 and timer_de_fin > 1700:
        temps = 18
    if timer_de_fin < 1700 and timer_de_fin > 1600:
        temps = 17
    if timer_de_fin < 1600 and timer_de_fin > 1500:
        temps = 16
    if timer_de_fin < 1500 and timer_de_fin > 1400:
        temps = 15
    if timer_de_fin < 1400 and timer_de_fin > 1300:
        temps = 14
    if timer_de_fin < 1300 and timer_de_fin > 1200:
        temps = 13
    if timer_de_fin < 1200 and timer_de_fin > 1100:
        temps = 12
    if timer_de_fin < 1100 and timer_de_fin > 1000:
        temps = 11
    if timer_de_fin < 1000 and timer_de_fin > 900:
        temps = 10
    if timer_de_fin < 900 and timer_de_fin > 800:
        temps = 9
    if timer_de_fin < 800 and timer_de_fin > 700:
        temps = 8
    if timer_de_fin < 700 and timer_de_fin > 600:
        temps = 7
    if timer_de_fin < 600 and timer_de_fin > 500:
        temps = 6
    if timer_de_fin < 500 and timer_de_fin > 400:
        temps = 5
    if timer_de_fin < 400 and timer_de_fin > 300:
        temps = 4
    if timer_de_fin < 300 and timer_de_fin > 200:
        temps = 3
    if timer_de_fin < 200 and timer_de_fin > 100:
        temps = 2
    if timer_de_fin < 100 and timer_de_fin > 0:
        temps = 1
    if timer_de_fin == 0:
        temps = 0

    aff_temps = font.render(str(temps), True, (255, 255, 255))
    screen.blit(aff_temps,(1700,20))

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
    if points == 50:
        print("victoire")
        pyg.quit()
        sys.exit()

    if game_start == 1:
        if timer_de_fin > 0:
            timer_de_fin -= 1
        else:
            print("défaite")
            pyg.quit()
            sys.exit()

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
            offset_marteau_x = - 60
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
            offset_marteau_x = 0
            offset_marteau_y = - 130
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