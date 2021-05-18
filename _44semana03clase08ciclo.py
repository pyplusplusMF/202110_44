def cicloWhile():
    n = 5
    while n > 0:
        print(n)
        n = n - 1
    print('Despegue!')
    print ("El valor de n despues del ciclo", n)
cicloWhile()

def factorial (n:int) -> int:
    factorial = 1 
    i = 1 #variable que controla el ciclo
    while (i <= n):
        #variable que incrementa su valor
        #es una variable acumuladora
        factorial = factorial * i
        i = i + 1 #variable que controla el ciclo
    return factorial
print (factorial(0))
print (factorial(1))
print (factorial(3))


def cicloControladoPorEvento():
    promedio, total, contar = 0.0, 0, 0

    print("Introduzca la nota de un estudiante (-1 para salir): ")
    grado = int(input())
    while grado != -1:
        total = total + grado
        contar = contar + 1
        print("Introduzca la nota de un estudiante (-1 para salir): ")
        grado = int(input())
    promedio = total / contar
    print("Promedio de notas del grado escolar es: " + str(promedio))
cicloControladoPorEvento()

def cicloWhileConElse():
    promedio, total, contar = 0.0, 0, 0
    mensaje = "Introduzca la nota de un estudiante (-1 para salir): "

    grado = int(input(mensaje))
    while grado != -1:
        total = total + grado
        contar += 1
        grado = int(input(mensaje))
    else:
        promedio = total / contar
        print("Promedio de notas del grado escolar: " + str(promedio))
cicloWhileConElse()

def cicloWhileBreak():
    variable = 10

    while variable > 0:
        print('Actual valor de variable:', variable)
        variable = variable - 1
        if variable == 5:
            print ("La variable ha tomado el valor de 5...Fin")
            break
cicloWhileBreak()


def cicloConContinue():
    variable = 10
    while variable > 0:
        variable = variable - 1
        if variable == 5:
            continue
        print('Actual valor de variable:', variable) # no imprime el 5
cicloConContinue()

def cicloControladoPorConfirmacion():
    continuar = 1
    while continuar == 1:
        print ("hola!")
        continuar = int(input("Continua? 1. si / 0. no"))
cicloControladoPorConfirmacion()

def factorialConFor(n:int) -> int:
    factorial = 1
    for i in range (1, n+1):
        factorial = factorial * i
    return factorial
print (factorialConFor(0))
print (factorialConFor(3))