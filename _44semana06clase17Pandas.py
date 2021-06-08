# Sesión del dia lunes 7 de junio

# Configurar Pandas

# 1. Abrir Simbolo de sistema como administrador
# 2. y luego escribir: 

# pip install pandas
# pip install matplotlib

# py -m pip install pandas

# https://pandas.pydata.org/pandas-docs/stable/reference/series.html

import pandas as pd

serie = pd.Series( [51,32,45,0.5,6.5,19.5,9.5,17,7,3.5,11.5,28.5,126,212,0.4] ) # Millones de habitantes 0.4 = 400k
# print (serie)

# A continuación vemos como es el indice de la serie
# lista = (serie.index)
# print (lista) 


serie.index =['Colombia', 'Perú', 'Argentina', 'Surinam', 'Nicaragua', 'Chile', 
              'Honduras', 'Guatemala', 'Paraguay', 'Uruguay', 'Bolivia', 
              'Venezuela', 'México', 'Brasil', 'Belize']
# print ('La serie es :')
# print (serie)

serie.name = 'Poblacion'
print ('La serie es :')
print (serie)


print ('La población de Colombia es: ')
print (serie ['Colombia'])

print ('La población de Brasil es: ')
print (serie ['Brasil'])

print ('La población de México y Brasil')
print (serie [ ['México', 'Brasil'] ])


print ('media ', serie.mean())
print ('mediana ', serie.median())
print ('desv estándar ', serie.std())
print ('maximo ', serie.max())
print ('minimo ', serie.min())

print ('Describe : ')
print (serie.describe())



dataFrame = pd.DataFrame ( {'Población': [51,32,45,0.5,6.5,19.5,9.5,17,7,3.5,11.5,
                             28.5,126,212, 0.4],
                           'Idioma':['Español', 'Español','Español','Neerlandés',
                                     'Español','Español','Español','Español',
                                     'Español','Español','Español','Español',
                                     'Español','Portugués','Inglés']
                           },
                           index = ['Colombia', 'Perú', 'Argentina', 'Surinam', 'Nicaragua', 'Chile', 
                                    'Honduras', 'Guatemala', 'Paraguay', 'Uruguay', 'Bolivia', 
                                    'Venezuela', 'México', 'Brasil', 'Belize']
                          )
print ('DataFrame a partir de una estructura tipo dict')
print (dataFrame)

print ('Los datos de la columna población son: ')
print ( dataFrame ['Población'] )

print ('Los datos de la columna idiomas son: ')
print ( dataFrame ['Idioma'])

print ('Los datos correspondientes a Mexico son: ')
print (dataFrame.loc['México'])

print ('Los datos correspondientes a Uruguay y Paraguay son: ')
print (dataFrame.loc[ ['Uruguay', 'Paraguay'] ])

print ('La población de México y de colombia son: ')
                       # los paises           # serie
print (dataFrame.loc[['México', 'Colombia'],'Población'] )


print ('Calculo de la media: ')
print ( dataFrame.mean() )

print ('Informacion compelta del DataFrame: ')
print (dataFrame.info())



