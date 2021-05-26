###ORDENAMIENTO BURBUJA
#https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif

'''
Se dispone de un diccionario de vinos donde las claves son nombres de vinos y los valores para cada vino 
son una lista con la información de su denominación de origen, la añada y su precio.
Diseñar una función lista_vinos (diccionario:dict, listaRango:list) -> list en que, 
dado un diccionario de vinos como el descrito y una lista con un rango de precios [menorPrecio, mayorPrecio], 
nos devuelva una lista de los nombres, ordenados alfabéticamente de los vinos 
que estén en este rango de precios.
'''

def lista_vinos (diccionario:dict, listaRango:list) -> list:
    
    '''for clave, valor in diccionario.items():
        print (clave, '-', valor[0], '-',valor[1], '-', valor[2])'''
        
    listaResultado = list()
    for clave, valor in diccionario.items ():
        if (valor[2] >= listaRango[0]  and valor[2] <= listaRango[1]):
            listaResultado.append(clave)
    listaResultado.sort()
    
    return listaResultado

'''
Imprimir una lista de los vinos en orden de añada
'''
def lista_vinos_anada (diccionario:dict) ->list:
    listaNombres = list()
    listaAnada = list()
    
    for clave, valor in diccionario.items():
        listaNombres.append(clave)
        listaAnada.append(valor[1])
    
    #print (listaNombres)
    #print (listaAnada)
    for i in range (len(listaNombres)):
        for j in range (len(listaNombres) - 1):
            if (listaAnada[j] > listaAnada[j+1]):
                
                aux = listaAnada[j]
                listaAnada[j] = listaAnada[j+1]
                listaAnada[j+1] = aux
                
                aux2 = listaNombres[j]
                listaNombres[j] = listaNombres[j+1]
                listaNombres[j+1] = aux2
    #print(listaAnada)
    #print(listaNombres)
    
    cantidadDeVinos = len(listaNombres)
    listaDeListas = [[None for y in range (2)] for x in range (cantidadDeVinos)]
    for i in range (cantidadDeVinos):
        listaDeListas[i][0] = listaNombres[i]
        listaDeListas[i][1] = listaAnada [i]
    #print (listaDeListas)
    return listaDeListas


'''
Esta funcion armará un diccionario nuevo cuyas claves serán las dos funciones anteriores
'''
def funcionNueva (diccionario:dict, listaRango:list) -> dict:
    diccionarioSalida = dict()
    diccionarioSalida ['vinoPorRango'] = lista_vinos(diccionario, listaRango)
    diccionarioSalida['vinosOrdenadosPorAnada'] = lista_vinos_anada(diccionario)
    return diccionarioSalida

    


diccionario = {'Tinto': ['las moras',2012,49900],
               'Blanco': ['Mar de Frades',2014, 89900],
               'Rosado': ['Cavernet Saugvinon',2016,69900], 
               'Espumoso': ['Rivarose Rosado',2011,74900],
               'Tinto dulce': ['Amarone',2015, 45000], 
               'Champagne': ['Veuve Clicquot', 2016,340400]
               }
lista = [50000, 80000]



print (lista_vinos(diccionario, lista ))
print (lista_vinos_anada(diccionario))

print (funcionNueva (diccionario, lista))