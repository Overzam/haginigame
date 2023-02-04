from win32api import GetSystemMetrics
import pygame as pyg
import sys

global width
global height

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
        self.statelist = [0, 0]                     # Initialisation de la liste d'état du bouton

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
    
    # Actualisation de a liste d'état du bouton
    def update_statelist(self):
        # La liste d'état se trouve sous la forme [état à l'instant t-1, état à l'instant t], de sorte qu'on mettra à jour l'image d'un bouton que si les deux états sont différents, c'est-à-dire que si le joueur à intéragit avec le bouton
        # Un état à un instant t se traduit lui-même par un tuple (bouton.hover, bouton.clicked), obtenu avec la méthode which_state()
        self.statelist = [self.statelist[1], self.which_state()]
    
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



class Menu:
    
    # Initialisation de chaque instance de cette classe
    def __init__(self, y, spritelist):
        self.y = y                          # Hauteur du menu à l'écran
        self.spritelist = spritelist        # Importation de la matrice contenant tous les sprites du menu
        self.i, self.j, self.k = 0, 1, 2    # Indices utilisés pour la navigation à l'intérieur de la matrice des sprites
        # Création des instances boutons du menu
        # Cellules qui contiennent les images des pièces du véhicule construites par le joueur
        self.bouton_centre = Button(width // 2 - spritelist[0][0][0].get_rect().width // 2, y - spritelist[0][0][0].get_rect().height // 2, spritelist[0][0][0], spritelist[1][self.j][0])
        self.bouton_gauche = Button(self.bouton_centre.hitbox.topleft[0] - (spritelist[0][0][0].get_rect().width + 1), self.bouton_centre.hitbox.topleft[1], spritelist[0][0][0], spritelist[1][self.i][0])
        self.bouton_droit = Button(self.bouton_centre.hitbox.topright[0] + 1, self.bouton_centre.hitbox.topright[1], spritelist[0][0][0], spritelist[1][self.k][0])
        # Les cellules sont positionnées côte à côte de sorte à former un menu coulissant
        # Flèches pour la navigation du menu
        self.fleche_gauche = Button(self.bouton_gauche.hitbox.topleft[0] - (spritelist[0][1][0].get_rect().width + 1), self.bouton_gauche.hitbox.topleft[1], spritelist[0][1][0], spritelist[0][2][0])
        self.fleche_droite = Button(self.bouton_droit.hitbox.topright[0] + 1, self.bouton_droit.hitbox.topright[1], spritelist[0][1][0], spritelist[0][3][0])
        # Liste contenant les cellules du menu coulissant, y compris les flèches
        self.buttonlist = [self.bouton_gauche, self.bouton_centre, self.bouton_droit, self.fleche_droite, self.fleche_gauche]
                
    # Méthode mettant à jour les sprites à l'intérieur des cellules du menu
    def update_all(self):
        # Liste de indices de navigation de la matrice des sprites
        self.indicelist = [self.i, self.j, self.k]
        # Actualisation de chaque bouton et son sprite à l'aide de la méthode update() de la classe Button
        for x in range(3):
            self.buttonlist[x].update(self.spritelist[0][0], self.spritelist[1][self.indicelist[x]])
    
    # Méthode mettant à jour la liste d'état de chaque bouton du menu coulissant
    def update_statelist_all(self):
        for x in self.buttonlist:
            # On utilise la méthode update_statelist() de la classe Button
            x.update_statelist()
        
    # Méthode affichant tous les boutons du menu coulissant
    def draw_all(self):
        # On affiche chaque bouton de la liste à l'aide de la méthode draw() de la classe Button
        for x in self.buttonlist:
            x.draw()
    
    # Méthode actualisant l'image des deux flèches et tout le menu (les images affichées à l'intérieur) si le joueur intéragit avec une des deux flèches
    def menu_arrow_update(self):
        # Les flèches sont aux index 3 et 4 du tableau self.buttonlist
        for x in range(3, 5):
            # Si le joueur intéragit ou arrête d'intéragir avec le bouton flèche
            if self.buttonlist[x].statelist[0] != self.buttonlist[x].statelist[1]:
                # Actualisation de l'image de la flèche
                self.buttonlist[x].update(self.spritelist[0][1], self.spritelist[0][x-1])
                # Si la flèche est cliquée
                if self.buttonlist[x].clicked:
                    # Si la flèche droite est cliquée (indice 3 dans self.buttonlist), on recule dans la matrice des sprites
                    if x == 3:
                        roll = -1
                    # Si la flèche gauche est cliquée (indice 4 dans self.buttonlist), on avance dans la matrice des sprites
                    else:
                        roll = 1
                    # Réaffectation des indices de spritelist des images affichées à l'intérieur des cellules du menu coulissant
                    # Indice = (indice incrémenté/décrémenté) modulo le nombre d'image dans le menu coulissant...
                    # ...de sorte qu'on pourra passer dans la matrice de l'objet de positon 4 à 0 et inversement de 0 à 4 == il y a un enroulement, le menu n'a ni début ni fin
                    self.i, self.j, self.k = (self.i + roll) % len(self.spritelist[1]), (self.j+ roll) % len(self.spritelist[1]), (self.k+ roll) % len(self.spritelist[1])
                    # Actualisation de chaque image dans les cellules du menu selon le roulement effectué
                    self.update_all()
                    
    # Méthode actualisant l'image de la cellule et du sprite représenté à l'intérieur des trois boutons centraux du menu coulissant  
    def menu_button_update(self):
        # Liste de indices de navigation de la matrice des sprites
        self.indicelist = [self.i, self.j, self.k]
        # Les boutons bouton_gauche, bouton_centre et bouton_droit sont respectivement d'indice 0, 1 et 2 dans le tableau self.buttonlist
        for x in range(3):
            # S'il y a changement d'état du bouton == intéraction ou arrêt de l'intéraction du joueur
            if self.buttonlist[x].statelist[0] != self.buttonlist[x].statelist[1]:
                # On actualise l'image de la cellule du bouton et l'image à l'intérieure de celui-ci selon son état avec la méthode update() de la classe Button
                self.buttonlist[x].update(self.spritelist[0][0], self.spritelist[1][self.indicelist[x]])
    
    # Méthode actualisant et affichant le menu coulissant selon les intéractions du joueur
    # Appelle directement toutes les autres méthodes de la classe Menu et indirectement toutes les méthodes de la classe Button
    # On appelera cette fonction à chque itération de la boucle jeu
    def interaction_menu(self):
        # On actualise les listes d'état des boutons du menu coulissant
        self.update_statelist_all()
        # On affiche les boutons du menu coulissant
        self.draw_all()
        # On fait rouler le menu si une des flèches est cliquée
        self.menu_arrow_update()
        # On actualise l'état des boutons du menu (hover, cliqué ou rien) si le joueur intéragit ou arrête d'intéragir avec 
        self.menu_button_update()

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

# Création des instances menu des menus coulissants du jeu
menu1 = Menu(height//4, spritelist)
menu2 = Menu(height//2, spritelist)
menu3 = Menu(3*height//4, spritelist)

# Booléen dont dépend la boucle de jeu
run = True

#############################################################################################################
############################################ Boucle de jeu ##################################################
#############################################################################################################

while run:
    
    # Fond blanc (pour l'instant)
    screen.fill((255, 255, 255))
    
    # Actualisation et affichage de chaque menu  coulissant
    menu1.interaction_menu()
    menu2.interaction_menu()
    menu3.interaction_menu()
    
    #pyg.key.set_repeat(10)
    
    for event in pyg.event.get():
        
        if event.type == pyg.QUIT:
            quit()
            
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_ESCAPE:
                quit()

    pyg.display.flip()