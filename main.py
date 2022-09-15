#L’ordinateur choisi au hasard (librairie random à importer) un nombre aléatoire entre 0 et 1000.
#L’ordinateur demande à l’usager d’entrer un nombre de 0 à 1000 de façon à trouver celui qu’il a choisi.

import random

# def rejouer():
#     rejoueron = str(input("Voulez-vous faire une autre partie (o/n)?_"))
#     if rejoueron == "o":
#         partie()
#     else:
#      print("Merci et aurevoir.")

def joueur_essai():

    essai = int(input("Entez votre essai :_"))
    return essai

def partie():
    nb_essais = 0
    x = random.randint(0, 100)
    print(x)
    print("J'ai coisi un nombre entre 0 et 100. A vous de le deviner...")

    choix_joueur = joueur_essai()

    nb_essais += 1

    if choix_joueur < x:
        print("Mauvaise réponse, le nombre est plus grand que", choix_joueur)
        joueur_essai()

    if choix_joueur > x:
        print("Mauvaise réponse, le nombre est plus petit que", choix_joueur)
        joueur_essai()

    if choix_joueur == x:
        print("Bravo! Bonne reponse. Vous avez reussi en", nb_essais, "essais!")

        rejouer = str(input("Voulez-vous faire une autre partie (o/n)?_"))
        if rejouer == "o":
            partie()
        else:
            print("Merci et aurevoir.")


joueur_essai()


