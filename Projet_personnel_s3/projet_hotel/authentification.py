from connection import *
class Authentification:
   
        def __init__(self,username,mot_de_passe):
            
            self.username=username
            self.mot_de_passe=mot_de_passe
          
        
        
        
        def verification(self):
            
             cur=con.cursor()
             cur.execute("select * from Utilisateur where username=%s and mot_de_passe=%s",(self.username,self.mot_de_passe))
             personne=cur.fetchall()
            
             #print(self.username)
             #print(self.mot_de_passe)
             #print(personne)

             if len(personne)==0:
             
                return False
             else:
                return True   

aut1=Authentification('BABA','pass02') 
aut2=Authentification('ALd','pass01')
print(aut1.verification())
    
        





        
        

        
        
        
    
        
       

        
    

