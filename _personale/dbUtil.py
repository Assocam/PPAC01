# IPC login backend.
#in postman metti http://10.10.21.10/login, metodo POST, formato Jason, Dati: {"username":"test", "password":"pwtest"}

from flask import Flask, request
import sqlite3  #crea file in locale che non permettono la multiutenza. Se ricevesse tante richieste le eseguirebbe in coda.


def initDB():

    connessione= sqlite3.Connection('databaseCorso.db') #se esiste si connette, altrimenti lo crea.
    sql="""
    create table if not exists utenti
    (ID INTEGER PRIMARY KEY,
    NOME VARCHAR(30),
    COGNOME VARAHCAR(30),
    USER VARCHAR(15) NOT NULL,
    PWD VARCHAR(15) NOT NULL
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


def doLogin(DB, user, passw):

    #cerca nel db lo username e la password
    connessione=sqlite3.connect(DB)
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
        #for r in records: #c'è solo una tupla a causa di fetchone 
            id, nome, cognome, utente, password = records
    
    cursore.close()
    connessione.close()

    utenteRet={}
    utenteRet['ID']=id
    utenteRet['NOME']=nome
    utenteRet['COGNOME']=cognome
    utenteRet['USERNAME']=utente
      utenteRet['PASSWORD']=password
    return id, nome, cognome, utente, password
