
def teoriaConjuntos():

  s = {(1, 2), True, 3.14, None, False, "Hola mundo" }
  print (s)

  s = { 3.14, False, "Hola mundo",5.1, (1, 2),True, None}
  print (s)

  a = set('Hola Pythonista')
  print(a)

  unicos = set([3, 5, 6, 1, 5,3,3,3,3,3,3,3,3,3,3,3,5,5,5,5])
  print(unicos)
  
  mi_conjunto = {1, 3, 2, 9, 3, 1}
  print(mi_conjunto)
  for numero in mi_conjunto:
      print(numero)

  conjunto = set ()
  conjunto.add (3)
  conjunto.add (-1)
  conjunto.add (3)
  print (conjunto)


  conjunto = set ()
  for i in range (5):
      elemento = int(input('Ingrese un elemento: '))
      conjunto.add (elemento)
  print (conjunto)
  '''
  Ingrese un elemento: 5
  Ingrese un elemento: 2
  Ingrese un elemento: -1
  Ingrese un elemento: -1
  Ingrese un elemento: 5
  {2, 5, -1}
  '''
  set_mutable = set([4.0, 'Carro', True])
  otro_set_mutable = set_mutable.copy()
  set_mutable == otro_set_mutable


teoriaConjuntos()


def operacionesConjunto ():
    conjuntoA = {1,2,3,4,5,6,7,8,9,10}
    conjuntoB = {1,3,5,7,9,11,13,15,17}
    
    #union
    AUB1 = conjuntoA.union(conjuntoB)
    AUB2 = conjuntoA | conjuntoB
    print ('AUB = ', AUB1)
    print ('AUB = ', AUB2)
    
    #interseccion
    AnB1 = conjuntoA.intersection(conjuntoB)
    AnB2 = conjuntoA & conjuntoB
    print ('AnB = ', AnB1)
    print ('AnB = ', AnB2)

    #Diferencia A - B
    ADB1 = conjuntoA.difference (conjuntoB)
    ADB2 = conjuntoA - conjuntoB
    print ('ADB = ', ADB1)
    print ('ADB = ', ADB2)
    
    #Diferencia B - A
    BDA1 = conjuntoB.difference (conjuntoA)
    BDA2 = conjuntoB - conjuntoA
    print ('BDA = ', BDA1)
    print ('BDA = ', BDA2)

    #Diferencia simétrica
    ADSB1 = conjuntoA.symmetric_difference(conjuntoB)
    ADSB2 = conjuntoA ^ conjuntoB
    print ('Diferencia simétrica A B = ', ADSB1)
    print ('Diferencia simétrica A B = ', ADSB2)

    set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
    set_mutable2 = set([11, 5, 9, 2, 4, 8])
    set_mutable3 = set([11, 5, 2, 4])
    print(set_mutable2.issubset(set_mutable1))
    print(set_mutable3.issubset(set_mutable1))

    set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
    set_mutable2 = set([11, 5, 9, 2, 4, 8])
    set_mutable3 = set([11, 5, 2, 4])
    print(set_mutable1.issuperset(set_mutable2))
    print(set_mutable1.issuperset(set_mutable3))

operacionesConjunto()


def metodosConjuntos():
   
    cadena = 'abc'
    print ('cadena ', cadena)
    conjunto = {1, 2}
    conjunto.update(cadena)
    print ('conjunto', conjunto )

metodosConjuntos()

#Documentacion de python para conjuntos 
#https://docs.python.org/es/3/library/stdtypes.html#set