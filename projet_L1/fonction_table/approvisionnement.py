#importation des modules connection
from connection import * 
from produit import *
from categorie import *
cur=conn.cursor()


# Fonction pour vérifier si une date est valide 
from datetime import datetime
def verifier_date(date_peremption, format="%Y-%m-%d"):
    try:
        datetime.strptime(date_peremption, format)  # Tentative de conversion
        return True  
    except ValueError:
        return False 

def recuperer_id_categorie(categorie):
    cur.execute('select id_categorie from categorie where nom=%s',(categorie,))
    id_categorie=cur.fetchall()
    id_categorie=id_categorie[0][0]
    return id_categorie
#print(recuperer_id_categorie('alimentation'))

def demander_prix_achat():
    prix_achat = input("Prix d'achat : ")
    while not prix_achat.isdigit() or float(prix_achat) <= 0:
        prix_achat = input("Prix d'achat doit être un nombre positif, réessayez : ")
    return float(prix_achat)

def demander_quantite():
    quantite = input("saisissez la quantite : ")
    while not quantite.isdigit() or int(quantite) <= 0:
        quantite = input("Quantité doit être un entier positif, réessayez : ")
    return int(quantite)

def ajouter_produit():
   libelle = input("Libellé du produit : ").strip().lower()
   while len(libelle)==0:
      libelle = input("Libellé du produit : ").strip().lower()
   prix_unitaire = input("Prix unitaire : ")
   while not prix_unitaire.isdigit() or float(prix_unitaire) <= 0:
      prix_unitaire = input("Prix doit être un nombre positif, réessayez : ")
   prix_unitaire = float(prix_unitaire)
   quantite =demander_quantite()
   date_peremption = input("Date de péremption (JJ/MM/AAAA) :")
   while not verifier_date(date_peremption, "%d/%m/%Y"):
      date_peremption = input("Date invalide (JJ/MM/AAAA) : ")
   print('les categorie sont: ')
   afficher_categorie()   
  # categorie=input('entrer la categorie:').strip().lower()
   liste_categorie=recuperer_ids_categorie()
   id_categorie=input(f'entrer la categorie(choisissez entre{liste_categorie} ):').strip()
   while int(id_categorie) not in liste_categorie :
      id_categorie=input(f'entrer la categorie(choisissez entre{liste_categorie} ):').strip()
   prix_achat=demander_prix_achat()

   return libelle,prix_unitaire,quantite,date_peremption,id_categorie,prix_achat


## Fonction pour insérer un produit dans la base de données
def insertion_produit():
    libelle,prix_unitaire,quantite,date_peremption,id_categorie,prix_achat=ajouter_produit()
    cur.execute('INSERT INTO produit(libelle,pu_vente,qtite_produit,date_perimption,id_categorie) values (%s,%s,%s,%s,%s)',(libelle,prix_unitaire,quantite,date_peremption,id_categorie))
    conn.commit()
    print('produit ajouter avec succes')
    return libelle,quantite,prix_achat
#insertion_produit() 


def verification_libelle(libelle_ajou):
    cur.execute('select libelle from produit')
    libelles=cur.fetchall()
    for libel in libelles :
        if libel[0]==libelle_ajou:
            return True


def recuperer_id_produit_appro(libelle_ajou):
    cur.execute('select id_produit from produit where libelle=%s',(libelle_ajou,))
    id_produit=cur.fetchall()[0][0]

    cur.execute('select id_approvisionnement from approvisionnement order by id_approvisionnement desc limit 1')
    id_approvisionnement=cur.fetchall()[0][0]
    return id_produit,id_approvisionnement



def approvisionnement():
    libelle_ajou=input('entrer le nom du produit a approvisionner ou taper (q) pour quitter:').strip().lower()
    if libelle_ajou.lower()=='q':
        return
    while not verification_libelle(libelle_ajou):
        print('ce produit n existe pas dans le stock .tapez (add) pour ajouter ce produit ou metter le nom du produit existant dans le stock')
        libelle_ajou=input('entrer le nom du produit a approvisionner:').strip().lower()
        if libelle_ajou.lower()=='add':     
            libelle,quantite,prix_achat=insertion_produit()
            cur.execute('insert into approvisionnement default values')
            conn.commit()
            id_produit,id_approvisionnement=recuperer_id_produit_appro(libelle)
            cur.execute('insert into ligne_approvisionnement(prix_achat,qt_approvisionnement,id_produit,id_approvisionnement) values(%s,%s,%s,%s)',(prix_achat,quantite,id_produit,id_approvisionnement))
            conn.commit()
            return
    quantite_appro=demander_quantite()
    prix_achat=demander_prix_achat()

    cur.execute('update produit set qtite_produit=qtite_produit+%s where libelle=%s',(quantite_appro,libelle_ajou))
    cur.execute('insert into approvisionnement default values')   
    conn.commit()
    id_produit,id_approvisionnement=recuperer_id_produit_appro(libelle_ajou)
    cur.execute('insert into ligne_approvisionnement(prix_achat,qt_approvisionnement,id_produit,id_approvisionnement) values(%s,%s,%s,%s)',(prix_achat,quantite_appro,id_produit,id_approvisionnement))
    conn.commit()


def afficher_approvisionnement():
    cur.execute('select produit.libelle,ligne_approvisionnement.qt_approvisionnement,ligne_approvisionnement.prix_achat,approvisionnement.date_appro from produit,ligne_approvisionnement,approvisionnement where produit.id_produit=ligne_approvisionnement.id_produit and ligne_approvisionnement.id_approvisionnement=approvisionnement.id_approvisionnement')
    infos=cur.fetchall()
    tableau = PrettyTable()
    tableau.field_names = ['Libellé Produit','Quantité Approvisionnée','Prix d\'Achat','Date Approvisionnement']
    for info in infos:
        tableau.add_row([info[0],info[1],info[2],info[3]])
    print(tableau)

















