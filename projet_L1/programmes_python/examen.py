'''
def continuer():
  choix=input("voulez-vous continuer?(oui|nom): ")
  while choix !="oui" and choix !="non":
      choix=input("voulez-vous continuer?(oui|nom): ")
      print("je n'ai pas compris")
  if choix=="oui":
        return True
  else:
        return False
print(continuer())
'''
'''
def commande(n):
    list_prix=[]
    while len(list_prix) !=n:
        prix=input("entrez un prix : ")
        list_prix.append(prix)
    return list_prix
print(commande(5))

'''
'''
def total(liste):
     somme=0
     for nombre in liste :
         somme += nombre
     return somme
print(total([18,30]))
'''


#def indice_max(liste):
 #  indice=0
 #  liste=[i]
  # for i in liste:
  #    if indice < liste[i] :
   #      indice=liste[i]
     #     indice =i
   #return indi_max
   
#print(indice_max([10,18,5]))
'''  

def indice_max(liste):
    indoce=0
    maxe=liste[0]
    for i in range(len(liste)):
        if liste[i] > maxe:
            maxe=liste[i]
            indice=i
    return indice
print(indice_max([12,3244,56,2,9,100]))
  '''
"""
def supprmax(liste):
      maxe_val=max(liste)
      listee=[]
      for i in liste:
        if i!=maxe_val:
            listee.append(i)
        
      return listee
print(supprmax([12,34,56,18]))
"""


def n_7(liste):
    return[x for x in liste if x %7==0]
print(n_7([12,14.28,21]))



#liste=[python]
def paquet(chaine):
    #for _ in liste:
        return '*'.join(chaine)
         
print(paquet("python"))
print(paquet("sossoukpe"))




def compter(chaine):
    maj = 0
    min = 0
    for c in chaine:
        if c.isalpha():
            if c.islower():
                min +=1
                
            else:
                maj +=1
print("maj:" ,maj)
print("mine:" ,min)

compter("bonjour LE MONDE")







Étape par étape

1. Créer la table matable  
sql
CREATE TABLE matable (
  nom TEXT,
  age INT
);


Et insérer des données :
sql
INSERT INTO matable VALUES ('Alice', 25), ('Bob', 30), ('Chloe', 22);


---

2. Créer les utilisateurs
sql
CREATE ROLE user1 LOGIN PASSWORD 'mdp1';
CREATE ROLE user2 LOGIN PASSWORD 'mdp2';
CREATE ROLE user3 LOGIN PASSWORD 'mdp3';


---

3. Créer un groupe (rôle sans LOGIN)  
sql
CREATE ROLE groupe1;


Puis vérifier :
sql
\dg


---

4. Ajouter user1 et user2 au groupe
sql
GRANT groupe1 TO user1, user2;


---

5. Donner les droits avec WITH GRANT OPTION

a. Consultation à user1 :
sql
GRANT SELECT ON matable TO user1 WITH GRANT OPTION;


b. Mise à jour à user2 :
sql
GRANT UPDATE ON matable TO user2 WITH GRANT OPTION;


c. Vérifier avec :
sql
\dp matable


d. Pour déclencher les actions : cela nécessite des triggers (hors du scope direct ici, à commenter dans un rapport).

---
6. Créer un second groupe
sql
CREATE ROLE groupe2;
GRANT groupe2 TO user1, user3;


---

7. user4 non créé :  
On ne peut pas ajouter un utilisateur non existant. Cela échoue :
sql
GRANT groupe2 TO user4; -- Erreur


---

8. Tester les actions en se connectant avec user3

---

9. Retirer le droit SELECT de user1
sql
REVOKE SELECT ON matable FROM user1;


---

10. Révoquer GRANT OPTION sans CASCADE
sql
REVOKE GRANT OPTION FOR SELECT ON matable FROM user1;


user2 garde son droit s’il l’a reçu avant.

---

11. Deux solutions pour révoquer :
- REVOKE GRANT OPTION FOR ...
- REVOKE ALL ON matable FROM user1 CASCADE;

---

12. Faire \dp matable  
Permet de voir qui a quels droits.

---

13. Tester user3  
S’il n’a pas été explicitement GRANT, il n’a pas accès. Sinon, oui.

---

14. Donner à user3 les droits de modification
sql
GRANT UPDATE ON matable TO user3;


---

Souhaites-tu les commandes regroupées dans un script SQL ?
