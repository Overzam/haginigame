import pygame as pyg
from pygame import *

import math
from random import randint

pyg.init()
pyg.mixer.init()
pyg.time.Clock()
pyg.font.init()
pyg.display.init()
start_ticks = pyg.time.get_ticks()

# Variables Globales
son = 1
height = 1080
width = 1920

pos = pyg.mouse.get_pos()
co_x = round(height / 10 * 16.3)
co_y = round(width / 12)
rayon_horloge = round(width / 25)
Duree_Anim = 4
Monte = False
Jeu_Lance = True
Bonne_repopnse = False
Defaite = False
Ancienne_Duree_Tempo2 = 0
anciennes_Secondes_citation = 0
a = 0
perdu = False
bonnne_rep = False
Score_Avant_Defaite = 0
Taille_Police = height // 22

# Liste de toutes les citations à recopier format : ["texte de la citation", duree demandee pour l'ecrire, "auteur"]
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
angle = - 2 / Duree * math.pi - math.pi // 2  # en radiant ( 180° = Pi en radiant )


# Definition du fond de jeu
screen = pyg.display.set_mode((width, height))
background = pyg.image.load("img_citations\Fond.png") # Charge l'image
background = pyg.transform.scale(background, (width, height)) # Taille de l'image
fond = background.convert()
screen.blit(fond, (0, 0)) # actualise le fond
pyg.display.flip()

# Definition de la feuille
Feuille = pyg.image.load("img_citations\Feuille.PNG") # Charge l'image
width_Feuille = width // 1.2  # taille en x de l'image
height_Feuille = height // 2  # taille en y de l'image
Feuille = pyg.transform.scale(Feuille, (int(width_Feuille), int(height_Feuille))).convert_alpha() # Taille de l'image
x_Feuille = width // 7
y_Feuille = height

# Couleurs de l'affichage des texte
noir = (0, 0, 0)  # fond
blanc = (255, 255, 255)  # ecriture

# Affichage du texte de reponse attendue
font=pyg.font.Font(None, Taille_Police)
Affichage_Texte_Reponse = font.render(Texte_Reponse,1,(noir))
x_Texte_Reponse = width // 6
y_Texte_Reponse = height + height // 20

# Affichage du texte de reponse donnee
Affichage_Texte_Reponse_Donnee = font.render(Texte_Reponse_Donnee,1,(blanc))
x_Texte_Reponse_Donnee = width // 5
y_Texte_Reponse_Donnee = height // 3

# Affichage du texte de Question
font=pyg.font.Font(None, Taille_Police)
Affichage_Texte_Question = font.render(Texte_Question,1,(noir))
x_Affichage_Texte_Question = width //10
y_Affichage_Texte_Question = height // 10

# Definition du son de parole de mohahati
Mohahati = pyg.mixer.music.load("son_citations\parole_mohahati.wav") 
pyg.mixer.music.play(10, 0.0) 
pyg.mixer.music.set_volume(0.25*son)
########################################################################################################################

def contour(valeur):  # entre 0 et 100
    Pas_x = width // 100
    Pas_y = height // 100
    rouge = (255, 0, 0)
    if valeur <= 50:
        pyg.draw.rect(screen, rouge, (width/2 - valeur * Pas_x, height - Pas_y,2 * valeur * Pas_x ,Pas_y))
        pyg.draw.rect(screen, rouge, (width/2 - valeur * Pas_x,0 ,2 * valeur * Pas_x ,Pas_y))
    else:
        pyg.draw.rect(screen, rouge, (0, height - Pas_y,width ,Pas_y))
        pyg.draw.rect(screen, rouge, (0,0 ,width ,Pas_y))

        pyg.draw.rect(screen, rouge, (0, height -(valeur-50)*Pas_y, Pas_x, (valeur-50) * Pas_y ))
        pyg.draw.rect(screen, rouge, (width - Pas_x, height -(valeur-50)*Pas_y, Pas_x, (valeur-50) * Pas_y ))
        
        pyg.draw.rect(screen, rouge, (0, 0, Pas_x, (valeur-50) * Pas_y ))
        pyg.draw.rect(screen, rouge, (width - Pas_x, 0, Pas_x, (valeur-50) * Pas_y ))

