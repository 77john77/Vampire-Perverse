import random
from art import text2art

print(text2art("FIGHT"))

def combat():
    # Définir les points de la vampire perverse et du héros
    VP_vie = 30
    joueur_vie = 30
    potions = 2

    # Boucle de combat
    while VP_vie > 0 and joueur_vie > 0:
        print("Vous avez", joueur_vie, "points de vie.")
        print("La vampire a", VP_vie, "points de sang.")
        print("Vous avez", potions, "potions de soin.")

        # Action du joueur
        choix = input("Appuyez sur 'a' pour attaquer, 'p' pour boire une potion de soin : ")
        if choix == 'a':
            # Lancer l'attaque pour le joueur et la vampire
            joueur_attaque = random.randint(1, 9)
            VP_attaque = random.randint(1, 9)

            # Afficher les résultats des lancers de dés
            print("Vous avez attaqué pour", joueur_attaque)
            print("La vampire perverse a attaqué pour", VP_attaque)

            # Calcul des dégâts
            joueur_degats = joueur_attaque
            VP_degats = VP_attaque

            # Si le joueur obtient un 8, il inflige 2 dégâts supplémentaires
            if joueur_attaque == 8:
                joueur_degats += 2
                print("Vous infligez 2 dégâts supplémentaires !")

            # Si la vampire obtient un 8, elle récupère 2 points de vie
            if VP_attaque == 8:
                VP_vie += 2
                print("La Vampire a récupéré 2 points de vie !")

            # Si le joueur obtient un 1, il inflige 0 dégâts
            if joueur_attaque == 1:
                joueur_degats -= 1
                print("Vous vous êtes raté !")

            # Si la vampire obtient un 1, elle récupère 1 point de vie
            if VP_attaque == 1:
                VP_vie += 1
                print("La Vampire a récupéré 1 point de vie !")

            # Appliquer les dégâts
            joueur_vie -= VP_degats
            VP_vie -= joueur_degats

            # Afficher les résultats
            print("Vous infligez", joueur_degats, "dégâts à la vampire.")
            print("La vampire vous suce", VP_degats, "points de vie.")

        elif choix == 'p':
            # Le joueur boit une potion de soin
            if potions > 0:
                joueur_vie += 10
                potions -= 1
                print("Vous avez récupéré 10 points de vie.")
            else:
                print("Vous n'avez plus de potions de soin !")

        else:
            print("Commande invalide !")

    # Afficher le résultat de la baston
    if joueur_vie > 0:
        print("Vous avez vaincu la vampire elle ne sucera plus personne !")
        print()
        # Affichage du texte "VICTOIRE"
        print(text2art("VICTOIRE"))
        print()
    else:
        print("La vampire vous a vaincu, il n'y a plus rien à sucer...")
        print()
        # Affichage du texte "ECHEC"
        print(text2art("ECHEC"))
        print()
    # Demander si le joueur veut relancer le jeu
    relancer = input("Voulez-vous relancer le jeu ? (o/n) : ")
    if relancer == 'o':
        combat()

# Lancer le jeu
combat()
