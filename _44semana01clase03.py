# Autor: Semana 01 Clase 3 - Funciones
# Fecha: 4 de mayo 7:47 p.m.

'''
Definir una función que reciba como parametro dos variables 
de tipo entero y retorne la suma de esas variables
'''

'''
print ("por favor ingrese el numero 1: ")
numero1 = int(input())
numero2 = int(input("por favor ingrese el numero 2: "))
suma = numero1 + numero2
print ("La suma es: "+str(suma))
'''

def suma(numero1:int, numero2:int) -> int:
    x = numero1 + numero2
    return x

def resta(numero1, numero2):
    x = numero1 - numero2
    return x

def multiplicacion (numero1, numero2):
    x = numero1 * numero2
    return x

def division (numero1, numero2):
    x = numero1 / numero2
    return x



x = 25.5 
y = 50

resultado1 = suma (x,y)
resultado2 = resta (x,y)
resultado3 = multiplicacion (x,y)
resultado4 = division (x,y)

print (str(x)+" + "+str(y)+ " es igual a : "+str(resultado1))
print (str(x)+" - "+str(y)+ " es igual a : "+str(resultado2))
print (str(x)+" * "+str(y)+ " es igual a : "+str(resultado3))
print (str(x)+" / "+str(y)+ " es igual a : "+str(resultado4))





def division(a, b):
    x = a / b
    return x

b = 0
a = 10

#print (division(a, b))


def division2(b, a):
    x = a / b
    return x

b = 0
a = 10

print (division2(a, b))

'''
def ejercicio1(num1, num2):
  print(num1, "+", num2)
  return num1 + num2

resultado = ejercicio1(13,7)
print(resultado)



def mas(val1, val2):
    
    A = val1 + val2 
    
    print(A)

mas(67,86)

def add(m1, m2):
  a = (m1 + m2)
  return a
n1= int(input())
n2= int(input())
print("El resultado de la suma es: "+str(add(n1, n2)))



def suma(a, b):
    return a + b
resultado = suma(7,3)
print(resultado)
'''