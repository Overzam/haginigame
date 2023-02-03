import pygame as pyg

width, height = 1920, 1080
screen = pyg.display.set_mode((width, height))

titre = "Jeu mastermind"
pyg.display.set_caption(titre)

pyg.init()

clock = pyg.time.Clock()

#definition du fond du jeu
background = pyg.image.load('img/bg.jpg')
background = pyg.transform.scale(background, (width, height))

mastermind_sprite = pyg.image.load('img/mastermind.png')
mastermind_sprite = pyg.transform.scale(mastermind_sprite, (1000, 1000))


noir =  pyg.image.load('img/couleur/noir.png')
noir = pyg.transform.scale(noir, (31, 31))

blanc =  pyg.image.load('img/couleur/blanc.png')
blanc = pyg.transform.scale(blanc, (31, 31))

blanc_rect = pyg.Rect(200, 200, 31, 31)

rouge =  pyg.image.load('img/couleur/rouge.png')
rouge = pyg.transform.scale(rouge, (31, 31))

rouge_rect = pyg.Rect(200, 400, 31, 31)



case_mastermind = [[[850, 300], [925, 300], [1000, 300], [1075, 300]],
[[850, 375], [925, 375], [1000, 375], [1075, 375]],
[[850, 450], [925, 450], [1000, 450], [1075, 450]],
[[850, 525], [925, 525], [1000, 525], [1075, 525]],
[[850, 600], [925, 600], [1000, 600], [1075, 600]],
[[850, 675], [925, 675], [1000, 675], [1075, 675]],
[[850, 750], [925, 750], [1000, 750], [1075, 750]]]


ligne_actuel = 6
colonne_actuel = 0
hover_blanc = False
hover_rouge = False
transpar = pyg.image.load('img/transpar.png')
stockage_couleur = transpar
stockage_quatre_couleur = [[transpar]*4] * 7
nb_colonne_confirme = 0
nb_ligne_confirme = 0
remplace_couleur = False
dans_case_a_remp = False
affiche_dans_case  = False
confirme = False

run = True
while run:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            run = False
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_ESCAPE:
                run = False
            if event.key == pyg.K_BACKSPACE:
                stockage_couleur = transpar
                dans_case_a_remp = False
                affiche_dans_case = False
        if event.type == pyg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if stockage_couleur == transpar:
                    if hover_blanc:
                        remplace_couleur = True
                        stockage_couleur = blanc
                    if hover_rouge:
                        remplace_couleur = True
                        stockage_couleur = rouge
                if remplace_couleur:
                    if dans_case_a_remp:
                        affiche_dans_case = True

    #definie le rect de la case actuelle
    case_rect = pyg.Rect(case_mastermind[ligne_actuel][colonne_actuel][0], case_mastermind[ligne_actuel][colonne_actuel][1], 31, 31)

    #affiche fond et mastermind
    screen.blit(background, (0,0))
    screen.blit(mastermind_sprite, (500, 50))

    #affiche tous les carrés du mastermind
    for i in range(4):
        for y in range(7):
            screen.blit(noir, (case_mastermind[y][i]))

    #affiche les piles de couleurs
    screen.blit(blanc, (200, 200))
    screen.blit(rouge, (200, 400))

    #prend les coo et le rect de la souris pour les comparer a celle des piles de couleurs
    mouse = pyg.mouse.get_pos()
    mouse_rect = pyg.Rect(mouse[0], mouse[1], 1, 1)

    #compare les 2 coo et touche_couelur = True si il se touche
    if mouse_rect.collidelist([blanc_rect]) != -1:
        hover_blanc = True
    else:
        hover_blanc = False

    if mouse_rect.collidelist([rouge_rect]) != -1:
        hover_rouge = True
    else:
        hover_rouge = False
    
    #si c'est dans la case a remplir dans_case = true
    if mouse_rect.collidelist([case_rect]) != -1:
        dans_case_a_remp = True
    else:
        dans_case_a_remp = False

    #si c'est dans case le bail du hover s'affiche
    if dans_case_a_remp:
        screen.blit(stockage_couleur, (case_mastermind[ligne_actuel][colonne_actuel][0], case_mastermind[ligne_actuel][colonne_actuel][1]))

    for i in range(nb_colonne_confirme):
        for y in range(nb_ligne_confirme):
            screen.blit(stockage_quatre_couleur[ligne_actuel][colonne_actuel], (case_mastermind[ligne_actuel][i][0], case_mastermind[ligne_actuel][i][1]))

    for i in range(nb_colonne_confirme):
        screen.blit(stockage_quatre_couleur[ligne_actuel][colonne_actuel], (case_mastermind[ligne_actuel][i][0], case_mastermind[ligne_actuel][i][1]))


    '''
    screen.blit(stockage_quatre_couleur[y - nb_colonne_confirme][i], (case_mastermind[y - nb_colonne_confirme][i][0], case_mastermind[y - nb_colonne_confirme][i][1]))
        screen.blit(stockage_quatre_couleur[ligne_actuel][i], (case_mastermind[ligne_actuel][i][0], case_mastermind[ligne_actuel][i][1]))
    '''
    
    if affiche_dans_case:
        stockage_quatre_couleur[ligne_actuel][colonne_actuel] =  stockage_couleur
        colonne_actuel += 1
        if colonne_actuel >= 4:
            colonne_actuel = 0
            nb_colonne_confirme = 0
            ligne_actuel -= 1
        nb_colonne_confirme += 1
        stockage_couleur = transpar
        dans_case_a_remp = False
        affiche_dans_case = False
        
    pyg.display.flip()