from connection import * 
from client import  * 
from produit import *
from paiement import *
from prettytable import PrettyTable
cur=conn.cursor()


def historique_ventes():
    query = """
        SELECT 
            client.nom, 
            client.prenom, 
            produit.libelle, 
            ligne_vente.quantite_vendue, 
            ligne_vente.montant, 
            vente.date_vente, 
            paiement.montant
        FROM 
            produit, ligne_vente, vente, client, paiement
        WHERE 
            produit.id_produit = ligne_vente.id_produit
            AND vente.id_vente = ligne_vente.id_vente
            AND client.id_client = vente.id_client
            AND paiement.id_vente = vente.id_vente
    """
    cur.execute(query)
    return cur.fetchall()
#print(historique_ventes()) 

def afficher_historique_ventes():
    histo=historique_ventes()
    table = PrettyTable()
    table.field_names = ["Nom Client", "Prénom Client", "Libellé Produit", "Quantité Vendue", "Montant de la Vente", "Date de Vente", "Montant du Paiement"]
    for row in histo:
        table.add_row(row)
    print(table)    






