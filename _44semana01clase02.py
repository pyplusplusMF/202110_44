'''
Ejercicio 1: Escriba un programa en python para calcular la nota promedio a partir de tres notas leídas.
'''
nota1 = 3.5
nota2 = 4.5
nota3 = 5.0
promedio = (nota1 + nota2 + nota3) / 3
print ("El promedio de las tres notas es: "+str(promedio))

'''
Ejercicio 2: Escriba un programa en python para calcular la nota definitiva de tres notas leídas teniendo en cuenta la siguiente ponderación: La nota 1 vale 30%, la nota 2 vale 20% y la nota tres vale 50%.

'''

nota1 = 5.0
nota2 = 3.8
nota3 = 2.5
nota1 = nota1 * 0.3
nota2 = nota2 * 0.2
nota3 = nota3 * 0.5
notaDefinitiva = nota1 + nota2 + nota3
print ("La nota definitiva es: "+str(notaDefinitiva))


nota1, nota2, nota3 = 5.0, 3.8, 2.5
notaDefinitiva = nota1 *0.3 + nota2 *0.2 + nota3 *0.5
print ("La nota definitiva es: "+str(notaDefinitiva))


'''
Ejercicio 3: Diseñar un algoritmo que lea dos valores reales y nos muestre los resultados de sumar, restar, dividir (el segundo número debe ser diferente de cero) y multiplicar dichos números.
'''
numero1 = 3.5
numero2 = 4.5
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
print("la suma de "+str(numero1)+" con "+str(numero2) + " es igual a "+str(suma))
print (str(numero1) + " + " + str(numero2) + " = "+str(suma))

'''
Ejercicio 4: Leer la temperatura dada en la escala Celsius e imprimir en su equivalente Fahrenheit. La fórmula de conversión es
'''

print("Ingrese el valor de temperatura a convertir")
temp = float(input())
celToF = (temp * (9 / 5) + 32)
print("El resultado es: "+str(celToF)+"ºF")
