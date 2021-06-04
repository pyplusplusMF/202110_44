# Clase del jueves 3 de Junio

import numpy as np
# https://numpy.org/devdocs/reference/arrays.html

arreglo1D = np.array ( [1, 2, 3] )
print ('arreglo1D = ', arreglo1D) #  [1 2 3]
print ('type = ', type (arreglo1D)) # <class 'numpy.ndarray'>
print ('Ndim = ', arreglo1D.ndim) # 1
print ('shape = ', arreglo1D.shape) # shape =  (3,)
print ('Size = ', arreglo1D.size) #  3
print ('dtype = ', arreglo1D.dtype) # int32
print ('nbytes = ', arreglo1D.nbytes) #12


arreglo2D = np.array ( [ [1, 2], [3, 4], [5,6] ] )
print ('arreglo2D = \n', arreglo2D)
#  [[1 2]
#   [3 4]
#   [5 6]]
print ('type = ', type (arreglo2D)) #<class 'numpy.ndarray'>
print ('Ndim = ', arreglo2D.ndim) # 2
print ('shape = ', arreglo2D.shape) # (3, 2)
print ('Size = ', arreglo2D.size) # 6
print ('dtype = ', arreglo2D.dtype) # int32
print ('nbytes = ', arreglo2D.nbytes) # 24


arreglo1D = np.array([1, 2, 3], dtype=np.int)
print ('arreglo1D = ', arreglo1D) # [1 2 3]
print ('arreglo1D dType = ', arreglo1D.dtype) # int32

arreglo1D = np.array([1, 2, 3], dtype=np.float)
print ('\narreglo1D = ', arreglo1D) # [1. 2. 3.]
print ('arreglo1D dType = ', arreglo1D.dtype) # float64

arreglo1D = np.array([1, 2, 3], dtype=np.complex)
print ('\narreglo1D = ', arreglo1D) # [1.+0.j 2.+0.j 3.+0.j]
print ('arreglo1D dType = ', arreglo1D.dtype) # complex128
print ('Parte Real = ', arreglo1D.real) # [1. 2. 3.]
print ('Parte Imaginaria = ', arreglo1D.imag) # [0. 0. 0.]


lista = [1,2,3,4]
array1D = np.array (lista)
print ('array1D = ', array1D) # [1 2 3 4]
print ('ndim = ', array1D.ndim) # 1
print ('shape = ', array1D.shape) # (4, )


listaAnidada =  [[1,2],[3,4]]
array2D = np.array (listaAnidada)
#  [[1 2]
#  [3 4]]
print ('array2D = \n', array2D)
print ('ndim = ', array2D.ndim) #  2
print ('shape = ', array2D.shape) # (2, 2)


# Generar un array con valores constantes
# 1. Array de ceros

arrayDeCeros = np.zeros(  (2,3) )
print ('arrayDeCeros 2D = \n', arrayDeCeros)
# [[0. 0. 0.]
#  [0. 0. 0.]]

# Conversion al tipo de dato entero 64
arrayDeCeros = np.zeros(  (2,3) , dtype = np.int64)
print ('\narrayDeCeros 2D = \n', arrayDeCeros)
#  [[0 0 0]
#  [0 0 0]]
print ('dtype = ',arrayDeCeros.dtype ) # int64



# 2. Array de unos
arrayDeUnos = np.ones ( (4) ) 
print ('\narrayDeUnos 1D = ', arrayDeUnos)
 # [1. 1. 1. 1.]

 # Se genero un arreglo de unos multiplicado po 5.4
x1 = 5.4 * np.ones(10)
print ('x1', x1)
# x1 [5.4 5.4 5.4 5.4 5.4 5.4 5.4 5.4 5.4 5.4]
# se genero un arreglo de 10 posiciones con valor de 5.4
# full recibe dos argumentos y evita la multiplicacion
x2 = np.full(10, 5.4)
print ('x2', x2)
# x2 [5.4 5.4 5.4 5.4 5.4 5.4 5.4 5.4 5.4 5.4]


arreglo1D = np.empty(5)
arreglo1D.fill (10)
print ('arreglo1D = ', arreglo1D)

arreglo1D = np.full (5, 8.0)
print ('arreglo1D = ', arreglo1D)


arreglo1D = np.arange (0.0, 10, 1)
print ('arreglo1D = ', arreglo1D)

arreglo1D = np.linspace (0, 5, 10)
print ('arreglo1D = ', arreglo1D)


x = np. logspace (0,2,5)
print (x)


x = np.array ([-1, 0 , 1])
y = np.array ([-2, 0, 2])
resultado = np.meshgrid(x + y)
print ('x + y = ', resultado )

z = (x + y) ** 2
print ('z = ', z)


# 1. Matriz identidad
matriz = np.identity (4)
print ('matriz = \n',matriz)
#  [[1. 0. 0. 0.]
#   [0. 1. 0. 0.]
#   [0. 0. 1. 0.]
#   [0. 0. 0. 1.]]


