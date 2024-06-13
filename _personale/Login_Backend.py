# IPC login backend.
#in postman metti http://10.10.21.10/login (indirizzo IP del prof), metodo POST, formato Json, Dati: {"username":"pippo", "password":"123"}

from flask import Flask, request
#import sqlite3  #crea file in locale che non permettono la multiutenza. Se ricevesse tante richieste le eseguirebbe in coda.
from dbUtil import initDB, doLogin


app=Flask('Login backend')
DB='databaseCorso.db'

initDB(DB)

@app.route('/login', methods=['POST'])
def evaluateLogin():
    try: 
        dati=request.json()
        u=dati["username"]
        p=dati["password"]

    except:
         return {"result": "errore nei dati"}, 403

    risultato= doLogin(DB, u,p)
    print(risultato)

    if risultato:
        retMSG='login ok'
        retCode=200
    else: 
        retMSG='not found'
        retCode=404

    return {"result": f"{retMSG}, {retCode}"}, 200

if __name__=='__main__':
    app.run(host="0.0.0.0", port=80) #i parametri di default sono Host=127.0.0.1 e port=5000 

