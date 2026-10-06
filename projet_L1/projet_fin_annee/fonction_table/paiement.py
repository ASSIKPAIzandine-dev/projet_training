from client import *
from connection import * 
cur=conn.cursor()




###verifier si le client a une dette 
def verification_dette(id_client):
    cur.execute("select statu from client ,vente,paiement where client.id_client=vente.id_client and vente.id_vente=paiement.id_vente and client.id_client=%s",(id_client,))
    rec_id_vente=cur.fetchall()[0][0]
    return rec_id_vente





#fonction pour demander a l'utilisateur de choisir entre paiement par tranche ou d'un seul coup
# elle retourne la valeur choisie par l'utilisateur
def entre_paiment():
    paie=input("paiement par tranche(1) ou d' un seul coup(2) :")
    while paie not in ("1","2"):
        print("réponse invalide choisissez entre (1/2)")
        paie=input("paiement par tranche(1) ou d' un seul coup(2) :")
    return paie 


# not important
def reste_paie(montant):
    cur.execute('select montant from paiement order by id_paiement DESC LIMIT 1') 
    reste_paier=cur.fetchall()[0][0]
    return reste_paier 

# fonction pour afficher le montant restant a payer pour un client si il veut effectuer un paiement
# elle prend en parametre le code du client
# elle affiche le montant restant a payer pour ce client
# si le client n'a pas de dette, elle affiche un message indiquant qu'il n
def voir_montant(code_client):
    cur.execute("select prix_total, sum(montant) from client,vente,paiement where client.id_client=vente.id_client and vente.id_vente=paiement.id_vente and statu=%s and code_client=%s  group by prix_total" ,("en cours",code_client))
    reste=cur.fetchall()
    if not reste:
        print("Vous n'avez pas de dette")
    else:
        print(f"Il vous reste {reste[0][0]-reste[0][1]} fcfa a payer")  

# fonction pour effectuer un paiement par tranche
# elle prend en parametre l'id de la vente et le montant total de la vente    
def paiement_tranche(id_vente,montant):
   paie_tranche=input("entrer le montant :")
   # on verifie si le montant est un nombre entier positif 
   while not paie_tranche.isdigit() or int(paie_tranche) <= 0  :  #or int(paie_tranche) > montant:
       if not paie_tranche.isdigit() or int(paie_tranche) <= 0:  
            print("mettre un montant valide svp !")
       elif int(paie_tranche) > montant:
            print("montant supérieur au prix total de la vente :")
       paie_tranche=input("entrer le montant :")
   paie_tranche=int(paie_tranche)
   # on insert le paiement dans la table paiement
   cur.execute('insert into paiement (montant,id_vente) values (%s,%s)',(paie_tranche,id_vente))
   conn.commit()
   print(f"il reste {montant-paie_tranche} ")
   print("paiement effectué avec succès !")


def mise_ajour_statu():
    cur.execute('select id_paiement from paiement order by id_paiement desc limit 1')
    id_paiement=cur.fetchall()[0][0]
    cur.execute('update paiement set statu=%s where id_paiement=%s',('valide',id_paiement))
    conn.commit()


# fonction pour effectuer un paiement d'un seul coup
# elle prend en parametre l'id de la vente et le montant total de la vente
def paiement_coup(id_vente,montant):
    print("vous avez choisi de payer d'un seul coup")
    paie_coup=input("entrer le montant :")
    while not paie_coup.isdigit() or int(paie_coup) < montant :
        if not paie_coup.isdigit() :
            print("mettre un montant valide svp !")
        elif int(paie_coup) < montant :
            print("montant inférieur au prix total de la vente :")
        paie_coup=input("entrer le montant :")
    paie_coup=int(paie_coup)  
    # si le montant payé est supérieur au montant de la vente, on rend la monnaie
    if paie_coup > montant :
        print(f"vous rendez une monnaie de {paie_coup-montant} fcfa")
    # on insert le paiement dans la table paiement    
    cur.execute('insert into paiement (montant,id_vente) values (%s,%s)',(paie_coup,id_vente))
    conn.commit()
    print("paiement effectué avec succès !")
   # mise_ajour_statu()
    
