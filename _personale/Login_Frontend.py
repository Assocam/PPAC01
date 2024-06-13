import requests

dati={}
dati['username']='pippo'
dati['password']='123'

domanda=requests.post('http://10.10.21.10/login', json=dati)
risposta=domanda.json()
print(risposta)


