import psycopg2 
def connection():
    conn=psycopg2.connect(host='localhost',dbname='gestion_stock',user='abdel',password='ags')
    return conn
conn=connection()



def fermer_connexion():
    conn.close()
    print("connexion fermer")













