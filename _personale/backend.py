from flask import Flask, request
import json 

backend= Flask('applicazioneBE') #l'applicazione chiamata applicazioneBE sta nella variabile backend

@backend.route('/datijson', methods=['GET']) 
#decoratore di rotta, che rende la seguente funzione una rotta di cui specifichiamo il nome e il "come".
def gestisci01():
    #nel body di postman bisogna mettere dei dati json (doppi apici), specificando raw e Json. {"username":"test", "password":"pwtest"}

#1) RECUPERO I DATI
    datij=request.json
    #dizrichiesta =json.loads(datij)

#2) VERIFICO I DATI
    print('ho ricevuto: ',datij)
    for k,v in datij.items():
        print(k,v)
    try:
        user=datij['username']
        pwd=datij['password']
    except:
        print('la richiesta non va bene')
        return {"messaggio":"errore nei dati"}, 403  #il 403 significa forbidden

#3)ELABORO
    pass

#4) RISPONDO
    retdata={}
    retdata['risposta']='ok'
    rispostajson=json.dumps(retdata)
    print('header della richiesta ', request.headers)
    print('ti ho risposto: ', rispostajson)
    return rispostajson, 200  #il 200 significa "ok".
    #il return è obbligatorio per flask. Deve restituire qualcosa in formato json.

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
    #la porta 80 è quella standard del web per l'http, il default di flask è 5000 (non si sa perchè)
print(__name__)