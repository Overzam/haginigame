import pygame
import time


pygame.init()

pyg = pygame
# Taille de la fenetre
window_x = 1920
window_y = 1080
#creation fenetre
pyg.display.set_caption('lejeu')
screen = pyg.display.set_mode((window_x,window_y))

def taillex(img):
    taille = int(img.get_width()*screen.get_width()/img.get_width())
    return taille
def tailley(img):
    taille = int(img.get_height()*screen.get_height()/img.get_height())
    return taille

#arriere plan + images
background = pyg.image.load('images/fondpc.png')
background = pyg.transform.scale(background,(taillex(background), tailley(background)))

nsipdf = pyg.image.load('images/icopdf.png')
nsipdf = pyg.transform.scale(nsipdf,(taillex(nsipdf),tailley(nsipdf)))
nsipdfsel = pyg.image.load('images/icopdfsel.png')
nsipdfsel = pyg.transform.scale(nsipdfsel,(taillex(nsipdfsel),tailley(nsipdfsel)))

hackico = pyg.image.load('images/icohack.png')
hackico = pyg.transform.scale(hackico,(taillex(hackico),tailley(hackico)))
hackicosel = pyg.image.load('images/icohacksel.png')
hackicosel = pyg.transform.scale(hackicosel,(taillex(hackicosel),tailley(hackicosel)))

hackfond = pyg.image.load('images/gta/fondhack.png')
hackfond = pyg.transform.scale(hackfond, (taillex(hackfond), tailley(hackfond)))

victoire = pyg.image.load('images/gta/victoire.png')
victoire = pyg.transform.scale(victoire, (taillex(victoire), tailley(victoire)))

def chemin(numchemin):
    chemin = pyg.image.load(f'images/gta/cheminhack{numchemin}.png')
    chemin = pyg.transform.scale(chemin,(taillex(chemin),tailley(chemin)))
    return chemin

running = True
menu = True
hack_running = False
selhack = False
selpdf = False

black = pyg.Color(0, 0, 0)
red = pyg.Color(255, 0, 0)
green = pyg.Color(0, 255, 0)
blue = pyg.Color(0, 0, 255)

def snake_lejeu(niveau):
    encours = True    
    
    if niveau == 1:
        posx_debut = 28
        posy_debut = 220
        posx_fin = 1883
    elif niveau == 2: 
        posx_debut = 28
        posy_debut = 795
        posy_fin = 28
    elif niveau == 3:
        posx_debut = 278
        posy_debut = 998
        posx_fin = 1893
    

    fps = pyg.time.Clock()
    

    snake_position = [posx_debut, posy_debut]
    

    snake_body = [[posx_debut, posy_debut]
                ]

    if niveau == 3:
        direction = 'HAUT'
    else :
        direction = 'DROITE'

    change = direction

    taille = 55
    vitesse = 20

    # fonction fin
 
    while encours:
                
        for event in pyg.event.get():
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_UP:
                    change = 'HAUT'
                if event.key == pyg.K_DOWN:
                    change = 'BAS'
                if event.key == pyg.K_LEFT:
                    change = 'GAUCHE'
                if event.key == pyg.K_RIGHT:
                    change = 'DROITE'
                
                if event.key == pyg.K_ESCAPE :
                    encours = False
                    pyg.quit()
            
        if change == 'HAUT' and direction != 'BAS':
            direction = 'HAUT'
        if change == 'BAS' and direction != 'HAUT':
            direction = 'BAS'
        if change == 'GAUCHE' and direction != 'DROITE':
            direction = 'GAUCHE'
        if change == 'DROITE' and direction != 'GAUCHE':
            direction = 'DROITE'
    
   
        if direction == 'HAUT':
            snake_position[1] -= vitesse
        if direction == 'BAS':
            snake_position[1] += vitesse
        if direction == 'GAUCHE':
            snake_position[0] -= vitesse
        if direction == 'DROITE':
            snake_position[0] += vitesse
    
        snake_body.insert(0, list(snake_position))
        screen.blit(hackfond, (0, 0))
        screen.blit(chemin(niveau), (0, 0))

        
        colchemin1 =[pyg.Rect(0, 0, 1920, 165),
                    pyg.Rect(685, 0, 1420, 741),
                    pyg.Rect(0, 329, 521, 750),
                    pyg.Rect(0, 905, 1920, 175)
                    ]
        
        
        for mur in colchemin1 :
            pyg.draw.rect(screen, (255,255,255), mur, 2)
        
        #finx = pyg.draw.line(screen, green, (posx_fin, 768),(posx_fin, 877), 2)          
          
        
        for pos in snake_body:
            pyg.draw.rect(screen, black, pyg.Rect(pos[0], pos[1], taille, taille))
    

        if niveau == 1:        
            if snake_position[0] > posx_fin - (taille ):
                
                screen.fill(green)
                pyg.display.update()
                time.sleep(0.2)
                niveau = 2
                return niveau
            '''
            elif snake_position[0] < - taille or snake_position[0] > window_x :
                screen.fill(red)
                pyg.display.update()
                time.sleep(0.2)
                niveau = 1
                return niveau
            elif snake_position[1] < - taille or snake_position[1] > window_y :
                screen.fill(red)
                pyg.display.update()
                time.sleep(0.2)
                niveau = 1
                return niveau        
            '''

        elif niveau == 2:
            if snake_position[1] < posy_fin:
                
                screen.fill(green)
                pyg.display.update()
                time.sleep(0.2)
                niveau = 3
                return niveau
            '''
            elif snake_position[0] < - taille or snake_position[0] > window_x :
                screen.fill(red)
                pyg.display.update()
                time.sleep(0.2)
                snake_lejeu(niveau)
            elif snake_position[1] < - taille or snake_position[1] > window_y :
                screen.fill(red)
                pyg.display.update()
                time.sleep(0.2)
                snake_lejeu(niveau)    
            '''
        elif niveau == 3:        
            if snake_position[0] > posx_fin - (taille ):
                encours = False
                hack_running = False
                niveau = 4
                return niveau

            '''
            elif snake_position[0] < - taille or snake_position[0] > window_x :
                screen.fill(red)
                pyg.display.update()
                time.sleep(0.2)
                snake_lejeu(niveau)
            elif snake_position[1] < - taille or snake_position[1] > window_y :
                screen.fill(red)
                pyg.display.update()
                time.sleep(0.2)
                snake_lejeu(niveau)
            ''' 
        

   
        pyg.display.update()
    

        fps.tick(vitesse)
    
    

