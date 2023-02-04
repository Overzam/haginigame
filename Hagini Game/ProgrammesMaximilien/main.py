import pygame as pyg

from pygame import *
pyg.init()
pyg.mixer.init() 
import math
from random import randint
from victoire import victoire

pyg.time.Clock()
pyg.font.init()
pyg.display.init()
start_ticks = pyg.time.get_ticks()


height = 1920//2
width = 1080//2
pos = pyg.mouse.get_pos()
co_x = round(width / 10 * 16.3)
co_y = round(height / 12)
rayon_horloge = round(height / 25)
Duree_Anim = 4
Duree_Anim_txt = 1
Monte = False
Jeu_Lance = True
Bonne_repopnse = False
Defaite = False
Ancienne_Duree_Tempo2 = 0
anciennes_Secondes_citation = 0
a = 0

# Liste de toutes les citations à recopier format : ["texte de la citation", duree demandee pour l'ecrire, auteur
Citations = [["azertyuiop",10,"Freud"],
             ["qsdfghjklm",20,"Spinoza"],
             ["wxcvbn",30,"Epictete"]]

Citation = Citations[randint(0,len(Citations)-1)]
Auteur = Citation[2]
Texte_Question = "Quelle est la citation de " + Auteur + " que nous avons étudiée ?"
Texte_Question_En_Cour = ""
Texte_Reponse_Donnee = ""
Texte_Reponse = Citation[0]
Duree = Citation[1]
Secondes_citation = Duree
angle = - 2 / Duree * 3.14 - 1.57  # en radiant ( 180° = 3.14 en radiant


# Definition du fond de jeu
screen = pyg.display.set_mode((height, width))
background = pyg.image.load("img_citations\Fond.png") # Charge l'image
background = pyg.transform.scale(background, (height, width)) # Taille de l'image
fond = background.convert()
screen.blit(fond, (0, 0)) # actualise le fond
pyg.display.flip()

# Definition de la feuille
Feuille = pyg.image.load("img_citations\Feuille.PNG") # Charge l'image
height_Feuille = height // 1.2  # taille en x de l'image
width_Feuille = width // 2  # taille en y de l'image
Feuille = pyg.transform.scale(Feuille, (int(height_Feuille), int(width_Feuille))).convert_alpha() # Taille de l'image
x_Feuille = height // 7
y_Feuille = width

# Couleurs de l'affichage des texte
noir = (0, 0, 0)  # fond
blanc = (255, 255, 255)  # ecriture
# Affichage du texte de reponse attendue
font=pyg.font.Font(None, 24)
Affichage_Texte_Reponse = font.render(Texte_Reponse,1,(noir))
x_Texte_Reponse = height // 6
y_Texte_Reponse = width + width // 20
# Affichage du texte de reponse donnee
Affichage_Texte_Reponse_Donnee = font.render(Texte_Reponse_Donnee,1,(blanc))
x_Texte_Reponse_Donnee = height // 5
y_Texte_Reponse_Donnee = width // 3

# Affichage du texte de Question
font=pyg.font.Font(None, 24)
Affichage_Texte_Question = font.render(Texte_Question,1,(noir))
x_Affichage_Texte_Question = height //10
y_Affichage_Texte_Question = width // 10

# Definition du son de parole de mohahati
Mohahati = pyg.mixer.music.load("son_citations\parole_mohahati.wav") 
pyg.mixer.music.play(10, 0.0) 

def Reussite():
    print("gagné")

def Echec():
    print("Perdu")

def anti_seche(x,y,x_Feuille,y_Feuille):
    if x > x_Feuille and x < x_Feuille + height_Feuille and y > y_Feuille and y < y_Feuille + width_Feuille:  # monte la feuille si on est dessus
        if y_Feuille < width // 8:
            y_Feuille += 10
    else:
        if y_Feuille < width - width // 20:
            y_Feuille -= 10


