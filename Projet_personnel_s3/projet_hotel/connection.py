import psycopg2

class Connexion:
    def __init__(self,host,user,bd,passw):
        
        self.host=host
        self.user=user
        self.database=bd
        self.password=passw
    def connection(self):
       conn=psycopg2.connect(host=self.host, user=self.user ,database= self.database , password= self.password)
       return conn
    
        
    
conection=Connexion('localhost','izandine','gestion_hotel','iza')
con=conection.connection()






