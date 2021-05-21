def listasParalelas():
    nombres = ['Juan', 'Ana', 'Marcos','Pablo', 'Laura']
    edades = [12,21,27,14,27]
    n = len (nombres)
    print ('{:<6}{:>15}'.format('nombres', 'edades'))
    for i in range (n):
        print ('{:<6}{:>15}'.format(nombres[i], edades[i]))
    listaDeMayores = []
    for i in range (n):
        if (edades[i] >=18):
            listaDeMayores.append(nombres[i])
    print ('La lista de las personas que son >= 18 son: ', listaDeMayores)
    #Obtener el listado de las personas que tienen la mayor edad
    mayor = max (edades)
    print ('La edad mayor es: ', mayor)
    listaDePersonasConMayorEdad = []
    for i in range (n):
        if (edades[i] == mayor):
            listaDePersonasConMayorEdad.append(nombres[i])
    print ('Las personas que tienen la edad mayor ', mayor, ' años son: ', listaDePersonasConMayorEdad)
listasParalelas()

def listasDeListas():
    lista = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    #print (lista[0]) # [1, 2, 3]
    #print (lista[1]) # [4,5,6]
    #print (lista[2]) # [7,8,9]
    #print (lista[3]) # [10,11,12]
    #print (lista[0][0]) # 1
    #print (lista[1][2]) # 6
    
    for i in range (len(lista)):#For externo
        for j in range (len(lista[i])): #For interno
                print ('{:^5}'.format(lista[i][j]), end = ' ')
        print ('')
    
    suma = 0
    for i in range (len(lista)): #For externo
        suma = 0
        for j in range (len(lista[i])): #For interno
            suma = suma + lista[i][j]
        print ('La suma de la sublista ', i, ' es: ', suma)
    
    tablero = [ ['B' for j in range (4)] for i in range (4)]
    print (tablero)
    for i in range(len(tablero)):
        for j in range (len(tablero[i])):
            print ('{:^2}'.format(tablero[i][j]), end = ' ')
        print (' ')
            
listasDeListas()   

def listaDeListasParte2():
    lista = [[1],[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5]]
    #1. Sumatoria de toda la lista
    #2. Sumar todas las sublistas y guardarla en una lista nueva
    
    sumatoriaTotal = 0
    listaSumatoria = [0 for i in range (len(lista))] # [ 0 , 0 , 0 , 0, 0 ]
    for i in range (len(lista)): #Ciclo for Externo
        for j in range (len(lista[i])): #Ciclo for interno
            listaSumatoria [i] += lista[i][j]
            sumatoriaTotal +=  lista[i][j]
    print ('1. La sumatoria de toda la lista es: ', sumatoriaTotal)
    print ('2. La suma de cada sublista es: ', listaSumatoria)
listaDeListasParte2()


def listaDeListasParte3():
    lista = [[1],[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5]]
    #1. Sumatoria de toda la lista
    #2. Sumar todas las sublistas y guardarla en una lista nueva
    sumatoriaTotal = 0
    listaSumatoria = []

    for i in range (len(lista)):
        sumatoriaTotal += sum(lista[i])
        listaSumatoria.append(sum(lista[i]))
        
    print ('1. La sumatoria de toda la lista es: ', sumatoriaTotal)
    print ('2. La suma de cada sublista es: ', listaSumatoria)
listaDeListasParte3()



def ejercicioDeListasParalelas():
    listaNombres = [['Juan','Ana'], ['Carlos','Maria'], ['Pedro','Laura']]  
    listaHijos = [['Marcos','Alberto','Silvia'],[],['Oscar']]
    #1. Imprimir el nombre del padre y el nombre de la madre con sus respectivos hijos
    #2. Imprimir el nombre del padre con la cantidad de hijos
    
    for i in range (len (listaNombres)):
        print ('Nombre del padre: ', listaNombres[i][0], end = ' - ')
        print ('Nombre de la madre: ', listaNombres[i][1])
        for j in range (len(listaHijos[i])):
            print ('Hijo ', j+1, ': ',listaHijos[i][j], end = ' ')
        print (' ')
ejercicioDeListasParalelas()

def teoriaTuplas():
  t1 = ('a', 'b', 'c', 'd', 'e')
  t = ('A',) + t1[1:] + ('GATO',)
  print ("t1 = ", t1)
  print ("t  = ", t)
teoriaTuplas()


def teoriaTuplas2():
    texto = "but soft what light in yonder window breaks"
    listaPalabras = texto.split()
    print (listaPalabras)
    listaNueva = list()
    for subcadena in listaPalabras:
        listaNueva.append((len(subcadena), subcadena))
    print(listaNueva)
    listaNueva.sort(reverse=True)
    print (listaNueva) #[(6, 'yonder'), (6, 'window'), (6, 'breaks'), (5, 'light'), (4, 'what'), (4, 'soft'), (3, 'but'), (2, 'in')]
    
    listaRespuesta = list()
    for longitud, palabra in listaNueva:
        listaRespuesta.append(palabra)
    print(listaRespuesta)
    #['yonder', 'window', 'breaks', 'light', 'what', 'soft', 'but', 'in']
    
teoriaTuplas2()


def ejemploTuplas():

  addr = 'monty@python.org'
  uname, domain = addr.split('@')
  print(uname)
  print(domain)
  
ejemploTuplas()