while Jeu_Lance:
    
    Duree_Tempo = round(Duree_Anim - ((pyg.time.get_ticks() - start_ticks) / 1000))
    pos = pyg.mouse.get_pos()
    if Duree_Tempo == 1:
        pyg.mixer.music.stop()
    
    if Duree_Tempo <= 3:
        Duree_Tempo2 = round(Duree_Anim_txt - ((pyg.time.get_ticks() - start_ticks) / 34)) # 34 c'est la vitesse d'apparition du texte
        if Duree_Tempo2 != Ancienne_Duree_Tempo2:
            Ancienne_Duree_Tempo2 = Duree_Tempo2
            if a < len(Texte_Question):
                Texte_Question_En_Cour += Texte_Question[a]
                a += 1
                
    
    Affichage_Texte_Question_En_Cour = font.render(Texte_Question_En_Cour,1,(noir))
 

    for event in pyg.event.get():
        # Definis la croix pour fermer la fenetre
        if event.type == pyg.QUIT:
            pyg.quit()

        if Duree_Tempo <= 0:
            if event.type == KEYDOWN:
                if event.key == pyg.K_KP_ENTER:
                    if Texte_Reponse_Donnee == Texte_Reponse:
                        Reussite()
                        print("bonne rep")
                    else:
                        Echec()
                    
        
                if event.key == pyg.K_BACKSPACE:
                    Texte_Reponse_Donnee = Texte_Reponse_Donnee[:-1]
                if event.key == pyg.K_a:
                    Texte_Reponse_Donnee += 'a'
                if event.key == pyg.K_b:
                    Texte_Reponse_Donnee += 'b'
                if event.key == pyg.K_c:
                    Texte_Reponse_Donnee += 'c'
                if event.key == pyg.K_d:
                    Texte_Reponse_Donnee += 'd'
                if event.key == pyg.K_e:
                    Texte_Reponse_Donnee += 'e'
                if event.key == pyg.K_f:
                    Texte_Reponse_Donnee += 'f'
                if event.key == pyg.K_g:
                    Texte_Reponse_Donnee += 'g'
                if event.key == pyg.K_h:
                    Texte_Reponse_Donnee += 'h'
                if event.key == pyg.K_i:
                    Texte_Reponse_Donnee += 'i'
                if event.key == pyg.K_j:
                    Texte_Reponse_Donnee += 'j'
                if event.key == pyg.K_k:
                    Texte_Reponse_Donnee += 'k'
                if event.key == pyg.K_l:
                    Texte_Reponse_Donnee += 'l'
                if event.key == pyg.K_m:
                    Texte_Reponse_Donnee += 'm'
                if event.key == pyg.K_n:
                    Texte_Reponse_Donnee += 'n'
                if event.key == pyg.K_o:
                    Texte_Reponse_Donnee += 'o'
                if event.key == pyg.K_p:
                    Texte_Reponse_Donnee += 'p'
                if event.key == pyg.K_q:
                    Texte_Reponse_Donnee += 'q'
                if event.key == pyg.K_r:
                    Texte_Reponse_Donnee += 'r'
                if event.key == pyg.K_s:
                    Texte_Reponse_Donnee += 's'
                if event.key == pyg.K_t:
                    Texte_Reponse_Donnee += 't'
                if event.key == pyg.K_u:
                    Texte_Reponse_Donnee += 'u'
                if event.key == pyg.K_v:
                    Texte_Reponse_Donnee += 'v'
                if event.key == pyg.K_w:
                    Texte_Reponse_Donnee += 'w'
                if event.key == pyg.K_x:
                    Texte_Reponse_Donnee += 'x'
                if event.key == pyg.K_y:
                    Texte_Reponse_Donnee += 'y'
                if event.key == pyg.K_z:
                    Texte_Reponse_Donnee += 'z' 
                if event.key == 32:
                    Texte_Reponse_Donnee += ' '
                Affichage_Texte_Reponse_Donnee = font.render(Texte_Reponse_Donnee, 1, (blanc))

    if Duree_Tempo <= 1 and Duree_Tempo >= 0 and y_Feuille > width - width // 20:
        y_Feuille -= 0.5
        y_Texte_Reponse -= 0.5

    if Duree_Tempo <= 0:
        x, y = pos[0], pos[1]
        if x > x_Feuille and x < x_Feuille + height_Feuille and y > y_Feuille and y < y_Feuille + width_Feuille:  # monte la feuille si on est dessus
            if y_Feuille > width - width // 8:
                y_Feuille -= 1
                y_Texte_Reponse -= 1
        else: # descend la feuille si on est plus dessus
            if y_Feuille < width - width // 20:
                y_Feuille += 1
                y_Texte_Reponse += 1
        Secondes_citation = round(Duree + Duree_Anim - ((pyg.time.get_ticks() - start_ticks) / 1000))
        
    if Secondes_citation == 0: # Test si temps ecoule
        print('perdu')
        pyg.quit()

    screen.blit(background, (0, 0))
    screen.blit(Feuille, (x_Feuille, y_Feuille))
    screen.blit(Affichage_Texte_Reponse, (x_Texte_Reponse, y_Texte_Reponse))
    screen.blit(Affichage_Texte_Reponse_Donnee, (x_Texte_Reponse_Donnee, y_Texte_Reponse_Donnee))
    screen.blit(Affichage_Texte_Question_En_Cour, (x_Affichage_Texte_Question, y_Affichage_Texte_Question))

    if Secondes_citation != anciennes_Secondes_citation:
        angle += 2 / Duree * 3.14 
    x = round(math.cos(angle) * rayon_horloge)
    y = round(math.sin(angle) * rayon_horloge)
    pyg.draw.line(screen, noir, (co_x, co_y), (co_x + x, co_y + y), 3)
    anciennes_Secondes_citation = Secondes_citation

    pyg.display.update()
    pyg.display.flip()