########################################################################################################################

def victoire():

    print("V comme victoire")

    Texte_Felicitation = "Hmmm...         Bien joué."
    Texte_Felicitation_En_cour = ""
    Fin = False

    Ancienne_Duree_Tempo = 0
    a = 0

    while not Fin:

        for event in pyg.event.get():
            # Definis la croix pour fermer la fenetre
            if event.type == pyg.QUIT:
                pyg.quit()

        Duree_Tempo = round( 0 + ((pyg.time.get_ticks() - start_ticks) / 60))  # 60 c'est la vitesse d'apparition du texte
        if Duree_Tempo != Ancienne_Duree_Tempo:
            Ancienne_Duree_Tempo = Duree_Tempo
            if a < len(Texte_Felicitation):
                Texte_Felicitation_En_cour += Texte_Felicitation[a]
                a += 1

        Affichage_Texte_Felicitation_En_Cour = font.render(Texte_Felicitation_En_cour, 1, (noir))


        Affichage_Texte_Reponse_Donnee = font.render(Texte_Reponse_Donnee, 1, (blanc))
        screen.blit(background, (0, 0))

        pyg.draw.line(screen, noir, (co_x, co_y), (co_x + x, co_y + y), 3)  # Affiche l'aiguille de l'horloge

        # y_Feuille += 1
        # y_Texte_Reponse += 1
        screen.blit(Feuille, (x_Feuille, y_Feuille))
        screen.blit(Affichage_Texte_Reponse, (x_Texte_Reponse, y_Texte_Reponse))

        screen.blit(Affichage_Texte_Reponse_Donnee, (x_Texte_Reponse_Donnee, y_Texte_Reponse_Donnee))
        screen.blit(Affichage_Texte_Felicitation_En_Cour, (x_Affichage_Texte_Question, y_Affichage_Texte_Question))
        pyg.display.update()
        pyg.display.flip()


########################################################################################################################

def transition():
    print("T comme transition")

    Texte_Remontrance = "TU ME FAIS HONTE !!!"
    Texte_Remontrance_En_cour = ""
    Fin = False

    Ancienne_Duree_Tempo = 0
    a = 0

    while not Fin:

        for event in pyg.event.get():
            # Definis la croix pour fermer la fenetre
            if event.type == pyg.QUIT:
                pyg.quit()

        Duree_Tempo = round( 0 + ((pyg.time.get_ticks() - start_ticks) / 60))  # 60 c'est la vitesse d'apparition du texte
        if Duree_Tempo != Ancienne_Duree_Tempo:
            Ancienne_Duree_Tempo = Duree_Tempo
            if a < len(Texte_Remontrance):
                Texte_Remontrance_En_cour += Texte_Remontrance[a]
                a += 1

        Affichage_Texte_Remontrance_En_Cour = font.render(Texte_Remontrance_En_cour, 1, (noir))


        Affichage_Texte_Reponse_Donnee = font.render(Texte_Reponse_Donnee, 1, (blanc))
        screen.blit(background, (0, 0))

        pyg.draw.line(screen, noir, (co_x, co_y), (co_x + x, co_y + y), 3)  # Affiche l'aiguille de l'horloge

        # y_Feuille += 1
        # y_Texte_Reponse += 1
        screen.blit(Feuille, (x_Feuille, y_Feuille))
        screen.blit(Affichage_Texte_Reponse, (x_Texte_Reponse, y_Texte_Reponse))

        screen.blit(Affichage_Texte_Reponse_Donnee, (x_Texte_Reponse_Donnee, y_Texte_Reponse_Donnee))
        screen.blit(Affichage_Texte_Remontrance_En_Cour, (x_Affichage_Texte_Question, y_Affichage_Texte_Question))
        pyg.display.update()
        pyg.display.flip()

########################################################################################################################

