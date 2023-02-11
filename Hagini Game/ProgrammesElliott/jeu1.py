from win32api import GetSystemMetrics
import pygame as pyg
import sys

# Déclaration des variables utilisées à travers les fonctions et classes du programme comme globales
global width, height
global mousestate
global noir, blanc, rouge
global start_ticks

# Initialisation de pygame
pyg.init()

# Initialisation du module font de pygame
pyg.font.init()

# Création de l'objet horloge, outil temporel de pygame
pyg.time.Clock()
# Temps en millisecondes après l'initialisation de pygame au début du lancement du programme
# Servira pour des calculs de durée
start_ticks = pyg.time.get_ticks()
    
#############################################################################################################
################################## Définition des classes et fonctions ######################################
#############################################################################################################

# Création de la classe Button à laquelle appartient tout bouton du menu
class Button:
    
    # Initialisation de chaque instance de cette classe
    def __init__(self, x=float, y=float, image=pyg.Surface, item_image=pyg.Surface):
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
    def update(self, buttonspritelist=list, spritelist=list):
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


# Création de la classe Menu
class Menu:
    
    # Initialisation de chaque instance de cette classe
    def __init__(self, y=float, spritelist=list):
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
            # et si le joueur ne maintient pas le clic gauche (mousestate != [True, True]), de sorte que maintenir clic gauche et déplacer la souris sur un autre bouton ne compte pas comme un clic /// ça aurait été une meilleure idée de vérifier ça directement dans la méthode update() ou which_state() de Button mais j'y arrive pas et ça ça marche donc bon...
            if self.buttonlist[x].statelist[0] != self.buttonlist[x].statelist[1] and mousestate != [True, True]:              #and mouse_not_held(mousestate)
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
            # Si le joueur relâche le clic gauche
            if mousestate == [True, False]:
                # On actualise l'image du bouton pour qu'il ne s'affiche plus comme cliqué
                self.buttonlist[x].update(self.spritelist[0][1], self.spritelist[0][x-1])
                    
    # Méthode actualisant l'image de la cellule et du sprite représenté à l'intérieur des trois boutons centraux du menu coulissant  
    def menu_button_update(self):
        # Liste de indices de navigation de la matrice des sprites
        self.indicelist = [self.i, self.j, self.k]
        # Les boutons bouton_gauche, bouton_centre et bouton_droit sont respectivement d'indice 0, 1 et 2 dans le tableau self.buttonlist
        for x in range(3):
            # S'il y a changement d'état du bouton == intéraction ou arrêt de l'intéraction du joueur
            # et si le joueur ne maintient pas le clic gauche (mousestate != [True, True]), de sorte que maintenir clic gauche et déplacer la souris sur un autre bouton ne compte pas comme un clic
            if self.buttonlist[x].statelist[0] != self.buttonlist[x].statelist[1] and mousestate != [True, True]:
                # On actualise l'image de la cellule du bouton et l'image à l'intérieure de celui-ci selon son état avec la méthode update() de la classe Button
                self.buttonlist[x].update(self.spritelist[0][0], self.spritelist[1][self.indicelist[x]])
            # Si le clic gauche est relâché
            if mousestate == [True, False]:
                # On actualise l'image du bouton pour qu'il ne s'affiche plus comme cliqué
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

'''
dialogue SITUATIONNEL selon sprite cliqué dans les boutons (ou alors selon sprite cliqué sur le modèle de tank pour confirmer que le joueur va rester dessus un certain temps pour tout afficher)
'''

