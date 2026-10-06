def finaliser_vente(conn, cur, ligne_vente):
    while True:
        montant = calcule_montant(ligne_vente, conn, cur)
        print(f"Le montant total est {montant}")
        validation = input("Voulez-vous valider (v), modifier (m) la vente ou annuler (a) un produit ? : ")
        while validation.lower() not in ('v', 'm', 'a'):
            validation = input("Mettez une réponse valide. Réessayez : ")
        if validation.lower() == 'm':
            modifier_vente(ligne_vente)
            # La boucle recommence, on redemande validation
        elif validation.lower() == 'a':
            print("Annulation de la vente.")
            ligne_vente.clear()
            return None
        elif validation.lower() == 'v':
            print("Vente validée !")
            return montant






def finaliser_vente(conn, cur, ligne_vente):
    while True:
        montant = calcule_montant(ligne_vente, conn, cur)
        print(f"Le montant total est {montant}")
        validation = input("Voulez-vous valider (v), modifier (m) la vente ou annuler (a) un produit ? : ")
        while validation.lower() not in ('v', 'm', 'a'):
            validation = input("Mettez une réponse valide. Réessayez : ")
        if validation.lower() == 'm':
            modifier_vente(ligne_vente)
            # La boucle recommence, on redemande validation
        elif validation.lower() == 'a':
            print("Annulation de la vente.")
            ligne_vente.clear()
            return None
        elif validation.lower() == 'v':
            print("Vente validée !")
            return montant



