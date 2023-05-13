from win32api import GetSystemMetrics
import pygame as pyg
import sys
import math
from pygame import mixer

# variables globales
global width, height
global x_scale, y_scale
global x_explo, y_explo
global start_ticks

pyg.init()

bruit_voiture = pyg.mixer.Sound('jeu/son/bruit_voiture.wav')

def jeu_tank():
    
    from Bury import cour_bas
    
    # Initialisation de pygame
    pyg.init()
    
    # Initialisation du module font de pygame
    pyg.font.init()
    
    # Création de l'objet horloge, outil temporel de pygame
    clock = pyg.time.Clock()
    # Temps en millisecondes après l'initialisation de pygame au début du lancement du programme
    # Servira pour des calculs de durée
    start_ticks = pyg.time.get_ticks()
    
    #############################################################################################################
    ################################## Définition des classes et fonctions ######################################
    #############################################################################################################
    
    # Classe tank, dont l'avatar est l'instanciation
    class Tank:
        
        # Initialisation de chaque instance de cette classe
        def __init__(self, start_position=tuple, rotation_speed=int, img=pyg.Surface, pv=int):
            self.x, self.y = start_position
            self.rotation_speed = rotation_speed
            self.angle = -90
            self.img = img
            self.pv = pv
        
        # Affiche le tank à l'écran
        def draw(self, screen):
            return blit_rotate_center(screen, self.img, (self.x, self.y), self.angle)
        
        # Fait tourner le tank sur lui-même
        def rotation(self, left=False, right=False):
            if left:
                self.angle += self.rotation_speed
            elif right:
                self.angle -= self.rotation_speed
    
    # Classe du circuit du jeu / fond d'écran
    class Background:
        
        # Initialisation
        def __init__(self, start_position=tuple, max_speed=int, rotation_speed=int, img=pyg.Surface, border_img_mask=pyg.Surface):
            self.x, self.y = start_position
            # C'est le circuit qui bouge au lieu du véhicule pour donner l'impression de scrolling
            self.max_speed = max_speed
            self.speed = 0
            self.rotation_speed = rotation_speed
            self.angle = 180
            self.acceleration = 0.05
            # Définition de l'image
            self.img = img
            # Définition du masque des contours du circuit qui servira pour le système de collision
            self.border_img_mask = border_img_mask
            self.center = self.img.get_rect().center
        
        # Méthode d'affichage
        def draw(self, screen):
            screen.blit(self.img, (self.x, self.y))
        
        # Angle du scrolling modifié quand le joueur tourne
        def rotation(self, left=False, right=False):
            if left:
                self.angle += self.rotation_speed
            elif right:
                self.angle -= self.rotation_speed
        
        # Vitesse du scrolling quand le joueur avance
        def move_forward(self):
            self.speed = max(self.speed - self.acceleration, -self.max_speed/2)
            self.move()
        
        # Vitesse du scrolling quand le joueur recule
        def move_backward(self):
            self.speed = min(self.speed + self.acceleration, self.max_speed)
            self.move()    
        
        # Scrolling
        def move(self):
            bruit_voiture.play()
            radian = math.radians(self.angle)
            self.x -= self.speed * math.sin(radian)
            self.y -= self.speed * math.cos(radian)
        
        # Ralentit progressivement si le bouton avancer est relâché
        def brake(self):
            bruit_voiture.stop()
            self.speed = max(self.speed - self.acceleration/2, 0)
            self.move()
        
        # Rebondit si le tank percute un rebord de la piste
        def bounce(self):
            self.speed = -self.speed / 2
            self.move()
    
    # Classe définissant chaque objet du jeu avec lequel on peut intéragir (checkpoint, mine, bordure du circuit)
    # Classe fourre-tout et donc assez peu cohérente (les checkpoints ont un attribut qui pourrait les faire exploser)...
    # ... mais j'ai plus vraiment le temps pour faire une abstract class ou je ne sais quoi
    class Prop:
        
        # Initialisation
        def __init__(self, position=tuple, img=pyg.Surface, interaction=tuple):
            self.x, self.y = position
            self.img = img
            self.mask = pyg.mask.from_surface(self.img)
            # si c'est un checkpoint, s'il fait rebondir au contact, s'il peut exploser, s'il est visible, l'index du trigger qui le fait s'afficher s'il en a un
            self.is_trigger, self.can_bounce, self.can_explode, self.visible, self.trigger_index = interaction
            # s'il a été atteint, s'il a explosé
            self.triggered, self.exploded = False, False
            # masque de l'image pour les collisions
            self.mask = pyg.mask.from_surface(self.img)
        
        # Affichage si l'objet est visible
        def draw(self, background):
            if self.visible:
                screen.blit(self.img, (self.x + background.x, self.y + background.y))
        
        # Collision du joueur avec l'objet
        def collide(self, player, background):
            player_mask = pyg.mask.from_surface(player.img)
            offset = (int(self.x + background.x - player.x), int(self.y + background.y - player.y))
            # Conséquence de l'intéraction
            if player_mask.overlap(self.mask, offset):
                # Checkpoint atteint
                if self.is_trigger:
                    self.triggered = True
                # fait rebondir
                if self.can_bounce:
                    background.bounce()
                # explose
                if self.can_explode:
                    self.exploded = True
        
        # Activation d'une mine
        def activate(self):
            self.can_bounce = True
            self.can_explode = True
            self.visible = True
            self.trigger_index = None
        
        # Désactivation d'une mine
        def deactivate(self):
            self.can_bounce = False
            self.can_explode = False
            self.visible = False
    
    
    # Classe de navigation de tous les objets du jeu nn joueurs
    class AllProps:
        
        # Initialisation
        def __init__(self, proplist=list):
            # On créé à partir de la liste donnée toutes les instances objet
            self.proplist = [Prop(i[0], i[1], i[2]) for i in proplist]
            # liste des non explosifs
            self.permanentlist = [prop for prop in self.proplist if prop.trigger_index == None]
            # liste des mines
            self.minelist = [prop for prop in self.proplist if prop.trigger_index != None]
            # dictionnaire des mines selon leurs triggers
            self.trigger_navigation_dict = {self.permanentlist[i]: [j for j in self.minelist if j.trigger_index == i] for i in range(len(self.permanentlist))}
            # liste des objets supprimés (mines explosées ou désactivées définitivement)
            self.delete = []
        
        # Affiche tous les objets du jeu
        def draw_all(self, background):
            for prop in self.proplist:
                prop.draw(background)
        
        # Collisions entre le joueur et tous les objets
        def collide_all(self, player, background):
            for prop in self.proplist:
                prop.collide(player, background)
        
        # Activation des mines selon le trigger activé
        def mine_trigger(self):
            for trigger in self.trigger_navigation_dict.keys():
                if trigger.triggered:
                    for mine in self.trigger_navigation_dict[trigger]:
                        mine.activate()
        
        # Désactivation une fois qu'un autre checkpoint est passé
        def mine_disengage(self):
            for trigger_index in range(len(self.permanentlist)):
                if self.permanentlist[trigger_index].triggered and self.permanentlist[trigger_index - 1].triggered:
                    past_trigger = self.permanentlist[trigger_index - 1]
                    for mine in self.trigger_navigation_dict[past_trigger]:
                        mine.deactivate()
    
    
    # Classe de l'animation d'explosion de jeu_1 dans Hagini Sauce
    class explo(pyg.sprite.Sprite):
        def __init__(self, pos_x, pos_y):
            super().__init__()
            self.sprites = []
            self.is_animating = False
            vide = pyg.image.load('img/transpar.png')
            explo1 = pyg.image.load('img/explosion-frame-1.png')
            explo1 = pyg.transform.scale(explo1, (x_explo - 5, y_explo - 5)).convert_alpha()
            explo2 = pyg.image.load('img/explosion-frame-2.png')
            explo2 = pyg.transform.scale(explo2, (x_explo, y_explo)).convert_alpha()
            explo3 = pyg.image.load('img/explosion-frame-3.png')
            explo3 = pyg.transform.scale(explo3, (x_explo, y_explo)).convert_alpha()
            explo4 = pyg.image.load('img/explosion-frame-4.png')
            explo4 = pyg.transform.scale(explo4, (x_explo, y_explo)).convert_alpha()
            explo5 = pyg.image.load('img/explosion-frame-5.png')
            explo5 = pyg.transform.scale(explo5, (x_explo, y_explo)).convert_alpha()
            explo6 = pyg.image.load('img/explosion-frame-6.png')
            explo6 = pyg.transform.scale(explo6, (x_explo, y_explo)).convert_alpha()
            explo7 = pyg.image.load('img/explosion-frame-7.png')
            explo7 = pyg.transform.scale(explo7, (x_explo, y_explo)).convert_alpha()
            explo8 = pyg.image.load('img/explosion-frame-8.png')
            explo8 = pyg.transform.scale(explo8, (x_explo, y_explo)).convert_alpha()
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
    
    # Deux fonctions convertissent les coordonnées, longueurs et largeur par rapport à la taille de l'écran/fenetre de jeu
    def scale_x(n=int):
        return int(n * x_scale)
    
    def scale_y(n=int):
        return int(n * y_scale)
    
    # Fonction pour quitter la fenêtre et arrêter l'exécution du programme
    def quit():
        run = False
        bruit_voiture.stop()
        cour_bas('Jeu Tank')
        
    #############################################################################################################
    ######################################### Définition des variables ##########################################
    #############################################################################################################
    
    font = pyg.font.Font('jeu/assets/Little_days.ttf', 32)    # Police pour le texte du jeu
    blanc, noir = (255,255,255), (0,0,0)            # Couleurs
    
    # Largeur et hauteur de l'écran
    scale = 2
    width, height = int(GetSystemMetrics(0) // scale), int(GetSystemMetrics(1) // scale)
    x_scale, y_scale = width / 1536, height / 864
    # Titre du jeu
    titre = 'Latour de Pise'
    pyg.display.set_caption(titre)
    screen = pyg.display.set_mode((width, height))
    # Définition du fond du jeu (pas utilisé)
    background = pyg.image.load('img/background.png')
    background = pyg.transform.scale(background, (width, height)).convert()
    fond = background.convert()
    # Affichage du fond
    screen.blit(fond, (0, 0))
    pyg.display.flip()
    # Chargement des sprites
    tank = pyg.image.load('img/tank2.png')
    tank = pyg.transform.scale(tank, (scale_y(48), scale_x(24))).convert_alpha()
    track = pyg.image.load('img/track.png')
    track = pyg.transform.scale(track, (scale_x(2560), scale_y(4040))).convert()
    track_border = pyg.image.load('img/track_border.png')
    track_border = pyg.transform.scale(track_border, (scale_x(2560), scale_y(4040))).convert_alpha()
    track_border_mask = pyg.mask.from_surface(track_border)
    checkpoint = pyg.image.load('img/finish.png')
    checkpoint = pyg.transform.scale(checkpoint, (scale_x(50), scale_y(250))).convert_alpha()
    checkpoint_horizontal = pyg.transform.rotate(checkpoint, 90)
    checkpoint_horizontal_1 = pyg.transform.scale(checkpoint_horizontal, (scale_x(240), scale_y(50))).convert_alpha()
    checkpoint_horizontal_2 = pyg.transform.scale(checkpoint_horizontal, (scale_x(210), scale_y(50))).convert_alpha()
    checkpoint_horizontal_3 = pyg.transform.scale(checkpoint_horizontal, (scale_x(600), scale_y(50))).convert_alpha()
    crosshair = pyg.image.load('img/crosshair.png')
    crosshair = pyg.transform.scale(crosshair, (scale_x(50), scale_y(50))).convert_alpha()
    
    # Initialisation de l'explosion
    x_explo, y_explo = scale_x(100), scale_y(100)
    anim_explo = pyg.sprite.Group()
    explosion = explo(0, 0)
    anim_explo.add(explosion)
    
    # Création de l'instance joueur de la classe Tank
    player = Tank((width/2, height/2), 2, tank, 50)
    
    # Création de l'instance fond d'écran/circuit
    x_offset, y_offset = scale_x(-1240), scale_y(-3320)
    circuit = Background((x_offset, y_offset), 6 / scale, 2, track, track_border_mask)
    
    # coordonnées de chaque cible ong fr
    a = ((1905,3060),(1960,2890),(1870,2780),(1990,2705),(1830,2605),(1930,2540),(1790,2440))
    b = ((2005,1560),(2195,1435),(2070,1360),(2180,1265),(2320,1210),(2245,1060),(2360,955))
    c = ((2120,420),(2035,380),(2105,320),(2010,290),(1960,210),(1910,290),(1875,220),(1860,600),(1790,660),(1750,745),(1530,750),(1490,825),(1410,870),(1435,1000),(1335,1040),(1295,1130),(1100,1270),(1040,1350),(950,1375),(1190,1410),(1100,1455),(1065,1550))
    d = ((1225,330),(1080,310),(910,290),(1010,420),(855,400),(730,360),(790,550),(660,535),(550,505),(640,670),(515,670),(535,805),(620,165),(390,185),(420,275),(260,255),(325,395),(195,415),(225,570),(170,710),(305,1030),(395,1055),(330,1195),(450,1270),(440,1380),(560,1400),(650,1510))
    e = ((870,1750),(920,1875),(840,1975),(720,2015),(1135,1760),(1155,1885),(1135,2000),(1090,2100),(1000,2165),(880,2180),(750,2170),(435,2190),(330,2270),(290,2380),(380,2495),(290,2090),(170,2215),(105,2350),(110,2480),(175,2580),(300,2637))
    f = ((1095,2455),(1115,2545),(1220,2575),(1195,2675),(1280,2750),(1200,2805),(1250,2905),(1170,2925),(1130,3030),(1045,3020),(965,3080),(490,2975),(380,3055),(315,3180),(400,3300),(515,3350),(640,3390),(715,3485),(790,3610),(615,3105),(610,3215),(715,3280),(830,3327),(925,3400),(935,3520),(930,3650))
    
    # Tableau d'objets
    objets = [[[[0,0],track_border,(0,1,0,0,None)],
              [[1908, 3765], checkpoint_horizontal_1,(1,0,0,1,None)],
              [[1570,2050],checkpoint_horizontal_3,(1,0,0,0,None)],
              [[1990, 730], checkpoint_horizontal_3,(1,0,0,0,None)],
              [[1530, 100], checkpoint,(1,0,0,0,None)],
              [[610, 1660], checkpoint_horizontal_3,(1,0,0,0,None)],
              [[650, 2450], checkpoint,(1,0,0,0,None)],
              [[762, 3765], checkpoint_horizontal_2,(1,0,0,1,None)]],
              [[[i[0], i[1]], crosshair, (0,0,0,0,1)] for i in a],
              [[[i[0], i[1]], crosshair, (0,0,0,0,2)] for i in b],
              [[[i[0], i[1]], crosshair, (0,0,0,0,3)] for i in c],
              [[[i[0], i[1]], crosshair, (0,0,0,0,4)] for i in d],
              [[[i[0], i[1]], crosshair, (0,0,0,0,5)] for i in e],
              [[[i[0], i[1]], crosshair, (0,0,0,0,6)] for i in f]]
    objets = [i for sublist in objets for i in sublist]
    objets = [[[scale_x(i[0][0]), scale_y(i[0][1])], i[1], i[2]] for i in objets]
    # Création de l'instance du groupe d'objets
    objets = AllProps(objets)
    
    # Touches maintenues ou non
    up_down, down_down, left_down, right_down = False, False, False, False
    
    # Booléen dont dépend la boucle de jeu
    run = True
    
    #############################################################################################################
    ############################################ Boucle de jeu ##################################################
    #############################################################################################################
    
    while run:
        
        # maximum de 120 fps parce que l'animation d'explosion accélérait le jeu
        clock.tick(120)
        
        # compte à rebours et affichage
        countdown = round(30 - ((pyg.time.get_ticks() - start_ticks) / 1000), 1)
        print_countdown = font.render(str(countdown)+'s', True, blanc, noir)
        print_pv = font.render('PV: '+str(player.pv), True, blanc, noir)
        # pour débugger
        '''
        print_speed = font.render(str(round(circuit.speed, 1)), True, blanc, noir)
        print_fps = font.render(str(round(clock.get_fps(), 1)), True, blanc, noir)
        '''
        
        # Affichage du fond et des objets par-dessus
        circuit.draw(screen)
        objets.draw_all(circuit)
        #Affichage de l'interface
        screen.blit(print_countdown, (scale_x(width/2 - 100), 0))
        screen.blit(print_pv, (scale_x(width/2 + 100), 0))
        '''
        screen.blit(print_speed, (scale_x(width/2 + 100), 0))
        screen.blit(print_fps, (0, 0))
        '''
        
        #Affichage du joueur
        player.draw(screen)
        
        
        for event in pyg.event.get():
            
            # Pour quitter le jeu
            if event.type == pyg.QUIT:
                quit()
            
            # touches maintenues
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_ESCAPE:
                    quit()
                if event.key == pyg.K_UP or event.key == pyg.K_z:
                    up_down = True
                if event.key == pyg.K_DOWN or event.key == pyg.K_s:
                    down_down = True
                if event.key == pyg.K_RIGHT or event.key == pyg.K_d:
                    right_down = True
                if event.key == pyg.K_LEFT or event.key == pyg.K_q:
                    left_down = True
            
            # touches relachées
            if event.type == pyg.KEYUP:
                if event.key == pyg.K_UP or event.key == pyg.K_z:
                    up_down = False
                if event.key == pyg.K_DOWN or event.key == pyg.K_s:
                    down_down = False
                if event.key == pyg.K_RIGHT or event.key == pyg.K_d:
                    right_down = False
                if event.key == pyg.K_LEFT or event.key == pyg.K_q:
                    left_down = False
        
        # Mouvement selon input
        
        # avance
        if up_down:
            
            #tourne à droite
            if right_down:
                circuit.rotation(right=True)
                player.rotation(right=True)
            
            # tourne à gauche
            elif left_down:
                circuit.rotation(left=True)
                player.rotation(left=True)
            
            # le fond d'écran recule quand le joueur avance
            circuit.move_backward()
        
        # recule
        elif down_down:
            
            if right_down:
                circuit.rotation(right=True)
                player.rotation(right=True)
                
            elif left_down:
                circuit.rotation(left=True)
                player.rotation(left=True)
                
            # le fond d'écran avance quand le joueur recule
            circuit.move_forward()
        
        # freine
        else:
            
           if right_down:
               circuit.rotation(right=True)
               player.rotation(right=True)
               
           elif left_down:
               circuit.rotation(left=True)
               player.rotation(left=True)
               
           circuit.brake()
        
        # Activation des mines
        objets.mine_trigger()
        # Désenclenchement des mines
        objets.mine_disengage()
        
        boum = None
        # Collisions
        objets.collide_all(player, circuit)
        for i in range(len(objets.proplist)):
            # Animation d'explosion
            if objets.proplist[i].exploded == True:
                boum = i
                player.pv -= 5
                x_anim = player.img.get_width() + player.x - x_explo
                y_anim = player.img.get_height() + player.y - y_explo
                anim_explo = pyg.sprite.Group()
                explosion = explo(x_anim+30, y_anim)
                anim_explo.add(explosion)
                explosion.animate()
                anim_explo.draw(screen)
                anim_explo.update(0.10)
        # On retire la mine du tableau
        if boum != None:
            objets.delete.append(objets.proplist.pop(boum))
        
        if countdown == 0 or player.pv <= 0:
            quit()
            '''
            DEFAITE
            '''
        if objets.proplist[7].triggered:
            quit()
            '''
            VICTOIRE
            '''
        
        # animation de l'explosion
        anim_explo.draw(screen)
        anim_explo.update(0.10)
        
        # mise à jour de l'affichage de la fenêtre
        pyg.display.flip()
        pyg.display.update()