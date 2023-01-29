from win32api import GetSystemMetrics
import pygame as pyg
import sys

# Initialisation de pygame
pyg.init()
    
#############################################################################################################
################################## Définition des classes et fonctions ######################################
#############################################################################################################

# Création de la classe Button à laquelle appartient tout bouton du menu
class Button:
    
    # Initialisation de chaque instance de cette classe
    def __init__(self, x, y, image, item_image):
        self.x = x                                  # Coordonnées
        self.y = y
        self.image = image                          # Image de la cellule
        self.item_image = item_image                # Image du sprite affiché à l'intérieur de la cellule
        self.hitbox = image.get_rect()              # Boîte de collision de la cellule
        self.hitbox.topleft = (x, y)
        self.item_hitbox = item_image.get_rect()    # Boîte de collision du sprite
        self.hover = False                          # Variable booléenne vraie si la souris est sur la cellule du bouton
        self.clicked = False                        # Variable booléenne vraie si le joueur à effectué un clic gauche sur la cellule
    
    # Méthode d'affichage du bouton
    def draw(self):
        self.item_hitbox.center = self.hitbox.center                            # On replace le sprite au centre de la cellule
        screen.blit(self.image, (self.hitbox.x, self.hitbox.y))                 # Affichage de la cellule
        screen.blit(self.item_image, (self.item_hitbox.x, self.item_hitbox.y))  # Affichage du sprite
    
    # Méthode retourant l'état du bouton (souris dessus ou non, cliqué ou non)
    def which_state(self):
        pos = pyg.mouse.get_pos()                   # Tuples contenant les coordonnées de la souris
        self.clicked = False
        if self.hitbox.collidepoint(pos):           # Si la souris se trouve dans la boîte de collision du bouton (cellule)
            self.hover = True                       # La souris est par-dessus le bouton
            self.clicked = (pyg.mouse.get_pressed()[0] and self.clicked == False)   # Est cliqué si la souris est dans la hitbox du bouton, si le clic gauche est pressé et si le bouton n'est pas déjà cliqué
            return (self.hover, self.clicked)       # Retourne le tuple d'état du bouton, soit (True, False): souris sur le bouton, soit (True, True): souris sur le bouton et le clic gauche est pressé
        return (False, False)                       # Si la souris n'est pas sur le bouton, retourne ce tuple d'état
    
    # Méthode mettant à jour un bouton (sa cellule et le sprite)
    def update(self, buttonspritelist, spritelist):
        if self.which_state()[0]:
            if self.which_state()[1]:               # Si le bouton est cliqué
                self.image = buttonspritelist[2]    # Image de la cellule quand le joueur clique dessus
                self.item_image = spritelist[2]     # Image du sprite quand le joueur clique
            else:                                   # Si la souris est sur le bouton
                self.image = buttonspritelist[1]
                self.item_image = spritelist[1]
        else:                                       # Si la souris n'est pas sur le bouton
            self.image = buttonspritelist[0]
            self.item_image = spritelist[0]
        self.draw()                                 # Affiche le bouton une fois ses sprites actualisés en fonction de son état

# Fonction mettant à jour les sprites à l'intérieur des cellules du menu
def update_all(buttonlist, spritelist, indicelist):
    if len(buttonlist) == len(indicelist):
        # Actualisation de chaque bouton et son sprite à l'aide de la méthode update() de la classe Button
        for i in range(len(buttonlist)):
            buttonlist[i].update(spritelist[0][0], spritelist[1][indicelist[i]])

# Fonction affichant tous les boutons d'une liste de boutons donnée
def draw_all(buttonlist):
    # Liste par compréhension réduisant la matrice des boutons à une liste à une seule entrée de sorte à rendre sa navigation triviale
    newbuttonlist = [i for sublist in buttonlist for i in sublist]
    # On affiche chaque bouton de la liste à l'aide de la méthode draw() de la classe Button
    for i in newbuttonlist:
        i.draw()

# Fonction pour quitter la fenêtre et arrêter l'exécution du programme
def quit():
    run  = False
    pyg.quit()
    sys.exit()

#############################################################################################################
######################################### Définition des variables ##########################################
#############################################################################################################

# 1920 = 3 * 5 * 2^7 -----> 1920/15=128 ----> 2 3 1 3 1 3 2
# 1080 = 3^3 * 2^3 * 5 ----> 1080 / 30 = 36 ---> ???
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
'''width = int(GetSystemMetrics(0) // 2)
height = int(GetSystemMetrics(1) // 2)'''

titre = 'feur'
pyg.display.set_caption(titre)
screen = pyg.display.set_mode((width, height))
'''hitbox_screen = pyg.Surface.get_rect(screen)'''
background = pyg.image.load('img/placeholder_bg.png')
background = pyg.transform.scale(background, (width, height)).convert()
fond = background.convert()
screen.blit(fond, (0, 0))
pyg.display.flip()

