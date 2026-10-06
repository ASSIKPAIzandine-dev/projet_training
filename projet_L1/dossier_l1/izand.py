diviseur=[ ]  
def listDiv(a):
  for i in range(1,a+1):
     if a%i==0:
       diviseur.append(i)
  
  return " les diviseur de "+str(a)+" sont "+str(diviseur)   
  
a=int(input("entrer un nombre:"))
print(listDiv(a))  



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
  

a=int(input("entrer un nombre:"))
print(listDiv(a))  
  
