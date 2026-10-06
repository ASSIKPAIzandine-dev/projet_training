import random
def mastermind(longue=4,maximum=6):
  secret=[]
   
  essai=0
  for i in range(longue):
     a=random.randint(1,maximum)
     secret.append(a)
     print(secret)   
  


  while True:
     code=list(secret)
     z=input("entrer un nombre de quatre chiffre:")
     while len(z)!=4:
        z=input("entrer un nombre de quatre chiffre:")
     j=[int(b) for b in z]
     
     
     essai+=1
     bien,mal=0,0
     for i in range (longue):
        
        if j[i]==code[i]:
          bien+=1
          j[i]="#"
          code[i]="*"
     if bien==4:
      print("gagne!")
      break
     for i in range (longue):  
         if j[i] in code:
            mal+=1
            code[code.index(j[i])]="*"      
     print("le bien placé est:",bien,"le mal placé est:",mal)
     if essai==5:
        print("vos essais sont fini")
        print("le code secret etait:", " ".join(map(str,secret)))
        break 
        
        
mastermind(longue=4,maximum=6) 
      
     
