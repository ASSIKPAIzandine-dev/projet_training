
import random


#Fonction pour générer le code secret
def generer_code_secret(longue, maximum):
    secret = []
    for i in range(longue):
        a = random.randint(1, maximum)
        secret.append(a)
        
    return secret

#Fonction pour demander l'entrée de l'utilisateur et vérifier sa validité
def demander_essai(longue):
    while True:
    #tentative pr dvn code secret
        z = input("Entrer Un Nombre De 4 Chiffres Entre L'Intervale 1 Et 6: ")
        while len(z) != longue or not z.isdigit():
            z = input("Entrer un nombre de 4 chiffres entre l'intervale 1 et 6: ")
        return [int(b) for b in z]

#Fonction pour comparer l'essai de l'utilisateur avec le code secret
def comparer_essai(code, j, longue):
    bien, mal = 0, 0
    # Vérifier les chiffres bien placés
    for i in range(longue):
        if j[i] == code[i]:
            bien += 1  # Pion rouge pour bien placé
            j[i] = "#"
            code[i] = "*"

    # Vérifier les chiffres mal placés
    for i in range(longue):
      if j[i] in code and j[i] != "#":
            mal += 1  # Pion blanc pour mal placé
            code[code.index(j[i])] = "*"
    
    return bien, mal

#Fonction principale du jeu
def mastermind(longue=4, maximum=6):
    print("                   💫BIENVENUE  AU JEUX DE MASTERMIND💫!")
    print("                    🤗BONNE CHANCE !!!😎")  # Demander si l'utilisateur veut jouer avec une autre personne
    jouer_avec_autrui = input("Voulez-vous jouer seul (S) ou avec une autre personne (A) ? (S/A): ").lower()

    if jouer_avec_autrui == 'a':
        print("Joueur 1, entrez votre code secret ! (4 chiffres entre 1 et 6)")
        secret = demander_essai(longue)  # Joueur 1 entre son code secret
        print("Joueur 2, devinez le code secret !")
    else:
        secret = generer_code_secret(longue, maximum)  # Générer un code secret aléatoire

    essai = 0
    var=True
    while var:
        secret = generer_code_secret(longue, maximum)
        essai = 0
        
        # Boucle de jeu 
        var=True
        while   var:
            code = list(secret)
            j = demander_essai(longue)
            essai += 1
            bien, mal = comparer_essai(code, j, longue)

            # Affichage avec pions rouges et blancs
            pions_rouges = "🔴" * bien  # Pions rouges (bien placés)
            pions_blancs = "⚪" * mal   # Pions blancs (mal placés)
            
            print("Pions rouges Bien placé :" ,pions_rouges )
            print("Pions blancs Mal placé : ",pions_blancs)
            # Condition de victoire
            if bien == 4:  # Si tous les pions sont bien placés (quatre pions rouges)
                print("🎇💥Gagné😄🍻🍷🍾🎆!")
                break

            # Limite d'essais
            if essai == 5:
                print("😭Vos essais sont finis☠️☠️☠️☠️.")
                print("Le code secret était :", "".join(map(str, secret)))
                break
        
        # Demander si l'utilisateur souhaite continuer
        continuer = input("Voulez-vous continuer ? (oui/non) : ")
        if continuer.lower() != "oui":
            print("Merci d'avoir joué !")
            var=False
            return

#Démarrer le jeu
mastermind(longue=4, maximum=6)

 
