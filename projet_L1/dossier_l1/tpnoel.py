#def longest_string():
 #       string1=input('entrez la premiere chaine:')
  #       string2=input('entrez la deuxieme chaine:') 
    #   if len( string1)>len(string2):
   #  print(f'la chaine la plus longue est :{string1}')
     # else:print(f'la chaine la plus longue est :{string2}')
#longest_string()


liste=[]
def multiple():
 # number=int(input("entrer un nombre:"))


  for i in range(0,10):
     multiple=number*i

     liste.append(multiple)
  print(liste) 
#multiple()

liste_chaine=["lapin","chat","chien","chiot","dragon","ornithorynque"]
def nombre_chaine():
  # liste_chaine=["lapin","chat","chien","chiot","dragon","ornithorynque"]

  for i in liste_chaine:

    print ( len(i))
 #nombre_chaine()


def ranger():
  T=[25,12,35,58,15,17,20]
  T.sort()
  print(T)  
ranger()




