# questo è il frontend per le API definite in "backend_definitivo.py" 


import requests
import PySimpleGUI as sg  #programmazione event driven
import  json


##### Register
#Input       :JSON - nome, cognome, username, password
sg.theme='darkGray'
layout=[[sg.Text('nome'), sg.Input(size=(20,1), key='NAME')],
        [sg.Text('cognome'), sg.Input(size=(20,1), key='SURNAME')],
        [sg.Text('username'), sg.Input(size=(20,1), key='USER')],
        [sg.Text('Password'), sg.Input(size=(20,1), key='PWD')],
        [sg.Button('Register', button_color='red'), sg.Button('Annulla')],
        [sg.Text('codice di ritorno', font=('Arial', 15)), sg.Text('', font=('Arial', 15), key='RISPOSTA')],
        [sg.Text('', font=('Arial', 15),key='risp')] ]

win=sg.Window('Register Corso Python', layout)  #una finestra con titolo 'register Corso Python'

nome='nessuno'
cognome='nessuno'
utente='nessuno'
password='nessuno'
dati={}

 #i valori di default
dati['nome']=nome 
dati['cognome']=cognome
dati['username']=utente 
dati['password']=password

while True:
    ev, va = win.read()
    if ev==sg.WIN_CLOSED or ev=='Annulla': #la chiusura del bottone
        break
    elif ev=='Register':
        nome =va['NAME']
        cognome=va['SURNAME']
        utente=va['USER']
        password=va['PWD']

        dati['nome']=nome
        dati['cognome']=cognome
        dati['username']=utente
        dati['password']=password

        
        domanda=requests.put('http://10.10.21.10/registrati', json=dati)

        risposta = domanda.json()
        codice = domanda.status_code

        r=json.dumps(risposta)

        win['RISPOSTA'].update(codice)
        win['risp'].update(r)