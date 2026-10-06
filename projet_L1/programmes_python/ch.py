#liste=[12,21,28,31]
#def n_7(liste):
#   return[n for n  in liste if n%7==0]
#resultat=n_7(liste)
#print(resultat)
#n_7()
'''liste=[]
#v=""
h=""
t=""
def ta_t(liste):

 for i in v:
  t+=i+"*"
 for i in t:
  liste.append(i)
 liste.pop()
 for k in liste:
  h+=k
ta_t(python)
'''
texte=input("veillez saisir un texte: ")
mot= texte.split()
mot_e=[]
for mot in mot:
 if mot.endswith('e'):
  mot_e.append(mot)
print(mot_e)
