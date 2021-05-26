def ejercicioEjemploListas ():
    itinerario = [['Santa Marta', 1],
                ['Cartagena', 2],
                ['San Andrés', 4],
                ]

    print ('itinerario original:' , itinerario)


    nombreDestino = str(input('¿Cual es el nombre del destino que desea añadir?: '))
    cantidadDias = int (input ('¿Cuantos dias?: '))
    listaDestinoNuevo = [nombreDestino, cantidadDias]
    itinerario.append (listaDestinoNuevo)
    print ('Asi va su itinerario: ', itinerario)

    nombreDestinoEliminar = str(input('¿Cual es el destino que usted va a eliminar? '))
    posicion = 0
    for i in range (len(itinerario)):
        if (nombreDestinoEliminar == itinerario[i][0]):
            posicion = i
    itinerario.pop (posicion)
    print ('Asi va su itinerario: ', itinerario)


    nombreDestino = str(input('¿Cual es el nombre del destino donde sea añadir dias?: '))
    cantidadDias = int (input ('¿Cuantos dias?: '))
    for i in range (len(itinerario)):
        if (nombreDestino == itinerario[i][0]):
            itinerario [i][1] += cantidadDias

    print ('Asi va su itinerario: ', itinerario)

    '''itinerario [0][1] += 1
    print (itinerario)'''

    print ('Aqui se intercambiaron las posiciones de la lista')
    itinerario[0], itinerario[-1] = itinerario[-1], itinerario[0]
    print ('Asi quedó su itinerario: ', itinerario)
    
ejercicioEjemploListas ()