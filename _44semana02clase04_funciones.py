def saludo(cadena):
    return "Hola {}! ¿cómo estas?".format(cadena)

def mostrarMensaje ():
    x = '*'*30
    print (x)
    print (':::¡Bienvenido!:::')
    print ('::Por favor espere su turno::')
    print (x)

def mostrarMensajePersonalizado (nombre):
    x = '*'*30
    print (x)
    print (':::¡Bienvenido!:::')
    #print (':::Hola! '+str(nombre)+':::')
    print (':::Hola! {}:::'.format(nombre))
    print ('::Por favor espere su turno::')
    print (x)

def suma2 (x, y):
    x = float(x)
    y = float(y)
    resultado = x + y
    salida = str(x)+" + "+str(y)+ " es igual a : "+str(resultado)
    return salida 