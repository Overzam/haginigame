import pygame as pyg
from pygame import *

display_width = 800
display_height = 600

couleur_fond = (128,128,128)
couleur_principale = (0,0,0)
couleur_secondaire = (255,255,255)

menu_width = round(display_width * (3 / 5))
menu_height = round(display_height * (3 / 5))

menu = pyg.display.set_mode((menu_width,menu_height))

ouvert = True

while ouvert:
    
    for event in pyg.event.get():
        #print(event)
        if event.type == pyg.QUIT:
            pyg.quit()
            quit()

        if event.type == KEYDOWN:
            if event.key == pyg.K_ESCAPE:
                ouvert = False
                
    pyg.draw.rect(menu, couleur_principale, (395,0,100,100))
        
            
    menu.fill(couleur_fond)
   
    pyg.display.update()
    pyg.display.flip()
    
    
