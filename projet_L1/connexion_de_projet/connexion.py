import psycopg2

class Connexion:
    def __init__(self):
        self.conn=psycopg2.connect(host='localhost', user = "izandine", database = 'gestion_hotel', password='iza')
        self.cur =self.conn.cursor()
    
conection=Connexion()
con=conection.conn
#print(con)


