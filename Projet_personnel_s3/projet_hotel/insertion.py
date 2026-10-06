from connection import *



cur=con.cursor()
cur.execute("insert into Utilisateur(id,username,mot_de_passe,roles)values(%s, %s, %s,%s)",(10,"badaou","apss01","gerant"))
con.commit()
cur.close()
con.close()


