from vente import *
from produit import *
from approvisionnement import *
from paiement import *
from client import *
from categorie import *
from connection import *
from stock import *
from historique import *



def menu():    

    print("")
    print('================ MENU ==================')
    print('0-Quitter le programme')
    print('1-rechercher un client')
    print('2-afficher tous les client')
    print('3-effectuer une vente')
    print('4-rechercher un produit')
    print('5-lister tous les produits')
    print('6-rechercher un produit par indice')
    print('7-modifier un produit')
    print('8-faire un approvisionnement')   
    print('9-enregistrer un paiement')
    print('10-afficher les produits par categories')
    print("11-afficher le montant total du stock")
    print("12-afficher l historique des ventes ")
    print("13-afficher l'historique des approvisionnements")


    
def main():
    continuer="oui"
    while continuer=="oui":
      menu()
      print('='*17,"MENU","="*17)
      choix=input('Que voulez-vous faire :')
      print("")
      while choix not in ('0','1','2','3','4','5','6','7','8','9','10','11','12', '13'):
          print('choix invalide')
          choix=input('Que voulez-vous faire :')  
      if choix=='0':
        continuer='non'
        fermer_connexion()       
      if choix == '1':
          afficher_client()
      elif choix=='2':
          afficher_tout_client()
      elif choix=='3':
          insertion_vente()
      elif choix=="4":
          rechercher_produit()        
      elif choix=="5":
          lister_produits()
      elif choix=='6':
          info_produit_indice()          
      elif choix=="7":
          modifier_produit()
      elif choix=="8":
          approvisionnement()   
      elif choix=="9":
         paiement_tranche_tranche()
      elif choix=='10':
         produit_par_categorie()
      elif choix=='11':
         calcul_stock_total()
      elif choix=='12':
        afficher_historique_ventes() 
      elif choix=='13':
        afficher_approvisionnement()    




main()





















