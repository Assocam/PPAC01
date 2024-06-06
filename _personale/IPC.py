from flask import Flask
import requests
backend= Flask('applicazioneBE') #l'applicazione chiamata applicazioneBE sta nella variabile backend
if (__name__ =='__main__'): #se non è un file utilizzato come import da altrove. 
    #Questo IF impedisce che ciò che sewgue venga eseguito nel caso in cui backend venga importato come modulo in un altro file. 
    backend.run(host='0.0.0.0', port=80) 
    #questo host significa che lo facciamo su tutti gli indirizzi. Mi mostrerà tutti gli indirizzi di rete che riesce a trovare.
    #l'host locale (il pc privato) è 127.0.0.1
    #la porta 80 è quella standard del web, il default di flask è 5000 (non si sa perchè)
print(__name__)
