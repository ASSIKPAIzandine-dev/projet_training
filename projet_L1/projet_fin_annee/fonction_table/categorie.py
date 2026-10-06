from connection import *
from prettytable import PrettyTable
cur=conn.cursor()


def verification_cotegorie(categorie_nom):
    cur.execute('select nom from categorie')
    noms=cur.fetchall()
    for nom in noms:
        if nom[0]==categorie_nom:
            return True

# fonction pour afficher les produits par categorie
# elle prend en parametre la categorie et affiche les produits de cette categorie
# elle utilise la fonction recuperer_id_categorie pour obtenir l'id de la categorie
# elle utilise la fonction verification_cotegorie pour verifier si la categorie existe
def produit_par_categorie():
    cat=input('entrer la categorie :').lower()
    while not verification_cotegorie(cat):
        print('categorie invalide!')
        cat=input('entrer la categorie :').lower()
    #id_categorie_nom = recuperer_id_categorie(conn,cur,cat)
    cur.execute('select libelle from produit,categorie where produit.id_categorie=categorie.id_categorie and nom=%s',(cat,))
    listes=cur.fetchall()
    tableau = PrettyTable()
    tableau.field_names = ["No","libelle"]
    i=0
    for liste in listes:
       i+=1
       tableau.add_row([i,liste[0]])
    print(tableau)

#produit_par_categorie()



## Fonction pour rechercher un produit par son indice
def libelle_par_indice():
    liste_libelle=[]
    indice=input("entrer l indice :").lower()
    while len(indice)==0:
        print("indice invalide !")
        indice=input("entrer l indice :")
    cur.execute('select * from produit WHERE libelle LIKE %s',('%' + indice + '%',))
    libelles=cur.fetchall()
    if len(libelles)==0:
        print("aucun produit avec  ce indice")
        return None
    else:    
        return libelles        
#print(libelle_par_indice(connection(),connection().cursor()))

def info_produit_indice():
    liste_tuples=[]
    liste_libelle=libelle_par_indice()
    if liste_libelle==None :
        return  
    else:
       tableau = PrettyTable()   
       tableau.field_names=["id","code","libelle","prix unitaire","quantité","date de péremption","id catégorie"]
       for libelle in liste_libelle:
            tableau.add_row([libelle[0],libelle[1],libelle[2],libelle[3],libelle[4],libelle[5], libelle[6]]) 
    print(tableau)     
#info_produit_indice()



def creer_categorie():
    nom=input("entrer le nom de la categorie :").strip().lower()
    while len(nom)==0:
        print("nom invalide !")
        nom=input("entrer le nom de la categorie :").strip().lower()
    cur.execute('INSERT INTO categorie(nom) values(%s)',(nom,))
    conn.commit()
    print('categorie ajouter avec succes')





