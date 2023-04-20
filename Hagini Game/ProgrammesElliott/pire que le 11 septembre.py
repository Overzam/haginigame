from win32api import GetSystemMetrics
import pygame as pyg
import sys
import math

# Initialisation de pygame
pyg.init()

def jeu_elliott(height, width):

    #############################################################################################################
    ################################## Définition des classes et fonctions ######################################
    #############################################################################################################

    class Voiture:
        def __init__(self, start_pos, max_vel, rot_vel, img):
            self.x, self.y = start_pos
            self.max_vel = max_vel
            self.vel = 0
            self.rot_vel = rot_vel
            self.angle = 0
            self.acceleration = 0.05
            self.img = img
            
        def rotation(self, gauche=False, droite=False):
            if gauche:
                self.angle += self.rot_vel
            elif droite:
                self.angle -= self.rot_vel
            
        def draw(self, screen):
            blit_rotate_center(screen, self.img, (self.x, self.y), self.angle)
            
        def move_forward(self):
            self.vel = min(self.vel + self.acceleration, self.max_vel)
            self.move()
            
        def move_backward(self):
            self.vel = max(self.vel - self.acceleration, -self.max_vel/2)
            self.move()    
            
        def move(self):
            radian = math.radians(self.angle)
            self.x -= self.vel * math.sin(radian)
            self.y -= self.vel * math.cos(radian)
        
        def reduce_speed(self):
            self.vel = max(self.vel - self.acceleration/(3/2), 0)
            self.move()
            
        def collide(self, mask, x=0, y=0):
            voiture_mask = pyg.mask.from_surface(self.img)
            offset = (int(self.x - x), int(self.y - y))
            point_intersection = mask.overlap(voiture_mask, offset)
            return point_intersection
        
        def bounce(self):
            self.vel = -self.vel/2
            self.move()
            
    def blit_rotate_center(screen, image, top_left, angle):
    	rotated_image = pyg.transform.rotate(image, angle)
    	new_rect = rotated_image.get_rect(center=image.get_rect(topleft = top_left).center)
    	screen.blit(rotated_image, new_rect.topleft)

    # Fonction pour quitter la fenêtre et arrêter l'exécution du programme
    def quit():
        run  = False
        pyg.quit()
        sys.exit()
        
    #############################################################################################################
    ######################################### Définition des variables ##########################################
    #############################################################################################################

    # Largeur et hauteur de l'écran
    #width, height = GetSystemMetrics(0), GetSystemMetrics(1)
    #width, height = int(GetSystemMetrics(0) // 2), int(GetSystemMetrics(1) // 2)
    # Titre du jeu
    titre = 'feur'
    pyg.display.set_caption(titre)
    screen = pyg.display.set_mode((width, height))
    # Définition et affichage du fond du jeu
    background = pyg.image.load('img/testbg.png')
    background = pyg.transform.scale(background, (width, height)).convert()
    fond = background.convert()

    image = pyg.image.load('img\white-car.png')
    image = pyg.transform.scale(image, (int(15*width/1920), int(30*height/1080))).convert_alpha()
    mine_spawn_map = pyg.image.load('img\white-car.png')
    mine_spawn_map = pyg.transform.scale(mine_spawn_map, (int(15*width/1920), int(30*height/1080))).convert_alpha()
    track = pyg.image.load('img/track.png')
    track = pyg.transform.scale(track, (width, height)).convert()
    track_border = pyg.image.load('img/track-border.png')
    track_border = pyg.transform.scale(track_border, (width, height)).convert_alpha()
    track_border_mask = pyg.mask.from_surface(track_border)
    finish_line = pyg.image.load('img/finish.png')
    finish_line = pyg.transform.scale(finish_line, (int(30*width/1100), int(60*height/600))).convert_alpha()
    finish_line_mask = pyg.mask.from_surface(finish_line)
    checkpoint = pyg.image.load('img/finish.png')
    checkpoint = pyg.transform.scale(checkpoint, (int(30*width/1100), int(60*height/600))).convert_alpha()
    checkpoint_mask = pyg.mask.from_surface(checkpoint)

    player = Voiture((600*width/1920, 900*height/1080), 4, 4, image)

    screen.blit(fond, (0, 0))
    pyg.display.flip()
    key_press = [0, 0]
    checkpoint_reached = False
    lap = 0

    # Booléen dont dépend la boucle de jeu
    run = True

    #############################################################################################################
    ############################################ Boucle de jeu ##################################################
    #############################################################################################################

    while run:
        
        #print(pyg.mouse.get_pos())
        
        screen.fill((0,0,0))
        screen.blit(track, (0,0))
        screen.blit(finish_line, (800*width/1920,885*height/1080))
        screen.blit(checkpoint, (800*width/1920,140*height/1080))
        player.draw(screen)
        
        pyg.key.set_repeat(10)
        
        # Pour quitter le jeu
        for event in pyg.event.get():
            
            if event.type == pyg.QUIT:
                quit()
                
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_ESCAPE:
                    quit()
                
                if type(key_press[1]) == list:
                    last_state = key_press[1]
                else:
                    last_state = pyg.key.get_pressed()
                
                key_press = [last_state, pyg.key.get_pressed()]
                
                moved = False
                
                
                '''
                print(key_press[1][pyg.K_UP])
                '''
                if key_press[1][pyg.K_UP]:
                    
                    if key_press[1][pyg.K_RIGHT]:
                        player.rotation(droite=True)
                
                    if key_press[1][pyg.K_LEFT]:
                        player.rotation(gauche=True)
                    
                    '''
                    elif key_press[0][pyg.K_UP] and (key_press[0][pyg.K_RIGHT] or key_press[0][pyg.K_LEFT]):
                        print('feur')
                    '''   
                    moved = True
                    player.move_forward()
                
                elif key_press[1][pyg.K_DOWN]:
                        
                        if key_press[1][pyg.K_RIGHT]:
                            player.rotation(droite=True)
                    
                        if key_press[1][pyg.K_LEFT]:
                            player.rotation(gauche=True)
                            
                        moved = True
                        player.move_backward()

                else:
                    if key_press[1][pyg.K_RIGHT]:
                        player.rotation(droite=True)
                    
                    if key_press[1][pyg.K_LEFT]:
                        player.rotation(gauche=True)
                    
                    #player.vel = 0
                    player.reduce_speed()

            if player.collide(track_border_mask) is not None:
                player.bounce()
            
            if player.collide(checkpoint_mask, *(800*width/1920,140*height/1080)) is not None:
                checkpoint_reached = True
            
            point_intersection_finish = player.collide(finish_line_mask, *(800*width/1920,885*height/1080))
            if point_intersection_finish is not None:
                if point_intersection_finish[0] >= 15 and checkpoint_reached == False:
                    player.bounce()
                else:
                    checkpoint_reached = False
                    lap += 1
            
            '''
            if pyg.key.get_pressed()[pyg.K_RIGHT]:
                player.rotation(droite=True)
            
            if pyg.key.get_pressed()[pyg.K_LEFT]:
                player.rotation(gauche=True)
                
            if pyg.key.get_pressed()[pyg.K_UP]:
                moved = True
                player.move_forward()
                
            if pyg.key.get_pressed()[pyg.K_DOWN]:
                moved = True
                player.move_backward()
            
            if not moved:
                player.reduce_speed()
                
            if player.collide(track_border_mask) is not None:
                player.bounce()
            '''    
        pyg.display.flip()
        