#martes 11 de mayo
'''
Diseñe una funcion que reciba como parámetro un número real que represente la calificación 
numérica de un examen y retorne la calificación cualitativa correspondiente al número dado. 
La calificación cualitativa será una de las siguientes:
    0.0 a 2.9 Deficiente
    3.0 a 3.4 Regular
    3.5 a 3.9 Aceptable
    4.0 a 4.4 Bueno
    4.5 a 5.0 Excelente
'''


def notaReal2(nota:float) ->str:
  salida = ""
  if (nota >= 0.0 and nota <= 2.9):
    salida = "Deficiente"
  elif(nota >= 3.0 and nota <= 3.4):
    salida = "Regular"
  elif(nota >=3.5 and nota <= 3.9):
    salida = "Aceptable"
  elif(nota >=4.0 and nota <= 4.4):
    salida = "Bueno"
  elif(nota >= 4.5 and nota <= 5.0):
    salida = "Excelente"
  
  return salida 

nota2 = -1
print (notaReal2(nota2))

def cadenas():
    frase = 'Monty Python'
    x = frase [:5] #Comienza en la posicion 0
    y = frase [2:] #comienza en la posicion 2
    print (x)
    print (y)

    fruta = 'banana'
    x = fruta[3:3]
    print ("x = ", x)
    
    fruta = 'limon'
    #la letra n esta en la posicion -1
    #la letra o esta en la posicion -2
    #la letra m esta en la posicion -3
    #la letra i esta en la posicion -4
    #la letra l esta en la posicion -5
    x = fruta[-5]
    print ("x = ", x) #letra l
    
    saludo = '¡Hola, mundo!'
    nuevo_saludo = 'J' + saludo[1:]
    print(nuevo_saludo)
    
    fruta = 'manzana'
    x = 'man'
    if (x in fruta):
        print (x, "se encuentra en ", fruta)
    
    palabra = 'guayaba'
    if palabra < 'banana':
        print('Tu palabra,' + palabra + ', viene antes de banana')
    elif palabra > 'banana':
        print('Su palabra,' + palabra + ', viene después de banana.')
    else:
        print('Está bien, su palabra es banana')
    
    letra1 = 'a' # 97 ASCII
    letra2 = 'A' # 65 ASCII
    if (letra1 > letra2):
        print (letra1, " es mayor que ", letra2)
    elif (letra1 < letra2):
        print (letra1 , " es menor que ", letra2)
    else:
        print (letra1, " es igual a ", letra2)
    
    x = ord('a') + ord('a')
    print (x) #194
    
    palabra1 = 'aa' #97 + 97 = 194 ASCII
    palabra2 = 'AA' #65 + 65 = 130 ASCII
    if (palabra1 > palabra2):
        print (palabra1, " es mayor que ", palabra2)
    
    palabra = 'banana'
    palabra_nueva = palabra.upper()
    print(palabra_nueva)
    
    palabra = 'banana'
    index = palabra.find('a')
    print(index)
    
    
    palabra = 'limon'
    encontrar = palabra.find('li')
    print (encontrar)
    
    palabra  = 'limon con sal'
    encontrar = palabra.find('on', 4)
    print (encontrar)
    
    linea = '        Aquí vamos          '
    print (linea.strip())

    linea = '\t Aquí vamos      '
    print (linea.strip())

    linea = 'Que Tengas Un Buen Día'
    print (linea.startswith('Que'))
    
    linea = "HOLA MUNDO"
    print (linea.lower())
    
    linea = "HOLA MUNDO"
    print (linea)
    print (linea.startswith('h'))

    linea = linea.lower()
    print (linea)
    print (linea.startswith('h'))
    
    camellos = 42
    x = 100
    y = 20
    print ('He visto %d camellos y %d dromedarios, tambien he visto %d elefantes' %(camellos, x, y) )  

    # Saldrán dos líneas en pantalla, una con Hola, la otra con Mundo
    cadena = "Hola\nMundo"  
    print(cadena)
    
    # Saldrá una única línea en pantalla y la \ y la n será visibles como caracteres normales.
    cadena2 = r"Hola\n\tMundo"
    print(cadena2)   
    
    cadena = "un uno, un dos, un tres"
    print (cadena)
    print (cadena.replace("un", "XXX"))        # saca por pantalla "XXX XXXo, XXX dos, XXX tres"
    print (cadena.replace("un", "XXX", 2))     # Sólo reemplaza 2 "un", así que saca por pantalla "XXX XXXo, un dos, un tres"
    print (cadena)    


    # saca "El valor es 12
    print ("El valor es {}".format(12))

    # saca "El valor es 12.3456
    print ("El valor es {}".format(12.3456))

    # Tres conjuntos {}, el primero para el primer parámetro de format(), el segundo para el segundo
    # y así sucesivamente.
    # saca "Los valores son 1, 2 y 3"
    print ("Los valores son {}, {} y {}".format(1,2,3))

    # Entre las llaves podemos poner la posición del parámetro. {2} es el tercer parámetro de format()
    # {0} es el primer parámetro de format.
    # saca "Los valores son 3, 2 y 1"
    print ("Los valores son {2}, {1} y {0}".format(1,2,3))
    
    
    # saca "2 y 1"
    print ("{pepe} y {juan}".format(juan=1, pepe=2))
    
    
    
    usuario = str(input("Ingrese su nombre de usuario: "))
    correo = usuario + "@gmail.com"
    print (correo)
    
cadenas()

