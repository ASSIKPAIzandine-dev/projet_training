
```python
import random

Fonction pour générer le code secret
def generer_code_secret(longue, maximum):
    secret = []
    for i in range(longue):
        a = random.randint(1, maximum)
        secret.append(a)
    return secret

Fonction pour demander l'entrée de l'utilisateur et vérifier sa validité
def demander_essai(longue):
    while True:
        z = input("Entrer Un Nombre De 4 Chiffres Entre L'Intervale 1 Et 6: ")
        while len(z) != longue or not z.isdigit():
            z = input("Entrer un nombre de 4 chiffres entre l'intervale 1 et 6: ")
        return [int(b) for b in z]

Fonction pour comparer l'essai de l'utilisateur avec le code secret
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

Fonction pour afficher l'historique sous forme de tableau
def afficher_historique(historique):
    print("\nHistorique des essais:")
    print(f"{'Essai':<6}{'Chiffres':<20}{'Bien Placés':<15}{'Mal Placés':<15}")  # En-têtes
    print("-" * 56)  # Séparateur pour un meilleur affichage
    for essai, (valeur, bien, mal) in enumerate(historique, start=1):
        # Affiche les données alignées sous chaque colonne
        print(f"{essai:<6}{' '.join(map(str, valeur)):<20}{bien:<15}{mal:<15}")
    print("-" * 56)

#Fonction principale du jeu
def mastermind(longue=4, maximum=6):
    historique = []  # Liste pour garder l'historique des essais
    while True:
        secret = generer_code_secret(longue, maximum)
        essai = 0
        
        # Boucle de jeu
        while True:
            code = list(secret)
            j = demander_essai(longue)
            essai += 1
            bien, mal = comparer_essai(code, j, longue)
            
            # Ajouter à l'historique
            historique.append((j, bien, mal))

            if bien == 4:
                print("Gagné !")
                break
print(f"Le bien placé est : {bien} | Le mal placé est : {mal}")
            
            if essai == 2:  # Limitation à 2 essais
                print("Vos essais sont finis.")
                print(f"Le code secret était : {''.join(map(str, secret))}")
                break

        # Afficher l'historique
        afficher_historique(historique)

        # Demander si l'utilisateur souhaite continuer
        continuer = input("Voulez-vous continuer ? (oui/non) : ")
        if continuer.lower() != "oui":
            print("Merci d'avoir joué !")
            break

Démarrer le jeu
mastermind(longue=4, maximum=6)
```


