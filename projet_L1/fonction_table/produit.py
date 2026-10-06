#importation des modules connection
from connection import * 
from prettytable import PrettyTable
cur=conn.cursor()
# Fonction pour vérifier si une date est valide .3


from datetime import datetime
def verifier_date(date_naissance, format="%Y-%m-%d"):
    try:
        datetime.strptime(date_naissance, format)  # Tentative de conversion
        return True  # La date est valide
    except ValueError:
        return False 

#fonction qui  ne prend rien en parametre 
#et qui permet de recuperer id des categories et les met dans la variable liste_categorie
#retourne une liste de id
def recuperer_ids_categorie():
    liste_categorie=[]
    cur.execute('select id_categorie from categorie')
    categorie=cur.fetchall()
    for cat in categorie:
        liste_categorie.append(cat[0])
    return liste_categorie
#print(recuperer_ids_categorie('alimentation'))





#fonction qui prend en parametre
def filtrer_categorie(categorie):
   cur.execute('select nom from categorie')
   categories=cur.fetchall()
   for cat in categories :
      if categorie==cat[0]:
         return True
#print(filtrer_categorie())



#fonction qui ne prend rien en parametre et qui affiche le numero et le nom  des categories dans un tableau
def afficher_categorie():
   cur.execute('select * from categorie') 
   categories=cur.fetchall()
   #print(categories)
   tableau = PrettyTable()
   tableau.field_names = ["No", "nom"]
   for cate in categories :
      tableau.add_row([cate[0], cate[1]])
   print(tableau)
  

#fonction qui permet de demander les informations d'un produit et qui ne prend rien en parametre
#retourne le libelle,le prix_unitaire,quantite,la date_perimption et en fin le id_categorie
def ajouter_produit():
   libelle = input("Libellé du produit : ").strip().lower()
   while len(libelle)<1:
      libelle = input("Libellé du produit : ").strip().lower()
   prix_unitaire = input("Prix unitaire : ")
   while not (prix_unitaire.isdigit() and float(prix_unitaire) > 0):
      prix_unitaire = input("Prix doit être un nombre positif, réessayez : ")
   prix_unitaire = float(prix_unitaire)
   quantite = input("Quantité du produit : ")
   while not (quantite.isdigit() and int(quantite) >= 0):
       quantite = input("Quantité doit être un entier positif, réessayez : ")
   quantite = int(quantite)
   date_peremption = input("Date de péremption (JJ/MM/AAAA) :")
   while not verifier_date(date_peremption, "%d/%m/%Y"):
      date_peremption = input("Date invalide (JJ/MM/AAAA) : ")
   print('les categorie sont: ')
   #fonction qui d'afficher les categories pour faciliter la tache à utilisateur en saisisant les chiffres au lieu de taper tout le nom du categorie
   afficher_categorie()
   liste_categorie=recuperer_ids_categorie(categorie)
   categorie=input(f'entrer la categorie(choisissez entre{liste_categorie} ):')
   while categorie not in liste_categorie : #not filtrer_categorie(categorie):
      categorie=input(f'entrer la categorie(choisissez entre{liste_categorie} ):')
   #id_categorie=recuperer_id_categorie(categorie)
   return libelle,prix_unitaire,quantite,date_peremption,id_categorie



#fonction qui permet d'inseré un produit dans la base
def insertion_produit():
    libelle,prix_unitaire,quantite,date_peremption,id_categorie=ajouter_produit()
    cur.execute('INSERT INTO produit(libelle,pu_vente,qtite_produit,date_perimption,id_categorie) values (%s,%s,%s,%s,%s)',(libelle,prix_unitaire,quantite,date_peremption,id_categorie))
    conn.commit()
#insertion_produit() 



#fonction qui prend libelle comme parametre  et qui permet de verifier si le libelle que utilisateur à saisie existe dans la base
#et qui retourne true si le libelle existe
def verification_nom(libelle):
    cur.execute('select libelle from produit')
    libelles=cur.fetchall()
    for libel in libelles :
        if libel[0]==libelle:
            return True

#fonction qui permet de rechercher un produit et celle fonction fais appelle a une autre fonction qui verifie le libelle saisie par l'utilisateur
#dans le cas contraire on lui dis que le produit n'existe pas
#et ensuite  affiche les informations des  produits dans un tableau
def rechercher_produit():    
   libelle = input("libelle du produit : ").strip().lower()
   while not verification_nom(libelle):
      libelle = input(" ce libelle n existe,réessayez :").strip().lower()
   cur.execute('select * from produit where libelle=%s',(libelle,))
   infos=cur.fetchall()
   tableau = PrettyTable()
   tableau.field_names = ["No","code", "libelle", "prix vente","quantite","date perimption"]
   i=0
   for info in infos:
      i+=1
      tableau.add_row([i,info[1],info[2],info[3],info[4],info[5]])
   print(tableau)


#fonction  qui ne prend rien en parametre et qui affiche les informations des  produits dans un tableau
def lister_produits():      
   cur.execute('select code_produit,libelle,pu_vente,qtite_produit,date_perimption from produit')
   infos=cur.fetchall()
   print(infos)
   tableau = PrettyTable()
   tableau.field_names = ["No","code", "libelle", "prix vente","quantite","date perimption"]
   i=0
   for info in infos:
      i+=1
      tableau.add_row([i,info[0],info[1],info[2],info[3],info[4]])
   print(tableau)


#lister_produits()





#fonction qui prend code_produit comme parametre,verifie si le code que utilisateur a saisie existe dans la bsae
#si le code existe il return true
def verification_code(code_produit):
    cur.execute('select code_produit from produit')
    codes=cur.fetchall()
    for cod in codes :
        if cod[0]==code_produit:
            return True

#fonction qui ne prend rien en parametre
#et qui permet de demander le code du produit que l'on souhaite à modifier ,
#permetre à utilisateur de modifier soit le libelle ou le prix unitaire du produit en saisisant les chiffres
#et qui permet de demander a l'utilisateur au tant de fois qu'une fonction n'est pas respecter
def modifier_produit():
   code_produit = input("Code du produit à modifier ou taper (q) pour quitter: ")
   if code_produit.lower() == 'q':
      return
   while not verification_code(code_produit):
      code_produit = input("Code invalide, réessayez : ")
   choix = input("Que souhaitez-vous modifier ? (libelle(1)/prix unitaire(2)) : ")
   while not (choix.lower() in ["1", "2"]):
      choix = input("Choix invalide, entrez 1/2: ")
   if choix.lower() == "1":
      modifier = input("Nouveau libellé :").strip().lower()
      while len(modifier)==0:
         modifier = input("Libellé invalide,entrez un bon libelle : ").strip().lower()
      cur.execute('update produit set libelle=%s where code_produit=%s',(modifier,code_produit))     
   elif choix.lower() == "2":
      modifier = input("Nouveau prix unitaire : ").strip().lower()
      while not (modifier.isdigit() and float(modifier) > 0):
        modifier = input("Prix doit être un nombre positif, réessayez : ").strip().lower()
      modifier = float(modifier)
      cur.execute('update produit set pu_vente=%s where code_produit=%s',(modifier,code_produit))   
   conn.commit()
   print("Produit modifié avec succès !")

#modifier_produit()

