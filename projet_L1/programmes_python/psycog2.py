import psycopg2
def connection():
    con = psycopg2.connect("host=localhost user=christophe password=sossoukpe16 dbname=personne")
    return con
connection()
def interface_utilisateur():
    nom = input("Entrer un nom : ")
    prenom = input("Entrer votre prénom : ")
    age = input("Entrer votre âge : ")
    return nom, prenom, age
interface_utilisateur()
def insertion():
    ma_connection = connection()
    cur = ma_connection.cursor()
    cur.execute("INSERT INTO personnes(nom, prenom, age) VALUES(%s, %s, %s);", (nom, prenom, age))
    ma_connection.commit()
    cur.close()
    ma_connection.close()
insertion()
def interface_utile():
    ma_connection = connection()
    cur = ma_connection.cursor()
def afficher():
    ma_connection = connection()
    cur = ma_connection.cursor()
    nom, prenom, age = interface_utilisateur()
    insertion(nom, prenom, age)
    cur.execute("INSERT INTO personnes(nom, prenom, age) VALUES(%s, %s, %s);", (nom, prenom, age))
    cur.execute("select * from personne")
    
    contenu_table = cur.fetchall()
    
    print(contenu_table)
    print(type(contenu_table))
    cur.close()
    ma_connection.close()
afficher()

def modifier():
   ma_connection= connection()
   cur=ma_connection.cursor()
   id=int(input("entrer  id :"))
   nom=input("")
   ma_connection= connection()
   cur=ma_connection.cursor()
   cur.execute("UPDATE personne SET nom=(%s) where id=(%s);",(nom,id))
   ma_connection.commit()
   cur.close()
   ma_connection.close()
modifier()


