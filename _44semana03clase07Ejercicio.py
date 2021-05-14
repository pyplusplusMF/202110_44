'''
Hacer un programa que pida al usuario las tres notas de un alumno (deben estar entre 0 y
5 y pueden tener decimales) y calcule el promedio e indique mediante un mensaje si aprobó
o no (aprueba con nota mayor a 3). Se debe validar que las notas introducidas estén dentro
del rango permitido
'''
#diccionario = {'nota1': 3.2, 'nota2': 5.0, 'nota3':2.8}
def evaluacionNota (diccionario:dict) -> str:
    n1 = float(diccionario['nota1'])
    n2 = float(diccionario['nota2'])
    n3 = float(diccionario['nota3'])
    
    notaInvalida = n1 < 0.0 or n2 <0.0 or n3 <0.0 or n1 >5.0 or n2 >5.0 or n3 >5.0
    salida = ""
    if (notaInvalida == True):
        salida = "Notas Invalidas"
    else:
        promedio = (n1 + n2 + n3) / 3
        promedio = round (promedio, 3)
        if (promedio >= 3.0):
            salida = "Aprobado"
        else:
            salida = "Reprobado"    
    return salida

diccionario1 = {'nota1':3.0, 'nota2':4.5, 'nota3':4.5} 
print (evaluacionNota(diccionario1))

diccionario2 = {'nota1':-3.0, 'nota2':4.5, 'nota3':4.5}  
print (evaluacionNota(diccionario2))

diccionario3 = {'nota1':30, 'nota2':4.5, 'nota3':4.5}  
print (evaluacionNota(diccionario3))

diccionario4 = {'nota1':1.8, 'nota2':1.8, 'nota3':1.8}  
print (evaluacionNota(diccionario4))


def evaluacionNota2 (diccionario:dict) -> dict:
    n1 = float(diccionario['nota1'])
    n2 = float(diccionario['nota2'])
    n3 = float(diccionario['nota3'])
    
    notaInvalida = n1 < 0.0 or n2 <0.0 or n3 <0.0 or n1 >5.0 or n2 >5.0 or n3 >5.0
    salida = ""
    if (notaInvalida == True):
        salida = "Notas Invalidas"
        promedio = -1
    else:
        promedio = (n1 + n2 + n3) / 3
        promedio = round (promedio, 3)
        if (promedio >= 3.0):
            salida = "Aprobado"
        else:
            salida = "Reprobado"    
    
    diccionarioSalida = dict()
    diccionarioSalida ['prom'] = promedio
    diccionarioSalida ['resultado'] = salida
    
    return diccionarioSalida

diccionario1 = {'nota1':3.0, 'nota2':4.5, 'nota3':4.5} 
print (evaluacionNota2(diccionario1))

diccionario2 = {'nota1':-3.0, 'nota2':4.5, 'nota3':4.5}  
print (evaluacionNota2(diccionario2))

diccionario3 = {'nota1':30, 'nota2':4.5, 'nota3':4.5}  
print (evaluacionNota2(diccionario3))

diccionario4 = {'nota1':1.8, 'nota2':1.8, 'nota3':1.8}  
print (evaluacionNota2(diccionario4))