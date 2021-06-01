#clase del dia lunes 31 de mayo
def listComprehension():
    # * nombreIterable * = [ itemToAppend for item in list ]

    # * nombreIterable * = [ itemToAppend for item in list if condit ]

    # * nombreIterable * = [ itemToAppend if condition else itemToAppend for item in list]
    
    # https://stackoverflow.com/questions/9987483/elif-in-list-comprehension-conditionals
    
    # crear una lista con el cuadrado de los numeros entre 0 y 5
    lista = [ i * i
            for i in range (5)]
    print ('lista ',lista)
    
    # Crear una lista de 100 numeros usando list comprehension
    listaNumeros = [ i
                    for i in range (100)]
    print ('listaNumeros ', listaNumeros)
    
    # Crear una lista de numeros pares entre 0 y 10 con list comprehension
    listaNumerosPares = [i  
                         for i in range (10)  
                         if i % 2 == 0] 
    print ('listaNumerosPares ',listaNumerosPares)
    
    # Crear una lista de cadenas de texto pares e impares entre 0 y 10 con list comprehension
    listaParesImpares = ['par'
                        if i %2 == 0
                        else
                        'impar'
                        for i in range (10)]
    print ('listaParesImpares ',listaParesImpares)

    # Crear una lista de cadenas de texto que a partir de un conjunto de numeros indique 
    # cual numero es positivo, cual negativo y cual cero.

    listaNumeros = [13,-1,0,-1,0,1,-5,-9,9]
    listaCero2 = ['positivo'
                if elemento > 0
                else
                'negativo'
                if elemento < 0
                else
                'cero'
                for elemento in listaNumeros]
    print ('listaCero2 ', listaCero2)
    
    #ejemplo para los diccionarios
    diccionario = { i : 2 * i
               for i in range (5)}
    print (diccionario)
    
    # Ejemplo para conjuntos
    conjunto = { x * x
           for x in range (5)}
    print (conjunto)
    
listComprehension()