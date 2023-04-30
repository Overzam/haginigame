import pygame as pyg
import random
import math
pyg.init()
####################################################################################################





#####################################################################################################
def thibaud(width, height):
    #class jeu
    class Game:

        def __init__(self):
            #def si jeu commencer
            self.is_playing = False
            self.all_players = pyg.sprite.Group()
            self.player = Player(self)
            self.all_players.add(self.player)

            #event neige
            self.neige_event = NeigeEvent(self)

            #groupe monstre
            self.all_monsters = pyg.sprite.Group()
            self.pressed = {}

        def start(self):
            self.is_playing = True
            self.spawn_monster()
            self.spawn_monster()

        def game_over(self):
             #remet le jeu a zero
             self.all_monsters = pyg.sprite.Group()
             self.player.vie = self.player.vie_max
             self.is_playing = False
             play_button_rect.x = math.ceil(screen.get_width() / 3)
             play_button_rect.y = math.ceil(screen.get_width() / 3)
        def update(self, screen):
            # appliquer image J1
            screen.blit(self.player.image, self.player.rect)

            # appliquer bar de vie
            self.player.update_vie(screen)

            #ACTU BAR EVENT
            self.neige_event.update_bar(screen)

            # RECUP balle
            for balle in self.player.all_balles:
                balle.move()

            # recup monstre
            for monster in game.all_monsters:
                monster.move()
                # dessin bar de vie
                monster.update_vie(screen)

            #recup Neige
            for neige in self.neige_event.all_neiges:
                neige.chute()

            # applique image balle
            self.player.all_balles.draw(screen)

            # appliquer image monstre
            self.all_monsters.draw(screen)

            # applique image event
            self.neige_event.all_neiges.draw(screen)

        def check_collision(self, sprite, group):
            return pyg.sprite.spritecollide(sprite, group, False, pyg.sprite.collide_mask)

        def spawn_monster(self):
            monster = Monster(self)
            self.all_monsters.add(monster)


    ############################################################################################################
    #class monstre
    class Monster(pyg.sprite.Sprite):
        def __init__(self, game):
            super().__init__()
            self.game = game
            self.vie =100
            self.vie_max = 100
            self.attack = 0.2
            self.image = pyg.image.load('images/stmg2.png')
            self.image = pyg.transform.scale(self.image, (125, 125))
            self.rect = self.image.get_rect()
            self.rect.x = 950 + random.randint(-200, 300)
            self.rect.y = 675 - random.randint(10, 200)
            self.speed = random.randint(1, 2)
            self.depla = 1

        def degat(self, amount):
            #infliger degat
            self.vie -= amount

            #verif limite vie
            if self.vie <=0 :
                #respawn monstre
                self.rect.x = 1000 + random.randint(0, 300)
                self.rect.y = 675 - random.randint(0, 300)
                self.speed = random.randint(1, 2)
                self.vie = self.vie_max

        def remove_monstre(self):
            self.monster.all_monsters.remove_monster(self)
            if self.rect.y < 10 or self.rect.y > 920:
                self.remove_monstre()

        def remove(self):
            self.player.all_balles.remove(self)
            if self.rect.x < 10 or self.rect.y > 920:
                self.remove()

        def update_vie(self, surface):
            #dessin bar de vie
            pyg.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 150, self.vie_max, 10])
            pyg.draw.rect(surface, (111, 210, 46), [self.rect.x+50, self.rect.y+150, self.vie, 10])
        def move(self):
            #mouv que sans collision avec joueur
            if not self.game.check_collision(self, self.game.all_players):
                self.rect.y -= self.speed
                self.depla += 1
                if abs(self.depla) > 600:
                    self.speed *= -1
                    self.depla = 0
            else:
                #degat
                self.game.player.degat(self.attack)
                self.rect.x += self.speed

    ################################################################################################################
    # classe joueur
    class Player(pyg.sprite.Sprite):

        def __init__(self, game):
            super().__init__()
            self.game = game
            self.vie = 100
            self.vie_max = 100
            self.attack = 30
            self.speed = 1
            self.all_balles = pyg.sprite.Group()
            self.image = pyg.image.load('images/tank.png')
            self.rect = self.image.get_rect()
            self.rect.x = 100
            self.rect.y = 675

        def degat(self, amount):
            if self.vie - amount > amount:
                self.vie -= amount
            else:
                self.game.game_over()
        def update_vie(self, surface):
            #dessin bar de vie
            pyg.draw.rect(surface, (60, 63, 60), [self.rect.x + 70, self.rect.y + 150, self.vie_max, 10])
            pyg.draw.rect(surface, (111, 210, 46), [self.rect.x + 70, self.rect.y+150, self.vie, 10])

        def tir(self):
            self.all_balles.add(Balle(self))
        def move_R(self):
            if not self.game.check_collision(self, self.game.all_monsters):
                self.rect.x += self.speed
        def move_L(self):
            if not self.game.check_collision(self, self.game.all_monsters):
                self.rect.x -= self.speed
        def move_up(self):
            if not self.game.check_collision(self, self.game.all_monsters):
                self.rect.y -= self.speed
        def move_down(self):
            if not self.game.check_collision(self, self.game.all_monsters):
                self.rect.y += self.speed
    ######################################################################################################################
    # class projectille
    class Balle(pyg.sprite.Sprite):
         def __init__(self, player):
            super().__init__()
            self.speed = 2
            self.player = player
            self.image = pyg.image.load('images/neige.png')
            self.image = pyg.transform.scale(self.image, (50, 50))
            self.rect = self.image.get_rect()
            self.rect.x = player.rect.x +185
            self.rect.y = player.rect.y +107

         def move(self):
            self.rect.x += self.speed

            # verif collision
            for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
                self.remove()
                #degat
                monster.degat(self.player.attack)

         def remove(self):
             self.player.all_balles.remove(self)
             #verif si balle sur ecran
             """if self.rect.x > 980 or self.rect.y > 720:
                self.remove()"""
    ########################################################################################################################
    #classe neige
    class Neige(pyg.sprite.Sprite):

        def __init__(self, neige_event):
            super().__init__()
            self.image = pyg.image.load('images/neige.png')
            self.image = pyg.transform.scale(self.image, (120, 120))
            self.rect = self.image.get_rect()
            self.speed = random.randint(1, 3)
            self.rect.x = random.randint(20, 800)
            self.rect.y = - random.randint(0, 800)
            self.neige_event = neige_event

        def remove(self):
            self.neige_event.all_neiges.remove(self)
        def chute(self):
            self.rect.y += self.speed

            #tombe sur le sol ou pas
            if self.rect.y >= 750:
                self.remove()

            if self.neige_event.game.check_collision(
                    self, self.neige_event.game.all_players
            ):
                print("j1 touché")
                self.remove()
                self.neige_event.game.player.degat(20)


    ########################################################################################################################
    #crée classe event
    class NeigeEvent:
        #on crée un compteur pour le chargement
        def __init__(self, game):
            self.pourcent = 0
            self.pourcent_speed = 20
            self.game = game

            #def groupe de sprite
            self.all_neiges = pyg.sprite.Group()


        def add_pourcent(self):
            self.pourcent += self.pourcent_speed / 30

        def is_full(self):
            return self.pourcent >= 100


        def chute_neige(self):
            self.all_neiges.add(Neige(self))

        def reset(self):
            self.pourcent = 0

        def essai_chute(self):
            #jauge full donc event
            if self.is_full():
                self.chute_neige()
                self.reset()

        def update_bar(self, surface):
            #ajouter poucentage
            self.add_pourcent()

            # appel essai chute
            self.essai_chute()

            #bar arriere plan
            pyg.draw.rect(surface, (0, 0, 0), [
                0, # x
                surface.get_height() - 25, # y
                surface.get_width(), # longueur
                10  # epaisseur
            ])
            #bar premier plan
            pyg.draw.rect(surface, (255, 0, 0), [
                0, # x
                surface.get_height() - 25, # y
                (surface.get_width() / 100) * self.pourcent, # longueur
                10  # epaisseur
            ])






    ########################################################################################################################
    ########################################################################################################################
    ########################################################################################################################
    ########################################################################################################################
    # fenetre
    pyg.display.set_caption("surviv")
    screen = pyg.display.set_mode((width, height))

    # arriere plan jeu
    background = pyg.image.load("images/fond.jpg")
    background = pyg.transform.scale(background, (width, height))

    #import banniere
    banner = pyg.image.load('images/boule.png')
    banner = pyg.transform.scale(banner, (500, 500))
    banner_rect = banner.get_rect()
    banner_rect.x = math.ceil(screen.get_width() / 3.5)

    #import charger bouton lancement
    play_button = pyg.image.load('images/button.png')
    play_button = pyg.transform.scale(play_button, (400, 150))
    play_button_rect = play_button.get_rect()
    play_button_rect.x = math.ceil(screen.get_width() / 3)
    play_button_rect.y = math.ceil(screen.get_width() / 3)
    #charger jeu
    game = Game()

    mur = [300, 450, 600]
    running = True
    red = (255, 0, 0)
    # boucle pricipale
    while running:
        mur = pyg.draw.rect(screen, red, [mur[1], 50, 20, 20])
        # arriere plan
        screen.blit(background, (0, 0))

        #verif si jeu en cours
        if game.is_playing:
            #declenche instruction
            game.update(screen)
        #verif
        else:
            #ajout banniere
            screen.blit(banner, banner_rect)
            screen.blit(play_button, play_button_rect)

        pyg.key.set_repeat(1)
        # ferme fenetre
        for event in pyg.event.get():

            if event.type == pyg.QUIT:
                running = False
                pyg.quit()
            if game.pressed.get(pyg.K_ESCAPE):
                running = False

        # detect lache touche

            if game.pressed.get(pyg.K_z):
                game.player.move_up()

            if game.pressed.get(pyg.K_s):
                game.player.move_down()

            if game.pressed.get(pyg.K_d):
                game.player.move_R()

            if game.pressed.get(pyg.K_q):
                game.player.move_L()

            if event.type == pyg.MOUSEBUTTONUP:
                game.player.tir()

            elif event.type == pyg.MOUSEBUTTONDOWN :
                if play_button_rect.collidepoint(event.pos):
                    game.start()
                    play_button_rect.x = 10000
                    play_button_rect.y = 10000



            if event.type == pyg.KEYDOWN:
                game.pressed[event.key] = True

            elif event.type == pyg.KEYUP:
                game.pressed[event.key] = False
                pyg.key.set_repeat(1)

    # maj ecran
        pyg.display.flip()




