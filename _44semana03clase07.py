def teoriaDiccionarios():
    #crear diccionarios
    #1. llaves vacias
    diccionario =  { }
    diccionario2 = dict()
    diccionario3 = dict(total= 55, descuento= True, subtotal= 15)
    
    print(diccionario)
    print(diccionario2)
    print(diccionario3)
    
    usuario = {
        'nombre': 'Nombre del usuario',
        'edad' : 23, 
        'curso': 'Curso de Python',
        'skills':{
                'programacion' : True,
                'base_de_datos': False
                },
        'No medallas' : 10
        }
    print(usuario)
    print(usuario['curso']) #Curso de Python
    print(usuario['skills']) #{'programacion': True, 'base_de_datos': False}
    print(usuario['skills']['base_de_datos']) #False

    diccionario = dict()
    print(diccionario)

    diccionario['marca'] = 'Mazda'
    print (diccionario)
    print(diccionario['marca']) #Mazda

    diccionario['marca'] = 'Subaru'
    print(diccionario['marca']) #Subaru

    print(diccionario)
    
    diccionario = {'Eduardo': 1, 'Fernando':2, 'Uriel':3, 'Rafael': 4}
    print(diccionario)
    print ("Claves", diccionario.keys())
    print ("Valores", diccionario.values())
    
    diccionario = {
     "clave1":234,
     "clave2":True,
     "clave3":"Valor 1",
    }
    print(diccionario)
    print (diccionario["clave1"])
    print (diccionario["clave2"])
    print (diccionario["clave3"])
    #print (diccionario["clave4"]) # KeyError
        
    versiones = dict(python=2.7, zope=2.13, plone=5.1, django=2.1)
    print (versiones)
    print (versiones['zope'])
    
    

    secuencia = ('python', 'zope', 'plone')
    versiones = dict.fromkeys(secuencia)
    print("Nuevo Diccionario : %s" %  str(versiones))
    print("Nuevo Diccionario : {}".format(str(versiones)))
    
    secuencia = ('python', 'zope', 'plone')
    versiones = dict.fromkeys(secuencia, 0.1)
    print("Nuevo Diccionario : %s" %  str(versiones))
    
    versiones = dict(python=2.7, zope=2.13, plone=5.1)
    print ("versiones", versiones)
    print (versiones.get('plone'))
    
    print(versiones.get('php'))
    
    versiones = dict(python=2.7, zope=2.13, plone=5.1)
    print ("versiones", versiones)
    print (versiones.items())
    #print (versiones.pop ('s.o')) KeyError
    
    versiones = dict(python=2.7, zope=2.13, plone=5.1)
    print(versiones)
    versiones_adicional = dict(django=2.1)
    print(versiones_adicional)
    
    versiones.update(versiones_adicional)
    print(versiones)
    
    versiones_adicional = dict(python = 3.9)
    versiones.update(versiones_adicional)
    print (versiones)
    
        
    usuario = {
        'nombre': 'Nombre del usuario',
        'edad' : 23, 
        'curso': 'Curso de Python',
        'skills':{
            'programacion' : True,
            'base_de_datos': False
        },
        'No medallas' : 10
    }
    print("La cantidad de llaves de primer nivel son: ", len(usuario))
    print ("La cantidad de llaves de segundo nivel de la clave skills son: ", len(usuario['skills']))
    
    versiones = dict(python=2.7, zope=2.13, plone=5.1, django=2.1)
    print(versiones)
    del versiones["python"] #{'zope': 2.13, 'plone': 5.1, 'django': 2.1}
    print(versiones)
    #del versiones["Java"] #KeyError
    
    Estudiantes = {  'Alumno1': {'nombre':'Daniel', 'edad':11, 'estatura':1.75, 'grado':'Master'},
                    'Alumno2':{'nombre':'Valentina', 'edad':32, 'estatura':1.85, 'grado':'Doctor'}   }

    print (Estudiantes ['Alumno1']['nombre'])
    print (Estudiantes ['Alumno2']['nombre'])
    if Estudiantes['Alumno1']['nombre'] == Estudiantes['Alumno2']['nombre']:
        print("Los nombres son iguales")
    else:
        print('Los nombres son diferentes')

    Informacion = {  'Alumno1': {'nombre':'Daniel', 'edad':11, 'estatura':1.75, 'grado':'Master'},
                    'Alumno2':{'nombre':'Valentina', 'edad':32, 'estatura':1.85, 'grado':'Doctor'}   }

    if Informacion['Alumno1']['edad'] > Informacion['Alumno2']['edad']:
        
        print(str(Informacion['Alumno1']['nombre']) + ' es mayor') 
        mayor = {'nombremayor':Informacion['Alumno1']['nombre'], 'edadmayor':Informacion['Alumno1']['edad'] }
        
    elif Informacion['Alumno1']['edad'] < Informacion['Alumno2']['edad']:
        
        print(str(Informacion['Alumno1']['nombre']) + ' es menor') 
        
        mayor = {'nombremayor':Informacion['Alumno2']['nombre'], 'edadmayor':Informacion['Alumno2']['edad'] }
    
    print ("Diccionario mayor", mayor)    
teoriaDiccionarios()
    
    