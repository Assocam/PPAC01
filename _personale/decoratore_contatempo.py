
import time

def contatempo(funzione):
    """questo decoratore calcola la durata della funzione"""
    def wrapper(*args, **kwargs):
        start=time.perf_counter()#start=datetime.datetime.now().microsecond
        lista=funzione(*args, **kwargs)
        stop= time.perf_counter() #stop=datetime.datetime.now().microsecond
        print('tempo = ',stop-start)
        return lista #il risultato della funzione
    return wrapper

@contatempo
def fibonacci(sequenza):  #questo argomento determina la lunghezza della lista di output
    primo=0
    secondo=1

    listafibo=[]
    for v in range(sequenza):
        fibo=primo+secondo
        primo=secondo
        secondo=fibo
        listafibo.append(fibo)
    
    return listafibo


print(fibonacci(14))


#altri esempi di utilizzo del decoratore:
# - scrivere qualcosa nel log
# - salvare qualcosa in un DB

