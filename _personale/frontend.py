import requests
#import json

datij={'username':'prova', 'password':'123'}
#datij=json.dumps(datij)

risposta=requests.get('http://127.0.0.1/datijson',
                      data=datij)

codice= risposta.status_code  #è il come mi ha risposto. E' un codice numerico

print('risposta:', risposta.text)
print('status code', codice)