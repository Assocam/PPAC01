# questo è il frontend per le API definite in "backend_definitivo.py" 
# da fare come compito a casa.
#prendi spunto anche da login_frontend.py

import requests
#import json

##### Login

datij={'username':'prova', 'password':'123'} 
risposta=requests.get('http://127.0.0.1/login', json=datij) 

codice= risposta.status_code  #è il come mi ha risposto. E' un codice numerico

print('risposta:', risposta.text)
print('status code', codice)

print("risposta json : ", risposta.json()) # è in formato json
print("tipo: ", type(risposta.json())) # è dato col tipo dictionary perchè è molto simile al formato json



##### Register
risposta=requests.put('http://127.0.0.1/register',  json=datij)

##### ListUsers
##usiamo le liste di PySimpleGUI, imparandole dalla documentazione


#### ListCourses