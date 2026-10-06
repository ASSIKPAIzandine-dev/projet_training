import random
import getpass

# Fonction pour générer le code secret
def generer_code_secret(longue, maximum):
    secret = [random.randint(1, maximum) for _ in range(longue)]
    return secret

# Fonction pour demander l'entrée de l'utilisateur et vérifier sa validité
def demander_essai(longue):
    while True:
        z = getpass.getpass("Joueur 1, entrez votre code secret (4 chiffres entre 1 et 6): ")
        if len(z) == longue and z.isdigit():
            return [int(b) for b in z]
        else:
            print("Entrée invalide. Assurez-vous de saisir exactement 4 chiffres entre 1 et 6.")

# Fonction pour deviner le code
def devine_e(longue):
    while True:
        r = input("Joueur 2, entrez votre nombre (4 chiffres entre 1 et 6): ")
        if len(r) == longue and r.isdigit():
            return [int(b) for b in r]
        else:
            print("Entrée invalide. Assurez-vous de saisir exactement 4 chiffres entre 1 et 6.")

# Fonction pour comparer l'essai de l'utilisateur avec le code secret
def comparer_essai(code, j):
    bien, mal = 0, 0
    code_temp = code.copy()
    j_temp = j.copy()

    # Vérifier les chiffres bien placés
    for i in range(len(code)):
        if j_temp[i] == code_temp[i]:
            bien += 1
            j_temp[i] = None
            code_temp[i] = None

    # Vérifier les chiffres mal placés
    for num in j_temp:
        if num is not None and num in code_temp:
            mal += 1
            code_temp[code_temp.index(num)] = None

    return bien, mal

# Fonction principale du jeu
def mastermind(longue=4, maximum=6, max_essais=12):
    print("                   💫BIENVENUE AU JEU DE MASTERMIND💫!")
    print("                    🤗BONNE CHANCE !!!😎")
    jouer_avec_autrui = input("Voulez-vous jouer seul (S) ou avec une autre personne (A) ? (S/A): ").lower()
    while jouer_avec_autrui !='s' and jouer_avec_autrui !='a':
      jouer_avec_autrui = input("Voulez-vous jouer seul (S) ou avec une autre personne (A) ? (S/A): ").lower()
    

    if jouer_avec_autrui == 'a':
        secret = demander_essai(longue)  # Joueur 1 entre le code secret
        print("Joueur 2, devinez le code secret !")
    elif jouer_avec_autrui == 's':
        secret = generer_code_secret(longue, maximum)

    essai = 0
    while essai < max_essais:
        essai += 1
        j = devine_e(longue)  # Joueur 2 fait sa devinette
        bien, mal = comparer_essai(secret, j)

        # Affichage avec pions rouges et blancs
        pions_rouges = "🔴" * bien
        pions_blancs = "⚪" * mal

        print("Pions rouges Bien placés :", pions_rouges)
        print("Pions blancs Mal placés :", pions_blancs)

        # Condition de victoire
        if bien == 4:
            print("Gagné!")
            break

        # Limite d'essais atteinte
        if essai == max_essais:
            print("Vos essais sont finis☠️☠️☠️☠️.")
            print("Le code secret était :", "".join(map(str, secret)))

    # Demander si l'utilisateur souhaite continuer
    continuer = input("Voulez-vous continuer ? (oui/non) : ")
    if continuer.lower() == "oui":
        mastermind(longue, maximum, max_essais)  # Relancer le jeu
    else:
        print("Merci d'avoir joué !")

# Démarrer le jeu
mastermind(longue=4, maximum=6)
