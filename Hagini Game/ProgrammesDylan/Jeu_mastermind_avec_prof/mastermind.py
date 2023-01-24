import random


couleur = ['rouge', 'blanc', 'vert', 'jaune', 'bleu', 'violet']
nb_essaie = 10
essaie = 0

def config_aleatoire():
    config = [0] * 4
    for i in range(4):
        valeur_couleur = random.randint(0,(5-i))
        config[i] = couleur[valeur_couleur]
        couleur.remove(config[i])
    return config
config = config_aleatoire()
print(config)

def joueur_choisi():
    choix_du_joueur = input("entre").split(" ")
    return choix_du_joueur

def pion_noir(choix_joueur):
    nb_pion_noir = 0
    for i in range(4):
        for y in range(4):
            if choix_joueur[i] == config[y]:
                nb_pion_noir += 1
    return nb_pion_noir

def pion_rouge(choix_joueur):
    nb_pion_rouge = 0
    for i in range(4):
        if choix_joueur[i] == config[i]:
            nb_pion_rouge += 1
    return nb_pion_rouge


run = True
victoire = False
while run:
    essaie += 1
    choix_joueur = joueur_choisi()
    if pion_rouge(choix_joueur) == 4:
        victoire = True
    print(pion_noir(choix_joueur))
    print(pion_rouge(choix_joueur))
    if victoire:
        run = False
    if essaie == nb_essaie:
        run = False
if victoire:
    print("bien joué")
else:
    print("la honte")