matriz = np.eye(3, k=1)
print ('\n matriz = \n', matriz)
# matriz = 
# [[0. 1. 0.]
#  [0. 0. 1.]
#  [0. 0. 0.]]
matriz = np.eye(3,k= -1)
print ('\n matriz = \n', matriz)
# [[0. 0. 0.]
#  [1. 0. 0.]
#  [0. 1. 0.]]


#3. Matriz diagonal
matriz = np.diag(np.arange(0,20,5))
print ('\n matriz = \n', matriz)
#  matriz = 
# [[ 0  0  0  0]
#  [ 0  5  0  0]
#  [ 0  0 10  0]
#  [ 0  0  0 15]]


# Crear la siguiente matriz de rango 2 con forma (3, 3)
# [[ 1  2  3]
#  [ 5  6  7]
#  [ 9 10 11 ]]
a = np.array([[1,2,3], [5,6,7], [9,10,11]])
print (a)

# Usar el rebanado para sacar el subconjunto que consiste en las 2 primeras filas
# y las columnas 1 y 2; b es el siguiente conjunto de forma (2, 2):
# [[2 3]
#  [6 7]]
b = a[:2, 1:3]
print(b)

# https://numpy.org/doc/stable/reference/arrays.indexing.html 


x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
print (x)
print (y)

suma = x + y
print ('La suma de las dos matrices es: ')
print (suma)


x = np.array([[1,2],[3,4]])
print (x)
print(np.sum(x))  # Calcular la suma de todos los elementos; imprime "10"
print('suma col = ', np.sum(x, axis=0))  # Calcula la suma de cada columna; imprime "[4 6]"
print('suma fil = ',np.sum(x, axis=1))  # Calcula la suma de cada fila; imprime "[3 7]"

x = np.array([[1,2], [3,4]])
print(x)    # Prints "[[1 2]
            #          [3 4]]"
print(x.T)  # Prints "[[1 3]
            #          [2 4]]"

# Esto está incluido en los materiales del curso
import numpy as np

def displayInicialTriqui():
    for i in range(0,3):
        for j in range(0,3):
            print("|_",end="")
        print("|")

def displayTriqui(matriz):
    for i in range(0,3):
        for j in range(0,3):
            if matriz[i,j]==1:
                print("|X", end="")
            else:
                if matriz[i,j]==10:
                    print("|O",end="")
                else:
                    print("|_",end="")
        print("|")
        
def estadoDelJuego(matriz)->int:
    #devuelve 1 si gana la X
    if 3 in np.sum(matriz, axis=0) or 3 in np.sum(matriz, axis=1) or np.sum(np.diagonal(matriz))==3 or np.sum(np.diagonal(np.fliplr(matriz)))==3:
        salida = 1
    else:
        #devuelve 2 si gana la Y
        if 30 in np.sum(matriz, axis=0) or 30 in np.sum(matriz, axis=1) or np.sum(np.diagonal(matriz))==30 or np.sum(np.diagonal(np.fliplr(matriz)))==30:
            salida = 2
        else:
            #devuelve 3 si no hay ganador
            if np.sum(matriz)==45 or np.sum(matriz)==54:
                salida = 3
            else:
                #devuelve 4 si aun hay juego
                salida = 4
    return salida

def jugarTriqui():
    #seleccionar aleatoriamente un jugador
    turno=False
    if np.random.rand()<0.5:
        turno=True
    #inicializar las variables del juego
    displayInicialTriqui()
    matriz = np.zeros((3,3))   # Crear una matriz de todos los ceros
    estado=4
    while(estado==4):
        #atrapar el movimiento de los jugadores
        tupla= tuple(input("Ingrese la casilla a jugar, ej: la casilla superior derecha es 1,3: "))
        #convertir la notacion de los jugadores a los indices de la matriz
        x=int(tupla[0])-1
        y=int(tupla[2])-1
        #validar movimiento dentro del tablero
        if x>=0 and x<= 2 and y>=0 and y<=2:
            #validar movimiento no antes hecho
            if matriz[x,y]==0:
                if turno:
                    matriz[x,y]=1
                else:
                    matriz[x,y]=10
                #llamar la funcion del estado del juego
                estado = estadoDelJuego(matriz)
                #llamar el visualizador
                displayTriqui(matriz)
                #cambiar de turno
                turno=not(turno)
            else:
                print("Recuerde jugar en casillas vacias!")
        else:
            print("Recuerda que el tablero es de 3 por 3!  ej: la casilla inferior izquierda es 3,1")
    # Publicar el resultado del juego
    if estado == 1 :
        print("El jugador X ha ganado!")
    else:
        if estado == 2 :
            print("El jugador O ha ganado!")
        else:
            print("No hubo ganadores!")
jugarTriqui()           