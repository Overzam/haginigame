import pygame as pyg
import random
import button
from pygame import *
mixer.init()

def yanis(width,height,son):
    clock = pyg.time.Clock()
    fps = 60
    pyg.init()

    bottom_panel = 500
    screen_width = width
    screen_height = height + bottom_panel

    screen = pyg.display.set_mode((screen_width, screen_height))
    pyg.display.set_caption("Roof Fight")
    pyg.mixer.music.load('assets/son/arcade.wav')
    pyg.mixer.music.play()
    pyg.mixer.music.set_volume(0.05* son)

    actual_fighter = 1
    total_fighter = 3
    global action_cooldown
    action_cooldown = 0
    action_wait_time = 20
    attack = False
    potion = False
    potion_effect = 40
    clicked = False
    game_over = 0

    font = pyg.font.SysFont('Forte', 45)

    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 255, 174)
    purple = (207, 122, 255)

    background = pyg.image.load('assets/img/background/FONDYANIS1.png').convert_alpha()
    panel = pyg.image.load('assets/img/autre/panel.png').convert_alpha()
    punch = pyg.image.load('assets/img/autre/punch.png').convert_alpha()
    potion_img = pyg.image.load('assets/img/autre/potion.png').convert_alpha()
    victory_img = pyg.image.load('assets/img/end/you_win.png').convert_alpha()
    victory_img = pyg.transform.scale(victory_img, (victory_img.get_width() * 1, victory_img.get_height() * 1))
    loose_img = pyg.image.load('assets/img/end/game_over.png').convert_alpha()
    loose_img = pyg.transform.scale(loose_img, (loose_img.get_width() * 1, loose_img.get_height() * 1))

    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    def draw_bg():
        screen.blit(background, (0, 0))

    def draw_panel():
        screen.blit(panel, (0, screen_height - bottom_panel))
        draw_text(f'{fighter.name} PV: {fighter.pv}', font, blue, 350, screen_height - bottom_panel + 15)
        for count, i in enumerate(badboy_list):
            draw_text(f'{i.name} PV: {i.pv}', font, purple, 1350, (screen_height - bottom_panel + 15) + count * 110)

    class Badboy():
        def __init__(self, x, y, name, max_pv, force, potions):
            self.name = name
            self.max_pv = max_pv
            self.pv = max_pv
            self.force = force
            self.start_potions = potions
            self.potions = potions
            self.alive = True
            image = pyg.image.load('assets/img/bot/robot2.png')
            self.image = pyg.transform.scale(image, (image.get_width() * 6, image.get_height() * 6))
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.rect.x = x
            self.rect.y = y
            self.move_direction = 2
            self.move_counter = 1


        def draw(self):
            screen.blit(self.image, self.rect)
            self.rect.x += self.move_direction
            self.move_counter += 1
            if abs(self.move_counter) > 95:
                self.move_direction *= -1
                self.move_counter = 0



        def attack(self, target):
            damage_sound = mixer.Sound('assets/son/robot.wav')

            damage_sound.play()
            rand = random.randint(-5, 5)
            damage = self.force + rand
            target.pv -= damage
            if target.pv < 1:
                target.pv = 0
                target.alive = False
                if target.pv < 1:
                    target.pv = 0
                    target.alive = False

                if self == badboy_list[0]:
                    del badboy_list[0]


    class Fighter(pyg.sprite.Sprite):
        def __init__(self, x, y, name, max_pv, force, potions):
            self.name = name
            self.max_pv = max_pv
            self.pv = max_pv
            self.force = force
            self.start_potions = potions
            self.potions = potions
            self.alive = True
            self.update_time = pyg.time.get_ticks()
            self.sprite = []
            self.sprite.append(pyg.image.load('assets/img/gentil/idle/0.png'))
            self.sprite.append(pyg.image.load('assets/img/gentil/idle/1.png'))
            self.sprite.append(pyg.image.load('assets/img/gentil/idle/2.png'))
            self.sprite.append(pyg.image.load('assets/img/gentil/idle/3.png'))
            self.frame_index = 0
            self.image = self.sprite[self.frame_index]
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.is_animating = False
            self.is_attacking = False
            self.attack_animation_time = 500
            self.last_attack_time = pyg.time.get_ticks()

        def idle(self):
            self.sprite.append(pyg.image.load('assets/img/gentil/idle/0.png'))
            self.sprite.append(pyg.image.load('assets/img/gentil/idle/1.png'))
            self.sprite.append(pyg.image.load('assets/img/gentil/idle/2.png'))
            self.sprite.append(pyg.image.load('assets/img/gentil/idle/3.png'))
            self.frame_index = 0
            self.update_time = pyg.time.get_ticks()
            self.is_attacking = False

        def attack(self, target):
            global action_cooldown
            if action_cooldown == 0:
                action_cooldown = action_wait_time
                self.is_attacking = True
            self.is_attacking = True
            rand = random.randint(-5, 5)
            damage = self.force + rand
            target.pv -= damage
            if target.pv < 1:
                target.pv = 0
                target.alive = False
            damage_text = Damage(target.rect.centerx, target.rect.centery, str(damage), red)
            damage_text_Group.add(damage_text)
            damage_sound = mixer.Sound('assets/son/punch.wav')
            damage_sound.play()
            if self.is_attacking:
                self.sprite = []
                self.sprite.append(pyg.image.load('assets/img/gentil/punch/0.png'))
                self.sprite.append(pyg.image.load('assets/img/gentil/punch/1.png'))
                self.sprite.append(pyg.image.load('assets/img/gentil/punch/2.png'))
                self.sprite.append(pyg.image.load('assets/img/gentil/punch/3.png'))
                self.sprite.append(pyg.image.load('assets/img/gentil/punch/4.png'))
                self.frame_index = 0
                self.update_time = pyg.time.get_ticks()
                self.frame_index = 0
                self.last_attack_time = pyg.time.get_ticks()






        def draw(self):
            screen.blit(self.image, self.rect)

        def update(self):
            global action_cooldown, clicked
            if self.is_attacking and pyg.time.get_ticks() - self.last_attack_time < self.attack_animation_time:
                if pyg.time.get_ticks() - self.update_time > 100:
                    self.frame_index += 1
                    if self.frame_index >= 4:
                        self.is_attacking = False
                        self.idle()
                    else:
                        self.sprite = []
                        self.sprite.append(pyg.image.load('assets/img/gentil/punch/0.png'))
                        self.sprite.append(pyg.image.load('assets/img/gentil/punch/1.png'))
                        self.sprite.append(pyg.image.load('assets/img/gentil/punch/2.png'))
                        self.sprite.append(pyg.image.load('assets/img/gentil/punch/3.png'))
                        self.sprite.append(pyg.image.load('assets/img/gentil/punch/4.png'))
                        self.update_time = pyg.time.get_ticks()

            animation_cooldown = 100

            self.frame_index += 0.005

            if self.frame_index >= len(self.sprite):
                self.frame_index = 0
                self.is_animating = False

            self.image = self.sprite[int(self.frame_index)]

            if pyg.time.get_ticks() - self.update_time > animation_cooldown:
                self.update_time = pyg.time.get_ticks()
                self.frame_index += 1



        def draw_fighter(fighter):
            if fighter.is_animating:
                screen.blit(punch)



    class BarreVie():
        def __init__(self, x, y, pv, max_pv):
            self.x = x
            self.y = y
            self.pv = pv
            self.max_pv = max_pv


        def draw(self, pv):
            self.pv = pv
            ratio = self.pv / self.max_pv
            pyg.draw.rect(screen, red, (self.x, self.y, 350, 30))
            pyg.draw.rect(screen, green, (self.x, self.y, 350 * ratio, 30))


    class Damage(pyg.sprite.Sprite):
        def __init__(self, x, y, damage, colour):
            pyg.sprite.Sprite.__init__(self)
            self.image = font.render(damage, True, colour)
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.counter = 0

        def update(self):
            self.rect.y -= 1
            self.counter += 1
            if self.counter > 30:
                self.kill()


    damage_text_Group = pyg.sprite.Group()

    #personnages:
    fighter = Fighter(385, 600, 'MC', 350, 45, 3)
    badboy1 = Badboy(1000, 250, 'Jackie', 400, 15, 1)
    badboy2 = Badboy(1300, 400, 'Michel', 480, 15, 2)

    badboy_list = []
    badboy_list.append(badboy1)
    badboy_list.append(badboy2)

    fighter_pv = BarreVie(290, screen_height - bottom_panel + 75, fighter.pv, fighter.max_pv)
    badboy1_pv = BarreVie(1320, screen_height - bottom_panel + 75, badboy1.pv, badboy1.max_pv)
    badboy2_pv = BarreVie(1320, screen_height - bottom_panel + 180, badboy2.pv, badboy2.max_pv)

    potion_button = button.Button(screen, 400, screen_height - bottom_panel + 120, potion_img, 100, 100)

    run = True

    while run:


        clock.tick(fps)

        draw_bg()

        draw_panel()

        fighter.update()
        fighter.draw()
        fighter_pv.draw(fighter.pv)
        badboy1_pv.draw(badboy1.pv)
        badboy2_pv.draw(badboy2.pv)

        for badboy in badboy_list:
            if badboy.alive:
                badboy.draw()



        damage_text_Group.update()
        damage_text_Group.draw(screen)

        attack = False
        potion = False
        target = None
        pyg.mouse.set_visible(True)
        pos = pyg.mouse.get_pos()

        for count, badboy in enumerate(badboy_list):
            if badboy.rect.collidepoint(pos):
                pyg.mouse.set_visible(False)
                screen.blit(punch, pos)
                if clicked == True:
                    attack = True
                    target = badboy_list[count]

        if potion_button.draw():
            potion = True
            potion_sound = mixer.Sound('assets/son/heal.wav')
            potion_sound.play()
        draw_text(str(fighter.potions), font, green, 490, screen_height - bottom_panel + 185)

        if game_over == 0:
            if fighter.alive == True:
                if actual_fighter == 1:
                    action_cooldown += 1
                    if action_cooldown >= action_wait_time:
                        if attack == True and target != None:
                            fighter.attack(target)
                            actual_fighter += 1
                            action_cooldown = 0
                        if potion == True:
                            if fighter.potions > 0:
                                if fighter.max_pv - fighter.pv > potion_effect:
                                    heal_amount = potion_effect
                                else:
                                    heal_amount = fighter.max_pv - fighter.pv
                                fighter.pv += heal_amount
                                fighter.potions -= 1
                                damage_text = Damage(fighter.rect.centerx, fighter.rect.centery, str(heal_amount), green)
                                damage_text_Group.add(damage_text)
                                actual_fighter += 1
                                action_cooldown = 0
            else:
                game_over = -1

            for count, badboy in enumerate(badboy_list):
                if actual_fighter == 2 + count:
                    if badboy.alive == True:
                        action_cooldown += 1
                        if action_cooldown >= action_wait_time:
                            if (badboy.pv / badboy.max_pv) < 0.5 and badboy.potions > 0:
                                if badboy.max_pv - badboy.pv > potion_effect:
                                    heal_amount = potion_effect
                                else:
                                    heal_amount = badboy.max_pv - badboy.pv
                                badboy.pv += heal_amount
                                badboy.potions -= 1
                                damage_text = Damage(badboy.rect.centerx, badboy.rect.centery, str(heal_amount), green)
                                damage_text_Group.add(damage_text)
                                actual_fighter += 1
                                action_cooldown = 0
                            else:
                                badboy.attack(fighter)
                                actual_fighter += 1
                                action_cooldown = 0
                    else:
                        actual_fighter += 1

            if actual_fighter > total_fighter:
                actual_fighter = 1

        alive_badboy = 0
        for badboy in badboy_list:
            if badboy.alive == True:
                alive_badboy += 1
        if alive_badboy == 0:
            game_over = 1

        if game_over != 0:
            if game_over == 1:
                screen.blit(victory_img, (0, 0))
            if game_over == -1:
                screen.blit(loose_img, (0, 0))


        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                run = False

            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_ESCAPE: # retour au menu
                    run = False

            if event.type == pyg.MOUSEBUTTONDOWN:
                clicked = True
            else:
                clicked = False

        pyg.display.update()


