#importation des modules connection
from connection import * 
from client import  * 
from produit import *
from paiement import *
cur=conn.cursor()

#fonction pour verifier si le nom du produit existe dans la base de donnees
# elle prend en parametre le nom du produit, la connexion et le curseur
# elle retourne True si le nom existe, sinon False
def verification_nom(libelle):
    cur.execute('select libelle from produit')
    libelles=cur.fetchall()
    for libel in libelles :
        if libel[0]==libelle:
            return True

#fonction pour verifier si la quantite de vente est suffisante
# elle prend en parametre la quantite de vente, le libelle du produit, la connexion et le curseur
# elle retourne True si la quantite de vente est superieure
def verifier_quantite(quantite_vente,libelle):
   cur.execute('select qtite_produit from produit where libelle=%s',(libelle,))
   qtite=cur.fetchall()
   return qtite[0][0]<int(quantite_vente)

#fonction pour recuperer la quantite du produit
# elle prend en parametre le libelle du produit, la connexion et le curseur
# elle retourne la quantite du produit
def recuperer_quantite(libelle):
    cur.execute('select qtite_produit from produit where libelle=%s',(libelle,))
    qtite=cur.fetchall()
    return qtite[0][0]


#fonctions pour permettre de continuer ou non
def condition(cont):
    while cont.lower() not in ('y','n'):
       print('reponse invalide !.repondez par y ou n')
       cont=input("voulez vous continuer? (y/n) :")
    if cont =='y':
        continuer='False'
        return continuer

#fonction pour calculer le montant total de la vente
# elle prend en parametre la liste des lignes de vente, la connexion et le curseur
# elle retourne le montant total
def calcule_montant(ligne_vente):
    print(ligne_vente)
    montant =0
    for libelle in ligne_vente:
        rec_libelle=libelle[0]
        cur.execute('select pu_vente from produit where libelle=%s',(rec_libelle,))
        prix=cur.fetchall()
        prix =prix[0][0]       
        montant +=(prix*libelle[1])
    return montant   


#fonction pour verifier si le libelle existe dans la liste des lignes de vente
# elle prend en parametre la liste des lignes de vente et le libelle a verifier
# elle retourne True si le libelle existe, sinon False
def verification_libelle_liste(ligne_vente,libelle_dim):
    for libelles in ligne_vente :
        print(libelles)
        if libelles[0]==libelle_dim:
            return True


#fonction pour parcourir la liste des lignes de vente et augmenter la quantite du produit
# elle prend en parametre la liste des lignes de vente, la quantite a augmenter et le libelle du produit
# elle modifie la quantite du produit dans la liste des lignes de vente
# elle ne retourne rien    
def parcour_liste_augmente(ligne_vente,quantite_dim,libelle_dim):
    for i in range(len(ligne_vente)):
        if ligne_vente[i][0] ==libelle_dim:
            ligne_vente[i][1]+=int(quantite_dim)
            return 

#fonction pour verifier si la quantite a diminuer est permise
# elle prend en parametre la liste des lignes de vente, la quantite a diminuer
def controle_qtite_dimunuer(ligne_vente,quantite_dim,libelle_dim):
    for i in range(len(ligne_vente)):
        if ligne_vente[i][0] ==libelle_dim:
            if ligne_vente[i][1] < int(quantite_dim) or ligne_vente[i][1] == int(quantite_dim) :
                print("wesh")
                return True    




##fonction pour modifier une vente
# elle prend en parametre la liste des lignes de vente
# elle demande a l'utilisateur de saisir le libelle du produit a modifier
# elle verifie si le libelle existe dans la liste des lignes de vente
# elle demande a l'utilisateur de choisir entre augmenter ou diminuer la quantite
# elle demande a l'utilisateur de saisir la quantite a augmenter ou diminuer
# elle modifie la quantite du produit dans la liste des lignes de vente
def modifier_vente(ligne_vente):
       libelle_dim = input("Entrer le libellé du produit à modifier  : ").strip().lower()
       # on verifie si le libelle existe dans la liste des lignes de vente
       while not verification_libelle_liste(ligne_vente, libelle_dim):
           libelle_dim = input("Ce libellé n'existe pas dans la vente ! Entrez le libellé du produit : ").strip().lower()
       choix_dimu = input("Voulez-vous augmenter (a) ou diminuer (d) la quantité ? Réponse (a/d) : ").strip().lower()
       while choix_dimu.lower() not in ('a', 'd'):
            choix_dimu = input("Voulez-vous augmenter (a) ou diminuer (d) la quantité ? Réponse (a/d) : ").strip().lower()
       if choix_dimu.lower() == 'a':
            quantite_dim = input("Quantité à augmenter : ")
            while not quantite_dim.isdigit() or int(quantite_dim) <= 0:
                print('Quantité non permise !')
                quantite_dim = input("Quantité à augmenter : ")
            quantite_dim = int(quantite_dim)
            # on appelle la fonction parcour_liste_augmente pour modifier la quantite du produit
            parcour_liste_augmente(ligne_vente, quantite_dim, libelle_dim)
       elif choix_dimu.lower() == 'd':
            quantite_dim = input("Quantité à diminuer : ")
            print(controle_qtite_dimunuer(ligne_vente, quantite_dim, libelle_dim))
            # on verifie si la quantite a diminuer est permise
            #en appelant la fonction controle_qtite_dimunuer pour verifier si la quantite a diminuer est permise
            while not quantite_dim.isdigit() or int(quantite_dim) <= 0 or not controle_qtite_dimunuer(ligne_vente, quantite_dim, libelle_dim):           
                print('Quantité non permise !')
                quantite_dim = input("Quantité à diminuer : ")
            quantite_dim = -int(quantite_dim)
            # on appelle la fonction parcour_liste_augmente pour modifier la quantite du produit
            # en passant la quantite a diminuer comme un nombre negatif
            # pour diminuer la quantite du produit dans la liste des lignes de vente
            parcour_liste_augmente(ligne_vente, quantite_dim, libelle_dim)
       #cont = input("Voulez-vous continuer ? (y/n) : ")
       #continuer = condition(cont)


