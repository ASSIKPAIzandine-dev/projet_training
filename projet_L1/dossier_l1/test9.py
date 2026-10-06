a=str(input("entrer une chaine de caractere :"))
b=str(input("entrer une chaine de caractere :"))
if len(a)<len(b):
    print("la chaine la plus longue est :",b)
elif len(a)>len(b):
    print("la chaine la plus longue est :",a)
elif len(a)==len(b):
    print("ces phrases ont la meme longueur")   
    
    
    
    
    
#a=int(input("entrer nombre :"))
#print("")
#for i in range(1,11):
 #  multiple=a * i
 #  print(a,"multiplé par",i,"est:",multiple)  
 
#liste_chaine=[ ]
#v="lapin","chat","chien","chiot","drogon","ornithorynque"
#liste_chaine.extend(v) 
#for i in liste_chaine:
 #  caractere=len(i)
  # print(i,"contient",caractere,"caracteres")
   
   
   
T=[25,12,35,58,15,17,20]
p=len(T)
for i in range(0,p):
   for j in range(i+1,p):
      if T[i] > T[j]:
        a=T[i]
        T[i]=T[j]
        T[j]=a
print(T)         


T=[25,12,35,58,15,17,20]
T.sort()
print(T)



      
#liste_chaine=[ ]
#v="lapin","chat","chien","chiot","drogon","ornithorynque"
#liste_chaine.extend(v) 
#a=str(input("entrer un nom:"))
#for i in liste_chaine:
   # if a==i:
   #   caractere=len(i)
   #   print(i,"contient",caractere,"caracteres")
   
   

def numeroJourAnnee(jour,mois):
     c=0
     T=[ ]
     v=[31,28,31,30,31,30,31,31,30,31,30,31]
     T.extend(v)
for j in range(0,mois-1):
     c=c+T[j]
     c=c+jour   
     return "il represente"+" "+ str(c)+"eme jour de l annee" 
    
jour=int(input('entrer le jour:'))
mois=int(input('entrer le numero :'))
print(numeroJourAnnee(jour,mois))
  


def hauteurparcourue():
  aller=nbre_marche*hauteur
  aller_retour=2*aller
  par_jour=5*aller_retour
  par_semaine=7*par_jour
  par_semaine=par_semaine/100
  return "il effectue "+str(par_semaine)+"m par semaine"
nbre_marche=int(input("entrer le nombre de marche:"))
hauteur=int(input("entrer la hauteur:"))
print(hauteurparcourue())

diviseur=[ ]  
def listDiv(a):
  for i in range(1,a+1):
     if a%i==0:
       diviseur.append(i)
  
  return " les diviseur de "+str(a)+" sont "+str(diviseur)   
  
#a=int(input("entrer un nombre:"))
#print(listDiv(a))  

diviseur=[ ]  
def listDiv(a):
  while a < 0 :
    a=int(input("entrer un nombre:"))
  if a==1:
    return "1 est premier"
  if a==2:
    return "2 n est pas premier"
    
  for i in range(2,int((a**0.5)+1)):
     if a%i==0:
        return str(a)+" n est  pas premier"
     elif a%i!=0:
        return str(a)+" est  premier"     
  

#a=int(input("entrer un nombre:"))
#print(listDiv(a))  
  

T=[ ]
for i in range (6):
   v=int(input("entrer un nombre:"))
   T.append(v)
L=[ ]
for i in T:
  if i % 2 == 0 :
    L.append(i)
print(L)           
 
 
 
 
 
 
 
 
 
 
  
  
  
  
  
  
      
