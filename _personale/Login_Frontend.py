#questo codice è da eseguire in locale

import requests
import PySimpleGUI as sg  #programmazione event driven
import  json

sg.theme='darkGray'
layout=[[sg.Text('username'), sg.Input(size=(20,1), key='USER')],
        [sg.Text('Password'), sg.Input(size=(20,1), key='PWD')],
        [sg.Button('Login', button_color='red'), sg.Button('Annulla')],
        [sg.Text('codice di ritorno', font=('Arial', 20)), sg.Text('', font=('Arial', 20), key='RISPOSTA')],
        [sg.Text('', font=('Arial', 20),key='risp')] ]

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
        risposta=domanda.json()
        codice=risposta.status_code
        win['RISPOSTA'].update(codice)  #non si può assegnare con win[]=codice. Devo usare update
        r=json.dumps(risposta)
        win['risp'].update(r)
        #print(f'Hai premuto login: {utente} e {password}')

win.close()




print(risposta)