#fonction pour permettre a l'utilisateur d'ajouter des produits a la vente
# elle prend en parametre la liste des lignes de vente
def ajouter_produit_vente(ligne_vente):
    continuer = True
    while continuer:
        print('Voici la liste des produits disponibles :')
        # on appelle la fonction lister_produits pour afficher la liste des produits disponibles
        # elle est importée du module produit
        lister_produits()
        libelle = input('Quel produit voulez-vous acheter ? : ').strip().lower()
        # on verifie si le nom du produit existe dans la base de donnees
        # en appelant la fonction verification_nom
        while not verification_nom(libelle):
           print('Mettez un nom valide (produit existant dans le stock) !')
           libelle = input('Mettez le nom du produit : ').strip().lower()
        #on recupere la quantite du produit dans le stock
        # en appelant la fonction recuperer_quantite
        # elle retourne la quantite du produit dans le stock   
        reste = recuperer_quantite(libelle)
        print(f'La quantité de ce produit dans le stock est {reste} unités. Combien voulez-vous vendre ?')
        quantite_vente = input('Entrez la quantité : ')
        # on verifie si la quantite de vente est un nombre entier positif
        # et si la quantite de vente est superieure a 0
        # et si la quantite de vente est inferieure ou egale a la quantite du produit dans le stock
        # en appelant la fonction verifier_quantite elle retourne True si la quantite de vente est superieure a la quantite       
        while  quantite_vente.isdigit()==False or verifier_quantite(quantite_vente, libelle)  or int(quantite_vente) <= 0:
          if quantite_vente.isdigit()==False or int(quantite_vente) <= 0 :
              print('Mettez une quantité valide svp !')
          else : 
              print(f'La quantité dans le stock est insuffisante. La quantité restante est {reste}')    
          quantite_vente = input('Entrez la quantité : ')
        # on stock le libelle et la quantite de vente dans une liste
        # on ajoute cette liste a la liste des lignes de vente
        ligne = [libelle, int(quantite_vente)]
        ligne_vente.append(ligne)
        print(f"Le produit {libelle} a été ajouté à la vente avec une quantité de {quantite_vente}.")
        cont = input("Voulez-vous continuer ? (y/n) : ")
        # on verifie si l'utilisateur veut continuer
        # en appelant la fonction condition
        continuer = condition(cont)

#fonction pour recuperer l'id du dernier client 
def recuperer_id_client_annule():
    cur.execute("select id_client from client order by id_client desc limit 1")
    id_client_annule=cur.fetchall()
    return id_client_annule[0][0]

# fonction pour finaliser la vente
# elle prend en parametre la liste des lignes de vente
# demande a l'utilisateur de valider la vente, de modifier la vente ou d'annuler une vente
# si l'utilisateur valide la vente, elle return le montant total de la vente
# si l'utilisateur modifie la vente, elle appelle la fonction modifier_vente
# si l'utilisateur annule une vente, elle vide la liste des lignes de vente et supprime le dernier client de la base de donnees
def finaliser_vente(ligne_vente):
    while True:
        # on calcule le montant total de la vente
        # en appelant la fonction calcule_montant
        montant = calcule_montant(ligne_vente)
        print(f"Le montant total est {montant}")
        validation = input("Voulez-vous valider (v), modifier (m) la vente ou annuler (a) une vente ? : ").strip().lower()
        while validation.lower() not in ('v', 'm', 'a'):
            validation = input("Mettez une réponse valide. Réessayez : ").strip().lower()
        if validation.lower() == 'm':
            print("Vous avez choisi de modifier la vente.")
            # on appelle la fonction modifier_vente pour modifier la vente
            modifier_vente(ligne_vente)
            # La boucle recommence, on redemande validation
        elif validation.lower() == 'a':
            print("Vente annuler avec succes.")
            ligne_vente.clear()
            # on recupere l'id du dernier client
            # en appelant la fonction recuperer_id_client_annule
            id_client_annule=recuperer_id_client_annule()
            cur.execute("delete from client where id_client=%s",(id_client_annule,) )
            conn.commit()
            return None
        elif validation.lower() == 'v':
            print("Vente enregistrer avec succes !")
            return montant

 
