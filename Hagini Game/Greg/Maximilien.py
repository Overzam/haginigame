import pygame as pyg
from pygame import *

import math
from random import randint

pyg.init()
pyg.mixer.init()
pyg.time.Clock()
pyg.font.init()
pyg.display.init()

son = 1
height = 1080 // 2
width = 1920 // 2



########################################################################################################################

def citation(height,width,son):
    start_ticks = pyg.time.get_ticks()



    # Autres variables
    Taille_Police = int(height * 0.035)

    pos = pyg.mouse.get_pos()

    co_x = round(width * 0.83)  # coordonne x du centre de l'horloge
    co_y = round(height * 0.31)  # coordonne y du centre de l'horloge
    rayon_horloge = round(width / 25)

    Duree_Anim = 4

    Jeu_Lance = True
    perdu = False
    bonne_rep = False

    Ancienne_Duree_Tempo2 = 0
    anciennes_Secondes_citation = 0
    a = 0
    Score_Avant_Defaite = 0

    # Liste de toutes les citations à recopier format : ["texte de la citation", duree demandee pour l'ecrire, "auteur"]
    Citations = [["Plus ils sont petits, plus ils cherchent à paraître grands.", 35, "Dylan Carlos Barros"],
                 ["Tu ne seras jamais une vraie voiture.", 30, "Matyas Matgo Gault"],
                 ["Ce qui compte ce n'est pas le vote, c'est comment on compte les votes.", 40, "Joseph Staline"],
                 ["L'histoire des peuples est l'histoire de la trahison de l'unité.", 35, "Antonin Artaud"],
                 ["L'histoire est le total des choses qui auraient pu être évitées.", 35, "Konrad Adenauer"],
                 ["L'histoire est un perpétuel recommencement.", 30, "Thucydide"],
                 ["Le scepticisme est le commencement de la foi.", 30, "Oscar Wilde"],
                 ["L'histoire des peuples est l'histoire de la trahison de l'unité.", 35, "Antonin Artaud"],
                 ["L'histoire est le total des choses qui auraient pu être évitées", 35, "Konrad Adenauer"],
                 ["La Libération ? J'en ai été le premier prévenu.", 30, "Sacha Guitry"],
                 ["Un peuple qui oublie son passé se condamne à le revivre.", 33, "Mathieu Alexander Delestre"],
                 ["L'histoire, ce riche trésor des déshonneurs de l'homme.", 33, "Henri Lacordaire"],
                 ["C'est un pauvre disciple que celui qui ne surpasse pas son maître.", 35, "Léonard de Vinci"],
                 ["La liberté est un rêve d'esclaves.", 25, "Nicolás Gómez Dávila"],
                 ["L'historien est un prophète qui regarde en arrière.", 31, "Heinrich Heine"],
                 ["Une civilisation débute dans le mythe et finit dans le doute.", 34, "Emil Michel Cioran"],
                 ["D'être domestique, on a ça dans le sang...", 30, "Octave Mirbeau"],
                 ["Il n'y a pas de faits il n'y a que des interprétations", 32, "Nietzsche"]]

    Citation = Citations[randint(0, len(Citations) - 1)]
    Auteur = Citation[2]
    Texte_Question = "Quelle est la citation de " + Auteur + " que nous avons étudiée ?"
    Texte_Question_En_Cour = ""
    Texte_Reponse_Donnee = ""
    Texte_Reponse = Citation[0]
    Duree = Citation[1]
    Secondes_citation = Duree
    angle = math.pi * 1.375  # en radiant ( 180° = Pi en radiant )

    Liste_carcteres = ['ç', ' ', 'ê', 'è', 'é', 'ù', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
                       'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                       'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '&', '*', '(',
                       ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\', ';', ':', ',', '.', '<', '>', '/', '?',
                       "'"]

    # Definition du fond de jeu
    screen = pyg.display.set_mode((width, height))
    background = pyg.image.load("assets\Fond.png").convert()  # Charge l'image
    background = pyg.transform.scale(background, (width, height))  # Taille de l'image
    fond = background.convert()
    screen.blit(fond, (0, 0))  # actualise le fond
    pyg.display.flip()

    # Definition de la feuille
    Feuille = pyg.image.load("assets\Feuille.PNG")  # Charge l'image
    width_Feuille = width * 0.75  # taille en x de l'image
    height_Feuille = height * 0.5  # taille en y de l'image
    Feuille = pyg.transform.scale(Feuille,(int(width_Feuille), int(height_Feuille))).convert_alpha()  # Taille de l'image
    x_Feuille = 0
    y_Feuille = height

    # Definition de moati
    Moati = pyg.image.load("assets/Moati.png")  # Charge l'image
    width_Moati = width * 0.4  # taille en x de l'image
    height_Moati = width * 0.4  # taille en y de l'image
    Moati = pyg.transform.scale(Moati, (int(width_Moati), int(height_Moati))).convert_alpha()  # Taille de l'image
    x_Moati = width * 0.7
    y_Moati = height * 0.4

    # Couleurs de l'affichage des texte
    noir = (0, 0, 0)  # fond
    blanc = (255, 255, 255)  # ecriture

    # Definition de la police
    Police = pyg.font.Font('assets/Little_days.ttf', Taille_Police)
    Police_Moahati = pyg.font.Font('assets/CHICKEN Pie.ttf', Taille_Police)

    # Affichage du texte de reponse attendue
    Affichage_Texte_Reponse = Police.render(Texte_Reponse, True, (noir))
    x_Texte_Reponse = width * 0.015
    y_Texte_Reponse = height * 1.075

    # Affichage du texte de reponse donnee
    Affichage_Texte_Reponse_Donnee = Police.render(Texte_Reponse_Donnee, True, (blanc))
    x_Texte_Reponse_Donnee = round(width * 0.04)
    y_Texte_Reponse_Donnee = height // 5

    # Affichage du texte de Question
    Affichage_Texte_Question = Police_Moahati.render(Texte_Question, True, (noir))
    x_Affichage_Texte_Question = width * 0.03
    y_Affichage_Texte_Question = height * 0.8

    # Definition du son de parole de mohahati
    Mohahati = pyg.mixer.music.load("assets\parole_mohahati.wav")
    pyg.mixer.music.play(10, 0.0)
    pyg.mixer.music.set_volume(0.25 * son)

    ########################################################################################################################

    def contour(valeur):  # entre 0 et 100
        Pas_x = width // 100
        Pas_y = height // 100
        rouge = (255, 0, 0)
        if valeur <= 50:
            pyg.draw.rect(screen, rouge, (width / 2 - valeur * Pas_x, height - Pas_y, 2 * valeur * Pas_x, Pas_y))
            pyg.draw.rect(screen, rouge, (width / 2 - valeur * Pas_x, 0, 2 * valeur * Pas_x, Pas_y))
        else:
            pyg.draw.rect(screen, rouge, (0, height - Pas_y, width, Pas_y))
            pyg.draw.rect(screen, rouge, (0, 0, width, Pas_y))

            pyg.draw.rect(screen, rouge, (0, height - (valeur - 50) * Pas_y, Pas_x, (valeur - 50) * Pas_y))
            pyg.draw.rect(screen, rouge, (width - Pas_x, height - (valeur - 50) * Pas_y, Pas_x, (valeur - 50) * Pas_y))

            pyg.draw.rect(screen, rouge, (0, 0, Pas_x, (valeur - 50) * Pas_y))
            pyg.draw.rect(screen, rouge, (width - Pas_x, 0, Pas_x, (valeur - 50) * Pas_y))

    ########################################################################################################################

    def victoire():

        Texte_Felicitation = "Hmmm...         Bien joué."
        Texte_Felicitation_En_cour = ""
        Fin = False

        start_ticks = pyg.time.get_ticks()

        Ancienne_Duree_Tempo = 0
        a = 0

        # Definition du son de parole de mohahati
        Mohahati = pyg.mixer.music.load("assets\parole_mohahati.wav")
        pyg.mixer.music.play(10, 0.0)
        pyg.mixer.music.set_volume(0.25 * son)

        while not Fin:

            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    Fin = True

                if event.type == pyg.KEYDOWN:
                    if event.key == pyg.K_ESCAPE:  # retour au menu
                        Fin = True

            Temps = pyg.time.get_ticks() - start_ticks  # Duree du temps avant le commencement du jeu en secondes

            if Temps > 1000:  # arrete le son des paroles une sec avant le commencement du jeu
                pyg.mixer.music.stop()
                for event in pyg.event.get():
                    if event.type == KEYDOWN:
                        if event.unicode == ' ':
                            Fin = True



            Duree_Tempo = round(
                0 + ((pyg.time.get_ticks() - start_ticks) / 60))  # 60 c'est la vitesse d'apparition du texte
            if Duree_Tempo != Ancienne_Duree_Tempo:
                Ancienne_Duree_Tempo = Duree_Tempo
                if a < len(Texte_Felicitation):
                    Texte_Felicitation_En_cour += Texte_Felicitation[a]
                    a += 1

            Affichage_Texte_Felicitation_En_Cour = Police_Moahati.render(Texte_Felicitation_En_cour, True, (noir))

            Affichage_Texte_Reponse_Donnee = Police.render(Texte_Reponse_Donnee, True, (blanc))
            screen.blit(background, (0, 0))

            pyg.draw.line(screen, noir, (co_x, co_y), (co_x + x, co_y + y), 3)  # Affiche l'aiguille de l'horloge

            screen.blit(Feuille, (x_Feuille, y_Feuille))
            screen.blit(Affichage_Texte_Reponse, (x_Texte_Reponse, y_Texte_Reponse))
            screen.blit(Moati, (x_Moati, y_Moati))
            screen.blit(Affichage_Texte_Reponse_Donnee, (x_Texte_Reponse_Donnee, y_Texte_Reponse_Donnee))
            screen.blit(Affichage_Texte_Felicitation_En_Cour, (x_Affichage_Texte_Question, y_Affichage_Texte_Question))
            pyg.display.update()
            pyg.display.flip()

    ########################################################################################################################

    def defaite():

        Texte_Remontrance = "VOUS ME FAITES HONTE !!!"
        Texte_Remontrance_En_cour = ""
        Fin = False

        start_ticks = pyg.time.get_ticks()

        Ancienne_Duree_Tempo = 0
        a = 0

        # Definition du son de parole de mohahati
        Mohahati = pyg.mixer.music.load("assets\parole_mohahati.wav")
        pyg.mixer.music.play(10, 0.0)
        pyg.mixer.music.set_volume(0.25 * son)

        while not Fin:

            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    Fin = True

                if event.type == pyg.KEYDOWN:
                    if event.key == pyg.K_ESCAPE:  # retour au menu
                        Fin = True

            Temps = pyg.time.get_ticks() - start_ticks  # Duree du temps avant le commencement du jeu en secondes

            if Temps > 1000:  # arrete le son des paroles une sec avant le commencement du jeu
                pyg.mixer.music.stop()
                for event in pyg.event.get():
                    if event.type == KEYDOWN:
                        if event.unicode == ' ':
                            Fin = True



            Duree_Tempo = round( 0 + ((pyg.time.get_ticks() - start_ticks) / 60))  # 60 c'est la vitesse d'apparition du texte
            if Duree_Tempo != Ancienne_Duree_Tempo:
                Ancienne_Duree_Tempo = Duree_Tempo
                if a < len(Texte_Remontrance):
                    Texte_Remontrance_En_cour += Texte_Remontrance[a]
                    a += 1

            Affichage_Texte_Remontrance_En_Cour = Police_Moahati.render(Texte_Remontrance_En_cour, True, (noir))

            Affichage_Texte_Reponse_Donnee = Police.render(Texte_Reponse_Donnee, True, (blanc))
            screen.blit(background, (0, 0))

            pyg.draw.line(screen, noir, (co_x, co_y), (co_x + x, co_y + y), 3)  # Affiche l'aiguille de l'horloge

            # y_Feuille += 1
            # y_Texte_Reponse += 1
            screen.blit(Feuille, (x_Feuille, y_Feuille))
            screen.blit(Affichage_Texte_Reponse, (x_Texte_Reponse, y_Texte_Reponse))
            screen.blit(Moati, (x_Moati, y_Moati))
            screen.blit(Affichage_Texte_Reponse_Donnee, (x_Texte_Reponse_Donnee, y_Texte_Reponse_Donnee))
            screen.blit(Affichage_Texte_Remontrance_En_Cour, (x_Affichage_Texte_Question, y_Affichage_Texte_Question))
            pyg.display.update()
            pyg.display.flip()

    ########################################################################################################################

    while Jeu_Lance:

        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                Jeu_Lance = False

            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_ESCAPE: # retour au menu
                    Jeu_Lance = False


        Duree_Tempo = round(Duree_Anim - ((
                                                      pyg.time.get_ticks() - start_ticks) / 1000))  # Duree du temps avant le commencement du jeu en secondes
        pos = pyg.mouse.get_pos()

        if Duree_Tempo == 1:  # arrete le son des paroles une sec avant le commencement du jeu
            pyg.mixer.music.stop()

        if Duree_Tempo <= 3:
            Duree_Tempo2 = round(
                0 + ((pyg.time.get_ticks() - start_ticks) / 34))  # 34 c'est la vitesse d'apparition du texte
            if Duree_Tempo2 != Ancienne_Duree_Tempo2:
                if a < len(Texte_Question):
                    Texte_Question_En_Cour += Texte_Question[a]
                    a += 1
                    Ancienne_Duree_Tempo2 = Duree_Tempo2

        Affichage_Texte_Question_En_Cour = Police_Moahati.render(Texte_Question_En_Cour, True, (noir))

        for event in pyg.event.get():
            # Definis la croix pour fermer la fenetre
            if event.type == pyg.QUIT:
                pyg.quit()

            if Duree_Tempo <= 0:
                if event.type == KEYDOWN:
                    if event.key == pyg.K_KP_ENTER:
                        if Texte_Reponse_Donnee == Texte_Reponse:
                            bonne_rep = True
                            Jeu_Lance = False

                    # code les lettres pour qu'elles soient ajoutées au texte de réponseA
                    if event.key == pyg.K_BACKSPACE:
                        Texte_Reponse_Donnee = Texte_Reponse_Donnee[:-1]

                    # ajoute le caractère à la reponse donnee si dans la liste de caractères possibles Liste_caracteres
                    if event.unicode in Liste_carcteres:
                        Texte_Reponse_Donnee += str(event.unicode)
                    Affichage_Texte_Reponse_Donnee = Police.render(Texte_Reponse_Donnee, True, (blanc))

        if Duree_Tempo <= 1 and Duree_Tempo >= 0 and y_Feuille > height - height // 20:
            y_Feuille -= 0.5
            y_Texte_Reponse -= 0.5

        if Duree_Tempo <= 0:
            x, y = pos[0], pos[1]
            if x > x_Feuille and x < x_Feuille + width_Feuille and y > y_Feuille and y < y_Feuille + height_Feuille:  # monte la feuille si on est dessus
                if y_Feuille > height - height // 8:
                    y_Feuille -= height // 130
                    y_Texte_Reponse -= height // 130
            else:  # descend la feuille si on est plus dessus
                if y_Feuille < height - height // 20:
                    y_Feuille += height // 130
                    y_Texte_Reponse += height // 130
            Secondes_citation = round(Duree + Duree_Anim - ((pyg.time.get_ticks() - start_ticks) / 1000))

        if Secondes_citation == 0:  # Test si temps ecoule
            perdu = True
            Jeu_Lance = False

        screen.blit(background, (0, 0))
        screen.blit(Feuille, (x_Feuille, y_Feuille))
        screen.blit(Affichage_Texte_Reponse, (x_Texte_Reponse, y_Texte_Reponse))
        screen.blit(Affichage_Texte_Reponse_Donnee, (x_Texte_Reponse_Donnee, y_Texte_Reponse_Donnee))
        screen.blit(Affichage_Texte_Question_En_Cour, (x_Affichage_Texte_Question, y_Affichage_Texte_Question))
        screen.blit(Moati, (x_Moati, y_Moati))

        # Affichage Horloge
        if Secondes_citation != anciennes_Secondes_citation:  # modifie l'angle de l'horologe chaque sec
            angle += 2 / Duree * math.pi  # en radiant

        x = round(math.cos(angle) * rayon_horloge)
        y = round(math.sin(angle) * rayon_horloge)
        pyg.draw.line(screen, noir, (co_x, co_y), (co_x + x, co_y + y),
                      3)  # fais le tracé de l'aiguille de l'horloge le centre est (co_x, co_y) et x, y c'est le décalage qu'il faut avec le centre pour que l'aiguille aille au bon endroit
        anciennes_Secondes_citation = Secondes_citation

        # S'ocupe du score avant defaite (le score c a quel point on est vu en train de tricher par le prof)
        if y_Feuille < height - height // 20:
            Score_Avant_Defaite += 0.5
        else:
            if Score_Avant_Defaite > 0:
                Score_Avant_Defaite -= 0.5

        contour(Score_Avant_Defaite)
        if Score_Avant_Defaite > 100:  # Test si le prof nous voit tricher
            perdu = True
            Jeu_Lance = False

        pyg.display.update()
        pyg.display.flip()

    if bonne_rep:
        victoire()

    if perdu:
        defaite()


########################################################################################################################

#citation(height,width,son)