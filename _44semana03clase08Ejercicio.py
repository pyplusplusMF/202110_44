  def evaluacionNota2 (diccionario:dict) -> dict:
    n1 = float(diccionario['nota1'])
    n2 = float(diccionario['nota2'])
    n3 = float(diccionario['nota3'])
    
    notaInvalida = n1 < 0.0 or n2 <0.0 or n3 <0.0 or n1 >5.0 or n2 >5.0 or n3 >5.0
    
    salida = ""
    if (notaInvalida):
        salida = "Notas Invalidas"
        promedio = -1
    else:
        promedio = round ( ((sum(diccionario.values())) / len(diccionario)) , 3)
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

diccionario4 = {'nota1':1.8858, 'nota2':1.88854, 'nota3':1.8868}  
print (evaluacionNota2(diccionario4))