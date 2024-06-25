# questo è il frontend per le API definite in "backend_definitivo.py" 


import requests
import PySimpleGUI as sg  #programmazione event driven
import  json


##### ListUsers

sg.theme='darkGray'
layout=[
        [sg.Button('List users', button_color='red'), sg.Button('Annulla')],
        [sg.Text('codice di ritorno', font=('Arial', 15)), sg.Text('', font=('Arial', 15), key='RISPOSTA')],
        [sg.Text('', font=('Arial', 15),key='risp')]]

win=sg.Window('Lista utenti Corso Python', layout)  


#dati['password']=password

while True:
    ev, va = win.read()
    if ev==sg.WIN_CLOSED or ev=='Annulla': #la chiusura del bottone
        break
    elif ev=='List users':

        domanda=requests.get('http://10.10.21.10/userList')

    risposta = domanda.json()
    codice = domanda.status_code

    r=json.dumps(risposta)
    print(r)
    win['RISPOSTA'].update(codice)
    win['risp'].update(r)



