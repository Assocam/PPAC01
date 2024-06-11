#questo script va eseguito mentre il backend è attivo (in ascolto), ma non può essere attivo sullo stesso IDE. 
#Esegui il backend, per esempio, nel terminale di python.

import requests
#import json

datij={'username':'prova', 'password':'123'} 

risposta=requests.get('http://127.0.0.1/datijson',  #nel backend abbiamo usato il metodo get.
                      #specifichiamo l'URL da interrogare.
                      json=datij) # al posto del parametro json posso mettere data=json.dumps(datij)


codice= risposta.status_code  #è il come mi ha risposto. E' un codice numerico

print('risposta:', risposta.text)
print('status code', codice)

#risposta.json #è in formato json