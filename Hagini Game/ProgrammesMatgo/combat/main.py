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

import pygame
import math
import time
import random

pygame.init()

pygame.display.set_caption("FightinGODS")
screen = pygame.display.set_mode((750, 420))

'''Definition'''
'''page d'accueil'''

Fond_accueil = pygame.image.load("Assets/IMG-0711.PNG")
Fond_Round = pygame.image.load("Assets/IMG-0704.PNG")

Fond_Commande = pygame.image.load("Assets/Mvt-Joueur-.png")
Fond_instru = pygame.image.load("Assets/instru1.png")
Fond_erreur = pygame.image.load("Assets/solomode.png")

fleche = pygame.image.load("Assets/fleche.png")

moment_move = 0

momentum = 0

def countdown(num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(min_sec_format, end='/r')
        time.sleep(1)
        num_of_secs -= 1

    print('Countdown finished.')

def FondAccueil():
    screen.blit(Fond_accueil, (0, 0))

def Fonderreur():
    screen.blit(Fond_erreur, (0, 0))

def FondCommande():
    screen.blit(Fond_Commande, (0, 0))

def FondTru():
    screen.blit(Fond_instru, (0, 0))


play_button = pygame.image.load("Assets/IMG-0694.PNG")
play_button = pygame.transform.scale(play_button, (200, 92))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_height() / 1.5)
play_button_rect.y = math.ceil(screen.get_width() / 3.5)


def Bouton_de_jeu():
    screen.blit(play_button, play_button_rect)


option_button = pygame.image.load("Assets/boption.png")
option_button = pygame.transform.scale(option_button, (60, 60))
option_button_rect = option_button.get_rect()
option_button_rect.x = math.ceil(screen.get_width() / 1.1)
option_button_rect.y = math.ceil(screen.get_height() / 1.2)


def optionButton():
    screen.blit(option_button, option_button_rect)


commande_button = pygame.image.load("Assets/instru.png")
commande_button = pygame.transform.scale(commande_button, (100, 46))
commande_button_rect = commande_button.get_rect()
commande_button_rect.x = math.ceil(screen.get_width() / 1.20)
commande_button_rect.y = math.ceil(screen.get_height() / 9.5)

def commandebutton():
    screen.blit(commande_button, commande_button_rect)

    
    
instru_button = pygame.image.load("Assets/IMG-0695.PNG")
instru_button = pygame.transform.scale(instru_button, (100, 46))
instru_button_rect = instru_button.get_rect()
instru_button_rect.x = math.ceil(screen.get_width() / 2.5)
instru_button_rect.y = math.ceil(screen.get_height() / 2.1)




def instrubutton():
    screen.blit(instru_button, instru_button_rect)
    


solo_button = pygame.image.load("Assets/solo.png")
solo_button = pygame.transform.scale(solo_button, (200, 92))
solo_button_rect = solo_button.get_rect()
solo_button_rect.x = math.ceil(screen.get_width() / 2.5)
solo_button_rect.y = math.ceil(screen.get_height() / 2.5)

def solobutton():
    screen.blit(solo_button, solo_button_rect)
    
deux_button = pygame.image.load("Assets/deuxjoueurs.png")
deux_button = pygame.transform.scale(deux_button, (200, 92))
deux_button_rect = deux_button.get_rect()
deux_button_rect.x = math.ceil(screen.get_width() / 2.5)
deux_button_rect.y = math.ceil(screen.get_height() / 1.5)

def DeuxJoueurs():
    screen.blit(deux_button, deux_button_rect)

deux_Button = pygame.image.load("Assets/deuxjoueurs.png")
deux_Button = pygame.transform.scale(deux_Button, (100, 46))
deux_Button_rect = deux_Button.get_rect()
deux_Button_rect.x = math.ceil(screen.get_width() / 1.2)
deux_Button_rect.y = math.ceil(screen.get_height() / 5.5)

def deuxjoueurs():
    screen.blit(deux_Button, deux_Button_rect)

def Fond_joueurP():
    screen.blit(Fond_accueil, (0, 0))
    
def Fond_selectJ():
    screen.blit(Fond_Round, (0, 0))
    


def Fond_joueurD():
    screen.blit(Fond_accueil, (0, 0))
    