## fonction pour enregistrer une vente
# elle demande a l'utilisateur de choisir les produits a vendre
# elle ajoute les produits a la liste des lignes de vente
# elle calcule le montant total de la vente
# elle demande a l'utilisateur de valider la vente, de modifier la vente ou d'annuler une vente
# si l'utilisateur valide la vente, elle retourne la liste des lignes de vente
def enregistrer_vente():
    ligne_vente = []
    ajouter_produit_vente(ligne_vente)
    montant = None
    if ligne_vente: 
        montant = finaliser_vente(ligne_vente)
        if montant is None:  # vente annulée
            conn.close()
            return None, None
    return ligne_vente, montant


#fonction pour recuperer l'id du produit a partir de son nom
# elle prend en parametre le nom du produit, la connexion et le curseur
def recuperer_id_produit(nom_id_rech):
    cur.execute('select id_produit from produit where libelle=%s',(nom_id_rech,))
    id_pro_lg=cur.fetchall()
    id_pro_lg=id_pro_lg[0][0]
    return id_pro_lg

#fonction pour recuperer l'id de la derniere vente
# elle prend en parametre la connexion et le curseur
def recuperer_id_vente() :
    cur.execute('select id_vente from vente order by id_vente DESC LIMIT 1')
    id_ven_lg=cur.fetchall()  
    id_ven_lg=id_ven_lg[0][0]
    return id_ven_lg

#fonction pour inserer les lignes de vente dans la table ligne_vente
# elle insere chaque ligne de vente dans la table ligne_vente
# elle utilise la fonction recuperer_id_vente pour obtenir l'id de la derniere vente
def insertion_ligne_vente(ligne_vente):
    id_ven_lg=recuperer_id_vente()
    for tuples in ligne_vente:
        nom_id_rech=tuples[0]
        id_pro_lg=recuperer_id_produit(nom_id_rech)
        quantite_vendue=tuples[1]
        cur.execute('insert into ligne_vente (quantite_vendue,id_produit,id_vente) values(%s,%s,%s)',(quantite_vendue,id_pro_lg,id_ven_lg))
        conn.commit()



#fonction pour inserer une vente dans la table vente
# elle verifie si un client existe dans la base de donnees
# si oui, elle utilise l'id du client existant
# si non, elle appelle la fonction insertion_client_table pour inserer un nouveau client
# elle appelle la fonction enregistrer_vente pour obtenir les lignes de vente et le montant total
def insertion_vente():
    # on appele la fonction insertion_client_table pour inserer un client
    # si le client n'existe pas, on l'insere dans la base de donnees
    # si le client existe, on utilise l'id du client existant
    var=insertion_client_table()
    # on verifie si le client existe deja dans la base de donnees
    # si non, on utilise l'id du dernier client insere   
    if var==None:
        id_client=cur.execute('select id_client from client order by id_client DESC LIMIT 1')
        id_client=cur.fetchall()
        id_client=id_client[0][0]
    else:
        id_client=var[0]  
        # on verifie si le client a une dette en cours
        # en appelant la fonction verification_dette
        # si le statut de la dette est "en cours", on demande a l'utilisateur de payer d'abord avant de faire une nouvelle vente
        # si le statut de la dette est "valide", on continue la vente
        # si le statut de la dette est "aucune 
        statu=verification_dette(id_client)
        if statu=="en cours":
            print("")
            print("Ce client n a pas encore fini de payer sa dette . payer d abord avant d effectuer une autre vente") 
            return
    # on appelle la fonction enregistrer_vente pour obtenir les lignes de vente et le montant total        
    ligne_vente,montant=enregistrer_vente()
    # on verifie si les lignes de vente et le montant sont valides
    # si non, on sort de la fonction
    if ligne_vente is None or montant is None:
       return  
    # on insere la vente dans la table vente s il valide          
    cur.execute('insert into vente (id_client) values(%s)',(id_client,))
    # on appelle la fonction insertion_ligne_vente pour inserer les lignes de vente dans la table ligne_vente
    insertion_ligne_vente(ligne_vente)
    # on recuperer l'id de la derniere vente pour l inserer dans la table paiement
    id_vente=recuperer_id_vente()
    # on insere le paiement dans la table paiement
    # en utilisant l'id de la derniere vente et le montant total de la vente
    paiement(id_vente,montant)
    conn.commit()
#insertion_vente()

















