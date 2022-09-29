#L’ordinateur choisi au hasard (librairie random à importer) un nombre aléatoire entre 0 et 1000.
#L’ordinateur demande à l’usager d’entrer un nombre de 0 à 1000 de façon à trouver celui qu’il a choisi.

import random


def nb_hasard():
    return random.randint(borne_minimal, borne_maximal)


def nouvelle_essai():
        global essai
        essai = int(input("Entez votre essai :_"))
        global nb_essais
        nb_essais += 1
        return essai


while True:

    borne_minimal = int(input("Choisisser la borne minimal:_"))
    borne_maximal = int(input("Choisisser la borne maximal:_"))

    nb_hasard()
    nombre_choisi = nb_hasard()
    nb_essais = 0
    print(nombre_choisi)
    print("J'ai coisi un nombre entre ", borne_minimal, " et ", borne_maximal, ". A vous de le deviner...")
    essai = int(input("Entez votre essai :_"))
    nb_essais += 1

    if essai < nombre_choisi:
        print("Mauvaise réponse, le nombre est plus grand que", essai)
        nouvelle_essai()
    elif essai > nombre_choisi:
        print("Mauvaise réponse, le nombre est plus petit que", essai)
        nouvelle_essai()
    else:
        print("Bravo! Bonne reponse. Vous avez reussi en", nb_essais, "essais!")
        break
