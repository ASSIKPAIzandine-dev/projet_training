#importation des modules connection
from connection import * 
from prettytable import PrettyTable
cur=conn.cursor()

#Fonction pour vérifier si une date est valide 
from datetime import datetime
def verifier_date(date_naissance, format="%Y-%m-%d"):
    try:
        datetime.strptime(date_naissance, format) 
        return True 
    except ValueError:
        return False 

# Fonction pour vérifier si le numéro de téléphone est unique
# elle retourne une liste de tous les numéros de téléphone des clients
def vérification_numtel_unique():
    liste_tel=[]
    cur.execute("select numero_tel from client")
    all_num=cur.fetchall()
    for tel in all_num :
        liste_tel.append(tel[0])
    return liste_tel



# Fonction pour vérifier si le client existe déjà dans la base de données
# elle prend en paramètre le nom et le numéro de téléphone du client
def verification_client_exist(nom,numerotel):
    cur.execute('select id_client,nom,numero_tel from client ')
    infos=cur.fetchall()
    for info in infos:
        if nom==info[1] and numerotel==info[2]:
            #print('client trouver')
            return info[0]  
    #print('client non trouver')          
    return True

# Enregistrement des informations du client 
def ajouter_client():
    print("=====info du client=====")
    nom=input('entrer le nom du client:')
    while len(nom)<1:
        print(f"svp mettez un nom valide!")
        nom=input('entrer le nom du client:')

    prenom=input('entrer le prenom du client:')
    while len(prenom)<1:
        print(f"svp mettez un prenom valide!")
        prenom=input('entrer le prenom du client:')
    

    adresse=input('entrer l adresse du client:')
    while len(adresse)<1:
        print(f"svp mettez une adresse valide!")
        adresse=input('entrer l adresse du client:')
    
    sexe=input('entrer le sexe du client(m/f):')
    while sexe.lower() not in ['f','m']:
        print(f"svp mettez un sexe valide (m/f)!")
        sexe=input('entrer le sexe du client:')
    sexe=sexe.lower()

    date_naissance=input('entrer la date de naissance du client (jj/mm/aaaa):')
    while not verifier_date(date_naissance, "%d/%m/%Y"):
        print(f"svp mettez une date de naissance valide (jj/mm/aaaa)!")
        date_naissance=input('entrer la date de naissance du client (jj/mm/aaaa):')
    # verifier si le client existe déjà et verifier si le numéro de téléphone est unique
    # on vérifie si le client existe déjà dans la base de données avec le nom et le numéro de téléphone
    # si oui on ne l'enregistre pas
    # sinon on l'enregistre   
    liste_tel=vérification_numtel_unique()  
    numerotel=input('entrer le numero de telephone du client:') 
    
    while  not numerotel.isdigit() or (int(numerotel) in liste_tel and  not isinstance(verification_client_exist(nom,numerotel),bool)):
        if not numerotel.isdigit():
            print(f"svp mettez un numero de telephone valide!")
        else:
            print("le numéro est unique ! ce numéro de tel existe déjà pour un autre client")
        numerotel=input('entrer le numero de telephone du client:')
    numerotel=int(numerotel)      


    if isinstance(verification_client_exist(nom,numerotel),bool):
        print('c est un nouveau client ')
        return nom,prenom,numerotel,adresse,sexe,date_naissance
    else :
        id_client=verification_client_exist(nom,numerotel)
        print('c est un ancien client')
        return (id_client,)


## Fonction pour insérer un client dans la base de données 
def insertion_client_table():
    tuples=ajouter_client()
    if len(tuples)>1:
        nom,prenom,numerotel,adresse,sexe,date_naissance=tuples 
        cur.execute('INSERT INTO client(nom,prenom,sexe,numero_tel,adresse,date_nais) values(%s,%s,%s,%s,%s,%s)',(nom,prenom,sexe,numerotel,adresse,date_naissance))
        #a revoir
        conn.commit()
        print('client enregistrer avec succes')
    else:     
        return tuples
#insertion_client_table()



def verification_code(code):
    cur.execute('select code_client from client')
    codes=cur.fetchall()
    for cod in codes :
        if cod[0]==code:
            return True
        

def afficher_client():   
    print("recherche d un client par son code")
    code=input("entrer le code du client a recherche:")
    while not verification_code(code):
        print('aucun client avec cet code mettez un code valide ou quit pour quitte')
        code=input("entrer le code du client a recherche:")
        if code=='quit':
            return
    cur.execute('select * from client where code_client=%s',(code,))    
    infos=cur.fetchall()
    tableau = PrettyTable()
    tableau.field_names = ['id_client','code_client','nom','prenom','sexe','numero tel','adresse','date naissance']
    i=0
    for info in infos:
       i+=1
       tableau.add_row([info[0],info[1],info[2],info[3],info[4],info[5],info[6],info[7]])
    print(tableau)

     
    
def afficher_tout_client(): 
    cur.execute('select * from client')
    infos=cur.fetchall()
    tableau = PrettyTable()
    tableau.field_names = ['No','code_client','nom','prenom','sexe','numero tel','adresse','date naissance']
    i=0
    for info in infos:
       i+=1
       tableau.add_row([info[0],info[1],info[2],info[3],info[4],info[5],info[6],info[7]])
    print(tableau)      





















        