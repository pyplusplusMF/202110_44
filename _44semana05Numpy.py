# Clase 1 de Junio 
# Instalacion de Numpy

# linea de comando para instalar numpy
# py -m pip install numpy (conda)
# pip install numpy
# https://numpy.org/install/

import numpy as np

arreglo = np.array ([ 1, 2, 3, 4, 5])
print ('arreglo = ', arreglo)  # [1 2 3 4 5]
print ('El tipo de dato de la variable arreglo es: ', type(arreglo)) #<class 'numpy.ndarray'>

arreglo2D = np.array( [ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ]  )
print ('arreglo2D = \n', arreglo2D)
#  [[1 2 3]
#   [4 5 6]
#   [7 8 9]]
print ('El tipo de dato de la variable arreglo2D es: ', type(arreglo2D)) #<class 'numpy.ndarray'>

arreglo2D = np.array ([ [ 1, 2 ], [ 4, 5 ], [ 7, 8 ] ]  )
print ('arreglo2D = \n', arreglo2D)
#  [[1 2]
#   [4 5]
#   [7 8]]
print ('El tipo de dato de la variable arreglo2D es: ', type(arreglo2D)) #<class 'numpy.ndarray'>

arregloDeCeros = np.zeros ( 10 )
print ('arregloDeCeros = ', arregloDeCeros)
# [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
# [0 0 0 0 0 0 0 0 0 0] np.zeros ( 10, int )

matrizDeCeros = np.zeros ((3,3))
print ('matriz de ceros = \n', matrizDeCeros)
#  [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]

