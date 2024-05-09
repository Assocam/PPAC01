import datetime
import math

#PASSARE UN NUMERO INDEFINITO DI ARGOMENTI SOTTO FORMA DI LISTA
# L'asterisco rende args una lista, args lo possiamo anche rinominare.

def somma(*args):
  totale=0
  for a in args:
    try: 
      totale +=a
    except:
      totale+=1.0
  return totale

print(somma(2,3))
print(somma(2,3,4,5,6))
print(somma(2.7,3.4,4,5.0,'ciao'))

#ARGOMENTI KEYWORD PASSATI SOTTO FORMA DI DIZIONARIO
# Il doppio asterisco rende kwargs un dizionario, kwargs lo possiamo anche rinominare.

def prova(**kwargs):
  for chiave, valore in kwargs.items():
    print(chiave, valore)
    a=kwargs.get('primo',1) 
    #il secondo argomento è il default che vogliamo dare ad a, nel caso in cui non venga dato in input alla funzione. 
    b=kwargs.get('secondo',2)
    print('a+b=', a+b)

prova(primo=232,secondo=999)
prova(primo=232,altro="other",secondo=999)
prova(eta=20, nome='filippo')


#LAMBDA
# è una funzione anonima da usare in linea
# viene eseguita più velocemente rispetto alla stessa funzione definita senza lambda
lista=[2,3,4,5]
lambda_start =datetime.datetime.now().microsecond
for l in lista:
  r=lambda x: (math.cos(math.pi/x)) # x è un segnaposto e può essere rinominato.
  print(l, r(l))

lambda_stop = datetime.datetime.now().microsecond
print('la durata di lambda è', lambda_stop-lambda_start)

##
fun_start =datetime.datetime.now().microsecond
def funzione(a):
  return math.cos(math.pi/a)

for l in lista:
  print(l, funzione(l))

fun_stop = datetime.datetime.now().microsecond
print('la durata della funzione è', fun_stop-fun_start)