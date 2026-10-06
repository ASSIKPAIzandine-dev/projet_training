import psycopg2
def connection():
    con = psycopg2.connect("host=localhost user=christophe password=sossoukpe16 dbname=personne")
    return con
connection()
def interface_utilisateur():
    id =input("entrer un id: ")
    nom = input("Entrer un nom : ")
    prenom = input("Entrer votre prénom : ")
    age = input("Entrer votre age: ")
    return id,nom, prenom, age
def insertion():
    id,nom, prenom, age = interface_utilisateur()
    ma_connection = connection()
    cur = ma_connection.cursor()
    cur.execute("INSERT INTO personne(id,nom, prenom, age) VALUES(%s, %s, %s,%s);", (id,nom, prenom, age))
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
    cur.execute("select * from personne")
    contenu_table = cur.fetchall()
    print(contenu_table)
    print(type(contenu_table))
    cur.close()
    ma_connection.close()
    for i in range (len(contenu_table)):
       # print(contenu_table[i])
        print(contenu_table[i][1])
        
afficher()

def supprimer():
   ma_connection= connection()
   cur=ma_connection.cursor()
   id=input('entrer le id de la personne a supprimer :')
   cur.execute("delete from personne where id=(%s)",id)
   ma_connection.commit()
   cur.close()
   ma_connection.close()
supprimer()

def modifier():
    ma_connection= connection()
    cur=ma_connection.cursor()
    id=int(input("entre id :"))
    nom=input("")
    ma_connection= connection()
    cur=ma_connection.cursor()
    cur.execute("UPDATE personne SET nom=(%s) where id=(%s);",(nom,id))
    ma_connection.commit()
    cur.close()
    ma_connection.close()
modifier()

afficher()