def Fond_round():
    screen.blit(Fond_Round, (0, 0))
    
def Fond_commande():
    screen.blit(Fond_Round, (0, 0))    


def Fond_d_option():
    screen.blit(OptionFond, (0, 0))

backgroundPS = pygame.image.load("Assets/IMG-0705.PNG")


def background_Premiere_Selection():
    screen.blit(backgroundPS, (0, 0))


backgroundDS = pygame.image.load("Assets/IMG-0706.PNG")


def background_Deuxieme_Selection():
    screen.blit(backgroundDS, (0, 0))


premierPerso = pygame.image.load("Assets/FOURENS.png")
premierPerso = pygame.transform.scale(premierPerso, (138, 320))
premierPerso_rect = premierPerso.get_rect()
premierPerso_rect.x = math.ceil(screen.get_width() / 7.5)
premierPerso_rect.y = math.ceil(screen.get_height() / 5)


def premierPersonnage():
    screen.blit(premierPerso, premierPerso_rect)


deuxiemePerso = pygame.image.load("Assets/deuxieme_personnage.png")
deuxiemePerso = pygame.transform.scale(deuxiemePerso, (138, 217))
deuxiemePerso_rect = deuxiemePerso.get_rect()
deuxiemePerso_rect.x = math.ceil(screen.get_width() / 2.5)
deuxiemePerso_rect.y = math.ceil(screen.get_height() / 4.3)


def deuxiemePersonnage():
    screen.blit(deuxiemePerso, deuxiemePerso_rect)


troisiemePerso = pygame.image.load("Assets/troisieme_personnage.png")
troisiemePerso = pygame.transform.scale(troisiemePerso, (138, 304))
troisiemePerso_rect = troisiemePerso.get_rect()
troisiemePerso_rect.x = math.ceil(screen.get_width() / 1.5)
troisiemePerso_rect.y = math.ceil(screen.get_height() / 4.8)


def troisiemePersonnage():
    screen.blit(troisiemePerso, troisiemePerso_rect)

'''ROUND'''

roundP = pygame.image.load("Assets/tif/Pround.PNG")
roundP = pygame.transform.scale(roundP, (150, 150))
roundP_rect = roundP.get_rect()
roundP_rect.x = math.ceil(screen.get_width() / 7.5)
roundP_rect.y = math.ceil(screen.get_height() / 2.8)


def ROUNDP():
    screen.blit(roundP, roundP_rect)

roundD = pygame.image.load("Assets/Dround.PNG")
roundD = pygame.transform.scale(roundD, (150, 150))
roundD_rect = roundP.get_rect()
roundD_rect.x = math.ceil(screen.get_width() / 2.5)
roundD_rect.y = math.ceil(screen.get_height() / 2.8)


def ROUNDD():
    screen.blit(roundD, roundD_rect)

roundT = pygame.image.load("Assets/tif/Tround.PNG")
roundT = pygame.transform.scale(roundT, (150, 150))
roundT_rect = roundT.get_rect()
roundT_rect.x = math.ceil(screen.get_width() / 1.5)
roundT_rect.y = math.ceil(screen.get_height() / 2.8)


def ROUNDT():
    screen.blit(roundT, roundT_rect)

'''Combat'''

backgroundCP = pygame.image.load("Assets/fond_jeu_2.jpg")
backgroundCP = pygame.transform.scale(backgroundCP, (750, 420))


def backgroundCPremier():
    screen.blit(backgroundCP, (0, 0))


backgroundCD = pygame.image.load("Assets/fond_jeu.jpg")
backgroundCD = pygame.transform.scale(backgroundCD, (750, 420))


