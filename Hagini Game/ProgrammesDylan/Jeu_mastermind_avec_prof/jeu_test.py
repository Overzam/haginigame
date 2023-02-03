import pygame as pyg
import random

'''
creation du jeu sans interface:
'''

def pion_noir(choix_joueur):
    nb_pion_noir = 0
    for i in range(4):
        for y in range(4):
            if choix_joueur[i] == config[y]:
                nb_pion_noir += 1
    return nb_pion_noir

def pion_rouge(choix_joueur):
    nb_pion_rouge = 0
    for i in range(4):
        if choix_joueur[i] == config[i]:
            nb_pion_rouge += 1
    return nb_pion_rouge

def gagne():
    print("gagné")

def perdu():
    print("perdu")


width, height = 1920, 1080
screen = pyg.display.set_mode((width, height))

titre = "Jeu mastermind"
pyg.display.set_caption(titre)

pyg.init()

clock = pyg.time.Clock()

#definition du fond du jeu et des images
background = pyg.image.load('img/bg.jpg')
background = pyg.transform.scale(background, (width, height))

mastermind_sprite = pyg.image.load('img/mastermind.png')
mastermind_sprite = pyg.transform.scale(mastermind_sprite, (1000, 1000))

pion_n = [pyg.image.load('img/pion/pion_noir_0.png'), pyg.image.load('img/pion/pion_noir_1.png'), 
pyg.image.load('img/pion/pion_noir_2.png'), pyg.image.load('img/pion/pion_noir_3.png'), pyg.image.load('img/pion/pion_noir_4.png')] 
for i in range(5):
    pion_n[i] = pyg.transform.scale(pion_n[i], (100, 50))

pion_r = [pyg.image.load('img/pion/pion_rouge_0.png'), pyg.image.load('img/pion/pion_rouge_1.png'), 
pyg.image.load('img/pion/pion_rouge_2.png'), pyg.image.load('img/pion/pion_rouge_3.png'), pyg.image.load('img/pion/pion_rouge_4.png')] 
for i in range(5):
    pion_r[i] = pyg.transform.scale(pion_r[i], (100, 50))

noir =  pyg.image.load('img/couleur/noir.png')
noir = pyg.transform.scale(noir, (31, 31))

blanc =  pyg.image.load('img/couleur/blanc.png')
blanc = pyg.transform.scale(blanc, (31, 31))
blanc_apercu = pyg.transform.scale(blanc, (93, 93))
blanc_rect = pyg.Rect(200, 200, 93, 93)

rouge =  pyg.image.load('img/couleur/rouge.png')
rouge = pyg.transform.scale(rouge, (31, 31))
rouge_apercu = pyg.transform.scale(rouge, (93, 93))
rouge_rect = pyg.Rect(200, 400, 93, 93)

vert =  pyg.image.load('img/couleur/vert.png')
vert = pyg.transform.scale(vert, (31, 31))
vert_apercu = pyg.transform.scale(vert, (93, 93))
vert_rect = pyg.Rect(200, 600, 93, 93)

orange =  pyg.image.load('img/couleur/orange.png')
orange = pyg.transform.scale(orange, (31, 31))
orange_apercu = pyg.transform.scale(orange, (93, 93))
orange_rect = pyg.Rect(200, 800, 93, 93)      

bleu =  pyg.image.load('img/couleur/bleu.png')
bleu = pyg.transform.scale(bleu, (31, 31))
bleu_apercu = pyg.transform.scale(bleu, (93, 93))
bleu_rect = pyg.Rect(400, 200, 93, 93)      

violet =  pyg.image.load('img/couleur/violet.png')
violet = pyg.transform.scale(violet, (31, 31))
violet_apercu = pyg.transform.scale(violet, (93, 93))
violet_rect = pyg.Rect(400, 400, 93, 93)      

jaune =  pyg.image.load('img/couleur/jaune.png')
jaune = pyg.transform.scale(jaune, (31, 31))
jaune_apercu = pyg.transform.scale(jaune, (93, 93))
jaune_rect = pyg.Rect(400, 600, 93, 93)
  
couleur = [rouge, blanc, vert, jaune, bleu, violet, orange]

def config_aleatoire():
    config = [0] * 4
    for i in range(4):
        valeur_couleur = random.randint(0,(5-i))
        config[i] = couleur[valeur_couleur]
        couleur.remove(config[i])
    return config
config = config_aleatoire()

case_mastermind = [[[850, 300], [925, 300], [1000, 300], [1075, 300]],
[[850, 375], [925, 375], [1000, 375], [1075, 375]],
[[850, 450], [925, 450], [1000, 450], [1075, 450]],
[[850, 525], [925, 525], [1000, 525], [1075, 525]],
[[850, 600], [925, 600], [1000, 600], [1075, 600]],
[[850, 675], [925, 675], [1000, 675], [1075, 675]],
[[850, 750], [925, 750], [1000, 750], [1075, 750]]]