# Création de la classe Dialogbox (boîte de dialogue)
class Dialogbox:
    
    # Initialisation de chaque instance de cette classe
    def __init__(self, width=float, height=float, x=float, y=float, dialogdict=dict):
        self.width, self.height = width, height             # Largeur et hauteur de la boîte de dialogue
        self.x, self.y = x, y                               # Coordonnées x et y du coin haut gauche de la boîte de dialogue
        self.dialogbox_rect = pyg.Rect((self.x, self.y), (self.width, self.height))                 # Définition du rectangle de collisions de la boîte de dialogue
        self.write_zone_rect = pyg.Rect((self.x , self.y), (self.width * 0.95, self.height * 0.9))  # Définition de la zone dans laquelle sera affichée le texte, ce dernier ne devant pas en sortir
        self.write_zone_rect.center = self.dialogbox_rect.center
        ''' CALCULER LA TAILLE DE LA POLICE EN FONCTION DES MENSURATIONS DE LA BOITE DE DIALOGUE OU DE L'ECRAN POUR NE PAS QUE LE TEXTE DEPASSE LA BOITE VERTICALEMENT (PAS UNE SOLUTION PARFAITE MAIS PAS VRAIMENT UTILE DE TRAVAILLER 5 A 10H DE PLUS POUR CODER UN PETIT ASCENSEUR) '''
        self.font = pyg.font.Font(None, 24)                 # On créé la police du texte de la boîte de dialogue
        self.line_height = self.font.get_linesize()         # Hauteur en pixel que prend une ligne de texte avec la police utilisée ---> espace que l'on mettra entre chaque ligne affichée
        self.dialogdict = dialogdict                        # Dictionnaire regroupant tous les dialogues affichable par la boîte de dialogue sous la forme {'dialogue_1': [ligne_1, ligne_2, ligne_3], 'dialogue_2': [ligne_1, ligne_2, ligne_3, ligne_4], etc.}, où la clé portera le nom de la condition requise pour lancer le dialogue en valeur
        ''' UNE FOIS LES LIGNES ADAPTEES, ELLES NE SERONT PLUS MODIFIEES, IL FAUT DONC POUR ETRE OPTIMAL LES STOCKER SOUS LA FORME DE TUPLES ET NON DE TABLEAUX QUI SONT PLUS COUTEUX '''
        self.dict_slice()                                   # On coupe à l'avance chaque ligne de dialogue du dictionnaire si celle-ci prend trop de place (dépasse) la zone d'affichage du texte lorsqu'elle est affichée, utilise la méthode dict_slice() de cette classe
        ''' self.image = image '''
        # Initialisation des variables qui permettront d'afficher le dialogue ligne par ligne et caractère par caractère
        self.current_line_number, self.charindex = 0, 0     # Numéro de la ligne en train d'être affichée et position du prochain caractère à afficher dans le string de la ligne de dialogue
        self.current_dialog, self.current_line = [], ''     # Dialogue à afficher sous forme de tableau contenant des strings, celui en première position étant la première ligne et ainsi de suite, ligne incomplète à laquelle ajoutera le charactère suivant et l'affichera
        self.delay, self.last_char_time = 0.03, 0           # Délai entre l'affichage de deux charactères successifs et instant de l'affichage du dernier caractère en date
        
    # Méthode modifiant les tableaux de lignes de dialogue du dictionnaire suivant la méthode list_slice()
    def dict_slice(self):
        # Pour toutes les clés et leur tableau de lignes de dialogue en valeur dans le dictionnaire
        for key, valuelist in self.dialogdict.items():
            # Pour chaque ligne de dialogue, sous forme de chaîne de caractère, dans chaque tableau du dictionnaire des dialogues
            for line_index in range(len(valuelist)):
                # On appelle la méthode list_slice()
                valuelist[line_index] = self.list_slice(valuelist[line_index])
            # On réaffecte le tableau de lignes de dialogue du dictionnaire
            # Ce que fait la liste par compréhension: [['a'], ['b'], ['c'], ['d']] ---> ['a', 'b', 'c', 'd']
            self.dialogdict[key] = [i for sublist in valuelist for i in sublist]
        
    # Méthode RECURSIVE coupant une ligne de dialogue à l'emplacement d'un espace de sorte qu'elle s'affiche dans la zone d'affichage de la boîte de dialogue sans en dépasser
    # ATTENTION: modifie les lignes de dialogue de manière destructive: enlève des espaces dans les lignes de dialogue
    def list_slice(self, line):
        # Si la ligne de dialogue ne dépasse pas la largeur de la zone d'affichage
        if pyg.font.Font.size(self.font, line)[0] <= self.write_zone_rect.width:
            # On ne la modifie pas
            return [line]
        # Sinon on coupe la liste en deux
        ''' PAS OPTIMAL, ON TRAVERSE TOUTE LA CHAINE DE CARACTERE DEPUIS LE DEBUT, ALORS QU'ON PEUT DIRECTEMENT PARTIR DE L'INDEX CORRESPONDANT A self.write_zone_rect.width MAIS QU'IL FAUDRAIT CALCULER PAR CONTRE '''
        # On initialise une variable scan qui sera l'index du caractère où on coupe la liste en deux
        scan = 0
        # Tant qu'on n'est pas arrivé à la fin de la liste (n'arrivera pas) et que la chaîne de caractère est toujours affichable 
        while scan < len(line) - 1 and pyg.font.Font.size(self.font, line[:scan])[0] < self.write_zone_rect.width:
            # Si le caractère est un espace
            if line[scan] == ' ':
                # On trace temporairement la coupe à l'index de l'espace
                cut = scan
            # On regarde pour le caractère suivant
            scan += 1
        # On retourne la première partie affichable de la chaîne de caractère, et on appelle cette même méthode sur le reste de la chaîne dans le cas où la deuxième partie n'est pas affichable
        return [line[:cut]] + self.list_slice(line[cut+1:])    
        
    # Méthode de base pour afficher une ligne de texte
    def draw_line(self, line, line_number):
        # On créé une surface (=image) contenant le texte à afficher
        line_to_print = self.font.render(line, 1, noir)
        # On affiche ce "rendu" du texte dans la zone d'écriture et à la bonne ligne
        screen.blit(line_to_print, (self.write_zone_rect.x, self.write_zone_rect.y + line_number * self.line_height))
    
    # Méthode affichant la ligne en cours caractère par caractère
    def draw_line_progressive(self):
        # Ligne de dialogue complète à afficher
        dialog_line = self.current_dialog[self.current_line_number]
        # Si la ligne en train d'être affichée n'est pas encore complète
        if self.current_line != dialog_line:
            # Temps en secondes
            time = (pyg.time.get_ticks() - start_ticks) / 1000
            # Une fois le délai après le dernier caractère affiché écoulé
            if time > self.delay + self.last_char_time:
                # Le caractère qu'on affiche maintenant sera le dernier caractère de la prochaine itération de la boucle
                self.last_char_time = time
                # On ajoute le prochain caractère à la ligne incomplète en cours d'affichage
                self.current_line += dialog_line[self.charindex]
                # Index du prochain caractère à être affiché
                self.charindex += 1
                # On affiche la ligne incomplète à l'aide de la méthode draw_line()
                self.draw_line(self.current_line, self.current_line_number)
        # Sinon si la ligne est complète
        else:
            # On l'affiche
            self.draw_line(dialog_line, self.current_line_number)
            self.current_line_number += 1   # On passe à la ligne suivante
            self.current_line = ''          # La prochaine ligne est pour l'instant vide
            self.charindex = 0              # Le prochain caractère à afficher sera le tout premier de la prochaine ligne
    
    def draw_all_lines(self):
        # On affiche les lignes qu'on a fini d'afficher
        for x in range(len(self.current_dialog[:self.current_line_number])):
            self.draw_line(self.current_dialog[x], x)
        
        # Si toutes les lignes n'ont pas encore été entièrement affichées
        if len(self.current_dialog) != len(self.current_dialog[:self.current_line_number]):
            # On affiche la ligne en cours d'affichage caractère par caractère
            self.draw_line_progressive()
        # Affiche en continu la ligne en cours d'affichage (sinon l'affichage est discontinu)
        self.draw_line(self.current_line, self.current_line_number)
        
    # Méthode pour afficher la boîte de dialogue dans son entiereté, la boîte et le texte à l'intérieur
    def draw(self):
        # On affiche la boîte de dialogue et la zone d'affichage du texte
        ''' TEMPORAIRE, à remplacer par screen.blit(self.image, (self.x, self.y)) '''
        pyg.draw.rect(screen, noir, self.dialogbox_rect, 1)
        pyg.draw.rect(screen, rouge, self.write_zone_rect, 1)
        
        # On affiche le texte de la boîte de dialogue
        self.draw_all_lines()

