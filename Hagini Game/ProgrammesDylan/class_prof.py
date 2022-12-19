import pygame as pyg


width, height = 1920, 1080
screen = pyg.display.set_mode((width, height))
pyg.init()


#definition des images
prof_gentil = pyg.image.load('img/prof_gentil.png').convert_alpha()
prof_moitie =pyg.image.load('img/prof_moitie.png').convert_alpha()
prof_mechant = pyg.image.load('img/prof_mechant.png').convert_alpha()

prof_gentil = pyg.transform.scale(prof_gentil, (500, 500))
prof_moitie =pyg.transform.scale(prof_moitie, (500, 500))
prof_mechant = pyg.transform.scale(prof_mechant, (500, 500))

etat_prof = [prof_gentil, prof_moitie, prof_mechant]



class Prof:
    def __init__(self, pos_x, pos_y, pv):
        self.x = int(pos_x)
        self.y = int(pos_y)
        self.pv = int(pv)
        self.max_pv = 100
        self.pv_vise = self.pv
        self.taille_barre_de_vie = 400
        self.barre_de_vie_ratio = self.max_pv/ self.taille_barre_de_vie
        self.rect = pyg.Rect(self.x, self.y, 32, 32)
        self.color = (250, 120, 60)
        self.sprite_actuel = 0
        self.barre_de_vie_changement_vitesse = 0.5

    def prend_degat(self, nb_degat):
        if self.pv > 0:
            self.pv_vise -= nb_degat
    
    def barre_de_vie(self):
        taille_transition = 0
        couleur_transition = (255,255,0)
        
        if self.pv > self.pv_vise:
            self.pv -= self.barre_de_vie_changement_vitesse
            taille_transition = int((self.pv - 5 - self.pv) / self.barre_de_vie_ratio)
            

        taille_barre_de_vie = int(self.pv / self.barre_de_vie_ratio)
        health_bar = pyg.Rect(10,45,taille_barre_de_vie,25)
        transition_bar = pyg.Rect(health_bar.right,45,taille_transition,25)
        
        pyg.draw.rect(screen,(255,0,0),health_bar)
        pyg.draw.rect(screen,couleur_transition,transition_bar)	
        pyg.draw.rect(screen,(255,255,255),(10,45,self.taille_barre_de_vie,25),4)

    def draw(self, screen):
        screen.blit(etat_prof[self.sprite_actuel], (self.x, self.y))

    def update(self, sprite_a_afficher):
        self.sprite_actuel = sprite_a_afficher
        self.rect = pyg.Rect(int(self.x), int(self.y), 32, 32)