'''
Desarrollar una función que reciba como parámetro un diccionario de resultados
de partidos de futbol y devuelva el nombre de los paises participantes en una lista
'''
def ejemplo1(diccionario:dict)->list:
    
    conjuntoPaises = set()
    for clave, valor in diccionario.items():
        #print (clave[0], '[', valor[0], '] - [', valor[1], ']', clave[1])
        conjuntoPaises.add (clave[0])
        conjuntoPaises.add (clave[1])
    
    
    listaPaises = list(conjuntoPaises)
    
    return listaPaises


resultados = {
        ('Honduras', 'Chile'): (1, 1),
        ('Espana', 'Suiza'): (0, 1),
        ('Suiza', 'Chile'): (0, 0),
        ('Espana', 'Honduras'): (2, 0),
        ('Suiza', 'Honduras'): (1, 0),
        ('Espana', 'Chile'): (2, 1),
}

print (ejemplo1(resultados))