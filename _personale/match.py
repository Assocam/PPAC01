#il match case è stato nintrodotto solo dalla versione 3.10 di python

a=10
match a:
     case 10:
          print('valore 10')
     case 11:
        print('valore 10')
     case 12:
          print('valore 10')
     case _:
          print('valore non contemplato')

punto=(2,4)
match punto:
     case (x,y):
          print({x/y})
          print(f'hai dato {punto[0]} e {punto[1]}')
     case (x,0):
        print('division by 0')
     case (0,y):
          print('sempre 0')
     case _:
          print('valore non contemplato')