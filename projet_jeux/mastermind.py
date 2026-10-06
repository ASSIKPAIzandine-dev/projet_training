

import tkinter as tk
from tkinter import messagebox
import random

# --- LOGIQUE DU JEU ---
def generer_code_secret(longue, maximum):
    return [random.randint(1, maximum) for _ in range(longue)]

def comparer_essai(code, j):
    bien, mal = 0, 0
    code_temp = list(code)
    j_temp = list(j)
    for i in range(len(code)):
        if j_temp[i] == code_temp[i]:
            bien += 1
            j_temp[i] = code_temp[i] = None
    for num in j_temp:
        if num is not None and num in code_temp:
            mal += 1
            code_temp[code_temp.index(num)] = None
    return bien, mal

# --- INTERFACE GRAPHIQUE ---
def dessiner_resultat(essai_str, bien, mal):
    y_offset = (6 - essais_restants - 1) * 55 + 40
    
    # Texte de l'essai
    canvas.create_text(70, y_offset + 25, text=f"Essai {6-essais_restants}: {essai_str}", 
                       fill="white", font=("Helvetica", 11, "bold"))

    # Dessiner les "Bien placés" (Rouge + Texte BP)
    for i in range(bien):
        x = 180 + (i * 45)
        canvas.create_oval(x, y_offset+5, x+40, y_offset+45, fill="#FF4B2B", outline="white", width=2)
        canvas.create_text(x+20, y_offset+25, text="BP", fill="white", font=("Arial", 10, "bold"))

    # Dessiner les "Mal placés" (Bleu + Texte MP)
    for i in range(mal):
        x = 360 + (i * 45)
        canvas.create_oval(x, y_offset+5, x+40, y_offset+45, fill="#00D2FF", outline="white", width=2)
        canvas.create_text(x+20, y_offset+25, text="MP", fill="white", font=("Arial", 10, "bold"))

def mettre_a_jour_label():
    label_essais.config(text=f"ESSAIS RESTANTS : {essais_restants}")

def nouvelle_partie():
    global secret, essais_restants
    secret = generer_code_secret(4, 8)
    essais_restants = 6
    entree.delete(0, tk.END)
    canvas.delete("all")
    mettre_a_jour_label()
    # Légendes précises
    canvas.create_text(210, 20, text="🔴 BP = Bien Placé", fill="#FF4B2B", font=("Arial", 10, "bold"))
    canvas.create_text(380, 20, text="🔵 MP = Mal Placé", fill="#00D2FF", font=("Arial", 10, "bold"))
    canvas.create_line(10, 35, 470, 35, fill="gray")

def verifier_essai():
    global essais_restants
    essai = entree.get()
    if len(essai) != 4 or not essai.isdigit():
        messagebox.showerror("Erreur", "Entrez exactement 4 chiffres")
        return
    
    essai_liste = [int(ch) for ch in essai]
    bien, mal = comparer_essai(secret, essai_liste)
    
    essais_restants -= 1
    mettre_a_jour_label()
    dessiner_resultat(essai, bien, mal)
    entree.delete(0, tk.END)

    if bien == 4:
        messagebox.showinfo("Victoire", "🎉 Bravo ! Le code était bien " + essai)
        nouvelle_partie()
    elif essais_restants == 0:
        messagebox.showinfo("Perdu", f"☠️ Terminé ! Le code était : {''.join(map(str, secret))}")
        nouvelle_partie()

# Fenêtre principale
root = tk.Tk()
root.title("Mastermind Expert 🎯")
root.geometry("500x600")
root.configure(bg="#2C3E50")

# Label des essais restants
label_essais = tk.Label(root, text="", fg="#F1C40F", bg="#2C3E50", font=("Helvetica", 14, "bold"))
label_essais.pack(pady=5)

tk.Label(root, text="ENTREZ 4 CHIFFRES (1-8)", fg="white", bg="#2C3E50", font=("Helvetica", 10)).pack()
entree = tk.Entry(root, font=("Helvetica", 20), width=10, justify="center", bg="#ECF0F1")
entree.pack(pady=5)

btn_frame = tk.Frame(root, bg="#2C3E50")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="VALIDER", command=verifier_essai, bg="#27AE60", fg="white", font=("Arial", 10, "bold"), padx=20).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="ANNULER", command=nouvelle_partie, bg="#E74C3C", fg="white", font=("Arial", 10, "bold"), padx=10).pack(side=tk.LEFT)

canvas = tk.Canvas(root, width=480, height=420, bg="#34495E", highlightthickness=0)
canvas.pack(pady=10)

nouvelle_partie()
root.mainloop()