transpar = pyg.image.load('img/transpar.png')
stockage_couleur = transpar

stockage_quatre_couleur = [[[transpar], [transpar], [transpar], [transpar]],
[[transpar], [transpar], [transpar], [transpar]],
[[transpar], [transpar], [transpar], [transpar]],
[[transpar], [transpar], [transpar], [transpar]],
[[transpar], [transpar], [transpar], [transpar]],
[[transpar], [transpar], [transpar], [transpar]],
[[transpar], [transpar], [transpar], [transpar]]]

choix_joueur = [transpar, transpar, transpar, transpar]

nb_pion_noir = [0, 0, 0, 0, 0, 0, 0]
nb_pion_rouge = [0, 0, 0, 0, 0, 0, 0]


nb_colonne = 4
nb_ligne = 7
colonne_actuel = 0
ligne_actuel = 6
nb_ligne_confirme = 0
nb_essaie = 7
essaie = 0
affiche_couleur = False

run = True
while run:
    mouse = pyg.mouse.get_pos()
    mouse_rect = pyg.Rect(mouse[0], mouse[1], 1, 1)    
    case_rect = pyg.Rect(case_mastermind[ligne_actuel][colonne_actuel][0], case_mastermind[ligne_actuel][colonne_actuel][1], 31, 31)
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            run = False
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_ESCAPE:
                run = False
        if event.type == pyg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if mouse_rect.collidelist([case_rect]) != -1:
                    if not stockage_couleur == transpar:
                        stockage_quatre_couleur[ligne_actuel][colonne_actuel] = stockage_couleur
                        choix_joueur[colonne_actuel] = stockage_couleur
                        colonne_actuel += 1
                        if colonne_actuel >= 4:
                            nb_pion_noir[ligne_actuel] = pion_noir(choix_joueur)
                            nb_pion_rouge[ligne_actuel] = pion_rouge(choix_joueur)
                            ligne_actuel -= 1
                            nb_ligne_confirme += 1
                            essaie += 1
                            if pion_rouge(choix_joueur) == 4:
                                gagne()
                                run = False
                            if essaie >= nb_essaie:
                                perdu()
                                run = False
                            colonne_actuel = 0
                            
                if mouse_rect.collidelist([blanc_rect]) != -1:
                    stockage_couleur = blanc
                if mouse_rect.collidelist([rouge_rect]) != -1:
                    stockage_couleur = rouge
                if mouse_rect.collidelist([vert_rect]) != -1:
                    stockage_couleur = vert
                if mouse_rect.collidelist([orange_rect]) != -1:
                    stockage_couleur = orange
                if mouse_rect.collidelist([bleu_rect]) != -1:
                    stockage_couleur = bleu
                if mouse_rect.collidelist([violet_rect]) != -1:
                    stockage_couleur = violet   
                if mouse_rect.collidelist([jaune_rect]) != -1:
                    stockage_couleur = jaune


    screen.blit(background, (0, 0))
    screen.blit(mastermind_sprite, (500, 50))

    #affiche les piles de couleurs
    screen.blit(blanc_apercu, (200, 200))
    screen.blit(rouge_apercu, (200, 400))
    screen.blit(vert_apercu, (200, 600))
    screen.blit(orange_apercu, (200, 800))
    screen.blit(bleu_apercu, (400, 200))
    screen.blit(violet_apercu, (400, 400))
    screen.blit(jaune_apercu, (400, 600))

    for i in range(nb_ligne):
        for y in range(nb_colonne):
            screen.blit(noir, (case_mastermind[i][y]))    

    
    for i in range(colonne_actuel):
        screen.blit(stockage_quatre_couleur[ligne_actuel][i], (case_mastermind[ligne_actuel][i]))

    for i in range(nb_ligne_confirme):
        for y in range(4):
            screen.blit(stockage_quatre_couleur[ligne_actuel+i+1][y], (case_mastermind[ligne_actuel+i+1][y]))
        for y in range(nb_ligne_confirme):
            screen.blit(pion_n[nb_pion_noir[nb_ligne-y-1]], (case_mastermind[nb_ligne - nb_ligne_confirme][0][0]-160, case_mastermind[nb_ligne - y-1][0][1]))
            screen.blit(pion_r[nb_pion_rouge[nb_ligne-y-1]], (case_mastermind[nb_ligne - nb_ligne_confirme][0][0]+335, case_mastermind[nb_ligne - y-1][0][1]))

    pyg.display.flip()