# Dimensions des images du menu calculées directement à partir des valeurs de largeur et de hauteur de l'écran
cell_dimensions = (width//4, height//5)
arrow_dimensions = [height // 5 - 10] * 2
arrowcell_dimensions = [i + 10 for i in arrow_dimensions]
sprite_dimensions = [i // 1.5 for i in cell_dimensions]

# Importation et transformation des images du menu
# Images des cellules
img0_1 = pyg.image.load('img/menu_cell_normal.png')
img0_1 = pyg.transform.scale(img0_1, cell_dimensions).convert_alpha()
img0_2 = pyg.image.load('img/menu_cell_hover.png')
img0_2 = pyg.transform.scale(img0_2, cell_dimensions).convert_alpha()
img0_3 = pyg.image.load('img/menu_cell_click.png')
img0_3 = pyg.transform.scale(img0_3, cell_dimensions).convert_alpha()
img0_1_alpha = pyg.transform.scale(img0_1, arrowcell_dimensions).convert_alpha()
img0_2_alpha = pyg.transform.scale(img0_2, arrowcell_dimensions).convert_alpha()
img0_3_alpha = pyg.transform.scale(img0_3, arrowcell_dimensions).convert_alpha()
# Images des sprites affichés à l'intérieur des cases
img0_4 = pyg.image.load('img/arrow.png')
img0_4 = pyg.transform.scale(img0_4, arrow_dimensions).convert_alpha()
img0_5 = pyg.transform.flip(img0_4, 1, 0)
img1_1 = pyg.image.load('img/normal.png')
img1_1 = pyg.transform.scale(img1_1, sprite_dimensions).convert_alpha()
img1_2 = pyg.image.load('img/hover.png')
img1_2 = pyg.transform.scale(img1_2, sprite_dimensions).convert_alpha()
img1_3 = pyg.image.load('img/click.png')
img1_3 = pyg.transform.scale(img1_3, sprite_dimensions).convert_alpha()
img2_1 = pyg.image.load('img/normal2.png')
img2_1 = pyg.transform.scale(img2_1, sprite_dimensions).convert_alpha()
img2_2 = pyg.image.load('img/hover2.png')
img2_2 = pyg.transform.scale(img2_2, sprite_dimensions).convert_alpha()
img2_3 = pyg.image.load('img/click2.png')
img2_3 = pyg.transform.scale(img2_3, sprite_dimensions).convert_alpha()
img3_1 = pyg.image.load('img/normal3.png')
img3_1 = pyg.transform.scale(img3_1, sprite_dimensions).convert_alpha()
img3_2 = pyg.image.load('img/hover3.png')
img3_2 = pyg.transform.scale(img3_2, sprite_dimensions).convert_alpha()
img3_3 = pyg.image.load('img/click3.png')
img3_3 = pyg.transform.scale(img3_3, sprite_dimensions).convert_alpha()
img4_1 = pyg.image.load('img/normal4.png')
img4_1 = pyg.transform.scale(img4_1, sprite_dimensions).convert_alpha()
img4_2 = pyg.image.load('img/hover4.png')
img4_2 = pyg.transform.scale(img4_2, sprite_dimensions).convert_alpha()
img4_3 = pyg.image.load('img/click4.png')
img4_3 = pyg.transform.scale(img4_3, sprite_dimensions).convert_alpha()
img5_1 = pyg.image.load('img/normal5.png')
img5_1 = pyg.transform.scale(img5_1, sprite_dimensions).convert_alpha()
img5_2 = pyg.image.load('img/hover5.png')
img5_2 = pyg.transform.scale(img5_2, sprite_dimensions).convert_alpha()
img5_3 = pyg.image.load('img/click5.png')
img5_3 = pyg.transform.scale(img5_3, sprite_dimensions).convert_alpha()

# Matrice contenant toutes les images du menu
# Rend la réaffectation d'une image suite à une intéraction du joueur facile
spritelist = [[[img0_1, img0_2, img0_3], [img0_1_alpha, img0_2_alpha, img0_3_alpha], [img0_4]*3, [img0_5]*3],
              [[img1_1, img1_2, img1_3],
              [img2_1, img2_2, img2_3],
              [img3_1, img3_2, img3_3],
              [img4_1, img4_2, img4_3],
              [img5_1, img5_2, img5_3]]]

# Indices utilisés pour la navigation à l'intérieur de la matrice des images
i, j, k = 0, 1, 2

# Création des instances boutons du menu
# Cellules qui contiennent les images des pièces du véhicule construit par le joueur
button_1 = Button(0, 0, spritelist[0][0][0], spritelist[1][i][0])
button_1.hitbox.center = width//2, height//2
button_1.x, button_1.y = button_1.hitbox.topleft
button_2 = Button(button_1.hitbox.topright[0] + 1, button_1.hitbox.topright[1], spritelist[0][0][0], spritelist[1][j][0])
button_3 = Button(button_1.hitbox.x - cell_dimensions[0] - 1, button_1.hitbox.y, spritelist[0][0][0], spritelist[1][k][0])
# Les cellules sont positionnées côte à côte de sorte à former un menu coulissant
# Flèches pour la navigation du menu
arrow_1 = Button(0, 0, spritelist[0][1][0], spritelist[0][2][0])
arrow_2 = Button(0, 0, spritelist[0][1][0], spritelist[0][3][0])
arrow_1.hitbox.center = button_2.hitbox.center[0] + ((button_2.hitbox.width + arrow_1.hitbox.width) // 2 + 1), button_2.hitbox.center[1]
arrow_2.hitbox.center = button_3.hitbox.center[0] - ((button_3.hitbox.width + arrow_2.hitbox.width) // 2 + 1), button_3.hitbox.center[1]

# Liste contenant les cellules du menu coulissant y compris les flèches
buttonlist = [[arrow_1, arrow_2], [button_3, button_1, button_2]]

# Liste d'état se trouvera lors de l'exécution sous la forme [état à l'instant t-1, état à l'instant t]
# de sorte qu'on mettra à jour l'image d'un bouton que si les deux états sont différents, c'et-àdire que le joueur à intéragit avec le bouton
# Un état à un instant t se traduit lui-même par un tuple (bouton.hover, bouton.clicked) ---> cf. définition de la classe Button au tout début du programme
# Initialisation des listes d'état de chaque bouton du menu
button_1_state, button_2_state, button_3_state, arrow_1_state, arrow_2_state = [0,0], [0,0], [0,0], [0,0], [0,0]

# Booléen dont dépend la boucle de jeu
run = True

#############################################################################################################
############################################ Boucle de jeu ##################################################
#############################################################################################################

while run:
    
    # Fond blanc (pour l'instant)
    screen.fill((255, 255, 255))
    
    # On actualise les listes d'état de chaque bouton à l'aide de la méthode which_state() de la classe Button, qui retourne l'état à l'instant t
    button_1_state, button_2_state, button_3_state, arrow_1_state, arrow_2_state = [button_1_state[1], button_1.which_state()], [button_2_state[1], button_2.which_state()], [button_3_state[1], button_3.which_state()], [arrow_1_state[1], arrow_1.which_state()], [arrow_2_state[1], arrow_2.which_state()]
    
    # On affiche tous les boutons du menu
    draw_all(buttonlist)
    
    # On actualise l'image de la flèche si son état change (= si le joueur intéragit avec le bouton)
    if arrow_1_state[0] != arrow_1_state[1]:
        arrow_1.update(spritelist[0][1], spritelist[0][2])
        # Roulement des sprites des cellules du menu si le joueur clique sur une des flèches
        if arrow_1.clicked:
            # Actualisation des indices
            # Indice = (indice incrémenté/décrémenté) modulo le nombre d'image dans le menu coulissant
            # de sorte qu'on pourra passer dans la matrice de l'objet de positon 4 à 0 et inversement de 0 à 4 == il y a un enroulement, le menu n'a ni début ni fin
            i, j, k = (i+1) % len(spritelist[1]), (j+1) % len(spritelist[1]), (k+1) % len(spritelist[1])
            # Roulement des sprites en actualisant chaque cellule contenant un sprite
            update_all(buttonlist[1], spritelist, [i, j, k])
    if arrow_2_state[0] != arrow_2_state[1]:
        arrow_2.update(spritelist[0][1], spritelist[0][3])
        if arrow_2.clicked:
            i, j, k = (i-1) % len(spritelist[1]), (j-1) % len(spritelist[1]), (k-1) % len(spritelist[1])
            update_all(buttonlist[1], spritelist, [i, j, k])
    
    # Actualisation d'un bouton si le joueur intéragit avec (il passe la souris dessus et/ou clique ou enlève sa souris)
    if button_3_state[0] != button_3_state[1]:
        button_3.update(spritelist[0][0], spritelist[1][i])
    if button_1_state[0] != button_1_state[1]:
        button_1.update(spritelist[0][0], spritelist[1][j])
    if button_2_state[0] != button_2_state[1]:
        button_2.update(spritelist[0][0], spritelist[1][k])
    
    
    #pyg.key.set_repeat(10)
    
    for event in pyg.event.get():
        
        if event.type == pyg.QUIT:
            quit()
            
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_ESCAPE:
                quit()

    pyg.display.flip()