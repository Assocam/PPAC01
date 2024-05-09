def somma(*args):
  totale=0
  for a in args:
    totale +=a
  return totale

print(2,3)
print(2,3,4,5,6)


def prova(**kwargs):
  for chiave, valore in kwargs.items():
    print(chiave, valore)
    a=kwargs['primo']
    b=kwargs['secondo']
    print('a+b=', a+b)

prova(primo=232,secondo=999)
prova(primo=232,altro="altro",secondo=999)
