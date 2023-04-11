# librairies
import pygame
import time


pyg = pygame
 
# Taille de la fenetre
window_x = 1920
window_y = 1080

niveau = 1

def snake_lejeu(niveau):
    encours = True    
    # couleurs
    black = pyg.Color(0, 0, 0)
    red = pyg.Color(255, 0, 0)
    green = pyg.Color(0, 255, 0)
    blue = pyg.Color(0, 0, 255)
    
    # Initialisation de pygame
    pyg.init()
    
    
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
    


    # Initialisation
    screen = pyg.display.set_mode((window_x, window_y))
    pyg.display.set_caption('hack')
    


    def taillex(img):
        taille = int(img.get_width()*screen.get_width()/img.get_width())
        return taille

    def tailley(img):
        taille = int(img.get_height()*screen.get_height()/img.get_height())
        return taille

    fond = pyg.image.load('assets/testfond.png')
    fond = pyg.transform.scale(fond,(taillex(fond), tailley(fond)))

    # FPS (frames per second) controller
    fps = pyg.time.Clock()
    
    # defining snake default position
    snake_position = [posx_debut, posy_debut]
    
    # defining first 4 blocks of snake body
    snake_body = [[posx_debut, posy_debut]
                ]

    if niveau == 3:
        direction = 'HAUT'
    else :
        direction = 'DROITE'

    change = direction


    taille = 55
    vitesse = 100

    
    # fonction fin


    def chemin(numchemin):
        chemin = pyg.image.load(f'assets/gta/cheminhack{numchemin}.png')
        chemin = pyg.transform.scale(chemin,(taillex(chemin),tailley(chemin)))
        return chemin   

    hackfond = pyg.image.load('assets/gta/fondhack.png')
    hackfond = pyg.transform.scale(hackfond, (taillex(hackfond), tailley(hackfond)))

    
 
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
                    
    
        if change == 'HAUT' and direction != 'BAS':
            direction = 'HAUT'
        if change == 'BAS' and direction != 'HAUT':
            direction = 'BAS'
        if change == 'GAUCHE' and direction != 'DROITE':
            direction = 'GAUCHE'
        if change == 'DROITE' and direction != 'GAUCHE':
            direction = 'DROITE'
    
   
        if direction == 'HAUT':
            snake_position[1] -= 20
        if direction == 'BAS':
            snake_position[1] += 20
        if direction == 'GAUCHE':
            snake_position[0] -= 20
        if direction == 'DROITE':
            snake_position[0] += 20
    

        snake_body.insert(0, list(snake_position))
        screen.blit(hackfond, (0, 0))
        screen.blit(chemin(niveau), (0, 0))
        #finx = pyg.draw.line(screen, green, (posx_fin, 768),(posx_fin, 877), 2)          
          
        
        for pos in snake_body:
            pyg.draw.rect(screen, black, pyg.Rect(pos[0], pos[1], taille, taille))
    

        if niveau == 1:        
            if snake_position[0] > posx_fin - (taille ):
                niveau += 1
                screen.fill(green)
                pyg.display.update()
                time.sleep(0.2)
                snake_lejeu(niveau)
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

        elif niveau == 2:
            if snake_position[1] < posy_fin:
                niveau += 1
                screen.fill(green)
                pyg.display.update()
                time.sleep(0.2)
                snake_lejeu(niveau)
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
                
                pyg.display.update()
                time.sleep(0.2)
                encours = False
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
        

        # Refresh game screen
        pyg.display.update()
    
        # Frame Per Second /Refresh Rate
        fps.tick(vitesse)
    screen.fill(blue)
def snakelike():
    snake_lejeu(niveau)