# Fonction chargeant toutes les images du jeu
# Je l'ai mis à l'intérieur d'une fonction car gêne la visibilité du code par sa taille et sa répétition
def image_load():
    # Dimensions des images du menu calculées directement à partir des valeurs de largeur et de hauteur de l'écran
    cell_dimensions = (width//4, height//5)
    arrow_dimensions = [cell_dimensions[1] - 10] * 2
    arrowcell_dimensions = [i + 10 for i in arrow_dimensions]
    sprite_dimensions = [int(i // 1.5) for i in cell_dimensions]
    
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
    
    # On retourne la spritelist
    return spritelist

# Fonction pour quitter la fenêtre et arrêter l'exécution du programme
def quit():
    run  = False
    pyg.quit()
    sys.exit()

#############################################################################################################
######################################### Définition des variables ##########################################
#############################################################################################################

# Largeur et hauteur de l'écran
width, height = GetSystemMetrics(0), GetSystemMetrics(1)
#width, height = int(GetSystemMetrics(0) // 2), int(GetSystemMetrics(1) // 2)
# Titre du jeu
titre = 'feur'
pyg.display.set_caption(titre)
screen = pyg.display.set_mode((width, height))
'''hitbox_screen = pyg.Surface.get_rect(screen)'''
# Définition et affichage du fond du jeu
background = pyg.image.load('img/placeholder_bg.png')
background = pyg.transform.scale(background, (width, height)).convert()
fond = background.convert()
screen.blit(fond, (0, 0))
pyg.display.flip()

# Initialisation du tableau d'état du clic gauche de la souris
mousestate = [0, 0]

# Définition couleurs
noir = (0,0,0)
blanc = (255,255,255)
rouge = (255, 0, 0)

# Appel de la fonction image_load() qui renvoie la matrice contenant toutes les images du jeu
spritelist = image_load()

''' TEST '''


''' METTRE DANS UNE FONCTION COMME POUR LA SPRITELIST QUAND CE SERA COMPLET '''
''' PLUSIEURS BOITES DE DIALOGUE DONC PLUSIEURS DICTIONNAIRES QU'ON POURRAIT REGROUPER DANS UN TABLEAU DE LA MEME MANIERE QUE LA SPRITELIST '''
# Dictionnaire contenant toutes les lignes de dialogue d'une boîte dialogue
# On préférera que cette variable soit un dictionnaire pour naviguer de manière naturelle à travers les dialogues: quand bouton_gauche cliqué, charger dans la boîte de dialogue la liste de lignes de dialogues correspondant à la clé 'bouton_gauche'
textdict = {'feur': ['Ah bon bah quand même!', 'C" est quand même con d''utiliser de si mauvais placeholders quelle idée de merde franchement', 'OMORI est un très mauvais jeu, on ne peux faire plus gay qu"OMORI, c"est strictement possible, personnellement je déteste OMORI, particulièrement toute la partie avec Humphrey qui est sincèrement une horreur d"un point de vue game-design, une horreur vraiment. Pourtant les Slimegirls sont grave baisables mais je suis arrêté par le simple ennui de cette zone du jeu. Deeper Well juste avant était bien plus intéressant bien que snas gameplay vraiment je me répète, c"est un placeholder AAAAAAAAAAAAAHHH']}

# Création des instances menu des menus coulissants du jeu
menu1 = Menu(height//4, spritelist)
menu2 = Menu(height//2, spritelist)
menu3 = Menu(3*height//4, spritelist)

# Création de l'instnce boîte de dialogue
test_dialogbox = Dialogbox(width//2, height//2, 50, 50, textdict)
test_dialogbox.current_dialog = test_dialogbox.dialogdict['feur']


''' /TEST '''

# Booléen dont dépend la boucle de jeu
run = True

#############################################################################################################
############################################ Boucle de jeu ##################################################
#############################################################################################################

while run:
    
    # Fond blanc (pour l'instant)
    screen.fill(blanc)
    
    # Tableau de l'état du clic gauche
    mousestate = [mousestate[1], pyg.mouse.get_pressed()[0]]
    
    ''' TEST '''
    
    # Affichage de la boîte de dialogue et de son texte
    test_dialogbox.draw()
    
    '''
    # Actualisation et affichage de chaque menu coulissant
    menu1.interaction_menu()
    menu2.interaction_menu()
    menu3.interaction_menu()
    '''
    
    ''' /TEST '''
    
    ''' pyg.key.set_repeat(10) '''
    
    # Pour quitter le jeu
    for event in pyg.event.get():
        
        if event.type == pyg.QUIT:
            quit()
            
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_ESCAPE:
                quit()

    pyg.display.flip()