def snakelike():
    while snake_lejeu(1) != 2:
        snake_lejeu(1)
    while snake_lejeu(2) != 3:
        snake_lejeu(2)
    while snake_lejeu(3) != 4:
        snake_lejeu(3)
    screen.blit(victoire, (0, 0))
    pyg.display.update()
    time.sleep(1)
    print('bien')

'''
    niveau = 1
    snake_lejeu(niveau)
    if snake_lejeu(niveau) == 2:
        niveau += 1
        snake_lejeu(niveau)
    if snake_lejeu(niveau) == 3:
        snake_lejeu(niveau)
    '''


def fin():
    screen.blit(blue)    


while running:
    
    '''
    if hack_running :
        snakelike()
    '''
    if selpdf:
        screen.blit(background, (0, 0))
        screen.blit(nsipdf, (0, 0))
        screen.blit(hackico, (0, 0))
        screen.blit(nsipdfsel, (0, 0))

    elif selhack:
        screen.blit(background, (0, 0))
        screen.blit(nsipdf, (0, 0))
        screen.blit(hackico, (0, 0))   
        screen.blit(hackicosel, (0, 0))

    elif menu:
        colhack = pyg.draw.rect(screen, (255,255,255), pyg.Rect(6, 174, 162, 124), 2)
        colpdf = pyg.draw.rect(screen, (255,255,255), pyg.Rect(6, 14, 162, 124), 2)
        screen.blit(background, (0, 0))
        screen.blit(nsipdf, (0, 0))
        screen.blit(hackico, (0, 0))
        
    
    pyg.display.flip()

    for event in pyg.event.get():

        if event.type == pyg.QUIT:
            running = False

        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_ESCAPE :
                if hack_running:
                    hack_running = False
                    print('salope')
                if running and hack_running == False:
                    print('quitter')
                    pyg.QUIT()

        if event.type == pyg.MOUSEBUTTONDOWN and hack_running == False:
            if colpdf.collidepoint(event.pos):
                selhack = False
                selpdf = True
            else:
                selpdf = False

        if event.type == pyg.MOUSEBUTTONDOWN and hack_running == False:
            if colhack.collidepoint(event.pos) and selhack:
                selhack = False
                hack_running = True
                snakelike()
                hack_running = False
                
                
            elif colhack.collidepoint(event.pos):
                selpdf = False
                selhack = True
            else:
                selhack = False
