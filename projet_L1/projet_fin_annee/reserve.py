def modifier_vente(ligne_vente):
    continuer = True
    while continuer:
       libelle_dim = input("Entrer le libellé du produit à modifier : ")
       while not verification_libelle_liste(ligne_vente, libelle_dim):
           libelle_dim = input("Ce libellé n'existe pas dans la vente ! Entrez le libellé du produit : ")
       choix_dimu = input("Voulez-vous augmenter (a) ou diminuer (d) la quantité ? Réponse (a/d) : ")
       while choix_dimu.lower() not in ('a', 'd'):
            choix_dimu = input("Voulez-vous augmenter (a) ou diminuer (d) la quantité ? Réponse (a/d) : ")
       if choix_dimu.lower() == 'a':
            quantite_dim = input("Quantité à augmenter : ")
            parcour_liste_augmente(ligne_vente, quantite_dim, libelle_dim)
       elif choix_dimu.lower() == 'd':
            quantite_dim = input("Quantité à diminuer : ")
            while controle_qtite_dimunuer(ligne_vente, quantite_dim, libelle_dim):
                print('Quantité non permise !')
                quantite_dim = input("Quantité à diminuer : ")
            quantite_dim = -int(quantite_dim)
            parcour_liste_augmente(ligne_vente, quantite_dim, libelle_dim)
       #cont = input("Voulez-vous continuer ? (y/n) : ")
       #continuer = condition(cont)

def ajouter_produit_vente(conn, cur, ligne_vente):
    continuer = True
    while continuer:
        libelle = input('Quel produit voulez-vous acheter ? : ')
        while not verification_nom(libelle, conn, cur):
           print('Mettez un nom valide (produit existant dans le stock) !')
           libelle = input('Mettez le nom du produit : ')
        reste = recuperer_quantite(libelle, conn, cur)
        print(f'La quantité de ce produit dans le stock est {reste} unités. Combien voulez-vous vendre ?')
        quantite_vente = input('Entrez la quantité : ')
        while verifier_quantite(quantite_vente, libelle, conn, cur) or int(quantite_vente) <= 0:
          if verifier_quantite(quantite_vente, libelle, conn, cur):
              print(f'La quantité dans le stock est insuffisante. La quantité restante est {reste}')
          elif int(quantite_vente) <= 0:
              print('Mettez une quantité valide svp !')
          quantite_vente = input('Entrez la quantité : ')
        ligne = [libelle, int(quantite_vente)]
        ligne_vente.append(ligne)
        print(ligne_vente)
        cont = input("Voulez-vous continuer ? (y/n) : ")
        continuer = condition(cont)


def finaliser_vente(conn, cur, ligne_vente):
    montant = calcule_montant(ligne_vente, conn, cur)
    print(f"Le montant total est {montant}")
    validation = input("Voulez-vous valider (v), modifier (m) la vente ou annuler (a) un produit ? : ")
    while validation.lower() not in ('v', 'm', 'a'):
       validation = input("Mettez une réponse valide. Réessayez : ")
    if validation.lower() == 'm':
       modifier_vente(ligne_vente)
       montant = calcule_montant(ligne_vente, conn, cur) 
       print(f"Le montant total après modification est {montant}")
    elif validation.lower() == 'a':
       print("Annulation de la vente.")
       ligne_vente.clear()
    return montant


def enregistrer_vente():
    conn = connection()
    cur = conn.cursor()
    ligne_vente = []
    print('Que voulez-vous ?')
    ajouter_produit_vente(conn, cur, ligne_vente)
    if ligne_vente: 
       finaliser_vente(conn, cur, ligne_vente)
    conn.close()


enregistrer_vente()









# ...existing code...

def saisir_lignes_vente():
    conn = connection()
    cur = conn.cursor()
    print('la liste des produits dans le stock ')
    ligne_vente = []
    continuer = 'oui'
    while continuer:
        lister_produits()
        libelle = input('quelle produit voulez vous achetez :')
        while not verification_nom(libelle, conn, cur):
            print('mettez un nom valide(produit existant dans le stock) !')
            libelle = input('mettez le nom du produit:')
        reste = recuperer_quantite(libelle, conn, cur)
        print(f'la quantite de ce produit dans le stock est {reste} unite .combien voulez vous vendre:')
        quantite_vente = input('entrer la quantite:')
        while not quantite_vente.isdigit() or verifier_quantite(quantite_vente, libelle, conn, cur) or int(quantite_vente) <= 0:
            if verifier_quantite(quantite_vente, libelle, conn, cur):
                print(f'la quantite dans le stock est insuffisante . la quantite restante est {reste}')
            elif int(quantite_vente) <= 0 or not quantite_vente.isdigit():
                print(f'mettez une quantite valide svp !')
            quantite_vente = input('entrer la quantite:')
        ligne = [libelle, int(quantite_vente)]
        ligne_vente.append(ligne)
        print(ligne_vente)
        cont = input("voulez vous continuer? (y/n) :")
        continuer = condition(cont)
    conn.close()
    return ligne_vente

def valider_vente(ligne_vente):
    conn = connection()
    cur = conn.cursor()
    montant = calcule_montant(ligne_vente, conn, cur)
    print(f"le montant total est {montant}")
    continuer = 'oui'
    while continuer == 'oui':
        validation = input("voulez vous validez(v) la vente ou modifier(m) une vente ou annuler:a un produit?  :")
        while validation.lower() not in ('v', 'm', 'a'):
            validation = input("mettez une réponse valide. ressayez :")
        if validation == 'm':
            modifier_vente(ligne_vente)
        elif validation == 'a':
            conn.close()
            return None, None
        elif validation == 'v':
            print('vente valide !')
            continuer = 'non'
            conn.close()
            return ligne_vente, montant

