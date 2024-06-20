import sqlite3

class dbBackend:
    #costruire la tabella utenti
    def __init__(self, nomeDB, nome, cognome, u, p):
        self.DBname=nomeDB
        conn=sqlite3.connect(nomeDB)
        errore='nessuno'
        #costrutire la tabella utenti
        sql=""""
        CREATE TABLE IF NOT EXISTS UTENTI
        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOME VARCHAR(25) NOT NULL,
        COGNOME VARCHAR(25) NOT NULL,
        USER VARCHAR(25) NOT NULL UNIQUE,
        PASSWORD VARCHAR(25) NOT NULL
        )
        """

        cur=conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()

        #inserisco l'utente amministrativo
        sql="""
        INSERT INTO UTENTI 
        (NOME, COGNOME, USER, PASSWORD)
        VALUES (?,?,?,?)"""

        cur.conn.cursor()
        try:
            cur.execute(sql, (nome, cognome, u,p))
            conn.commit()
        except Exception as e:
            print(str(e))
            conn.rollback()
        finally:
            cur.close()
            conn.close()
    
    def connettiti(self):
        conn=sqlite3.connect(self.DBname)
        self.Connection = conn
    
    def selectUtenti(self):
        sql="SELECT * FROM UTENTI"
        cur= self.Connection.cursor()
        cur.execute(sql)
        risultato=cur....

    def selectUtente(self, user, passw):
        sql="""
            SELECT * FROM UTENTI
            WHERE USER=?
            AND PASSWORD=?
            """
        cur=self.Connection.cursor()
        
        risultato=cur.fetchone()
        cur.close()
     

    def InsertUtente(self, nome, cognome, user, passw):
        sql="""SELECT * FROM UTENTI
        (NOME, COGNOME, USER, PASSWORD)
        VALUES (?,?,?,?)"""
        
        cur=self.connection.cursor()
       
        riuscito=False
        try:
            cur.execute(sql, (nome, cognome, user, passw))
            self.Connection.commit()
        except Exception as e:
            print(str(e))
            errore= str(e)
            self.Connection.rollback()
        finally:
                cur.close()
                self.Connection.close()

        return riuscito, errore

        
