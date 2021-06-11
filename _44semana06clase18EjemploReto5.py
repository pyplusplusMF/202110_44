# Clase del martes 8 de junio
# Ejemplo del Reto 5
# Lectura del archivo titanic3.csv y cargado en un DataFrame
# Ejercicio de ayuda _44semana06clase17EjercicioPandas.py

def funcionEjemplo (nombreArchivo:str) -> dict:
    import pandas as pd
    # archivos
    # 1. Cargar el archivo titanic en un dataframe
    dataFrame = pd.read_csv(nombreArchivo)
    # print (dataFrame)
    # dataFrame.info()
    nombres = dataFrame['name']
    # print ('nombres: ')
    # print (nombres)

    mayorEdad = max ( dataFrame['age'])
    # print ('La edad mayor es: ', mayorEdad, 'años')
    # La edad mayor es:  80.0 años

    menorEdad = min ( dataFrame['age'])
    # print ('La edad menor es: ', menorEdad, 'años')
    # La edad menor es:  0.1667 años

    tarifaPromedio = round ( (dataFrame['fare'].mean()) , 2 )
    # print ('La tarifa promedio es: ', tarifaPromedio, 'usd')
    # La tarifa promedio es:  33.3 usd
    
    diccionario = dict()
    diccionario['nombres'] = list(nombres[:10])
    diccionario['edadMayor'] = mayorEdad
    diccionario['edadMenor'] = menorEdad
    diccionario['tarifaPromedio'] = tarifaPromedio
    
    return diccionario

print (funcionEjemplo ('titanic3.csv'))

# {'nombres': ['Allen, Miss. Elisabeth Walton', 'Allison, Master. Hudson Trevor', 'Allison, Miss. Helen Loraine', 'Allison, Mr. Hudson Joshua Creighton', 'Allison, Mrs. Hudson J C (Bessie Waldo Daniels)', 'Anderson, Mr. Harry', 'Andrews, Miss. Kornelia Theodosia', 'Andrews, Mr. Thomas Jr', 'Appleton, Mrs. Edward Dale (Charlotte Lamson)', 'Artagaveytia, Mr. Ramon'], 'edadMayor': 80.0, 'edadMenor': 0.1667, 'tarifaPromedio': 33.3}


# Trabajo autonomo
# descargar el material 
# https://github.com/luismescobarf/clasesCiclo1/tree/master/AppCRUD_CapaDatos