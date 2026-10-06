from abc import ABC,abstractmethod
class Personne(ABC):
    

    def __init__(self,a,b,c,d):
        self.nom = a
        self.prenom = b
        self.sexe = c
        self.datenaiss = d
    @abstractmethod
    def afficher(self):     
        print(self.nom,self.prenom,self.sexe,self.datenaiss)
        
        
    #def grandir(self):
    
    
