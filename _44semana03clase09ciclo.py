def ciclosBreakContinue ():
    continuar = 1
    while True:#while continuar == 1:
        numero = int(input("Ingrese un numero: "))
        if (numero % 2 == 0):
            print ("El numero es par")
            continue
        print ("Si vino a esta linea es porque el numero no fue par")
        
        continuar = int(input("¿Desea continuar? 1. si, 0.no"))
        if (continuar == 0):
            print ("Usted eligio salir")
            break
ciclosBreakContinue()


def ciclosBreakContinue ():
    continuar = 1
    while True:#while continuar == 1:
        numero = int(input("Ingrese un numero: "))
        if (numero % 2 == 0):
            print ("El numero es par")
            continue
        print ("Si vino a esta linea es porque el numero no fue par")
        
        continuar = int(input("¿Desea continuar? 1. si, 0.no"))
        if (continuar == 0):
            print ("Usted eligio salir")
            break
ciclosBreakContinue()


def introduccionFor():
    for x in range(0, 3):
        print("Estamos en la iteración " + str(x))
    
    for j in range(0, 10, 2):
        print("Estamos en la iteración " + str(j))
    '''
    Estamos en la iteración 0
    Estamos en la iteración 2
    Estamos en la iteración 4
    Estamos en la iteración 6
    Estamos en la iteración 8'''   
    for j in range(10, 0, -2):
        print("Estamos en la iteración " + str(j))
    '''
    Estamos en la iteración 10
    Estamos en la iteración 8
    Estamos en la iteración 6
    Estamos en la iteración 4
    Estamos en la iteración 2'''
introduccionFor()

#link de la documentacion de python para el rango 
#https://docs.python.org/es/3/library/stdtypes.html#range
#https://docs.python.org/3/library/functions.html#func-range
#excepciones 
#https://docs.python.org/es/3/library/exceptions.html#ValueError


def cicloForDict():
    frutas = {'Fresa':'roja', 'Limon':'verde', 'Papaya':'naranja', 
              'Manzana':'amarilla', 'Guayaba':'rosa'}
    claves = list (frutas.keys())
    valores = list (frutas.values())
    clavesYvalores = list(frutas.items())
    
    print ("claves", claves)
    print ("valores", valores)
    print ("claves y valores: ", clavesYvalores)
    
    #primer ciclo, recorriendo el diccionario completo
    print ("\nPrimer Ciclo")
    for clave in frutas:
        print ("Clave: ", clave, " Valor: ", frutas[clave])
    
    #segundo ciclo, recorriendo solo las claves mediante keys
    print ("\nSegundo Ciclo")
    for clave in frutas.keys():
        print ("Clave: ", clave, " Valor: ", frutas[clave])
        
    #tercer ciclo, recorriendo solo los valores mediante values
    print ("\nTercer Ciclo")
    for valor in frutas.values():
        print ("Valores: ", valor)
    
    #cuarto ciclo, recorriendo tanto las claves como los valores con items
    print ("\nCuarto Ciclo")
    for clave, valor in frutas.items():
        print ("Clave: ", clave, " Valor: ", valor)
    
cicloForDict()

def cicloForConStr():
    db_connection = "127.0.0.1","5432","root","nomina"

    for parametro in db_connection:
        print(parametro)
    else:
        print(""""El comando PostgreSQL es: 
    $ psql -h {server} -p {port} -U {user} -d {db_name}""".format(
            port=db_connection[1], 
            user=db_connection[2], db_name=db_connection[3], server=db_connection[0]))
cicloForConStr()



