#L’ordinateur choisi au hasard (librairie random à importer) un nombre aléatoire entre 0 et 1000.
#L’ordinateur demande à l’usager d’entrer un nombre de 0 à 1000 de façon à trouver celui qu’il a choisi.

import random

def partie():
    x = random.randint(0, 2)
    nb_essai = 0

    print("J'ai coisi un nombre entre 0 et 100. A vous de le deviner...")

    def joueur_essai():

        global nb_essai
        essai = int(input("Entez votre essai :_"))
        nb_essai += 1
        print(nb_essai)

        if essai < x:
            print("Mauvaise réponse, le nombre est plus grand que", essai)
            joueur_essai()

        if essai > x:
            print("Mauvaise réponse, le nombre est plus grand que", essai)
            joueur_essai()

        if essai == x:
            print("Bravo! Bonne reponse. Vous avez reussi en", nb_essai, "essais!")
    joueur_essai()

rejouer = str(input("Voulez-vous faire une autre partie (o/n)?_"))