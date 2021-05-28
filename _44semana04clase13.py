#Clase del dia jueves 27 de mayo de 2021

def repasoCiclos():
    #imprimir los numeros del 4 al 30 de 2 en 2
    for numero in range(4, 31, 2):
        print(numero, end = ' ')
    print ('\notra forma')
    #otra forma
    for i in range (31):
        if (i >= 4 and i % 2 == 0):
            print (i, end =  ' ')
    #otra forma con while
    print ('\nOtra forma con While')
    i = 4
    while (i<=30):
        print (i, end = ' ')
        i += 2

    print ('\nOtra forma con listas')
    lista = [] #list()
    for i in range (4, 31, 2):
        lista.append(i)
    print (lista)

repasoCiclos()

def ejemplo2():
    #Cree una lista con cuadrados de los números, de dos en dos, 
    #del 4 al 30, que son divisibles entre 3.
    lista = []
    step = 2
    start = 4
    stop = 31
    for i in range (start, stop, step):
        residuo = i % 3
        if (residuo == 0):
            cuadrado = i ** 2
            lista.append(cuadrado)
    print (lista)
ejemplo2()


def ejemplo3():
    #Cree una lista con cuadrados de los números, de dos en dos, 
    #del 4 al 30, que son divisibles entre 3.
    lista = []
    for i in range (4, 31, 2):
        if (i%3== 0):
            lista.append(i**2)
    print (lista)
ejemplo3()

def ejemplo4():
    # Cree un diccionario en el que las llaves sean una tupla entre 
    # los números del 3 al 10 y su respectivo cubo.
    # Y dónde los valores sean las listas con los cuadrados de 
    # los números de dos en dos, entre el 4 y el 30,
    # que son divisibles enteros con el primer elemento de su llave correspondiente.
    mi_diccionario = dict()
    for y in range(3, 11):
        mi_diccionario[(y, y**3)] = []
        for x in range(4, 31, 2):
            if x%y == 0:
                mi_diccionario[(y, y**3)].append(x**2)

    print(mi_diccionario)
    
    mi_diccionario = { (x, x**3) : [ y**2 for y in range(4,31,2) if y%x == 0 ] for x in range(3, 11) }
    print(mi_diccionario)
ejemplo4()

#list comprehension
def ejemplo5():
    listaDeCeros = [0 for x in range (4)]
    print (listaDeCeros)
    listaDeListas = [[0 for j in range (3)] for i in range (5)]
    print (listaDeListas)
ejemplo5() 
#https://docs.python.org/es/3/tutorial/datastructures.html


