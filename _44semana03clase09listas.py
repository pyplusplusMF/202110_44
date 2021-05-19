def listas():
    lista = [ ] #crea una lista vacia
    print (lista)
    lista2 = list() #crea una lista vacia
    print (lista2)
#listas()

def listas2():
    print ("\nEjemplo de una lista vacia: ")
    lista = [] #lista vacia, no tiene nada
    n = 4 #cantidad de elementos de la lista
    #el ciclo se repetirá 4 veces
    for i in range (n):
        dato = int(input("Ingrese un dato en la posicion "+str(i)+" : "))
        lista.append(dato) #se añaden los elementos a la lista
    print ("lista = ", lista) 
    
    print ("\nEjemplo de una lista Definida con cer0s ")
    #aqui la lista se definio con cuatro cer0s
    listaDefinida  = [0 for x in range (n)]
    print (listaDefinida)
    for i in range (n):
        dato = int(input("Ingrese un dato en la posicion "+str(i)+" : ")) 
        #en este paso se añaden los elementos en la posicion correspondiente
        listaDefinida [i] = dato #se asigno la variable datos a la lista
    print ("listaDefinida = ", listaDefinida)
    
    print ("\nEjemplo de una lista infinita. Mediante un ciclo controlado por el usuario")
    listaInfinita = []
    i = 0
    while (True):
        #este ciclo esta controlado por el usuario mediante una confirmacion
        dato = int(input("Ingrese un dato en la posicion "+str(i)+" : ")) 
        #la lista va creciendo cuando la persona decida si desea continuar o no
        listaInfinita.append(dato)
        
        continuar = str(input("Continuar? s/n: "))
        #esta es la pregunta de confirmacion si desea seguir o no
        if (continuar == 's'):
            i += 1
            continue
        else:
            print ("Chao")
            break  
    print ("listaInfinita = ", listaInfinita)
listas2()


def listas3():
    preguntas = ['nombre', 'objetivo', 'sistema operativo']
    respuestas = ['Leonardo', 'aprender Python y Plone', 'Linux']

    for pregunta, respuesta in zip(preguntas, respuestas):
        print('¿Cual es tu {0}?, la respuesta es: {1}.'.format(
            pregunta, respuesta))
    
    
    preguntas = ['nombre', 'objetivo', 'sistema operativo']
    respuestas = ['Leonardo', 'aprender Python y Plone', 'Linux']

    for i in range (len(preguntas)):
        print ("¿Cual es tu ",preguntas [i], ", la respuesta es ",respuestas[i] )
        
listas3()