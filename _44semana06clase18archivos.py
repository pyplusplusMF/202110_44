# Clase del martes 8 de junio
# Tema: archivos

def ejemplo1():
  import pandas as pd
  data = {'first_name': ['Sigrid', 'Joe', 'Theodoric','Kennedy', 'Beatrix', 'Olimpia', 'Grange', 'Sallee'],
        'last_name': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Parlett', 'Guenther', 'Douce', 'Johnstone'],
        'age': [27, 31, 36, 53, 48, 36, 40, 34],
        'amount_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
        'amount_2': [8.06,  "?", 5.90,  "?",  "?", 7.48, 4.37,  "?"]}

  datosDataFrame = pd.DataFrame(data)

  print(datosDataFrame)

  #Acaba la implementacion

  datosDataFrame.to_csv('archivo1.csv')
  datosDataFrame.to_csv('archivo2.csv', sep=';')
ejemplo1()


def ejemplo2():
  import pandas as pd
  dataFrame = pd.read_csv('archivo1.csv')
  print (dataFrame)
ejemplo2()


def ejemplo3():
  import pandas as pd
  # Lectura de un archivo personalizando la cabecera
  df = pd.read_csv('archivo1.csv',
                  skiprows = 1,
                  names=['UID', 'Primer Nombre', 'Apellido', 'Edad', 'Venta #1', 'Venta #2'])
  print (df)
  print(type(df['Venta #2'][2]))
ejemplo3()


def ejemplo4():
  import pandas as  pd
  dataFrame = pd.read_csv('archivo1.csv',
                 skiprows=1,
                 names=['UID', 'Primer Nombre', 'Apellido', 'Edad', 'Venta #1', 'Venta #2'],
                 na_values=['?'],
                 index_col='UID')
  print (dataFrame)
ejemplo4()


def ejemplo1Excel():
  import pandas as pd

  data = {'first_name': ['Sigrid', 'Joe', 'Theodoric','Kennedy', 'Beatrix', 'Olimpia', 'Grange', 'Sallee'],
          'last_name': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Parlett', 'Guenther', 'Douce', 'Johnstone'],
          'age': [27, 31, 36, 53, 48, 36, 40, 34],
          'amount_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
          'amount_2': [8.06,  "?", 5.90,  "?",  "?", 7.48, 4.37,  "?"]}
  print (data)
  df = pd.DataFrame(data, columns = ['first_name', 'last_name', 'age', 'amount_1', 'amount_2'])
  df.to_excel('archivo3.xlsx', sheet_name='ejemplo1')
# ejemplo1Excel()

def ejemplo2Excel():
  import pandas as pd
  dataFrame = pd.read_excel('archivo3.xlsx', sheet_name='ejemplo1')
  print (dataFrame)
# ejemplo2Excel()


def ejemplo1TXT():
  lista = ["Línea 1", "Línea 2", "Línea 3", "Línea 4", "Línea 5"]
  fic = open("archivo4.txt", "w")
  for linea in lista:
      fic.write(linea)
      fic.write("\n")
  fic.close()
ejemplo1TXT()


def ejemplo2TXT():
  lista = ["Línea 1", "Línea 2", "Línea 3", "Línea 4", "Línea 5"]
  fic = open("archivo5.txt", "w")
  fic.writelines("%s\n" % s for s in lista)
  fic.close()
ejemplo2TXT()


def ejemplo3TXT():
  fic = open('archivo5.txt', "r")
  lineas = fic.readlines()
  print (lineas)
  lineas = [s.rstrip('\n') for s in lineas]
  print (lineas)
  fic.close()
ejemplo3TXT()

def ejemplo1JSON():
  import json

  data = {}
  data['clients'] = []

  data['clients'].append({
      'first_name': 'Sigrid',
      'last_name': 'Mannock',
      'age': 27,
      'amount': 7.17})

  data['clients'].append({
      'first_name': 'Joe',
      'last_name': 'Hinners',
      'age': 31,
      'amount': [1.90, 5.50]})

  data['clients'].append({
      'first_name': 'Theodoric',
      'last_name': 'Rivers',
      'age': 36,
      'amount': 1.11})

  with open('archivo6.json', 'w') as file:
      json.dump(data, file, indent=4)
ejemplo1JSON()

def ejemplo2JSON():
  import json
  with open('archivo6.json') as file:
    data = json.load(file)

    for client in data['clients']:
        print('First name:', client['first_name'])
        print('Last name:', client['last_name'])
        print('Age:', client['age'])
        print('Amount:', client['amount'])
        print('')
ejemplo2JSON()

def ejemplo3JSON():
  import json
  import requests

  resp = requests.get('http://ip-api.com/json/208.80.152.201')
  json.loads(resp.content)
ejemplo3JSON()


