#L’ordinateur choisi au hasard (librairie random à importer) un nombre aléatoire entre 0 et 1000.
#L’ordinateur demande à l’usager d’entrer un nombre de 0 à 1000 de façon à trouver celui qu’il a choisi.

import random


x = random.randint(0, 100)
nb_essais = 0
print(x)
print("J'ai coisi un nombre entre 0 et 100. A vous de le deviner...")

def rejouer():
     nb_essais = 0
     rejoueron = str(input("Voulez-vous faire une autre partie (o/n)?_"))
     if rejoueron == "o":
         partie()
     else:
        print("Merci et aurevoir.")

     return nb_essais



def partie():
    essai = int(input("Entez votre essai :_"))
    return essai
    raison()


def raison():
    global essai

    choix_joueur = essai

    if choix_joueur < x:
        print("Mauvaise réponse, le nombre est plus grand que", choix_joueur)
        partie()

    if choix_joueur > x:
        print("Mauvaise réponse, le nombre est plus petit que", choix_joueur)
        partie()

    if choix_joueur == x:
        print("Bravo! Bonne reponse. Vous avez reussi en", nb_essais, "essais!")
        #rejouer = str(input("Voulez-vous faire une autre partie (o/n)?_"))
        #if rejouer == "o":
            #partie()
       # else:
            #print("Merci et aurevoir.")


partie()


