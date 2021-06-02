# Clase del martes 1 de Junio
# Map. Filter y Reduce

def ejercicio1MapParte1():
    # Transformar todos los elementos a su cuadrado
    lista = [1,2,3,4,5,6,7,8,9,10]
    print ('lista original ', lista)
    for i in range (len(lista)):
        lista [i] = lista[i] * lista[i]
    print ('lista transformada ', lista)
ejercicio1MapParte1()


def ejercicio1MapParte2():
    
    def transformarLista (lista:list)-> list:
        for i in range (len(lista)):
            lista[i] = lista[i] * lista[i]
        return lista
    
    lista = [1,2,3,4,5,6,7,8,9,10]
    print ('lista original = ', lista)
    print ('lista transformada = ', transformarLista(lista))
    
ejercicio1MapParte2()


def ejercicio1MapParte3():
    # Aqui usamosMap y una funcion que transforma cada elemento
    def transformarElemento (elemento:int) -> int:
        return elemento * elemento
    
    lista = [1,2,3,4,5,6,7,8,9,10]
    print ('lista original = ', lista)
    lista = list (map (transformarElemento,lista ))
    print ('lista transformada = ', lista)

ejercicio1MapParte3()

def ejercicio1MapParte4():
    # Aqui vamos a usar map y lambda
    # def transformarElemento (elemento:int) -> int:
    #     return elemento * elemento
    lista = [1,2,3,4,5,6,7,8,9,10]
    print ('lista original = ', lista)
    lista =  list (map(lambda elemento: elemento * elemento , lista))
    print ('lista transformada = ', lista)

ejercicio1MapParte4()


def ejercicio1ConPow():
    # Aqui map recibe dos listas
    lista =    [1,2,3]
    potencia = [3,2,4]
    
    potencias = list ( map ( pow, lista, potencia ) )
    print ('las potencias son = ', potencias )
    # las potencias son =  [1, 4, 81]
ejercicio1ConPow()

def ejercicio1Filter():
    # De forma imperativa
    tupla = (0,10,0,50,6,-1,7,10,6,20,1,0)
    # Crearemos una nueva tupla con los elementos que son mayores a 5
    lista = []
    for i in range (len(tupla)):
        if (tupla[i] > 5):
            lista.append(tupla[i])
    lista = tuple(lista) #se transformó a una tupla
    print ('Resultado con los elementos filtrados = ', lista)
ejercicio1Filter()

def ejercicio2Filter ():
    
    def filtrar (elemento:int) -> bool:
        return elemento > 5

    tupla = (0,10,0,50,6,-1,7,10,6,20,1,0)
    # Crearemos una nueva tupla con los elementos que son mayores a 5
    tuplaFiltrada = tuple (filter (filtrar, tupla))
    print ('Resultado con los elementos filtrados = ', tuplaFiltrada)
    # (10, 50, 6, 7, 10, 6, 20)
ejercicio2Filter()


def ejercicio3Filter():
    
    tupla = (0,10,0,50,6,-1,7,10,6,20,1,0)
    # Crearemos una nueva tupla con los elementos que son mayores a 5
    # lambda argumentos_de_la_funcion : cuerpo_de_la_funcion
    # filter (funcion_que_se_aplica , objeto Iterable)
    
    tuplaFiltrada = tuple (filter(lambda elemento: elemento > 5 , tupla))
    print ('Resultado con los elementos filtrados = ', tuplaFiltrada)
    # (10, 50, 6, 7, 10, 6, 20)
ejercicio3Filter()

def ejercicio1FilterPares():
    # Dada una lista de números, vamos a filtrar todos los elementos que son pares
    lista = [10,4,5,10,6,8,10,9,3,7,19,21,63]
    listaFiltrada = []
    for i in range (len(lista)):
        if (lista[i] % 2 == 0):
            listaFiltrada.append (lista[i])
    print ('los elementos pares son: ', listaFiltrada)
    # [10, 4, 10, 6, 8, 10]
# ejercicio1FilterPares()

def ejercicio2FilterPares():
    # Dada una lista de números, vamos a filtrar todos los elementos que son pares
    lista = [10,4,5,10,6,8,10,9,3,7,19,21,63]
    
    def filtrarPares (elemento:int) -> bool:
        return elemento % 2 == 0
    
    listaFiltrada = list (filter (filtrarPares,lista))
    print ('los elementos pares son: ', listaFiltrada)
    # [10, 4, 10, 6, 8, 10]
