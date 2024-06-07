import requests
#import json

datij={'username':'prova', 'password':'123'}

risposta=requests.get('http://127.0.0.1/datijson',
                      json=datij) # al posto del parametro json posso mettere data=json.dumps(datij)


codice= risposta.status_code  #è il come mi ha risposto. E' un codice numerico

print('risposta:', risposta.text)
print('status code', codice)