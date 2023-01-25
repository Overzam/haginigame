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


case_rect = pyg.Rect(case_mastermind[0][0][0], case_mastermind[0][0][1], 31, 31)
touche_blanc = False
transpar = pyg.image.load('img/transpar.png')
stockage_couleur = transpar
remplace_couleur = False
dans_case_a_remp = False
affiche_dans_case  = False

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
                    if touche_blanc:
                        remplace_couleur = True
                        stockage_couleur = blanc
                    if touche_rouge:
                        remplace_couleur = True
                        stockage_couleur = rouge
                if remplace_couleur:
                    if dans_case_a_remp:
                        affiche_dans_case = True

    screen.blit(background, (0,0))
    screen.blit(mastermind_sprite, (500, 50))
    for i in range(4):
        for y in range(7):
            screen.blit(noir, (case_mastermind[y][i]))
    screen.blit(blanc, (200, 200))
    screen.blit(rouge, (200, 400))
    mouse = pyg.mouse.get_pos()
    mouse_rect = pyg.Rect(mouse[0], mouse[1], 1, 1)
    if mouse_rect.collidelist([blanc_rect]) != -1:
        touche_blanc = True
    else:
        touche_blanc = False
    mouse_rect = pyg.Rect(mouse[0], mouse[1], 1, 1)
    if mouse_rect.collidelist([rouge_rect]) != -1:
        touche_rouge = True
    else:
        touche_rouge = False
    
    if mouse_rect.collidelist([case_rect]) != -1:
        dans_case_a_remp = True
    else:
        dans_case_a_remp = False
    if dans_case_a_remp:
        screen.blit(stockage_couleur, (case_mastermind[0][0]))
    if affiche_dans_case:
        screen.blit(stockage_couleur, (case_mastermind[0][0]))

    pyg.display.flip()