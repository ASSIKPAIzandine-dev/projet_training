
import random

#Fonction pour générer le code secret (utilisée lorsque c'est un joueur qui doit deviner)
def generer_code_secret(longue, maximum):
    secret = []
    for i in range(longue):
        a = random.randint(1, maximum)
        secret.append(a)
    return secret

#Fonction pour demander l'entrée de l'utilisateur et vérifier sa validité
def demander_essai(longue):
    while True:
        z = input("Entrer un nombre de quatre chiffres entre 1 et 6 : ")
        while len(z) != 4 or not z.isdigit():
            z = input("Entrer un nombre de quatre chiffres entre 1 et 6 : ")
        return [int(b) for b in z]

#Fonction pour comparer l'essai de l'utilisateur avec le code secret
def comparer_essai(code, j, longue):
    bien, mal = 0, 0
# Vérifier les chiffres bien placés
    for i in range(longue):
        if j[i] == code[i]:
            bien += 1
            j[i] = "#"
            code[i] = "*"

    # Vérifier les chiffres mal placés
    for i in range(longue):
        if j[i] in code:
            mal += 1
            code[code.index(j[i])] = "*"

    return bien, mal

#Fonction pour le jeu avec autrui
def jouer_avec_autrui(longue=4, maximum=6):
    print("Bienvenue dans Mastermind ! Vous allez jouer à deux.")
    print("Le premier joueur choisira un code secret et le deuxième joueur va devoir le deviner.")
    
    # Premier joueur entre le code secret
    secret = []
    while len(secret) != longue:
        secret_input = input(f"Joueur 1, entrez un code secret de {longue} chiffres entre 1 et {maximum}: ")
        if len(secret_input) == longue and secret_input.isdigit():
            secret = [int(x) for x in secret_input]
        else:
            print("Code secret invalide, essayez à nouveau.")
    
    print("\nJoueur 2, c'est à vous de deviner le code secret !")

    essai = 0
    historique = []
    jeu_en_cours = True  # Variable pour contrôler la boucle

    # Boucle du jeu
    while jeu_en_cours:
        # Demander à Joueur 2 de faire une tentative
        code = list(secret)
        j = demander_essai(longue)
        essai += 1
        bien, mal = comparer_essai(code, j, longue)

        # Afficher les résultats
        pions_bien = "🔴" * bien
        pions_mal = "⚪" * mal
        print(f"Pions bien placés : {pions_bien}, Pions mal placés : {pions_mal}")

        # Ajouter l'essai à l'historique
        historique.append((j, pions_bien, pions_mal))

        # Afficher l'historique des tentatives
        print("\nHistorique des tentatives :")
        print("Tentative | Pions Bien Placés | Pions Mal Placés")
        for i, (tentative, pions_bien, pions_mal) in enumerate(historique, 1):
            print(f"{i:9} | {pions_bien:18} | {pions_mal:18}")

        # Si le joueur a deviné correctement
        if bien == 4:
            print("\nJoueur 2 a gagné ! Le code secret était :", "".join(map(str, secret)))
            jeu_en_cours = False  # Arrêter le jeu

        # Si le joueur atteint le maximum d'essais
        elif essai == 5:
            print("Vos essais sont finis.")
            print("Le code secret était :", "".join(map(str, secret)))
            jeu_en_cours = False  # Arrêter le jeu

#Fonction pour jouer en solo (le joueur doit deviner un code généré aléatoirement)
def jouer_en_solo(longue=4, maximum=6):
     print("Bienvenue dans Mastermind ! Vous allez jouer seul.")
     secret = generer_code_secret(longue, maximum)
     essai = 0
     historique = []
     jeu_en_cours = True  # Variable pour contrôler la boucle

    # Boucle de jeu
     while jeu_en_cours:
        code = list(secret)
        j = demander_essai(longue)
        essai += 1
        bien, mal = comparer_essai(code, j, longue)

        # Afficher les résultats
        pions_bien = "🔴" * bien
        pions_mal = "⚪" * mal
        print(f"Pions bien placés : {pions_bien}, Pions mal placés : {pions_mal}")

        # Ajouter l'essai à l'historique
        historique.append((j, pions_bien, pions_mal))

        # Afficher l'historique des tentatives
        print("\nHistorique des tentatives :")
        print("Tentative | Pions Bien Placés | Pions Mal Placés")
        for i, (tentative, pions_bien, pions_mal) in enumerate(historique, 1):
            print(f"{i:9} | {pions_bien:18} | {pions_mal:18}")

        # Si le joueur a deviné correctement
        if bien == 4:
            print("\nFélicitations, vous avez gagné ! Le code secret était :", "".join(map(str, secret)))
            jeu_en_cours = False  # Arrêter le jeu

        # Si le joueur atteint le maximum d'essais
        elif essai == 5:
            print("Vos essais sont finis.")
            print("Le code secret était :", "".join(map(str, secret)))
            jeu_en_cours = False  # Arrêter le jeu

#Fonction principale pour démarrer le jeu
def mastermind(longue=4, maximum=6):
    print("Bienvenue dans Mastermind !")
    choix = input("Souhaitez-vous jouer en solo ou avec autrui ? (solo/autrui) : ").lower()

    if choix == "autrui":
        jouer_avec_autrui(longue, maximum)
    elif choix == "solo":
        jouer_en_solo(longue, maximum)
    else:
        print("Choix invalide. Veuillez choisir 'solo' ou 'autrui'.")

#Démarrer le jeu
mastermind(longue=4, maximum=6)