ejercicio2FilterPares()


def ejercicio3FilterPares():
    # Dada una lista de números, vamos a filtrar todos los elementos que son pares
    lista = [10,4,5,10,6,8,10,9,3,7,19,21,63]
    # def filtrarPares (elemento:int) -> bool:
    #     return elemento % 2 == 0
    listaFiltrada = list (filter (lambda  elemento : elemento % 2 == 0  , lista))
    print ('los elementos pares son: ', listaFiltrada)
    # [10, 4, 10, 6, 8, 10]
ejercicio3FilterPares()


def ejercicio1Reduce():
    # sumar todos los elementos de una lista
    lista = [10,4,5,10,6,8,10,9,3,7,19,21,63]
    sumatoria = 0
    for elemento in lista:
        sumatoria = sumatoria + elemento
    print ('sumatoria = ', sumatoria) # 175
ejercicio1Reduce()


def ejercicio2Reduce ():
    
    def sumaLista (lista:list) -> int:
        sumatoria = 0
        for elemento in lista:
            sumatoria = sumatoria + elemento
        return sumatoria
    
    # sumar todos los elementos de una lista
    lista = [10,4,5,10,6,8,10,9,3,7,19,21,63]
    print ('sumatoria = ', sumaLista(lista)) # 175
# ejercicio2Reduce()

def ejercicio3Reduce():
    from functools import reduce
    
    def sumaLista (sumatoria = 0, elemento = 0):
        return sumatoria + elemento

    # sumar todos los elementos de una lista
    lista = [10,4,5,10,6,8,10,9,3,7,19,21,63]
    
    resultado = reduce (sumaLista, lista)
    print ('sumatoria = ', resultado) # 175
# ejercicio3Reduce()

def ejercicio4Reduce():
    from functools import reduce
    # def sumaLista (sumatoria = 0, elemento = 0):
    #     return sumatoria + elemento
    
    # sumar todos los elementos de una lista
    lista = [10,4,5,10,6,8,10,9,3,7,19,21,63]
    resultado = reduce (lambda sumatoria = 0, elemento = 0 : sumatoria + elemento , lista)
    print ('sumatoria = ', resultado) # 175
ejercicio4Reduce()


def ejercicio1ReduceStrings():
    
    # Concatenar todos los elementos de una lista
    lista = ['Python', 'Java', 'PHP', 'Ruby', 'Perl', 'Kotlin']
    concatenacion = ' '.join(lista)
    print ('concatenacion ', concatenacion)
    # Python Java PHP Ruby Perl Kotlin 
    
    sumatoriaStrings = ' '
    for elemento in lista:
        sumatoriaStrings = sumatoriaStrings + ' ' + elemento
    print('sumatoriaStrings = ', sumatoriaStrings)
    # Python Java PHP Ruby Perl Kotlin
    
ejercicio1ReduceStrings()

def ejercicio2ReduceStrings():
    from functools import reduce
    def concatenacion (sumatoriaStrings = ' ', elemento = ' ') -> str:
        return sumatoriaStrings + ' ' + elemento 
    
    # Concatenar todos los elementos de una lista
    lista = ['Python', 'Java', 'PHP', 'Ruby', 'Perl', 'Kotlin']
    
    stringConcatenado = reduce (concatenacion, lista)
    print ('Los elementos concatenados son: ', stringConcatenado)
    # Python Java PHP Ruby Perl Kotlin
ejercicio2ReduceStrings()


def ejercicio3ReduceStrings():
    from functools import reduce
    # def concatenacion (sumatoriaStrings = ' ', elemento = ' ') -> str:
    #     return sumatoriaStrings + ' ' + elemento     
    
    # Concatenar todos los elementos de una lista
    lista = ['Python', 'Java', 'PHP', 'Ruby', 'Perl', 'Kotlin']
    stringConcatenado = reduce ( 
                                lambda  sumatoriaStrings = ' ', elemento = ' ' :  sumatoriaStrings + ' ' + elemento, 
                                lista )
    print ('Los elementos concatenados son: ', stringConcatenado)
    # Python Java PHP Ruby Perl Kotlin
ejercicio3ReduceStrings()