def enregistrer_vente():
    ligne_vente = saisir_lignes_vente()
    if not ligne_vente:
        return
    ligne_vente, montant = valider_vente(ligne_vente)
    if ligne_vente is None:
        return
    return ligne_vente, montant




       quantite_vente = input('entrer la quantite:')
       cont="True" 
       while cont:
           if not quantite_vente.isdigit() or int(quantite_vente) <= 0:
               print(f'mettez une quantite valide svp !')
           elif verifier_quantite(quantite_vente, libelle, conn, cur):
               print(f'la quantite dans le stock est insuffisante . la quantite restante est {reste}')
           else:
               cont="False"
               break
           quantite_vente = input('entrer la quantite:')











def modifier_vente(ligne_vente):
    #continuer='oui'
    #while continuer:
    libelle_dim=input ("entrer le libelle du produit a modifier :")
    while not verification_libelle_liste(ligne_vente,libelle_dim):
      libelle_dim=input ("ce libelle n existe pas dans la vente !.entrer la libelle du produit a diminuer :")
    choix_dimu=input('voulez vous augmenter(a) ou dimunuer(d) la quantite.reponse(a|d):')
    while choix_dimu.lower() not in ('a','d'):
       choix_dimu=input('voulez vous augmenter(a) ou dimunuer(d) la quantite. reponse(a|d):')
    if choix_dimu.lower()=='a': 
       quantite_dim =input("quantité a augmente :")
       parcour_liste_augmente(ligne_vente,quantite_dim,libelle_dim)

    elif choix_dimu.lower()=='d':
       quantite_dim =input("quantité a diminué :")
       while controle_qtite_dimunuer(ligne_vente,quantite_dim,libelle_dim):
          print('quantite non permis !')
          quantite_dim =input("quantité a diminué :")
       quantite_dim=-(int(quantite_dim))
       parcour_liste_augmente(ligne_vente,quantite_dim,libelle_dim)
    print(ligne_vente)   


#fonction pour enregistrer une vente
# elle demande a l'utilisateur de saisir le libelle du produit a acheter
# elle verifie si le libelle existe dans la base de donnees
# elle demande a l'utilisateur de saisir la quantite a vendre
# elle verifie si la quantite a vendre est suffisante
# elle ajoute le libelle et la quantite a vendre dans une liste de vente
def enregistrer_vente():
    conn= connection()
    cur=conn.cursor()
    print('la liste des produits dans le stock ')
    ligne_vente=[]
    continuer='oui'
    while continuer :
       lister_produits() 
       libelle= input('quelle produit voulez vous achetez :')
       while not verification_nom(libelle,conn,cur):
            print('mettez un nom valide(produit existant dans le stock) !')
            libelle=input('mettez le nom du produit:')
       reste=recuperer_quantite(libelle,conn,cur)
       print(f'la quantite de ce produit dans le stock est {reste} unite .combien voulez vous vendre:')
       quantite_vente=input('entrer la quantite:')
       while not quantite_vente.isdigit() or verifier_quantite(quantite_vente,libelle,conn,cur) or int(quantite_vente)<=0  :
            if verifier_quantite(quantite_vente,libelle,conn,cur):
                 print(f'la quantite dans le stock est insuffisante . la quantite restante est {reste}')
            elif int(quantite_vente)<=0 or not quantite_vente.isdigit():
                 print(f'mettez une quantite valide svp !')
            quantite_vente=input('entrer la quantite:')
       ligne=[]
       ligne=[libelle,int(quantite_vente)]
       ligne_vente.append(ligne)
      # print(ligne_vente)
       cont=input("voulez vous continuer? (y/n) :")
       continuer=condition(cont)  
    montant = calcule_montant(ligne_vente,conn,cur)
    print(f"le montant total est {montant}")  
    continuer='oui'
    while continuer=='oui' :
        validation=input("voulez vous validez(v) la vente ou modifier(m) une vente ou annuler:a un produit?  :")   
        while validation.lower() not in  ('v','m','a'):
            validation =input("mettez une réponse valide. ressayez :")
        if validation=='m':
            modifier_vente(ligne_vente)
        elif validation=='a':
            return
        elif validation=='v':
            print('vente valide !')  
            continuer='non' 
            return ligne_vente,montant









ligne_vente, montant = enregistrer_vente()
if ligne_vente is None or montant is None:
    return  # ou gérer l'annulation comme tu veux




def enregistrer_vente():
    conn = connection()
    cur = conn.cursor()
    ligne_vente = []
    print('Que voulez-vous ?')
    ajouter_produit_vente(conn, cur, ligne_vente)
    if ligne_vente: 
       finaliser_vente(conn, cur, ligne_vente)
    conn.close()    





print("""
   _____           _   _                ____              _   _                  
  / ____|         | | (_)              |  _ \            | | (_)                 
 | |  __  ___  ___| |_ _  ___  _ __    | |_) | ___  _   _| |_ _  __ _ _   _  ___ 
 | | |_ |/ _ \/ __| __| |/ _ \| '_ \   |  _ < / _ \| | | | __| |/ _` | | | |/ _ \
 | |__| |  __/\__ \ |_| | (_) | | | |  | |_) | (_) | |_| | |_| | (_| | |_| |  __/
  \_____|\___||___/\__|_|\___/|_| |_|  |____/ \___/ \__,_|\__|_|\__, |\__,_|\___|
                                                                   | |           
                                                                   |_|         """)





















