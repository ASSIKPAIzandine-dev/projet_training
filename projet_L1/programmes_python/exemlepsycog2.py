

📘 EXPLICATION LIGNE PAR LIGNE :

1. import psycopg2  
   → Importe la bibliothèque permettant de se connecter à PostgreSQL.

2. def connection():  
   → Fonction pour se connecter à la base PostgreSQL.
3. con = psycopg2.connect(...)  
   → Établit la connexion. Tu dois renseigner les bons paramètres (host, user, password, dbname).

4. return con  
   → Retourne la connexion à la base.

---

5. def interface_utilisateur():  
   → Fonction qui demande les infos à l'utilisateur.

6–8. input(...)  
   → L’utilisateur saisit nom, prénom et âge.

9. return nom, prenom, age  
   → On retourne les valeurs saisies.

---

10. def insertion(nom, prenom, age):  
   → Fonction qui insère les données dans la table.

11–13. Connexion, exécution SQL, commit  
   → On insère les valeurs avec des paramètres sécurisés (%s, %s, %s).

14–15. Fermeture du curseur et connexion

---

16. def afficher():  
   → Fonction principale qui orchestre le tout.

17–18. Connexion + curseur

20–21. Appel…
Explique moi chaque fonction en détail
Voici l’explication détaillée de chaque fonction du script :

---

1. connection()

But : Établir une connexion à la base PostgreSQL.

Détail :
- psycopg2.connect(...) : permet de se connecter à une base PostgreSQL.
  - Tu dois indiquer l’hôte (localhost), l’utilisateur (user=postgres), le mot de passe (password=1234) et la base (dbname=ma_base).
- return con : renvoie l’objet connexion pour pouvoir l’utiliser dans d’autres fonctions.

📌 Exemple d’usage :
python
con = connection()

Cela te permet d’accéder à la base pour faire des requêtes.

---

2. interface_utilisateur()

But : Récupérer les informations de l’utilisateur via le clavier.

Détail :
- input(...) : demande à l’utilisateur de saisir son nom, prénom et âge.
- return nom, prenom, age : renvoie les 3 val…
- commit() valide l’insertion en base.
- cur.close() et connection.close() ferment proprement la session.

📌 Exemple d’appel :
python
insertion("Kodjo", "Aminou", 22)


---

4. afficher()

But : 
- Demander les infos de l’utilisateur,
- Les insérer dans la base,
- Puis afficher toutes les lignes de la table personnes.

Détail :
- Appelle interface_utilisateur() pour récupérer les données.
- Appelle insertion() pour les insérer.
- Fait un SELECT * FROM personnes pour afficher les enregistrements existants.
- fetchall() lit toutes les lignes du résultat.
- print() affiche le contenu.

📌 Exécution simple :
python
afficher()

➡ L'utilisateur entre ses infos, elles sont insérées, puis toutes les données sont affichées.

---

Souhaites-tu que je te montre un exemple d'exécu…