while Jeu_Lance:
    
    Duree_Tempo = round(Duree_Anim - ((pyg.time.get_ticks() - start_ticks) / 1000)) # Duree du temps avant le commencement du jeu en secondes
    pos = pyg.mouse.get_pos()

    if Duree_Tempo == 1: # arrete le son des paroles une sec avant le commencement du jeu
        pyg.mixer.music.stop()


    if Duree_Tempo <= 3:
        Duree_Tempo2 = round(0 + ((pyg.time.get_ticks() - start_ticks) / 34)) # 34 c'est la vitesse d'apparition du texte
        if Duree_Tempo2 != Ancienne_Duree_Tempo2:
            if a < len(Texte_Question):
                Texte_Question_En_Cour += Texte_Question[a]
                a += 1
                Ancienne_Duree_Tempo2 = Duree_Tempo2

    Affichage_Texte_Question_En_Cour = font.render(Texte_Question_En_Cour,1,(noir))
 

    for event in pyg.event.get():
        # Definis la croix pour fermer la fenetre
        if event.type == pyg.QUIT:
            pyg.quit()

        if Duree_Tempo <= 0:
            if event.type == KEYDOWN:
                if event.key == pyg.K_KP_ENTER:
                    if Texte_Reponse_Donnee == Texte_Reponse:
                        bonnne_rep = True
                        Jeu_Lance = False

                # code les lettres pour qu'elles soient ajoutées au texte de réponse
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

    if Duree_Tempo <= 1 and Duree_Tempo >= 0 and y_Feuille > height - height // 20:
        y_Feuille -= 0.5
        y_Texte_Reponse -= 0.5

    if Duree_Tempo <= 0:
        x, y = pos[0], pos[1]
        if x > x_Feuille and x < x_Feuille + width_Feuille and y > y_Feuille and y < y_Feuille + height_Feuille:  # monte la feuille si on est dessus
            if y_Feuille > height - height // 8:
                y_Feuille -= height // 130
                y_Texte_Reponse -= height // 130
        else: # descend la feuille si on est plus dessus
            if y_Feuille < height - height // 20:
                y_Feuille += height // 130
                y_Texte_Reponse += height // 130
        Secondes_citation = round(Duree + Duree_Anim - ((pyg.time.get_ticks() - start_ticks) / 1000))
    
    
    if Secondes_citation == 0: # Test si temps ecoule
        print('perdu')
        perdu = True
        Jeu_Lance = False
    
    screen.blit(background, (0, 0))
    screen.blit(Feuille, (x_Feuille, y_Feuille))
    screen.blit(Affichage_Texte_Reponse, (x_Texte_Reponse, y_Texte_Reponse))
    screen.blit(Affichage_Texte_Reponse_Donnee, (x_Texte_Reponse_Donnee, y_Texte_Reponse_Donnee))
    screen.blit(Affichage_Texte_Question_En_Cour, (x_Affichage_Texte_Question, y_Affichage_Texte_Question))


    # Affichage Horloge
    if Secondes_citation != anciennes_Secondes_citation: # modifie l'angle de l'horologe chaque sec
        angle += 2 / Duree * math.pi # en radiant

    x = round(math.cos(angle) * rayon_horloge)
    y = round(math.sin(angle) * rayon_horloge)
    pyg.draw.line(screen, noir, (co_x, co_y), (co_x + x, co_y + y), 3) # fais le tracé de l'aiguille de l'horloge le centre est (co_x, co_y) et x, y c'est le décalage qu'il faut avec le centre pour que l'aiguille aille au bon endroit
    anciennes_Secondes_citation = Secondes_citation


    # S'ocupe du score avant defaite (le score c a quel point on est vu en train de tricher par le prof)
    if y_Feuille < height - height // 20:
        Score_Avant_Defaite += 0.5
    else:
        if Score_Avant_Defaite > 0:
            Score_Avant_Defaite -= 0.5
    contour(Score_Avant_Defaite)        
            
    if Score_Avant_Defaite > 100: # Test si le prof nous voit tricher
        perdu = True
        Jeu_Lance = False


    pyg.display.update()
    pyg.display.flip()

if perdu:
    transition()

if bonnne_rep:
    victoire()

