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

volumeico = pyg.image.load('images/parametres/volume.png')
volumeico = pyg.transform.scale(volumeico, (taillex(volumeico), tailley(volumeico)))

parametresico = pyg.image.load('images/parametres/parametres.png')
parametresico = pyg.transform.scale(parametresico, (taillex(parametresico), tailley(parametresico)))

def nbvol(hauteurvolume):
    volu = pyg.image.load(f'images/parametres/{hauteurvolume}.10.png')
    volu = pyg.transform.scale(volu,(taillex(volu),tailley(volu)))
    return volu


def chemin(numchemin):
    chemin = pyg.image.load(f'images/gta/cheminhack{numchemin}.png')
    chemin = pyg.transform.scale(chemin,(taillex(chemin),tailley(chemin)))
    return chemin

def volu(x):

    if x > 10 :
        screen.blit(nbvol(10), (0, 0))

        x = 10
        

    elif x <= 0:
        print('a')
    else :
        screen.blit(nbvol(x), (0, 0))
        pyg.display.flip()

running = True
menu = True
hack_running = False
selhack = False
selpdf = False
parametres = False
volume = False

black = pyg.Color(0, 0, 0)
red = pyg.Color(255, 0, 0)
green = pyg.Color(0, 255, 0)
blue = pyg.Color(0, 0, 255)
white = pyg.Color(255, 255, 255)

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
          
        for pos in snake_body:
            pyg.draw.rect(screen, black, pyg.Rect(pos[0], pos[1], taille, taille))
    



        couleurserpentx = pyg.Surface.get_at(screen, (snake_position[0]-1, snake_position[1]-1))
        couleurserpenty = pyg.Surface.get_at(screen, (snake_position[0]+taille, snake_position[1]+taille))
            
        if niveau == 1:      
            niveaupasse = False  
            if snake_position[0] > posx_fin - (taille ):
                
                niveaupasse = True
                screen.fill(green)
                pyg.display.update()
                time.sleep(0.2)
                return niveaupasse
 
            elif couleurserpentx == (49, 49, 49, 255) or couleurserpentx == (31,31,31,255) or couleurserpenty == (49, 49, 49, 255) or couleurserpenty == (31,31,31,255):
                screen.fill(red)
                pyg.display.update()
                time.sleep(0.2)
                return niveaupasse
            
        elif niveau == 2:
            niveaupasse = False  
            if snake_position[1] < posy_fin:
                niveaupasse = True
                screen.fill(green)
                pyg.display.update()
                time.sleep(0.2)
                return niveaupasse
            
            elif couleurserpentx == (49, 49, 49, 255) or couleurserpentx == (31,31,31,255) or couleurserpenty == (49, 49, 49, 255) or couleurserpenty == (31,31,31,255):
                screen.fill(red)
                pyg.display.update()
                time.sleep(0.2)
                return niveaupasse
  
        elif niveau == 3:    
            niveaupasse = False      
            if snake_position[0] > posx_fin - (taille ):
                niveaupasse = True
                encours = False
                return niveaupasse

            elif couleurserpentx == (49, 49, 49, 255) or couleurserpentx == (31,31,31,255) or couleurserpenty == (49, 49, 49, 255) or couleurserpenty == (31,31,31,255):
                screen.fill(red)
                pyg.display.update()
                time.sleep(0.2)
                return niveaupasse
            
        pyg.display.update()

        fps.tick(vitesse)
    
def snakelike():
    while snake_lejeu(1) == False:
        snake_lejeu(1)
    while snake_lejeu(2) == False:
        snake_lejeu(2)
    while snake_lejeu(3) == False:
        snake_lejeu(3)
    screen.blit(victoire, (0, 0))
    pyg.display.update()
    time.sleep(1)
    print('bien')

def fin():
    screen.blit(blue)    

hautvol = 5
while running:
    
    if parametres :
        
        screen.blit(background, (0, 0))
        screen.blit(nsipdf, (0, 0))
        screen.blit(hackico, (0, 0))        
        screen.blit(parametresico,(0, 0))
        

    elif selpdf:
        screen.blit(background, (0, 0))
        screen.blit(nsipdf, (0, 0))
        screen.blit(hackico, (0, 0))
        screen.blit(nsipdfsel, (0, 0))

    elif selhack:
        screen.blit(background, (0, 0))
        screen.blit(nsipdf, (0, 0))
        screen.blit(hackico, (0, 0))   
        screen.blit(hackicosel, (0, 0))

    elif volume :
        screen.blit(background, (0, 0))
        screen.blit(nsipdf, (0, 0))
        screen.blit(hackico, (0, 0))
        screen.blit(volumeico,(0, 0))
        
        volu(hautvol)

    else:
        colmoins = pyg.draw.rect(screen, (255,255,255), pyg.Rect(16, 986, 20, 20), 2)
        colplus = pyg.draw.rect(screen, (255,255,255), pyg.Rect(258, 986, 19, 20), 2)
        colvol= pyg.draw.rect(screen, (255,255,255), pyg.Rect(0, 971, 364, 51), 2)
        colhack = pyg.draw.rect(screen, (255,255,255), pyg.Rect(6, 174, 162, 124), 2)
        colpdf = pyg.draw.rect(screen, (255,255,255), pyg.Rect(6, 14, 162, 124), 2)
        colpara = pyg.draw.rect(screen, (255,255,255), pyg.Rect(0, 1023, 60, 57), 2)
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
                volume = False
                parametres = False
            else:
                selpdf = False


        if event.type == pyg.MOUSEBUTTONDOWN and hack_running == False:
            if colhack.collidepoint(event.pos) and selhack:
                selhack = False
                hack_running = True
                snakelike()
                hack_running = False
                parametres = False
                
            elif colhack.collidepoint(event.pos):
                selpdf = False
                selhack = True
                parametres = False

            else:
                selhack = False

        if event.type == pyg.MOUSEBUTTONDOWN and hack_running == False:
            if colpara.collidepoint(event.pos):
                selhack = False
                selpdf = False
                parametres = True
                         
            else :
                parametres = False


        if event.type == pyg.MOUSEBUTTONDOWN and hack_running == False:
            if colvol.collidepoint(event.pos):
                volume = True
        
        if event.type == pyg.MOUSEBUTTONDOWN and volume == True:
            if colmoins.collidepoint(event.pos):
                hautvol -=1
                if hautvol > 10:
                    hautvol = 9
                if hautvol < 0 :
                    hautvol = 0
                
                volu(hautvol)
            if colplus.collidepoint(event.pos):
                hautvol +=1
                volu(hautvol)