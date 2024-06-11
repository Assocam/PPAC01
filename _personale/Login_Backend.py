# IPC login backend.
#in postman metti http://10.10.21.10/login, metodo POST, formato Jason, Dati: {"username":"test", "password":"pwtest"}

from flask import Flask, request
import sqlite3  #crea file in locale che non permettono la multiutenza. Se ricevesse tante richieste le eseguirebbe in coda.

app=Flask('Fare il login')

connessione= sqlite3.Connection('databaseCorso.db') 
sql="""
create table if not exists utenti
(ID INTEGER PRIMARY KEY,
NOME VARCHAR(30),
COGNOME VARAHCAR(30),
USER VARCHAR(15),
PWD VARCHAR(15)
)
"""

cursor=connessione.cursor()
cursor.execute(sql)
connessione.commit()
cursor.close()


#inserisco i dati di partenza
sql="""
insert into utenti
(ID, NOME, COGNOME, USER, PWD) VALUES
(?, ?, ?, ?, ?)
"""

cursor=connessione.cursor()
try:
    cursor.execute(sql, (1,"pippo","pluto","ppp","123"))
    connessione.commit()
except:
    connessione.rollback()
cursor.close()

cursor=connessione.cursor()
try:
    cursor.execute(sql, (2,"nome1","cognome1","user1","pw1"))
    connessione.commit()
except:
    connessione.rollback()
cursor.close()

def doLogin(user, passw):

    #cerca nel db lo username e la password
    connessione=sqlite3.commenct('databaseCorso.db')
    cursore=connessione.cursor()
    sql="""
        select * from utenti
        where user= ?
        and pwd=?
        """
    cursore.execute(sql, (user, passw))
    records=cursore.fetchone()

    id=0
    nome=''
    cognome=''
    user=''
    password=''

    if records:
        for r in records:
            id, nome, cognome, utente, password = r
    
    cursore.close()
    connessione.close()

    return id, nome, cognome, utente, password



@app.route('/login', methods=['POST'])
def evaluateLogin():
    try: 
        dati=request.json()
        u=dati["username"]
        p=dati["password"]

    except:
         return {"result": "errore nei dati"}, 403

    risultato= doLogin(u,p)
    print(risultato)
    return {"result": f"user {u}, password {p}"}, 200

if __name__=='__main__':
    app.run(host="0.0.0.0", port=80) #i parametri di default sono Host=127.0.0.1 e port=5000 

