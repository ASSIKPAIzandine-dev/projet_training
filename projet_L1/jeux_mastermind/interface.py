
import tkinter as tk
from tkinter import messagebox
import random

# Générer le code secret
def generer_code_secret(longue, maximum):
    return [random.randint(1, maximum) for _ in range(longue)]

# Comparer l'essai avec le code secret
def comparer_essai(code, j):
    bien, mal = 0, 0
    code_temp = code.copy()
    j_temp = j.copy()

    for i in range(len(code)):
        if j_temp[i] == code_temp[i]:
            bien += 1
            j_temp[i] = None
            code_temp[i] = None

    for num in j_temp:
        if num is not None and num in code_temp:
            mal += 1
            code_temp[code_temp.index(num)] = None

    return bien, mal

# Lancer une nouvelle partie
def nouvelle_partie():
    global secret, essais_restants
    secret = generer_code_secret(4, 6)
    essais_restants = 12
    entree.delete(0, tk.END)
    historique.delete(1.0, tk.END)
    messagebox.showinfo("Mastermind", "💫 Nouvelle partie lancée! Bonne chance 😎")

# Vérifier l'essai du joueur
def verifier_essai():
    global essais_restants
    essai = entree.get()
    if len(essai)!= 4 or not essai.isdigit() or not all(1 <= int(ch) <= 6 for ch in essai):
        messagebox.showerror("Erreur", "Entrez exactement 4 chiffres entre 1 et 6.")
        return

    essais_restants -= 1
    essai_liste = [int(ch) for ch in essai]
    bien, mal = comparer_essai(secret, essai_liste)

    historique.insert(tk.END, f"Essai: {essai} → 🔴:{bien} ⚪:{mal}\n")

    if bien == 4:
        messagebox.showinfo("Victoire", "🎉 Gagné! Vous avez deviné le code.")
        nouvelle_partie()
    elif essais_restants == 0:
        messagebox.showinfo("Perdu", f"☠️ Fin des essais. Le code était: {''.join(map(str, secret))}")
        nouvelle_partie()

# Interface principale
fenetre = tk.Tk()
fenetre.title("Mastermind 🎯")

tk.Label(fenetre, text="Entrez 4 chiffres entre 1 et 6:").pack()
entree = tk.Entry(fenetre)
entree.pack()

tk.Button(fenetre, text="Valider", command=verifier_essai).pack(pady=5)
tk.Button(fenetre, text="Nouvelle Partie", command=nouvelle_partie).pack()

historique = tk.Text(fenetre, height=10, width=40)
historique.pack(pady=10)

nouvelle_partie()
fenetre.mainloop()