def backgroundCDeuxieme():
    screen.blit(backgroundCD, (0, 0))






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
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.health = 100
        self.exp = 100
        self.max_exp = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 1
        self.image = pygame.image.load("Assets/2/2.png")
        self.image2 = pygame.image.load("Assets/2/2coup.png")
        self.rect = self.image.get_rect()
        self.rect.x = 255
        self.rect.y = 160

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
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        # puis celle de couleur rouge
        pygame.draw.rect(surface, bar_color, bar_position)

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
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        # puis celle de couleur rouge
        pygame.draw.rect(surface, bar_color, bar_position)

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
class PlayerII(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.health = 100
        self.max_health = 100
        self.exp = 100
        self.max_exp = 100
        self.attack = 10
        self.velocity = 1
        self.image = pygame.image.load('Assets/3r/3r.png')
        self.image2 = pygame.image.load('Assets/3r/3coupr.png')
        self.rect = self.image.get_rect()
        self.rect.x = 445
        self.rect.y = 153

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
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        # puis celle de couleur rouge
        pygame.draw.rect(surface, bar_color, bar_position)

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
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        # puis celle de couleur rouge
        pygame.draw.rect(surface, bar_color, bar_position)


    def move_left(self):
        '''if not self.game.check_collision(self, self.game.player):'''
        self.rect.x -= self.velocity

    def move_right(self):
        self.rect.x += self.velocity


'''Fin de combat '''

background_Fin = pygame.image.load("Assets/IMG-0707.PNG")

background_Egalite = pygame.image.load("Assets/Fin-Egalite.png")


def Fond_de_fin():
    screen.blit(background_Fin, (0, 0))

def Fond_Egalite():
    screen.blit(background_Egalite, (0, 0))


Button_continuer = pygame.image.load("Assets/IMG-0693.PNG")
Button_continuer = pygame.transform.scale(Button_continuer, (150, 85))
Button_continuer_rect = Button_continuer.get_rect()
Button_continuer_rect.x = math.ceil(screen.get_height() / 0.75)
Button_continuer_rect.y = math.ceil(screen.get_width() / 2.4)


def button_continuer():
    screen.blit(Button_continuer, Button_continuer_rect)


image_KO = pygame.image.load("Assets/IMG-0702.PNG")
image_KO = pygame.transform.scale(image_KO, (400, 400))
image_KO_rect = Button_continuer.get_rect()
image_KO_rect.x = math.ceil(screen.get_height() / 2.5)
image_KO_rect.y = math.ceil(screen.get_width() / 12)


def KO():
    screen.blit(image_KO, image_KO_rect)


bouton_rejouer = pygame.image.load("Assets/IMG-0695.PNG")
bouton_rejouer = pygame.transform.scale(bouton_rejouer, (150, 70))
bouton_rejouer_rect = bouton_rejouer.get_rect()
bouton_rejouer_rect.x = math.ceil(screen.get_height() / 6)
bouton_rejouer_rect.y = math.ceil(screen.get_width() / 2.3)


def button_rejouer():
    screen.blit(bouton_rejouer, bouton_rejouer_rect)


bouton_menu = pygame.image.load("Assets/IMG-0696.PNG")
bouton_menu = pygame.transform.scale(bouton_menu, (150, 70))
bouton_menu_rect = bouton_menu.get_rect()
bouton_menu_rect.x = math.ceil(screen.get_width() / 1.5)
bouton_menu_rect.y = math.ceil(screen.get_height() / 1.285)


def button_menu():
    screen.blit(bouton_menu, bouton_menu_rect)


premier_perso_fin_victoire = pygame.image.load("Assets/Fin_du_match_premier_perso.png")
premier_perso_fin_victoire = pygame.transform.scale(premier_perso_fin_victoire, (180, 180))
premier_perso_fin_victoire_rect = premier_perso_fin_victoire.get_rect()
premier_perso_fin_victoire_rect.x = math.ceil(screen.get_width() / 12.5)
premier_perso_fin_victoire_rect.y = math.ceil(screen.get_height() / 3.2)


def Fin_premier_perso_victoire():
    screen.blit(premier_perso_fin_victoire, premier_perso_fin_victoire_rect)


deuxieme_perso_fin_victoire = pygame.image.load("Assets/Fin_du_match_deuxieme_perso.png")
deuxieme_perso_fin_victoire = pygame.transform.scale(deuxieme_perso_fin_victoire, (180, 180))
deuxieme_perso_fin_victoire_rect = deuxieme_perso_fin_victoire.get_rect()
deuxieme_perso_fin_victoire_rect.x = math.ceil(screen.get_width() / 12.5)
deuxieme_perso_fin_victoire_rect.y = math.ceil(screen.get_height() / 3.2)


def Fin_deuxieme_perso_victoire():
    screen.blit(deuxieme_perso_fin_victoire, deuxieme_perso_fin_victoire_rect)


troisieme_perso_fin_victoire = pygame.image.load("Assets/Fin_du_match_troisieme_perso.png")
troisieme_perso_fin_victoire = pygame.transform.scale(troisieme_perso_fin_victoire, (180, 180))
troisieme_perso_fin_victoire_rect = troisieme_perso_fin_victoire.get_rect()
troisieme_perso_fin_victoire_rect.x = math.ceil(screen.get_width() / 12.5)
troisieme_perso_fin_victoire_rect.y = math.ceil(screen.get_height() / 3.2)


def Fin_troisieme_perso_victoire():
    screen.blit(troisieme_perso_fin_victoire, troisieme_perso_fin_victoire_rect)


premier_perso_fin_defaite = pygame.image.load("Assets/Fin_du_match_premier_perso.png")
premier_perso_fin_defaite = pygame.transform.scale(premier_perso_fin_defaite, (180, 180))
premier_perso_fin_defaite_rect = premier_perso_fin_defaite.get_rect()
premier_perso_fin_defaite_rect.x = math.ceil(screen.get_width() / 1.6)
premier_perso_fin_defaite_rect.y = math.ceil(screen.get_height() / 3.2)


def Fin_premier_perso_defaite():
    screen.blit(premier_perso_fin_defaite, premier_perso_fin_defaite_rect)


deuxieme_perso_fin_defaite = pygame.image.load("Assets/Fin_du_match_deuxieme_perso.png")
deuxieme_perso_fin_defaite = pygame.transform.scale(deuxieme_perso_fin_defaite, (180, 180))
deuxieme_perso_fin_defaite_rect = deuxieme_perso_fin_defaite.get_rect()
deuxieme_perso_fin_defaite_rect.x = math.ceil(screen.get_width() / 1.6)
deuxieme_perso_fin_defaite_rect.y = math.ceil(screen.get_height() / 3.2)


def Fin_deuxieme_perso_defaite():
    screen.blit(deuxieme_perso_fin_defaite, deuxieme_perso_fin_defaite_rect)


troisieme_perso_fin_defaite = pygame.image.load("Assets/Fin_du_match_troisieme_perso.png")
troisieme_perso_fin_defaite = pygame.transform.scale(troisieme_perso_fin_defaite, (180, 180))
troisieme_perso_fin_defaite_rect = troisieme_perso_fin_victoire.get_rect()
troisieme_perso_fin_defaite_rect.x = math.ceil(screen.get_width() / 1.6)
troisieme_perso_fin_defaite_rect.y = math.ceil(screen.get_height() / 3.2)


def Fin_troisieme_perso_defaite():
    screen.blit(troisieme_perso_fin_defaite, troisieme_perso_fin_defaite_rect)


'''Jeu'''

running = True
PageAccueil = True
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
selecCombat = False
COMBAT = False
selecCOMBAT = False
ROUND = False
Jeu = False
DeuxJ = False
premier_personnage = 0
deuxieme_personnage = 0
nb_de_round = 0
nb_de_combat = 0
victoire_premier_personnage = 0
victoire_deuxieme_personnage = 0
Fond = 1

while running:

    while PageAccueil:
        FondAccueil()
        optionButton()
        Bouton_de_jeu()
        optionButton()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    PageAccueil = False
                    Jeu = True
                if option_button_rect.collidepoint(event.pos):
                    PageAccueil = False
                    Option = True
            if event.type == pygame.QUIT:
                PageAccueil = False
                running = False
                
    while Jeu:
        FondAccueil()
        solobutton()
        DeuxJoueurs()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if solo_button_rect.collidepoint(event.pos):
                    Jeu = False
                    selecP = True
                if deux_button_rect.collidepoint(event.pos):
                    Jeu = False
                    selectionP = True
            if event.type == pygame.QUIT:
                Jeu = False
                running = False

    while selecP:
        background_Premiere_Selection()
        premierPersonnage()
        deuxiemePersonnage()
        troisiemePersonnage()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
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
            if event.type == pygame.QUIT:
                selecP = False
                running = False

    while selecD:
        background_Deuxieme_Selection()
        premierPersonnage()
        deuxiemePersonnage()
        troisiemePersonnage()

        pygame.display.flip()
        victoire_premier_personnage = 0
        victoire_deuxieme_personnage = 0

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
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
            if event.type == pygame.QUIT:
                selecP = False
                running = False

    while selecROUND:
        nb_de_round = 0
        nb_de_combat = 0
        Fond_round()
        ROUNDP()
        ROUNDD()
        ROUNDT()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
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
            if event.type == pygame.QUIT:
                selecROUND = False
                running = False

    while Option:
        FondCommande()
        optionButton()
        commandebutton()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if option_button_rect.collidepoint(event.pos):
                    Option = False
                    PageAccueil = True
                elif commande_button_rect.collidepoint(event.pos):
                    Option = False
                    Commande = True
            if event.type == pygame.QUIT:
                Option = False
                running = False

    while Commande:
        FondTru()
        optionButton()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if option_button_rect.collidepoint(event.pos):
                    Commande = False
                    Option = True
            if event.type == pygame.QUIT:
                Commande = False
                running = False

    while selectionP:
        background_Premiere_Selection()
        premierPersonnage()
        deuxiemePersonnage()
        troisiemePersonnage()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
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
            if event.type == pygame.QUIT:
                selectionP = False
                running = False

    while selectionD:
        background_Deuxieme_Selection()
        premierPersonnage()
        deuxiemePersonnage()
        troisiemePersonnage()

        pygame.display.flip()
        victoire_premier_personnage = 0
        victoire_deuxieme_personnage = 0

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
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
            if event.type == pygame.QUIT:
                selectionP = False
                running = False
                
    while ROUND:
        nb_de_round = 0
        nb_de_combat = 0
        Fond_round()
        ROUNDP()
        ROUNDD()
        ROUNDT()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
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
            if event.type == pygame.QUIT:
                ROUND = False
                running = False




    while selecCombat:
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

            g_or_d = random.randint(1,2)
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
                personnage_de_droite_garde = pygame.image.load("Assets/1r/1r.png")
            elif deuxieme_personnage == 2:
                personnage_de_droite_garde = pygame.image.load("Assets/2r/2r.png")
            elif deuxieme_personnage == 3:
                personnage_de_droite_garde = pygame.image.load("Assets/3r/3r.png")

            screen.blit(personnage_de_droite_garde, game.playerII.rect)

            if premier_personnage == 1:
                personnage_de_gauche_garde = pygame.image.load("Assets/1/1.png")
            elif premier_personnage == 2:
                personnage_de_gauche_garde = pygame.image.load("Assets/2/2.png")
            elif premier_personnage == 3:
                personnage_de_gauche_garde = pygame.image.load("Assets/3/3.png")

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


            # joueur2 -> gauche ou droite
            if game.pressed.get(pygame.K_q) and game.playerII.rect.x > 0:
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

            elif game.pressed.get(pygame.K_d) and game.playerII.rect.x + game.playerII.rect.width < screen.get_width():
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

            #main
            elif game.pressed.get(pygame.K_z):
                p1 = game.player.rect.x
                p2 = game.playerII.rect.x
                if deuxieme_personnage == 1:
                    screen.blit(pygame.image.load("Assets/1r/1coupr.png"), game.playerII.rect)
                elif deuxieme_personnage == 2:
                    screen.blit(pygame.image.load("Assets/2r/2coupr.png"), game.playerII.rect)
                elif deuxieme_personnage == 3:
                    screen.blit(pygame.image.load("Assets/3r/3coupr.png"), game.playerII.rect)
                if p2 - p1 <= ECART2:
                    if (n % 2) == 0:
                        player.health -= 0.001
                        playerII.exp -= 0.03
                        if playerII.exp <= 10 and playerII.exp >= 0 :
                            if deuxieme_personnage == 1:
                                screen.blit(pygame.image.load("Assets/mainSPR.png"), game.playerII.rect)
                            elif deuxieme_personnage == 2:
                                screen.blit(pygame.image.load("Assets/mainSDR.png"), game.playerII.rect)
                            elif deuxieme_personnage == 3:
                                screen.blit(pygame.image.load("Assets/mainSTR.png"), game.playerII.rect)
                                if p2 - p1 <= ECART2:
                                    player.health -= 0.05
                        elif playerII.exp < 0:
                            playerII.exp = 100
                        n += 1
                    else:
                        player.health -= 0.01
                        playerII.exp -= 0.03
                        if playerII.exp <= 10 and playerII.exp >= 0 :
                            if deuxieme_personnage == 1:
                                screen.blit(pygame.image.load("Assets/mainSPR.png"), game.playerII.rect)
                            elif deuxieme_personnage == 2:
                                screen.blit(pygame.image.load("Assets/mainSDR.png"), game.playerII.rect)
                            elif deuxieme_personnage == 3:
                                screen.blit(pygame.image.load("Assets/mainSTR.png"), game.playerII.rect)
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

            if player.health <= 0:
                victoire_deuxieme_personnage += 1

                if nb_de_combat < nb_de_round :
                    selecCOMBAT = False
                    selecCombat = True
                else:
                    selecCOMBAT = False
                    selecCombat = False
                    dead = True

            pygame.display.flip()

            # si joueur ferme fenetre
            for event in pygame.event.get():
                # pour vérifier
                if event.type == pygame.QUIT:
                    selecCOMBAT = False
                    selecCombat = False
                    running = False

                # joueur lache une touche
                elif event.type == pygame.KEYDOWN:
                    # touche utiliser ?
                    game.pressed[event.key] = True
                elif event.type == pygame.KEYUP:
                    game.pressed[event.key] = False


    while dead:
        FondAccueil()
        button_continuer()
        KO()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Button_continuer_rect.collidepoint(event.pos):
                    dead = False
                    Fin_de_combat = True
            if event.type == pygame.QUIT:
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
                    pygame.display.flip()
                elif deuxieme_personnage == 2:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pygame.display.flip()
                else:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pygame.display.flip()
            if premier_personnage == 2:
                if deuxieme_personnage == 1:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_premier_perso_defaite()
                    pygame.display.flip()
                elif deuxieme_personnage == 2:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pygame.display.flip()
                else:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pygame.display.flip()
            if premier_personnage == 3:
                if deuxieme_personnage == 1:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_premier_perso_defaite()
                    pygame.display.flip()
                elif deuxieme_personnage == 2:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pygame.display.flip()
                else:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pygame.display.flip()
        if victoire_premier_personnage < victoire_deuxieme_personnage :
            if deuxieme_personnage == 1:
                if premier_personnage == 1:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_premier_perso_defaite()
                    pygame.display.flip()
                elif premier_personnage == 2:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pygame.display.flip()
                else:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pygame.display.flip()
            elif deuxieme_personnage == 2:
                if premier_personnage == 1:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_premier_perso_defaite()
                    pygame.display.flip()
                elif premier_personnage == 2:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pygame.display.flip()
                else:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pygame.display.flip()
            else:
                if premier_personnage == 1:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_premier_perso_defaite()
                    pygame.display.flip()
                elif premier_personnage == 2:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pygame.display.flip()
                else:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pygame.display.flip()

        if victoire_premier_personnage == victoire_deuxieme_personnage:
            if deuxieme_personnage == 1:
                if premier_personnage == 1:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_premier_perso_defaite()
                    pygame.display.flip()
                elif premier_personnage == 2:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pygame.display.flip()
                else:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pygame.display.flip()
            elif deuxieme_personnage == 2:
                if premier_personnage == 1:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_premier_perso_defaite()
                    pygame.display.flip()
                elif premier_personnage == 2:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pygame.display.flip()
                else:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pygame.display.flip()
            else:
                if premier_personnage == 1:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_premier_perso_defaite()
                    pygame.display.flip()
                elif premier_personnage == 2:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pygame.display.flip()
                else:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bouton_menu_rect.collidepoint(event.pos):
                    Fin_de_combat = False
                    PageAccueil = True
                if bouton_rejouer_rect.collidepoint(event.pos):
                    Fin_de_combat = False
                    selectionP = True
            if event.type == pygame.QUIT:
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
                personnage_de_droite_garde = pygame.image.load("Assets/1r/1r.png")
            elif deuxieme_personnage == 2:
                personnage_de_droite_garde = pygame.image.load("Assets/2r/2r.png")
            elif deuxieme_personnage == 3:
                personnage_de_droite_garde = pygame.image.load("Assets/3r/3r.png")

            screen.blit(personnage_de_droite_garde, game.playerII.rect)

            if premier_personnage == 1:
                personnage_de_gauche_garde = pygame.image.load("Assets/1/1.png")
            elif premier_personnage == 2:
                personnage_de_gauche_garde = pygame.image.load("Assets/2/2.png")
            elif premier_personnage == 3:
                personnage_de_gauche_garde = pygame.image.load("Assets/3/3.png")

            screen.blit(personnage_de_gauche_garde, game.player.rect)

            player.update_health_bar(screen)
            playerII.update_health_bar(screen)
            player.update_exp_bar(screen)
            playerII.update_exp_bar(screen)


            #prot 1

            if game.pressed.get(pygame.K_s):
                p1 = game.player.rect.x
                p2 = game.playerII.rect.x
                if game.pressed.get(pygame.K_DOWN):
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

            if game.pressed.get(pygame.K_q) and game.player.rect.x > 0:
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

            elif game.pressed.get(pygame.K_d) and game.player.rect.x + game.player.rect.width < screen.get_width():
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
            if game.pressed.get(pygame.K_z):
                p1 = game.player.rect.x
                p2 = game.playerII.rect.x
                if premier_personnage == 1:
                    screen.blit(pygame.image.load("Assets/1/1coup.png"), game.player.rect)
                elif premier_personnage == 2:
                    screen.blit(pygame.image.load("Assets/2/2coup.png"), game.player.rect)
                elif premier_personnage == 3:
                    screen.blit(pygame.image.load("Assets/3/3coup.png"), game.player.rect)
                if p2 - p1 <= ECART2:
                    if game.pressed.get(pygame.K_i):
                        playerII.health -= 0.01
                        player.exp -= 0.5
                        if player.exp <= 10 and player.exp >= 0 :
                            if premier_personnage == 1:
                                screen.blit(pygame.image.load("Assets/mainP.png"), game.player.rect)
                            elif premier_personnage == 2:
                                screen.blit(pygame.image.load("Assets/mainSD.png"), game.player.rect)
                            elif premier_personnage == 3:
                                screen.blit(pygame.image.load("Assets/mainST.png"), game.player.rect)
                                if p2 - p1 <= ECART2:
                                    playerII.health -= 0.5
                        elif player.exp < 0:
                            player.exp = 100
                    else:
                        playerII.health -= 0.1
                        player.exp -= 0.5
                        if player.exp <= 10 and player.exp >= 0 :
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
            if game.pressed.get(pygame.K_k) and game.playerII.rect.x > 0:
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
                    pygame.K_m) and game.playerII.rect.x + game.playerII.rect.width < screen.get_width():
                game.playerII.move_right()

                print('p1:')
                print(game.player.rect.x)
                print('p2:')
                print(game.playerII.rect.x)

            #main
            elif game.pressed.get(pygame.K_o):
                p1 = game.player.rect.x
                p2 = game.playerII.rect.x
                if deuxieme_personnage == 1:
                    screen.blit(pygame.image.load("Assets/1r/1coupr.png"), game.playerII.rect)
                elif deuxieme_personnage == 2:
                    screen.blit(pygame.image.load("Assets/2r/2coupr.png"), game.playerII.rect)
                elif deuxieme_personnage == 3:
                    screen.blit(pygame.image.load("Assets/3r/3coupr.png"), game.playerII.rect)
                if p2 - p1 <= ECART2:
                    if game.pressed.get(pygame.K_a):
                        player.health -= 0.01
                        playerII.exp -= 0.5
                        if playerII.exp <= 10 and playerII.exp >= 0 :
                            if deuxieme_personnage == 1:
                                screen.blit(pygame.image.load("Assets/mainSPR.png"), game.playerII.rect)
                            elif deuxieme_personnage == 2:
                                screen.blit(pygame.image.load("Assets/mainSDR.png"), game.playerII.rect)
                            elif deuxieme_personnage == 3:
                                screen.blit(pygame.image.load("Assets/mainSTR.png"), game.playerII.rect)
                                if p2 - p1 <= ECART2:
                                    player.health -= 0.5
                        elif playerII.exp < 0:
                            playerII.exp = 100
                    else:
                        player.health -= 0.1
                        playerII.exp -= 0.5
                        if playerII.exp <= 10 and playerII.exp >= 0 :
                            if deuxieme_personnage == 1:
                                screen.blit(pygame.image.load("Assets/mainSPR.png"), game.playerII.rect)
                            elif deuxieme_personnage == 2:
                                screen.blit(pygame.image.load("Assets/mainSDR.png"), game.playerII.rect)
                            elif deuxieme_personnage == 3:
                                screen.blit(pygame.image.load("Assets/mainSTR.png"), game.playerII.rect)
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

            pygame.display.flip()

            # si joueur ferme fenetre
            for event in pygame.event.get():
                # pour vérifier
                if event.type == pygame.QUIT:
                    COMBAT = False
                    Combat = False
                    running = False

                # joueur lache une touche
                elif event.type == pygame.KEYDOWN:
                    # touche utiliser ?
                    game.pressed[event.key] = True
                elif event.type == pygame.KEYUP:
                    game.pressed[event.key] = False

    while dead:
        FondAccueil()
        button_continuer()
        KO()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Button_continuer_rect.collidepoint(event.pos):
                    dead = False
                    Fin_de_combat = True
            if event.type == pygame.QUIT:
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
                    pygame.display.flip()
                elif deuxieme_personnage == 2:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pygame.display.flip()
                else:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pygame.display.flip()
            if premier_personnage == 2:
                if deuxieme_personnage == 1:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_premier_perso_defaite()
                    pygame.display.flip()
                elif deuxieme_personnage == 2:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pygame.display.flip()
                else:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pygame.display.flip()
            if premier_personnage == 3:
                if deuxieme_personnage == 1:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_premier_perso_defaite()
                    pygame.display.flip()
                elif deuxieme_personnage == 2:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pygame.display.flip()
                else:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pygame.display.flip()
        if victoire_premier_personnage < victoire_deuxieme_personnage :
            if deuxieme_personnage == 1:
                if premier_personnage == 1:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_premier_perso_defaite()
                    pygame.display.flip()
                elif premier_personnage == 2:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pygame.display.flip()
                else:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pygame.display.flip()
            elif deuxieme_personnage == 2:
                if premier_personnage == 1:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_premier_perso_defaite()
                    pygame.display.flip()
                elif premier_personnage == 2:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pygame.display.flip()
                else:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pygame.display.flip()
            else:
                if premier_personnage == 1:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_premier_perso_defaite()
                    pygame.display.flip()
                elif premier_personnage == 2:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pygame.display.flip()
                else:
                    Fond_de_fin()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pygame.display.flip()

        if victoire_premier_personnage == victoire_deuxieme_personnage:
            if deuxieme_personnage == 1:
                if premier_personnage == 1:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_premier_perso_defaite()
                    pygame.display.flip()
                elif premier_personnage == 2:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pygame.display.flip()
                else:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_premier_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pygame.display.flip()
            elif deuxieme_personnage == 2:
                if premier_personnage == 1:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_premier_perso_defaite()
                    pygame.display.flip()
                elif premier_personnage == 2:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pygame.display.flip()
                else:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_deuxieme_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pygame.display.flip()
            else:
                if premier_personnage == 1:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_premier_perso_defaite()
                    pygame.display.flip()
                elif premier_personnage == 2:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_deuxieme_perso_defaite()
                    pygame.display.flip()
                else:
                    Fond_Egalite()
                    button_menu()
                    button_rejouer()
                    Fin_troisieme_perso_victoire()
                    Fin_troisieme_perso_defaite()
                    pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bouton_menu_rect.collidepoint(event.pos):
                    Fin_de_combat = False
                    PageAccueil = True
                if bouton_rejouer_rect.collidepoint(event.pos):
                    Fin_de_combat = False
                    selectionP = True
            if event.type == pygame.QUIT:
                Fin_de_combat = False
                running = False

print("Fermeture du jeu")
pygame.quit()