# fonction principale pour effectuer un paiement
# elle prend en parametre l'id de la vente et le montant total de la vente     
def paiement(id_vente,montant):
    paie=entre_paiment()
    if paie == "1":
       paiement_tranche(id_vente,montant)
    else  :
       paiement_coup(id_vente,montant)





# fonction qui permet de recuperer l'id de la vente a partir du code du client
# elle prend en parametre le code du client
def id_vente_rec(code_paie):
    cur.execute("select id_vente from client,vente where client.id_client=vente.id_client and code_client=%s",(code_paie,))
    id_vente=cur.fetchall()[0][0]
    return id_vente


# fonction qui verifie si le paiement est valide pour une vente
def valide_paiement(id_vente):
    cur.execute('select statu from paiement where id_vente=%s',(id_vente,))
    statu=cur.fetchall()[0][0]
    return statu=="valide"

# fonction qui recupere le montant total de la vente a partir de l'id de la vente
def verification_montant(id_vente):
    cur.execute("select prix_total from vente where id_vente=%s",(id_vente,))
    return cur.fetchall()[0][0]

# fonction qui calcule la somme des montants payés pour une vente
# elle prend en parametre l'id de la vente
def sommes_montant(id_vente):
    cur.execute("select sum(montant) from paiement where id_vente=%s",(id_vente,))
    return cur.fetchall()[0][0]

# fonction qui verifie si le paiement est valide pour un client
# elle prend en parametre le code du client
def vérification_paiement_valide(code_paie):
    cur.execute("select statu from client,vente, paiement where client.id_client=vente.id_client and vente.id_vente=paiement.id_vente and code_client=%s",(code_paie,))
    return cur.fetchall()[0][0]=="valide" 


# fonction pour effectuer un paiement par tranche 
def paiement_tranche_tranche() :
    code_paie=input("entrer le code du client qui souhaite faire le paiement ou tapper (q) pour quitter:")
    # si il met q alors on quitte la fonction
    if code_paie.lower() == 'q':
        return
    # on verifie si le code du client existe dans la base de donnees    
    while not verification_code(code_paie):
        print("aucun client avec ce code ")
        code_paie=input("entrer le code du client qui souhaite faire le paiement :")
    # cette fonction permet de voir le montant restant a payer pour un client   
    # elle prend en parametre le code du client
    # si le client n'a pas de dette, elle affiche un message indiquant qu'il n'a pas de dette
    # sinon elle affiche le montant restant a payer pour ce client
    # elle appelle la fonction voir_montant pour afficher le montant restant a payer 
    voir_montant(code_paie)  
    # on verifie si le paiement est valide pour ce client
    # si oui, on affiche un message indiquant que le paiement a déjà été validé  
    if vérification_paiement_valide(code_paie):  
        print("le paiement de ce client a déjà validé merci !") 
        return         
    montant_tranche=input ("entrer le montant :")
    while not montant_tranche.isdigit() or int(montant_tranche)<=0:
        montant_tranche=input ("montant invalide ! ressayez :")
    montant_tranche=int(montant_tranche) 
    # on recupere l'id de la vente a partir du code du client
    # on appelle la fonction id_vente_rec pour recuperer l'id de la vente  et on insert le paiement dans la table paiement
    id_vente=id_vente_rec(code_paie)
    cur.execute("insert into paiement (montant,id_vente) values (%s,%s)",(montant_tranche,id_vente))
    conn.commit()
    print("paiement effectué avec succès !")
    # on recupere la somme des montants payés pour cette vente et le prix total de la vente
    # on appelle la fonction sommes_montant pour recuperer la somme des montants payés pour cette vente
    # on appelle la fonction verification_montant pour recuperer le prix total de la vente
    somme_montant= sommes_montant(id_vente)
    prix_total=verification_montant(id_vente)
    # on verifie si le paiement est valide pour cette vente
    # on appelle la fonction valide_paiement pour verifier si le paiement est valide pour cette
    if valide_paiement(id_vente) :
        print("votre paiement est validé merci !")
        
    elif somme_montant < prix_total:
        print(f"il vous reste {prix_total-somme_montant} fcfa a payer") 








          
