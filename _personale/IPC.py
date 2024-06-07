from flask import Flask, request
import requests
backend= Flask('applicazioneBE') #l'applicazione chiamata applicazioneBE sta nella variabile backend


def gestisci01():
    #nel body di postman bisogna mettere dei dati json (doppi apici), specificando raw e Json. {"codiceautore":"123"}
#1) RECUPERO I DATI
    datij=request.json

#2) VERIFICO I DATI
    print(datij)
#3)
    pass

#4) RISPONDO
    retdata={}
    retdata['risposta']='ok'
    rispostajson=json.dumps(retdata)
    print(request.headers)
    return rispostajson,200

@backend.route('/ciao', methods=['GET','POST'])
#in postman  scrivi http://127.0.0.1/ciao, con uno dei methods specificati in @backend.route() e otterrai l'output della funzione rottaCiao
#nel browser ottieni l'output solo se hai specificato methods=GET in @backend.route(), altrimenti ottieni "method not allowed"

#se esegui e poi vuoi cambiare il method: stoppa l'esecuzione con i dati Ctrl+C modifica method e riesegui.


def rottaCiao(): 

    come=request.method #method è una proprietà e non una funzione (non mettiamo le parentesi "()" )
    par=request.query_string
    parstring=par.decode('utf-8')
    if (come=='POST'):
        return f"""hai chiamato la rotta ciao \n
        con metodo {come} \n
        da {request.remote_addr}\n
        e i dati sono: {parstring}, 403"""
    else:
        return f"""hai chiamato la rotta ciao \n
        con metodo {come} \n
        da {request.remote_addr}\n
        e i dati sono: {parstring}, 200 """

#se come dato ottieni b significa binario.

#se nel browser/postman scrivi http://127.0.0.1/ciao?nonna=papera, come dato ottieni "b/nonna=papera". 
# Nonna è il parametro che è valorizzato come papera.
#Ma dopo la decodifica la b non c'è più in parstring.

if (__name__ =='__main__'): #se non è un file utilizzato come import da altrove. 
    #Questo IF impedisce che ciò che sewgue venga eseguito nel caso in cui backend venga importato come modulo in un altro file. 
    backend.run(host='0.0.0.0', port=80) 
    #questo host significa che lo facciamo su tutti gli indirizzi. Mi mostrerà tutti gli indirizzi di rete che riesce a trovare.
    #l'host locale (il pc privato) è 127.0.0.1
    #la porta 80 è quella standard del web, il defaul di flask è 5000 (non si sa perchè)
print(__name__)