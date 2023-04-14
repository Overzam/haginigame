# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


'''
Groupe n°1
Natacha GAUSSIN 1e4
Camille LOISON 1e4
Tifenn LETUVE 1e4
jeu vidéo : FightinGODS
'''

import pygame as pyg
import math
import time
import random

pyg.init()

pyg.display.set_caption("FightinGODS")
screen = pyg.display.set_mode((1920,1080))

'''Definition'''
'''page d'accueil'''

Fond_accueil = pyg.image.load("Assets/IMG-0711.PNG")
Fond_Round = pyg.image.load("Assets/IMG-0704.PNG")

Fond_Commande = pyg.image.load("Assets/Mvt-Joueur-.png")
Fond_instru = pyg.image.load("Assets/instru1.png")
Fond_erreur = pyg.image.load("Assets/solomode.png")

fleche = pyg.image.load("Assets/fleche.png")

ordi = pyg.image.load("Assets/ordi.png")
barre = pyg.image.load("Assets/barre.png")

cooldown_coup = -1

moment_move = 0

momentum = 0

game_offset_x = 100
game_offset_y = 100

def countdown(num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(min_sec_format, end='/r')
        time.sleep(1)
        num_of_secs -= 1

    print('Countdown finished.')

def FondAccueil():
    screen.blit(Fond_accueil, (0 + game_offset_x, 0 + game_offset_y))

def Fonderreur():
    screen.blit(Fond_erreur, (0 + game_offset_x, 0 + game_offset_y))

def FondCommande():
    screen.blit(Fond_Commande, (0 + game_offset_x, 0 + game_offset_y))

def FondTru():
    screen.blit(Fond_instru, (0 + game_offset_x, 0 + game_offset_y))


play_button = pyg.image.load("Assets/IMG-0694.PNG")
play_button = pyg.transform.scale(play_button, (200, 92))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(280)  + game_offset_x
play_button_rect.y = math.ceil(190) + game_offset_y


def Bouton_de_jeu():
    screen.blit(play_button, play_button_rect)


option_button = pyg.image.load("Assets/boption.png")
option_button = pyg.transform.scale(option_button, (60, 60))
option_button_rect = option_button.get_rect()
option_button_rect.x = math.ceil(690)  + game_offset_x
option_button_rect.y = math.ceil(360) + game_offset_y


def optionButton():
    screen.blit(option_button, option_button_rect)


commande_button = pyg.image.load("Assets/instru.png")
commande_button = pyg.transform.scale(commande_button, (100, 46))
commande_button_rect = commande_button.get_rect()
commande_button_rect.x = math.ceil(650)  + game_offset_x
commande_button_rect.y = math.ceil(10) + game_offset_y

def commandebutton():
    screen.blit(commande_button, commande_button_rect)

    
    
instru_button = pyg.image.load("Assets/IMG-0695.PNG")
instru_button = pyg.transform.scale(instru_button, (100, 46))
instru_button_rect = instru_button.get_rect()
instru_button_rect.x = math.ceil(screen.get_width() / 2.5)  + game_offset_x
instru_button_rect.y = math.ceil(screen.get_height() / 2.1) + game_offset_y




def instrubutton():
    screen.blit(instru_button, instru_button_rect)
    


solo_button = pyg.image.load("Assets/solo.png")
solo_button = pyg.transform.scale(solo_button, (200, 92))
solo_button_rect = solo_button.get_rect()
solo_button_rect.x = math.ceil(280) + game_offset_x
solo_button_rect.y = math.ceil(180) + game_offset_y

def solobutton():
    screen.blit(solo_button, solo_button_rect)
    
deux_button = pyg.image.load("Assets/deuxjoueurs.png")
deux_button = pyg.transform.scale(deux_button, (200, 92))
deux_button_rect = deux_button.get_rect()
deux_button_rect.x = math.ceil(280) + game_offset_x
deux_button_rect.y = math.ceil(300) + game_offset_y

def DeuxJoueurs():
    screen.blit(deux_button, deux_button_rect)

deux_Button = pyg.image.load("Assets/deuxjoueurs.png")
deux_Button = pyg.transform.scale(deux_Button, (100, 46))
deux_Button_rect = deux_Button.get_rect()
deux_Button_rect.x = math.ceil(280) + game_offset_x
deux_Button_rect.y = math.ceil(300) + game_offset_y

def deuxjoueurs():
    screen.blit(deux_Button, deux_Button_rect)

def Fond_joueurP():
    screen.blit(Fond_accueil, (0 + game_offset_x, 0 + game_offset_y))
    
def Fond_selectJ():
    screen.blit(Fond_Round, (0 + game_offset_x, 0 + game_offset_y))
    


def Fond_joueurD():
    screen.blit(Fond_accueil, (0 + game_offset_x, 0 + game_offset_y))
    


def Fond_round():
    screen.blit(Fond_Round, (0 + game_offset_x, 0 + game_offset_y))
    
def Fond_commande():
    screen.blit(Fond_Round, (0 + game_offset_x, 0 + game_offset_y))    


def Fond_d_option():
    screen.blit(OptionFond, (0 + game_offset_x, 0 + game_offset_y))

backgroundPS = pyg.image.load("Assets/IMG-0705.PNG")


def background_Premiere_Selection():
    screen.blit(backgroundPS, (0 + game_offset_x, 0 + game_offset_y))


backgroundDS = pyg.image.load("Assets/IMG-0706.PNG")


def background_Deuxieme_Selection():
    screen.blit(backgroundDS, (0 + game_offset_x, 0 + game_offset_y))


premierPerso = pyg.image.load("Assets/FOURENS.png")
premierPerso = pyg.transform.scale(premierPerso, (138, 320))
premierPerso_rect = premierPerso.get_rect()
premierPerso_rect.x = math.ceil(50) + game_offset_x
premierPerso_rect.y = math.ceil(70) + game_offset_y


def premierPersonnage():
    screen.blit(premierPerso, premierPerso_rect)


deuxiemePerso = pyg.image.load("Assets/deuxieme_personnage.png")
deuxiemePerso = pyg.transform.scale(deuxiemePerso, (138, 217))
deuxiemePerso_rect = deuxiemePerso.get_rect()
deuxiemePerso_rect.x = math.ceil(300) + game_offset_x
deuxiemePerso_rect.y = math.ceil(120) + game_offset_y


def deuxiemePersonnage():
    screen.blit(deuxiemePerso, deuxiemePerso_rect)


troisiemePerso = pyg.image.load("Assets/troisieme_personnage.png")
troisiemePerso = pyg.transform.scale(troisiemePerso, (138, 304))
troisiemePerso_rect = troisiemePerso.get_rect()
troisiemePerso_rect.x = math.ceil(550) + game_offset_x
troisiemePerso_rect.y = math.ceil(70) + game_offset_y


def troisiemePersonnage():
    screen.blit(troisiemePerso, troisiemePerso_rect)

'''ROUND'''

roundP = pyg.image.load("Assets/tif/Pround.PNG")
roundP = pyg.transform.scale(roundP, (150, 150))
roundP_rect = roundP.get_rect()
roundP_rect.x = math.ceil(100) + game_offset_x
roundP_rect.y = math.ceil(150) + game_offset_y


def ROUNDP():
    screen.blit(roundP, roundP_rect)

roundD = pyg.image.load("Assets/Dround.PNG")
roundD = pyg.transform.scale(roundD, (150, 150))
roundD_rect = roundP.get_rect()
roundD_rect.x = math.ceil(300) + game_offset_x
roundD_rect.y = math.ceil(150) + game_offset_y


def ROUNDD():
    screen.blit(roundD, roundD_rect)

roundT = pyg.image.load("Assets/tif/Tround.PNG")
roundT = pyg.transform.scale(roundT, (150, 150))
roundT_rect = roundT.get_rect()
roundT_rect.x = math.ceil(500) + game_offset_x
roundT_rect.y = math.ceil(150) + game_offset_y


def ROUNDT():
    screen.blit(roundT, roundT_rect)

'''Combat'''

backgroundCP = pyg.image.load("Assets/fond_jeu_2.jpg")
backgroundCP = pyg.transform.scale(backgroundCP, (750, 420))


def backgroundCPremier():
    screen.blit(backgroundCP, (0 + game_offset_x, 0 + game_offset_y))


backgroundCD = pyg.image.load("Assets/fond_jeu.jpg")
backgroundCD = pyg.transform.scale(backgroundCD, (750, 420))


def backgroundCDeuxieme():
    screen.blit(backgroundCD, (0 + game_offset_x, 0 + game_offset_y))






# nouvelle classe
class Game:

    def __init__(self):
        # generer le perso
        self.player = Player()
        self.playerII = PlayerII()
        self.pressed = {}


ECART = 75
ECART2 = 100
Ecart = 300
n = 1


# creer une classe joueur
class Player(pyg.sprite.Sprite):
    def __init__(self):
        pyg.sprite.Sprite.__init__(self)
        self.health = 100
        self.exp = 100
        self.max_exp = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 1
        self.image = pyg.image.load("Assets/2/2.png")
        self.image2 = pyg.image.load("Assets/2/2coup.png")
        self.rect = self.image.get_rect()
        self.rect.x = 255 + game_offset_x
        self.rect.y = 160 + game_offset_y

    def damage(self, amount):
        # infliger dégâts
        self.health -= amount

    def update_health_bar(self, surface):
        # couleur jauge ( rouge)
        bar_color = (211, 19, 19)

        # arrière plein jauge ( blanc)
        back_bar_color = (255, 255, 255)

        # position de la jauge,
        bar_position = [self.rect.x - 210, self.rect.y - 140, self.health, 15]

        # position arrière plan jauge
        back_bar_position = [self.rect.x - 210, self.rect.y - 140, self.max_health, 15]

        # apparition de la bar blanche
        pyg.draw.rect(surface, back_bar_color, back_bar_position)
        # puis celle de couleur rouge
        pyg.draw.rect(surface, bar_color, bar_position)

    def augmenter(self, amount):
        # augmenter des exp
        self.exp -= amount

    def update_exp_bar(self, surface):
        # couleur jauge ( rouge)
        bar_color = (255, 255, 255)

        # arrière plein jauge ( blanc)
        back_bar_color = (0, 128, 0)

        # position de la jauge,
        bar_position = [self.rect.x - 210, self.rect.y - 120, self.exp, 15]

        # position arrière plan jauge
        back_bar_position = [self.rect.x - 210, self.rect.y - 120, self.max_exp, 15]

        # apparition de la bar blanche
        pyg.draw.rect(surface, back_bar_color, back_bar_position)
        # puis celle de couleur rouge
        pyg.draw.rect(surface, bar_color, bar_position)

    def move_left(self):
        self.rect.x -= self.velocity

    def move_right(self):
        '''if not self.game.check_collision(self, self.game.playerII):'''
        self.rect.x += self.velocity


# deuxième joueur :

def __init__(self, game):
    # generer le perso
    self.playerII = PlayerII(game)
    self.game = game
    self.pressed = {}


# creer une classe joueur
class PlayerII(pyg.sprite.Sprite):
    def __init__(self):
        pyg.sprite.Sprite.__init__(self)
        self.health = 100
        self.max_health = 100
        self.exp = 100
        self.max_exp = 100
        self.attack = 10
        self.velocity = 1
        self.image = pyg.image.load('Assets/3r/3r.png')
        self.image2 = pyg.image.load('Assets/3r/3coupr.png')
        self.rect = self.image.get_rect()
        self.rect.x = 445 + game_offset_x
        self.rect.y = 153 + game_offset_y

    def update_health_bar(self, surface):
        # couleur jauge ( rouge)
        bar_color = (211, 19, 19)

        # arrière plein jauge ( blanc)
        back_bar_color = (255, 255, 255)

        # position de la jauge,
        bar_position = [self.rect.x + 150, self.rect.y - 140, self.health, 15]

        # position arrière plan jauge
        back_bar_position = [self.rect.x + 150, self.rect.y - 140, self.max_health, 15]

        # apparition de la bar blanche
        pyg.draw.rect(surface, back_bar_color, back_bar_position)
        # puis celle de couleur rouge
        pyg.draw.rect(surface, bar_color, bar_position)

    def update_exp_bar(self, surface):
        # couleur jauge ( rouge)
        bar_color = (255, 255, 255)

        # arrière plein jauge ( blanc)
        back_bar_color = (0, 128, 0)

        # position de la jauge,
        bar_position = [self.rect.x + 150, self.rect.y - 120, self.exp, 15]

        # position arrière plan jauge
        back_bar_position = [self.rect.x + 150, self.rect.y - 120, self.max_exp, 15]

        # apparition de la bar blanche
        pyg.draw.rect(surface, back_bar_color, back_bar_position)
        # puis celle de couleur rouge
        pyg.draw.rect(surface, bar_color, bar_position)


    def move_left(self):
        '''if not self.game.check_collision(self, self.game.player):'''
        self.rect.x -= self.velocity

    def move_right(self):
        self.rect.x += self.velocity


'''Fin de combat '''

background_Fin = pyg.image.load("Assets/IMG-0707.PNG")

background_Egalite = pyg.image.load("Assets/Fin-Egalite.png")


def Fond_de_fin():
    screen.blit(background_Fin, (0 + game_offset_x, 0 + game_offset_y))

def Fond_Egalite():
    screen.blit(background_Egalite, (0 + game_offset_x, 0 + game_offset_y))


Button_continuer = pyg.image.load("Assets/IMG-0693.PNG")
Button_continuer = pyg.transform.scale(Button_continuer, (150, 85))
Button_continuer_rect = Button_continuer.get_rect()
Button_continuer_rect.x = math.ceil(560) + game_offset_x
Button_continuer_rect.y = math.ceil(300) + game_offset_y


def button_continuer():
    screen.blit(Button_continuer, Button_continuer_rect)


image_KO = pyg.image.load("Assets/IMG-0702.PNG")
image_KO = pyg.transform.scale(image_KO, (400, 400))
image_KO_rect = Button_continuer.get_rect()
image_KO_rect.x = math.ceil(168) + game_offset_x
image_KO_rect.y = math.ceil(62.5) + game_offset_y


def KO():
    screen.blit(image_KO, image_KO_rect)


bouton_rejouer = pyg.image.load("Assets/IMG-0695.PNG")
bouton_rejouer = pyg.transform.scale(bouton_rejouer, (150, 70))
bouton_rejouer_rect = bouton_rejouer.get_rect()
bouton_rejouer_rect.x = math.ceil(70) + game_offset_x
bouton_rejouer_rect.y = math.ceil(326) + game_offset_y


def button_rejouer():
    screen.blit(bouton_rejouer, bouton_rejouer_rect)


bouton_menu = pyg.image.load("Assets/IMG-0696.PNG")
bouton_menu = pyg.transform.scale(bouton_menu, (150, 70))
bouton_menu_rect = bouton_menu.get_rect()
bouton_menu_rect.x = math.ceil(500) + game_offset_x
bouton_menu_rect.y = math.ceil(326) + game_offset_y


def button_menu():
    screen.blit(bouton_menu, bouton_menu_rect)


premier_perso_fin_victoire = pyg.image.load("Assets/Fin_du_match_premier_perso.png")
premier_perso_fin_victoire = pyg.transform.scale(premier_perso_fin_victoire, (180, 180))
premier_perso_fin_victoire_rect = premier_perso_fin_victoire.get_rect()
premier_perso_fin_victoire_rect.x = math.ceil(60) + game_offset_x
premier_perso_fin_victoire_rect.y = math.ceil(131) + game_offset_y


def Fin_premier_perso_victoire():
    screen.blit(premier_perso_fin_victoire, premier_perso_fin_victoire_rect)


deuxieme_perso_fin_victoire = pyg.image.load("Assets/Fin_du_match_deuxieme_perso.png")
deuxieme_perso_fin_victoire = pyg.transform.scale(deuxieme_perso_fin_victoire, (180, 180))
deuxieme_perso_fin_victoire_rect = deuxieme_perso_fin_victoire.get_rect()
deuxieme_perso_fin_victoire_rect.x = math.ceil(60) + game_offset_x
deuxieme_perso_fin_victoire_rect.y = math.ceil(131) + game_offset_y


def Fin_deuxieme_perso_victoire():
    screen.blit(deuxieme_perso_fin_victoire, deuxieme_perso_fin_victoire_rect)


troisieme_perso_fin_victoire = pyg.image.load("Assets/Fin_du_match_troisieme_perso.png")
troisieme_perso_fin_victoire = pyg.transform.scale(troisieme_perso_fin_victoire, (180, 180))
troisieme_perso_fin_victoire_rect = troisieme_perso_fin_victoire.get_rect()
troisieme_perso_fin_victoire_rect.x = math.ceil(60) + game_offset_x
troisieme_perso_fin_victoire_rect.y = math.ceil(131) + game_offset_y


def Fin_troisieme_perso_victoire():
    screen.blit(troisieme_perso_fin_victoire, troisieme_perso_fin_victoire_rect)


premier_perso_fin_defaite = pyg.image.load("Assets/Fin_du_match_premier_perso.png")
premier_perso_fin_defaite = pyg.transform.scale(premier_perso_fin_defaite, (180, 180))
premier_perso_fin_defaite_rect = premier_perso_fin_defaite.get_rect()
premier_perso_fin_defaite_rect.x = math.ceil(468.75) + game_offset_x
premier_perso_fin_defaite_rect.y = math.ceil(131) + game_offset_y


def Fin_premier_perso_defaite():
    screen.blit(premier_perso_fin_defaite, premier_perso_fin_defaite_rect)


deuxieme_perso_fin_defaite = pyg.image.load("Assets/Fin_du_match_deuxieme_perso.png")
deuxieme_perso_fin_defaite = pyg.transform.scale(deuxieme_perso_fin_defaite, (180, 180))
deuxieme_perso_fin_defaite_rect = deuxieme_perso_fin_defaite.get_rect()
deuxieme_perso_fin_defaite_rect.x = math.ceil(468.75) + game_offset_x
deuxieme_perso_fin_defaite_rect.y = math.ceil(131) + game_offset_y


def Fin_deuxieme_perso_defaite():
    screen.blit(deuxieme_perso_fin_defaite, deuxieme_perso_fin_defaite_rect)


troisieme_perso_fin_defaite = pyg.image.load("Assets/Fin_du_match_troisieme_perso.png")
troisieme_perso_fin_defaite = pyg.transform.scale(troisieme_perso_fin_defaite, (180, 180))
troisieme_perso_fin_defaite_rect = troisieme_perso_fin_victoire.get_rect()
troisieme_perso_fin_defaite_rect.x = math.ceil(468.75) + game_offset_x
troisieme_perso_fin_defaite_rect.y = math.ceil(131) + game_offset_y


def Fin_troisieme_perso_defaite():
    screen.blit(troisieme_perso_fin_defaite, troisieme_perso_fin_defaite_rect)


'''Jeu'''

running = True
PageAccueil = False
Option = False
Commande = False
Instru = False
selectionP = False
selectionD = False
selecP = False
selecD = False
selecROUND = False
Fin_de_combat = False
dead = False
Combat = False
selecCombat = True
COMBAT = False
selecCOMBAT = False
ROUND = False
Jeu = False
DeuxJ = False
premier_personnage = 1
deuxieme_personnage = 2
nb_de_round = 1
nb_de_combat = 0
victoire_premier_personnage = 0
victoire_deuxieme_personnage = 0
Fond = 1

while running:

    screen.blit(ordi, (0, 0))
    screen.blit(barre, (game_offset_x, game_offset_y - 28))

    while PageAccueil:
        FondAccueil()
        optionButton()
        Bouton_de_jeu()
        optionButton()
        pyg.display.flip()
        for event in pyg.event.get():
            if event.type == pyg.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    PageAccueil = False
                    Jeu = True
                if option_button_rect.collidepoint(event.pos):
                    PageAccueil = False
                    Option = True
            if event.type == pyg.QUIT:
                PageAccueil = False
                running = False
                
    while Jeu:
        FondAccueil()
        solobutton()
        DeuxJoueurs()
        pyg.display.flip()
        for event in pyg.event.get():
            if event.type == pyg.MOUSEBUTTONDOWN:
                if solo_button_rect.collidepoint(event.pos):
                    Jeu = False
                    selecP = True
                if deux_button_rect.collidepoint(event.pos):
                    Jeu = False
                    selectionP = True
            if event.type == pyg.QUIT:
                Jeu = False
                running = False

    while selecP:
        background_Premiere_Selection()
        premierPersonnage()
        deuxiemePersonnage()
        troisiemePersonnage()
        pyg.display.flip()

        for event in pyg.event.get():
            if event.type == pyg.MOUSEBUTTONDOWN:
                if premierPerso_rect.collidepoint(event.pos):
                    premier_personnage = 1
                    selecP = False
                    selecD = True
                elif deuxiemePerso_rect.collidepoint(event.pos):
                    premier_personnage = 2
                    selecP = False
                    selecD = True
                elif troisiemePerso_rect.collidepoint(event.pos):
                    premier_personnage = 3
                    selecP = False
                    selecD = True
            if event.type == pyg.QUIT:
                selecP = False
                running = False

    while selecD:
        background_Deuxieme_Selection()
        premierPersonnage()
        deuxiemePersonnage()
        troisiemePersonnage()

        pyg.display.flip()
        victoire_premier_personnage = 0
        victoire_deuxieme_personnage = 0

        for event in pyg.event.get():
            if event.type == pyg.MOUSEBUTTONDOWN:
                if premierPerso_rect.collidepoint(event.pos):
                    deuxieme_personnage = 1
                    selecD = False
                    selecROUND = True
                elif deuxiemePerso_rect.collidepoint(event.pos):
                    deuxieme_personnage = 2
                    selecD = False
                    selecROUND = True
                elif troisiemePerso_rect.collidepoint(event.pos):
                    deuxieme_personnage = 3
                    selecD = False
                    selecROUND = True
            if event.type == pyg.QUIT:
                selecP = False
                running = False

    while selecROUND:
        nb_de_round = 0
        nb_de_combat = 0
        Fond_round()
        ROUNDP()
        ROUNDD()
        ROUNDT()

        pyg.display.flip()

        for event in pyg.event.get():
            if event.type == pyg.MOUSEBUTTONDOWN:
                if roundP_rect.collidepoint(event.pos):
                    nb_de_round = 1
                    selecROUND = False
                    selecCombat = True
                elif roundD_rect.collidepoint(event.pos):
                    nb_de_round = 2
                    selecROUND = False
                    selecCombat = True
                elif roundT_rect.collidepoint(event.pos):
                    nb_de_round = 3
                    selecROUND = False
                    selecCombat = True
            if event.type == pyg.QUIT:
                selecROUND = False
                running = False

    while Option:
        FondCommande()
        optionButton()
        commandebutton()
        pyg.display.flip()
        for event in pyg.event.get():
            if event.type == pyg.MOUSEBUTTONDOWN:
                if option_button_rect.collidepoint(event.pos):
                    Option = False
                    PageAccueil = True
                elif commande_button_rect.collidepoint(event.pos):
                    Option = False
                    Commande = True
            if event.type == pyg.QUIT:
                Option = False
                running = False

    while Commande:
        FondTru()
        optionButton()
        pyg.display.flip()
        for event in pyg.event.get():
            if event.type == pyg.MOUSEBUTTONDOWN:
                if option_button_rect.collidepoint(event.pos):
                    Commande = False
                    Option = True
            if event.type == pyg.QUIT:
                Commande = False
                running = False

    while selectionP:
        background_Premiere_Selection()
        premierPersonnage()
        deuxiemePersonnage()
        troisiemePersonnage()
        pyg.display.flip()

        for event in pyg.event.get():
            if event.type == pyg.MOUSEBUTTONDOWN:
                if premierPerso_rect.collidepoint(event.pos):
                    premier_personnage = 1
                    selectionP = False
                    selectionD = True
                elif deuxiemePerso_rect.collidepoint(event.pos):
                    premier_personnage = 2
                    selectionP = False
                    selectionD = True
                elif troisiemePerso_rect.collidepoint(event.pos):
                    premier_personnage = 3
                    selectionP = False
                    selectionD = True
            if event.type == pyg.QUIT:
                selectionP = False
                running = False

    while selectionD:
        background_Deuxieme_Selection()
        premierPersonnage()
        deuxiemePersonnage()
        troisiemePersonnage()

        pyg.display.flip()
        victoire_premier_personnage = 0
        victoire_deuxieme_personnage = 0

        for event in pyg.event.get():
            if event.type == pyg.MOUSEBUTTONDOWN:
                if premierPerso_rect.collidepoint(event.pos):
                    deuxieme_personnage = 1
                    selectionD = False
                    ROUND = True
                elif deuxiemePerso_rect.collidepoint(event.pos):
                    deuxieme_personnage = 2
                    selectionD = False
                    ROUND = True
                elif troisiemePerso_rect.collidepoint(event.pos):
                    deuxieme_personnage = 3
                    selectionD = False
                    ROUND = True
            if event.type == pyg.QUIT:
                selectionP = False
                running = False
                
    while ROUND:
        nb_de_round = 0
        nb_de_combat = 0
        Fond_round()
        ROUNDP()
        ROUNDD()
        ROUNDT()

        pyg.display.flip()

        for event in pyg.event.get():
            if event.type == pyg.MOUSEBUTTONDOWN:
                if roundP_rect.collidepoint(event.pos):
                    nb_de_round = 1
                    ROUND = False
                    Combat = True
                elif roundD_rect.collidepoint(event.pos):
                    nb_de_round = 2
                    ROUND = False
                    Combat = True
                elif roundT_rect.collidepoint(event.pos):
                    nb_de_round = 3
                    ROUND = False
                    Combat = True
            if event.type == pyg.QUIT:
                ROUND = False
                running = False




    while selecCombat:

        screen.blit(ordi, (0,0))
        barre = pyg.transform.scale(barre, (750,28))
        screen.blit(barre, (game_offset_x, game_offset_y - 28))
        # generer le jeu
        game = Game()

        # charger joueur
        player = Player()
        playerII = PlayerII()

        nb_de_combat += 1
        Fond += 1

        selecCOMBAT = True

        # boucle si vrai
        while selecCOMBAT:

            # appliquer arrière plan
            if (Fond % 2) == 0:
                backgroundCPremier()
            else:
                backgroundCDeuxieme()

            screen.blit(fleche, (game.playerII.rect.x + 55, game.playerII.rect.y - 10))

            pos_base = game.player.rect.x

            g_or_d = random.randint(1,2)                                                                   # mouvement aléatoire du bot
            #print(momentum)
            if g_or_d == 1:
                move = random.randint(1,25)
                momentum += 1
                if momentum == 100:
                    momentum = 0
                    for i in range(move):
                            if game.player.rect.x == 1:
                                game.player.rect.x = 1
                            game.player.rect.x -= 1
                            game.player.move_left()
            if g_or_d == 2:
                move = random.randint(1,25)
                momentum += 1
                if momentum == 100:
                    momentum = 0
                    for i in range(move):
                            if game.player.rect.x == 1:
                                game.player.rect.x = 1
                            game.player.rect.x += 1
                            game.player.move_right()
            


            if deuxieme_personnage == 1:
                personnage_de_droite_garde = pyg.image.load("Assets/1r/1r.png")
            elif deuxieme_personnage == 2:
                personnage_de_droite_garde = pyg.image.load("Assets/2r/2r.png")
            elif deuxieme_personnage == 3:
                personnage_de_droite_garde = pyg.image.load("Assets/3r/3r.png")

            screen.blit(personnage_de_droite_garde, game.playerII.rect)

            if premier_personnage == 1:
                personnage_de_gauche_garde = pyg.image.load("Assets/1/1.png")
            elif premier_personnage == 2:
                personnage_de_gauche_garde = pyg.image.load("Assets/2/2.png")
            elif premier_personnage == 3:
                personnage_de_gauche_garde = pyg.image.load("Assets/3/3.png")

            screen.blit(personnage_de_gauche_garde, game.player.rect)

            player.update_health_bar(screen)
            playerII.update_health_bar(screen)
            player.update_exp_bar(screen)
            playerII.update_exp_bar(screen)




            if playerII.health <= 0:
                victoire_premier_personnage += 1

                if nb_de_combat < nb_de_round :
                    selecCOMBAT = False
                    selecCombat = True
                else:
                    selecCOMBAT = False
                    selecCombat = False
                    dead = True
            
            if game.player.rect.x < game_offset_x + 60:
                game.player.rect.x = game_offset_x + 60
            
            if game.player.rect.x > game.playerII.rect.x - 50:                                                        # empecher le bot d'aller derriere le joueur
                game.player.rect.x = game.playerII.rect.x - 50
    
            # joueur2 -> gauche ou droite
            if game.pressed.get(pyg.K_q) and game.playerII.rect.x > 0:
                p1 = game.player.rect.x
                p2 = game.playerII.rect.x

                if p2 < (p1 + ECART):
                    game.playerII.rect.x = game.playerII.rect.x + 0
                else:
                    game.playerII.rect.x = game.playerII.rect.x - 1
                    game.playerII.move_left()
                if p1 > (p2 - ECART):
                    moment_move += 1
                    #time.sleep(0.5)
                    if (n % 2) == 0:
                        ran_move = random.randint(1,25)
                        for i in range(ran_move):
                            game.player.rect.x -= 1
                            game.player.move_left()
                        '''
                        for i in range(25):
                            game.player.rect.x -= 1
                            game.player.move_left()
                        '''
                        n +=1
                    '''
                    else:
                        p1 = game.player.rect.x
                        p2 = game.playerII.rect.x
                        if premier_personnage == 1:
                            screen.blit(pygame.image.load("Assets/1/1coup.png"), game.player.rect)
                        elif premier_personnage == 2:
                            screen.blit(pygame.image.load("Assets/2/2coup.png"), game.player.rect)
                        elif premier_personnage == 3:
                            screen.blit(pygame.image.load("Assets/3/3coup.png"), game.player.rect)
                        if p2 - p1 <= ECART2:
                            if game.pressed.get(pygame.K_a):
                                playerII.health -= 0.1
                                player.exp -= 1.5
                                if player.exp <= 10 and player.exp >= 0:
                                    if premier_personnage == 1:
                                        screen.blit(pygame.image.load("Assets/mainP.png"), game.player.rect)
                                    elif premier_personnage == 2:
                                        screen.blit(pygame.image.load("Assets/mainSD.png"), game.player.rect)
                                    elif premier_personnage == 3:
                                        screen.blit(pygame.image.load("Assets/mainST.png"), game.player.rect)
                                        if p2 - p1 <= ECART2:
                                            playerII.health -= 1
                                elif player.exp < 0:
                                    player.exp = 100
                            
                            else:
                                playerII.health -= 1.5
                                player.exp -= 2
                                if player.exp <= 10 and player.exp >= 0:
                                    if premier_personnage == 1:
                                        screen.blit(pygame.image.load("Assets/mainP.png"), game.player.rect)
                                    elif premier_personnage == 2:
                                        screen.blit(pygame.image.load("Assets/mainSD.png"), game.player.rect)
                                    elif premier_personnage == 3:
                                        screen.blit(pygame.image.load("Assets/mainST.png"), game.player.rect)
                                        if p2 - p1 <= ECART2:
                                            playerII.health -= 2
                                elif player.exp < 0:
                                    player.exp = 100
                            '''
                        #n += 1
                if p1 < 1:
                     game.player.rect.x = 0



                print('p1:')
                print(game.player.rect.x)
                print('p2:')
                print(game.playerII.rect.x)
                print('n:')
                print(n)

            elif game.pressed.get(pyg.K_d) and game.playerII.rect.x + game.playerII.rect.width < screen.get_width():
                momentum_back = random.randint(1,25)                                                                        # le bot recule qd on recule
                if momentum_back == 1:
                    move = random.randint(1,5)
                    game.player.rect.x = pos_base
                    for i in range(move):
                        if game.player.rect.x == 1:
                            game.player.rect.x = 1
                        game.player.rect.x += 1
                        game.player.move_right()

                game.playerII.move_right()
                p1 = game.player.rect.x
                p2 = game.playerII.rect.x
                if p1 < (p2 - 100):
                    #time.sleep(0.5)
                    if (n % 2) == 0:
                        '''
                        for i in range(25):
                            game.player.rect.x += 1
                            game.player.move_right()
                        n += 1
                        '''
                    else:
                        game.player.rect.x += 0
                        n+= 1
                if p1 > p2:
                    game.player.rect.x -= 10
                    game.player.move_left()
                    n += 1


                print('p1:')
                print(game.player.rect.x)
                print('p2:')
                print(game.playerII.rect.x)

            if game.playerII.rect.x > game_offset_x + 650:
                game.playerII.rect.x = game_offset_x + 650

            #main
            elif game.pressed.get(pyg.K_z):
                p1 = game.player.rect.x
                p2 = game.playerII.rect.x
                if deuxieme_personnage == 1:
                    screen.blit(pyg.image.load("Assets/1r/1coupr.png"), game.playerII.rect)
                elif deuxieme_personnage == 2:
                    screen.blit(pyg.image.load("Assets/2r/2coupr.png"), game.playerII.rect)
                elif deuxieme_personnage == 3:
                    screen.blit(pyg.image.load("Assets/3r/3coupr.png"), game.playerII.rect)
                if p2 - p1 <= ECART2:
                    if (n % 2) == 0:                                                                           # coup de poing joueurs
                        player.health -= 0.1
                        playerII.exp -= 0.3
                        if playerII.exp <= 10 and playerII.exp >= 0 :
                            if deuxieme_personnage == 1:
                                screen.blit(pyg.image.load("Assets/mainSPR.png"), game.playerII.rect)
                            elif deuxieme_personnage == 2:
                                screen.blit(pyg.image.load("Assets/mainSDR.png"), game.playerII.rect)
                            elif deuxieme_personnage == 3:
                                screen.blit(pyg.image.load("Assets/mainSTR.png"), game.playerII.rect)
                                if p2 - p1 <= ECART2:
                                    player.health -= 0.05
                        elif playerII.exp < 0:
                            playerII.exp = 100
                        n += 1
                    else:
                        player.health -= 0.1
                        playerII.exp -= 0.3
                        if playerII.exp <= 10 and playerII.exp >= 0 :
                            if deuxieme_personnage == 1:
                                screen.blit(pyg.image.load("Assets/mainSPR.png"), game.playerII.rect)
                            elif deuxieme_personnage == 2:
                                screen.blit(pyg.image.load("Assets/mainSDR.png"), game.playerII.rect)
                            elif deuxieme_personnage == 3:
                                screen.blit(pyg.image.load("Assets/mainSTR.png"), game.playerII.rect)
                                if p2 - p1 <= ECART2:
                                    player.health -= 0.1
                        elif playerII.exp < 0:
                            playerII.exp = 100
                        n += 1
                '''
                if p2 - p1 <= ECART and (n % 2) == 0:
                    p1 = game.player.rect.x
                    p2 = game.playerII.rect.x
                    if premier_personnage == 1:
                        screen.blit(pygame.image.load("Assets/1/1coup.png"), game.player.rect)
                    elif premier_personnage == 2:
                        screen.blit(pygame.image.load("Assets/2/2coup.png"), game.player.rect)
                    elif premier_personnage == 3:
                        screen.blit(pygame.image.load("Assets/3/3coup.png"), game.player.rect)
                    if game.pressed.get(pygame.K_i):
                        playerII.health -= 0.001
                        player.exp -= 0.05
                        if player.exp <= 10 and player.exp >= 0:
                            if premier_personnage == 1:
                                screen.blit(pygame.image.load("Assets/mainP.png"), game.player.rect)
                            elif premier_personnage == 2:
                                screen.blit(pygame.image.load("Assets/mainSD.png"), game.player.rect)
                            elif premier_personnage == 3:
                                screen.blit(pygame.image.load("Assets/mainST.png"), game.player.rect)
                                if p2 - p1 <= ECART:
                                    playerII.health -= 0.05
                        elif player.exp < 0:
                            player.exp = 100
                    else:
                        playerII.health -= 0.01
                        player.exp -= 0.05
                        if player.exp <= 10 and player.exp >= 0:
                            if premier_personnage == 1:
                                screen.blit(pygame.image.load("Assets/mainP.png"), game.player.rect)
                            elif premier_personnage == 2:
                                screen.blit(pygame.image.load("Assets/mainSD.png"), game.player.rect)
                            elif premier_personnage == 3:
                                screen.blit(pygame.image.load("Assets/mainST.png"), game.player.rect)
                                if p2 - p1 <= ECART:
                                    playerII.health -= 0.1
                        elif player.exp < 0:
                            player.exp = 100
                    n += 1
                '''
            p1 = game.player.rect.x
            p2 = game.playerII.rect.x
            if p2 - p1 <= ECART2:
                momentum_coup = random.randint(1,50)
                if cooldown_coup < 30 and cooldown_coup > 0:
                    momentum_coup = 1
                if momentum_coup == 1: 
                    if cooldown_coup < 0:
                        cooldown_coup = 0                                                       # coup de poings bot
                    playerII.health -= 0.1
                    player.exp -= 0.7
                    if premier_personnage == 1:
                        screen.blit(pyg.image.load("Assets/1/1coup.png"), game.player.rect)
                    elif premier_personnage == 2:
                        screen.blit(pyg.image.load("Assets/2/2coup.png"), game.player.rect)
                    elif premier_personnage == 3:
                        screen.blit(pyg.image.load("Assets/3/3coup.png"), game.player.rect)
                        if p2 - p1 <= ECART2:
                            player.health -= 0.1
                    cooldown_coup += 1
                    print(cooldown_coup)
                    if cooldown_coup > 30:
                        cooldown_coup = -1
                elif player.exp < 0:
                    player.exp = 100
                n += 1



            if player.health <= 0:
                victoire_deuxieme_personnage += 1

                if nb_de_combat < nb_de_round :
                    selecCOMBAT = False
                    selecCombat = True
                else:
                    selecCOMBAT = False
                    selecCombat = False
                    dead = True

            pyg.display.flip()

            # si joueur ferme fenetre
            for event in pyg.event.get():
                # pour vérifier
                if event.type == pyg.QUIT:
                    selecCOMBAT = False
                    selecCombat = False
                    running = False

                # joueur lache une touche
                elif event.type == pyg.KEYDOWN:
                    # touche utiliser ?
                    game.pressed[event.key] = True
                elif event.type == pyg.KEYUP:
                    game.pressed[event.key] = False


    while dead:
        screen.blit(ordi, (0,0))
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                Option = False
                running = False
        pyg.display.flip()

        '''
        barre = pyg.transform.scale(barre, (765,28))
        screen.blit(barre, (game_offset_x, game_offset_y - 28))
        FondAccueil()
        button_continuer()
        KO()
        pyg.display.flip()
        for event in pyg.event.get():
            if event.type == pyg.MOUSEBUTTONDOWN:
                if Button_continuer_rect.collidepoint(event.pos):
                    dead = False
                    Fin_de_combat = True
            if event.type == pyg.QUIT:
                Option = False
                running = False
        '''
        

                
    while Fin_de_combat:
        if victoire_premier_personnage > victoire_deuxieme_personnage:
            if premier_personnage == 1:
                if deuxieme_personnage == 1:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_premier_perso_defaite()
                    pyg.display.flip()
                elif deuxieme_personnage == 2:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pyg.display.flip()
                else:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pyg.display.flip()
            if premier_personnage == 2:
                if deuxieme_personnage == 1:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_premier_perso_defaite()
                    pyg.display.flip()
                elif deuxieme_personnage == 2:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pyg.display.flip()
                else:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pyg.display.flip()
            if premier_personnage == 3:
                if deuxieme_personnage == 1:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_premier_perso_defaite()
                    pyg.display.flip()
                elif deuxieme_personnage == 2:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pyg.display.flip()
                else:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pyg.display.flip()
        if victoire_premier_personnage < victoire_deuxieme_personnage :
            if deuxieme_personnage == 1:
                if premier_personnage == 1:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_premier_perso_defaite()
                    pyg.display.flip()
                elif premier_personnage == 2:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pyg.display.flip()
                else:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pyg.display.flip()
            elif deuxieme_personnage == 2:
                if premier_personnage == 1:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_premier_perso_defaite()
                    pyg.display.flip()
                elif premier_personnage == 2:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pyg.display.flip()
                else:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pyg.display.flip()
            else:
                if premier_personnage == 1:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_premier_perso_defaite()
                    pyg.display.flip()
                elif premier_personnage == 2:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pyg.display.flip()
                else:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pyg.display.flip()

        if victoire_premier_personnage == victoire_deuxieme_personnage:
            if deuxieme_personnage == 1:
                if premier_personnage == 1:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_premier_perso_defaite()
                    pyg.display.flip()
                elif premier_personnage == 2:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pyg.display.flip()
                else:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pyg.display.flip()
            elif deuxieme_personnage == 2:
                if premier_personnage == 1:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_premier_perso_defaite()
                    pyg.display.flip()
                elif premier_personnage == 2:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pyg.display.flip()
                else:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pyg.display.flip()
            else:
                if premier_personnage == 1:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_premier_perso_defaite()
                    pyg.display.flip()
                elif premier_personnage == 2:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pyg.display.flip()
                else:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pyg.display.flip()

        for event in pyg.event.get():
            if event.type == pyg.MOUSEBUTTONDOWN:
                if bouton_menu_rect.collidepoint(event.pos):
                    Fin_de_combat = False
                    PageAccueil = True
                if bouton_rejouer_rect.collidepoint(event.pos):
                    Fin_de_combat = False
                    selectionP = True
            if event.type == pyg.QUIT:
                Fin_de_combat = False
                running = False
        
    
    while Combat:

        # generer le jeu
        game = Game()

        # charger joueur
        player = Player()
        playerII = PlayerII()

        nb_de_combat += 1
        Fond += 1

        COMBAT = True

        # boucle si vrai
        while COMBAT:

            # appliquer arrière plan
            if (Fond % 2) == 0:
                backgroundCPremier()
            else:
                backgroundCDeuxieme()

            if deuxieme_personnage == 1:
                personnage_de_droite_garde = pyg.image.load("Assets/1r/1r.png")
            elif deuxieme_personnage == 2:
                personnage_de_droite_garde = pyg.image.load("Assets/2r/2r.png")
            elif deuxieme_personnage == 3:
                personnage_de_droite_garde = pyg.image.load("Assets/3r/3r.png")

            screen.blit(personnage_de_droite_garde, game.playerII.rect)

            if premier_personnage == 1:
                personnage_de_gauche_garde = pyg.image.load("Assets/1/1.png")
            elif premier_personnage == 2:
                personnage_de_gauche_garde = pyg.image.load("Assets/2/2.png")
            elif premier_personnage == 3:
                personnage_de_gauche_garde = pyg.image.load("Assets/3/3.png")

            screen.blit(personnage_de_gauche_garde, game.player.rect)

            player.update_health_bar(screen)
            playerII.update_health_bar(screen)
            player.update_exp_bar(screen)
            playerII.update_exp_bar(screen)


            #prot 1

            if game.pressed.get(pyg.K_s):
                p1 = game.player.rect.x
                p2 = game.playerII.rect.x
                if game.pressed.get(pyg.K_DOWN):
                    if p2 - p1 <= ECART2:
                        player.health -= 0.000001
                    else :
                        player.health = player.health
                else :
                    player.health = player.health

            #prot 2
            '''if game.pressed.get(pygame.K_s):
                p1 = game.player.rect.x
                p2 = game.playerII.rect.x
                if game.pressed.get(pygame.K_DOWN):
                    if p2 - p1 <= ECART2:
                        player.health -= 0.000001
                    else :
                        player.health = player.health
                else :
                    player.health = player.health'''




            # joueur -> gauche ou droite

            if game.pressed.get(pyg.K_q) and game.player.rect.x > 0:
                p1 = game.player.rect.x
                p2 = game.playerII.rect.x
                '''if p1 < (p2 - 5):
                    game.player.rect.x = game.player.rect.x + 0
                else:
                    game.player.rect.x = game.player.rect.x + 1'''
                game.player.move_left()

                print('p1:')
                print(game.player.rect.x)
                print('p2:')
                print(game.playerII.rect.x)

            elif game.pressed.get(pyg.K_d) and game.player.rect.x + game.player.rect.width < screen.get_width():
                p1 = game.player.rect.x
                p2 = game.playerII.rect.x
                if p1 > (p2 - ECART):
                    game.player.rect.x = game.player.rect.x + 0
                else:
                    game.player.rect.x = game.player.rect.x + 1
                    game.player.move_right()

                print('p1:')
                print(game.player.rect.x)
                print('p2:')
                print(game.playerII.rect.x)





            #main
            if game.pressed.get(pyg.K_z):
                p1 = game.player.rect.x
                p2 = game.playerII.rect.x
                if premier_personnage == 1:
                    screen.blit(pyg.image.load("Assets/1/1coup.png"), game.player.rect)
                elif premier_personnage == 2:
                    screen.blit(pyg.image.load("Assets/2/2coup.png"), game.player.rect)
                elif premier_personnage == 3:
                    screen.blit(pyg.image.load("Assets/3/3coup.png"), game.player.rect)
                if p2 - p1 <= ECART2:
                    if game.pressed.get(pyg.K_i):
                        playerII.health -= 0.01
                        player.exp -= 0.5
                        if player.exp <= 10 and player.exp >= 0 :
                            if premier_personnage == 1:
                                screen.blit(pyg.image.load("Assets/mainP.png"), game.player.rect)
                            elif premier_personnage == 2:
                                screen.blit(pyg.image.load("Assets/mainSD.png"), game.player.rect)
                            elif premier_personnage == 3:
                                screen.blit(pyg.image.load("Assets/mainST.png"), game.player.rect)
                                if p2 - p1 <= ECART2:
                                    playerII.health -= 0.5
                        elif player.exp < 0:
                            player.exp = 100
                    else:
                        playerII.health -= 0.1
                        player.exp -= 0.5
                        if player.exp <= 10 and player.exp >= 0 :
                            if premier_personnage == 1:
                                screen.blit(pyg.image.load("Assets/mainP.png"), game.player.rect)
                            elif premier_personnage == 2:
                                screen.blit(pyg.image.load("Assets/mainSD.png"), game.player.rect)
                            elif premier_personnage == 3:
                                screen.blit(pyg.image.load("Assets/mainST.png"), game.player.rect)
                                if p2 - p1 <= ECART2:
                                    playerII.health -= 1
                        elif player.exp < 0:
                            player.exp = 100
                            


            if playerII.health <= 0:
                victoire_premier_personnage += 1

                if nb_de_combat < nb_de_round :
                    COMBAT = False
                    Combat = True
                else:
                    COMBAT = False
                    Combat = False
                    dead = True

            # joueur2 -> gauche ou droite
            if game.pressed.get(pyg.K_k) and game.playerII.rect.x > 0:
                p1 = game.player.rect.x
                p2 = game.playerII.rect.x

                if p2 < (p1 + ECART):
                    game.playerII.rect.x = game.playerII.rect.x + 0
                else:
                    game.playerII.rect.x = game.playerII.rect.x - 1
                    game.playerII.move_left()

                print('p1:')
                print(game.player.rect.x)
                print('p2:')
                print(game.playerII.rect.x)

            elif game.pressed.get(
                    pyg.K_m) and game.playerII.rect.x + game.playerII.rect.width < screen.get_width():
                game.playerII.move_right()

                print('p1:')
                print(game.player.rect.x)
                print('p2:')
                print(game.playerII.rect.x)

            #main
            elif game.pressed.get(pyg.K_o):
                p1 = game.player.rect.x
                p2 = game.playerII.rect.x
                if deuxieme_personnage == 1:
                    screen.blit(pyg.image.load("Assets/1r/1coupr.png"), game.playerII.rect)
                elif deuxieme_personnage == 2:
                    screen.blit(pyg.image.load("Assets/2r/2coupr.png"), game.playerII.rect)
                elif deuxieme_personnage == 3:
                    screen.blit(pyg.image.load("Assets/3r/3coupr.png"), game.playerII.rect)
                if p2 - p1 <= ECART2:
                    if game.pressed.get(pyg.K_a):
                        player.health -= 0.01
                        playerII.exp -= 0.5
                        if playerII.exp <= 10 and playerII.exp >= 0 :
                            if deuxieme_personnage == 1:
                                screen.blit(pyg.image.load("Assets/mainSPR.png"), game.playerII.rect)
                            elif deuxieme_personnage == 2:
                                screen.blit(pyg.image.load("Assets/mainSDR.png"), game.playerII.rect)
                            elif deuxieme_personnage == 3:
                                screen.blit(pyg.image.load("Assets/mainSTR.png"), game.playerII.rect)
                                if p2 - p1 <= ECART2:
                                    player.health -= 0.5
                        elif playerII.exp < 0:
                            playerII.exp = 100
                    else:
                        player.health -= 0.1
                        playerII.exp -= 0.5
                        if playerII.exp <= 10 and playerII.exp >= 0 :
                            if deuxieme_personnage == 1:
                                screen.blit(pyg.image.load("Assets/mainSPR.png"), game.playerII.rect)
                            elif deuxieme_personnage == 2:
                                screen.blit(pyg.image.load("Assets/mainSDR.png"), game.playerII.rect)
                            elif deuxieme_personnage == 3:
                                screen.blit(pyg.image.load("Assets/mainSTR.png"), game.playerII.rect)
                                if p2 - p1 <= ECART2:
                                    player.health -= 1
                        elif playerII.exp < 0:
                            playerII.exp = 100
                    





                '''if p2 - p1 <= ECART2:
                    player.health = player.health - 10'''


            if player.health <= 0:
                victoire_deuxieme_personnage += 1

                if nb_de_combat < nb_de_round :
                    COMBAT = False
                    Combat = True
                else:
                    COMBAT = False
                    Combat = False
                    dead = True

            pyg.display.flip()

            # si joueur ferme fenetre
            for event in pyg.event.get():
                # pour vérifier
                if event.type == pyg.QUIT:
                    COMBAT = False
                    Combat = False
                    running = False

                # joueur lache une touche
                elif event.type == pyg.KEYDOWN:
                    # touche utiliser ?
                    game.pressed[event.key] = True
                elif event.type == pyg.KEYUP:
                    game.pressed[event.key] = False

    while dead:
        FondAccueil()
        button_continuer()
        KO()
        pyg.display.flip()
        for event in pyg.event.get():
            if event.type == pyg.MOUSEBUTTONDOWN:
                if Button_continuer_rect.collidepoint(event.pos):
                    dead = False
                    Fin_de_combat = True
            if event.type == pyg.QUIT:
                Option = False
                running = False

    while Fin_de_combat:
        if victoire_premier_personnage > victoire_deuxieme_personnage:
            if premier_personnage == 1:
                if deuxieme_personnage == 1:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_premier_perso_defaite()
                    pyg.display.flip()
                elif deuxieme_personnage == 2:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pyg.display.flip()
                else:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pyg.display.flip()
            if premier_personnage == 2:
                if deuxieme_personnage == 1:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_premier_perso_defaite()
                    pyg.display.flip()
                elif deuxieme_personnage == 2:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pyg.display.flip()
                else:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pyg.display.flip()
            if premier_personnage == 3:
                if deuxieme_personnage == 1:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_premier_perso_defaite()
                    pyg.display.flip()
                elif deuxieme_personnage == 2:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pyg.display.flip()
                else:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pyg.display.flip()
        if victoire_premier_personnage < victoire_deuxieme_personnage :
            if deuxieme_personnage == 1:
                if premier_personnage == 1:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_premier_perso_defaite()
                    pyg.display.flip()
                elif premier_personnage == 2:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pyg.display.flip()
                else:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pyg.display.flip()
            elif deuxieme_personnage == 2:
                if premier_personnage == 1:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_premier_perso_defaite()
                    pyg.display.flip()
                elif premier_personnage == 2:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pyg.display.flip()
                else:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pyg.display.flip()
            else:
                if premier_personnage == 1:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_premier_perso_defaite()
                    pyg.display.flip()
                elif premier_personnage == 2:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pyg.display.flip()
                else:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pyg.display.flip()

        if victoire_premier_personnage == victoire_deuxieme_personnage:
            if deuxieme_personnage == 1:
                if premier_personnage == 1:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_premier_perso_defaite()
                    pyg.display.flip()
                elif premier_personnage == 2:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pyg.display.flip()
                else:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pyg.display.flip()
            elif deuxieme_personnage == 2:
                if premier_personnage == 1:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_premier_perso_defaite()
                    pyg.display.flip()
                elif premier_personnage == 2:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pyg.display.flip()
                else:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pyg.display.flip()
            else:
                if premier_personnage == 1:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_premier_perso_defaite()
                    pyg.display.flip()
                elif premier_personnage == 2:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pyg.display.flip()
                else:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pyg.display.flip()

        for event in pyg.event.get():
            if event.type == pyg.MOUSEBUTTONDOWN:
                if bouton_menu_rect.collidepoint(event.pos):
                    Fin_de_combat = False
                    PageAccueil = True
                if bouton_rejouer_rect.collidepoint(event.pos):
                    Fin_de_combat = False
                    selectionP = True
            if event.type == pyg.QUIT:
                Fin_de_combat = False
                running = False

print("Fermeture du jeu")
pyg.quit()