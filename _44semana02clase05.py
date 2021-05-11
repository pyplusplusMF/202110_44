#lunes 10 de mayo
#clase 8
def teoria1 ():
  x = 40.0
  y = x
  print (x != y) # x no es igual a y
  print (x > y) # x es mayor que y
  print (x < y) # x es menor que y
  print (x >= y) # x es mayor o igual que y
  print (x <= y) # x es menor o igual que y
  print ("x is y ¿", x, " es lo mismo que ", y , "? ",  x is y) # x es lo mismo que y
  print (x is not y) # x no es lo mismo que y
teoria1()


def teoria2():
  x = 800

  print ("and", x > 0 and x < 10)
  print ("or", x > 0 or x < 10)


  n = 8
  print (n%2 == 0 or n%3 == 0)
teoria2()


######ESTRUCTURA CONDICIONAL SIMPLE

def condicionalSimple():
  x = 10
  if x > 0 :
    print('x es positivo')
condicionalSimple()


### ESTRUCTURA CONDICIONAL ALTERNATIVA O DOBLE
def condicionalDoble():
  x = 10
  if x%2 == 0 :
      print('x es par')
  else :
      print('x es impar')
condicionalDoble()

#### ESTRUCRTURA CONDICIONAL MULTIPLE

def condicionalMultiple():
  x = 40
  y = 40

  if x < y:
      print('"x" es menor que "y"')
  elif x > y:
      print('"x" es mayor que "y"')
  else:
      print('"x" y "y" son iguales')

condicionalMultiple()

def condicionalMultiple2():
  letra = 'a'

  if letra == 'a':
      print('Mal resultado')
  elif letra == 'b':
      print('Buen resultado ')
  elif letra == 'c':
      print('Cerca, pero no es correcto')
  #else:
      #print ('Le letra no está en ninguna categoria')

condicionalMultiple2 ()

def condicionalAnidada():
  x = 10
  if 0 < x:
    if x < 10:
        print('x es un número positivo de un solo dígito.')
  
  if 0 < x and x < 10:
    print('es un número positivo de un solo dígito')
condicionalAnidada ()