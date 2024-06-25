# questo è il frontend per le API definite in "backend_definitivo.py" 

import requests
import PySimpleGUI as sg  #programmazione event driven
import  json

##### Login

sg.theme='darkGray'
layout=[[sg.Text('username'), sg.Input(size=(20,1), key='USER')],
        [sg.Text('Password'), sg.Input(size=(20,1), key='PWD')],
        [sg.Button('Login', button_color='red'), sg.Button('Annulla')],
        [sg.Text('codice di ritorno', font=('Arial', 15)), sg.Text('', font=('Arial', 15), key='RISPOSTA')],
        [sg.Text('', font=('Arial', 15),key='risp')] ]

win=sg.Window('Login Corso Python', layout)  #una finestra con titolo 'Login Corso Python'


utente='nessuno'
password='nessuno'
dati={}
 #i valori di default
dati['username']=utente 
dati['password']=password

while True:
    ev, va = win.read()
    if ev==sg.WIN_CLOSED or ev=='Annulla': #la chiusura del bottone
        break
    elif ev=='Login':
        utente=va['USER']
        password=va['PWD']

        dati['username']=utente
        dati['password']=password
        domanda=requests.post('http://10.10.21.10/login', json=dati)
    
#print('risposta:', risposta.text)
#print('status code', codice)
#print("risposta json : ", risposta.json()) # è in formato json
#print("tipo: ", type(risposta.json())) # è dato col tipo dictionary perchè è molto simile al formato json
       
    
        risposta = domanda.json()
        codice = domanda.status_code

        r=json.dumps(risposta)

        win['RISPOSTA'].update(codice)
        win['risp'].update(r)

#print(f'Hai premuto login: {utente} e {password}')
win.close()
print(risposta)

