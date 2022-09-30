"""
L’ordinateur choisi au hasard (librairie random à importer) un nombre aléatoire entre 0 et 1000.
L’ordinateur demande à l’usager d’entrer un nombre de 0 à 1000 de façon à trouver celui qu’il a choisi.
Alex Gaudreau
Groupe: 406
"""

import random


def parti():
    """
    Cette fonction commence la partie
    :return:
    """
    print("J'ai coisi un nombre entre ", borne_minimal, " et ", borne_maximal, ". A vous de le deviner...")
    nouvelle_essai()


def nouvelle_essai():
    """
     le joueur entre son essai et la fonction regarde si il a raison
    :return:
    """
    global nb_essais
    global nombre_choisi
    nb_essais += 1
    essai = int(input("Entez votre essai :_"))
    if essai < nombre_choisi:
        print("Mauvaise réponse, le nombre est plus grand que", essai)
        nouvelle_essai()
    elif essai > nombre_choisi:
        print("Mauvaise réponse, le nombre est plus petit que", essai)
        nouvelle_essai()
    else:
        print("Bravo! Bonne reponse. Vous avez reussi en", nb_essais, "essais!")


while True:
    nb_essais = 0
    borne_minimal = int(input("Choisisser la borne minimal:_"))
    borne_maximal = int(input("Choisisser la borne maximal:_"))
    nombre_choisi = random.randint(borne_minimal, borne_maximal)
    parti()
    rejouer = input("Voulez-vous faire une autre partie (o/n)?")
    if rejouer == "o":
        continue
    else:
        print("Merci et au revoir…")
        break
