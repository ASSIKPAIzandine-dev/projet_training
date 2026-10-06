#importation des modules connection
from connection import * 
from prettytable import PrettyTable
cur=conn.cursor()

def calcul_stock_total():
    montant=0
    cur.execute("select pu_vente,qtite_produit from produit")
    infos=cur.fetchall()
    for info in infos:
        montant+=info[0]*info[1]
    print(f"le stock total est:")
    tableau = PrettyTable()
    tableau.field_names = ["Montant total du stock"]
    tableau.add_row([str(montant)+" fcfa"])
    print(tableau)
























