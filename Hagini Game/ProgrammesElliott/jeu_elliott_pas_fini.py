# Importation des bibliothèques
from win32api import GetSystemMetrics
import pygame as pyg
import sys
import math

# Initialisation de pygame
pyg.init()

# Initialisation du module font de pygame
pyg.font.init()

# Création de l'objet horloge, outil temporel de pygame
pyg.time.Clock()

def jeu_elliott(width, height):
    # Temps en millisecondes après l'initialisation de pygame au début du lancement du programme
    # Servira pour des calculs de durée
    start_ticks = pyg.time.get_ticks()
    
    #############################################################################################################
    ################################## Définition des classes et fonctions ######################################
    #############################################################################################################
    
    # Classe tank, dont l'avatar est l'instanciation
    class Tank:
        
        # Initialisation de chaque instance de cette classe
        def __init__(self, start_position=tuple, max_speed=int, rotation_speed=int, img=pyg.Surface):
            self.x, self.y = start_position
            self.max_speed = max_speed
            self.speed = 0
            self.rotation_speed = rotation_speed
            self.angle = -90
            self.acceleration = 0.05
            self.img = img
            
            ''' points de vie du vehicule '''
            
        # Pour afficher le tank à l'écran
        def draw(self, screen):
            blit_rotate_center(screen, self.img, (self.x, self.y), self.angle)
        
        # Pour faire tourner le tank sur lui-même
        def rotation(self, left=False, right=False):
            if left:
                self.angle += self.rotation_speed
            elif right:
                self.angle -= self.rotation_speed
        
        # Vitesse quand le tank avance
        def move_forward(self):
            self.speed = min(self.speed + self.acceleration, self.max_speed)
            self.move()
        
        # Vitesse quand le tank recule
        def move_backward(self):
            self.speed = max(self.speed - self.acceleration, -self.max_speed/2)
            self.move()    
        
        # Mouvement du tank selon sa vitesse
        def move(self):
            radian = math.radians(self.angle)
            self.x -= self.speed * math.sin(radian)
            self.y -= self.speed * math.cos(radian)
        
        # Ralentit progressivement si le bouton avancer est relâché
        def brake(self):
            self.speed = max(self.speed - self.acceleration/(3/2), 0)
            self.move()
        
        # Rebondit si le tank percute un rebord de la piste
        def bounce(self):
            self.speed = -self.speed/2
            self.move()
        
        # Collision au pixel près
        def collide(self, mask, x=0, y=0):
            voiture_mask = pyg.mask.from_surface(self.img)
            offset = (int(self.x - x), int(self.y - y))
            point_intersection = mask.overlap(voiture_mask, offset)
            return point_intersection
    
    # Classe explosion de jeu_1 dans Hagini Sauce
    class explo(pyg.sprite.Sprite):
        def __init__(self, pos_x, pos_y):
            super().__init__()
            self.sprites = []
            self.is_animating = False
            vide = pyg.image.load('img/transpar.png')
            explo1 = pyg.image.load('img/explosion-frame-1.png')
            explo1 = pyg.transform.scale(explo1, (x_explo - 5, y_explo - 5))
            explo2 = pyg.image.load('img/explosion-frame-2.png')
            explo2 = pyg.transform.scale(explo2, (x_explo, y_explo))
            explo3 = pyg.image.load('img/explosion-frame-3.png')
            explo3 = pyg.transform.scale(explo3, (x_explo, y_explo))
            explo4 = pyg.image.load('img/explosion-frame-4.png')
            explo4 = pyg.transform.scale(explo4, (x_explo, y_explo))
            explo5 = pyg.image.load('img/explosion-frame-5.png')
            explo5 = pyg.transform.scale(explo5, (x_explo, y_explo))
            explo6 = pyg.image.load('img/explosion-frame-6.png')
            explo6 = pyg.transform.scale(explo6, (x_explo, y_explo))
            explo7 = pyg.image.load('img/explosion-frame-7.png')
            explo7 = pyg.transform.scale(explo7, (x_explo, y_explo))
            explo8 = pyg.image.load('img/explosion-frame-8.png')
            explo8 = pyg.transform.scale(explo8, (x_explo, y_explo))
            self.sprites.append(vide)
            self.sprites.append(explo1)
            self.sprites.append(explo2)
            self.sprites.append(explo3)
            self.sprites.append(explo4)
            self.sprites.append(explo5)
            self.sprites.append(explo6)
            self.sprites.append(explo7)
            self.sprites.append(explo8)
            self.current_sprite = 0
            self.image = self.sprites[self.current_sprite]
            self.rect = self.image.get_rect()
            self.rect.topleft = [pos_x, pos_y]
    
        def animate(self):
            self.is_animating = True
    
        def update(self, vitesse):
            if self.is_animating:
                self.current_sprite += vitesse
    
                if self.current_sprite >= len(self.sprites):
                    self.current_sprite = 0
                    self.is_animating = False
    
                self.image = self.sprites[int(self.current_sprite)]
    
    # Rotation d'une image sans distorsion à l'affichage
    def blit_rotate_center(screen, image, top_left, angle):
    	rotated_image = pyg.transform.rotate(image, angle)
    	new_rect = rotated_image.get_rect(center=image.get_rect(topleft = top_left).center)
    	screen.blit(rotated_image, new_rect.topleft)
    
    # Dessine toutes les mines
    def mine_draw(minelist, img):
        for mine in minelist:
            screen.blit(img, mine)
    
    # Collision entre le tank et les mines
    def mine_collide(minelist, tank, mine_mask):
        tank_mask = pyg.mask.from_surface(tank.img)
        for mine in minelist:
            offset = (int(tank.x - mine[0]), int(tank.y - mine[1]))
            if mine_mask.overlap(tank_mask, offset):
                # Animation d'explosion quand collison
                ''' ne fonctionne pas '''
                anim_explo = pyg.sprite.Group()
                explosion = explo(tank.x, tank.y)
                anim_explo.add(explosion)
                explosion.animate()
                anim_explo.draw(screen)
                anim_explo.update(0.35)
        return minelist
    
    # Fonction pour quitter la fenêtre et arrêter l'exécution du programme
    def quit():
        run  = False
        pyg.quit()
        sys.exit()
        
    #############################################################################################################
    ######################################### Définition des variables ##########################################
    #############################################################################################################
    
    font = pyg.font.Font('freesansbold.ttf', 32)    # Police pour le texte du jeu
    blanc, noir = (255,255,255), (0,0,0)            # Couleurs
    
    # Largeur et hauteur de l'écran
    #width, height = GetSystemMetrics(0), GetSystemMetrics(1)
    #width, height = int(GetSystemMetrics(0) // 2), int(GetSystemMetrics(1) // 2)
    # Titre du jeu
    titre = 'feur'
    pyg.display.set_caption(titre)
    screen = pyg.display.set_mode((width, height))
    # Définition du fond du jeu (pas utilisé)
    background = pyg.image.load('img/testbg.png')
    background = pyg.transform.scale(background, (width, height)).convert()
    fond = background.convert()
    # Affichage du fond
    screen.blit(fond, (0, 0))
    pyg.display.flip()
    # Chargement des sprites et création des masques pour les collisions de certains
    image = pyg.image.load('img/tank2.png')
    image = pyg.transform.scale(image, (int(30*width/1920), int(60*height/1080))).convert_alpha()
    mine_spawn_map = pyg.image.load('img/crosshair_spawn.png')
    mine_spawn_map = pyg.transform.scale(mine_spawn_map, (width, height)).convert_alpha()
    track = pyg.image.load('img/track.png')
    track = pyg.transform.scale(track, (width, height)).convert()
    track_border = pyg.image.load('img/track-border2.png')
    track_border = pyg.transform.scale(track_border, (width, height)).convert_alpha()
    track_border_mask = pyg.mask.from_surface(track_border)
    finish_line = pyg.image.load('img/finish.png')
    finish_line = pyg.transform.scale(finish_line, (int(30*width/1100), int(60*height/600))).convert_alpha()
    finish_line_mask = pyg.mask.from_surface(finish_line)
    checkpoint = pyg.image.load('img/finish.png')
    checkpoint = pyg.transform.scale(checkpoint, (int(30*width/1100), int(60*height/600))).convert_alpha()
    checkpoint_mask = pyg.mask.from_surface(checkpoint)
    crosshair = pyg.image.load('img/crosshair.png')
    crosshair = pyg.transform.scale(crosshair, (50, 50)).convert_alpha()
    crosshair_mask = pyg.mask.from_surface(crosshair)
    
    # Création de l'instance joueur de la classe Tank
    player = Tank((1000*width/1920, 900*height/1080), 4, 2, image)
    
    # Définiton de l'animation d'explosion
    x_explo = 100
    y_explo = 100
    anim_explo = pyg.sprite.Group()
    explosion = explo(player.x, width - 300)
    anim_explo.add(explosion)
    
    # Tableau d'inputs
    key_press = [0, 0]
    # Booléen vrai si le checkpoint (non affiché) a été atteint
    # Force à faire le tour du circuit pour faire un tour
    checkpoint_reached = False
    # Nombres de tours effectués et à faire
    lap = 0
    lap_goal = 3
    # Liste contnant les coordonnées de toutes les mines
    minelist = [[318,530],[415,480],[522,530],[619,480]]
    minelist = [[width*i[0]/1100, height*i[1]/600] for i in minelist]
    '''print(minelist)'''
    
    # Booléen dont dépend la boucle de jeu
    run = True
    
    #############################################################################################################
    ############################################ Boucle de jeu ##################################################
    #############################################################################################################
    
    while run:
        
        # Décompte
        countdown = round(90 - ((pyg.time.get_ticks() - start_ticks) / 1000))
        print_countdown = font.render(str(countdown), True, blanc, noir)
        print_lap = font.render(str(lap)+'/'+str(lap_goal), True, blanc, noir)
        
        # Affichage du fond et des objets par-dessus
        screen.blit(track, (0,0))
        screen.blit(finish_line, (800*width/1920,885*height/1080))
        screen.blit(print_countdown, (width/2 - 100,0))
        screen.blit(print_lap, (width/2 + 10, 0))
        '''mine_draw(minelist, crosshair)'''
        #Affichage du joueur
        player.draw(screen)
        
        # Affichag de l'animation d'explosion
        anim_explo.draw(screen)
        anim_explo.update(0.30)
        pyg.display.update()
        
        # Un input maintenu se répète, garantit un mouvement fluide sauf sur les pc de la salle de NSI qui sont salement lents
        pyg.key.set_repeat(10)
        
        '''mine_collide(minelist, player, crosshair_mask)'''
        
        for event in pyg.event.get():
            
            # Pour quitter le jeu
            if event.type == pyg.QUIT:
                quit()
                
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_ESCAPE:
                    quit()
                
                if type(key_press[1]) == list:
                    last_state = key_press[1]
                else:
                    last_state = pyg.key.get_pressed()
                
                # Tableau des inputs
                key_press = [last_state, pyg.key.get_pressed()]
                
                # Avancer
                if key_press[1][pyg.K_UP] or key_press[1][pyg.K_z]:
                    
                    # Tourner et avancer en meme temps
                    if key_press[1][pyg.K_RIGHT] or key_press[1][pyg.K_d]:
                        player.rotation(right=True)
                
                    if key_press[1][pyg.K_LEFT] or key_press[1][pyg.K_q]:
                        player.rotation(left=True)
                    
                    player.move_forward()
                
                # Reculer
                elif key_press[1][pyg.K_DOWN] or key_press[1][pyg.K_s]:
                        
                        # Tourner et reculer en meme temps
                        if key_press[1][pyg.K_RIGHT] or key_press[1][pyg.K_d]:
                            player.rotation(right=True)
                    
                        if key_press[1][pyg.K_LEFT] or key_press[1][pyg.K_q]:
                            player.rotation(left=True)
                            
                        player.move_backward()
                        
                # Ralentit
                else:
                    
                    # Tourne en ralentissant ou à l'arret
                    if key_press[1][pyg.K_RIGHT] or key_press[1][pyg.K_d]:
                        player.rotation(right=True)
                    
                    if key_press[1][pyg.K_LEFT] or key_press[1][pyg.K_q]:
                        player.rotation(left=True)
                        
                    player.brake()
                
            # Si le joueur touche la bordure il rebondit
            if player.collide(track_border_mask) is not None:
                player.bounce()
            
            # S'il atteint le checkpoint
            if player.collide(checkpoint_mask, *(800*width/1920,140*height/1080)) is not None:
                checkpoint_reached = True
            
            # Tour compté s'il atteint la ligne d'arrivée et a visité le checkpoint
            if player.collide(finish_line_mask, *(800*width/1920,885*height/1080)) and checkpoint_reached == True:
                lap += 1
                checkpoint_reached = False
            
            ''' condition de victoire non implémentée '''
            if lap == lap_goal:
                pass
                #win()
            
        pyg.display.flip()