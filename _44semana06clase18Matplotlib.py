# clase martes 8 de junio

import matplotlib.pyplot as plt

def ejemplo1():
  # grupo A
  x1=[2,5,6,14] 
  y1= [11,22,33,44]

  # grupo B
  x2=[2,5,6,15]
  y2=[4,12,18,45]

  #Graficar 2 lineas en la misma grid
  plt.plot(x1,y1, color="blue", linewidth = 3, label = 'Linea 1')
  plt.plot(x2,y2, color="green", linewidth = 3, label = 'Linea 2')

  plt.title('Dos Graficas juntas')
  plt.xlabel('Eje X')
  plt.ylabel('Eje Y')
  plt.legend()
  plt.grid()
  plt.show()

# ejemplo1()

def ejemplo2():
  # grupo A
  x1=[2,5,6,14] 
  y1= [11,22,33,44]

  # grupo B
  x2=[2,5,6,15]
  y2=[4,12,18,45]

  #Grafico de barras. Cuando coinciden la misma X, las apila
  plt.bar(x1,y1, color="blue", linewidth = 3, label = 'Barra 1')
  plt.bar(x2,y2, color="green", linewidth = 3, label = 'Barra 2')

  plt.title('Dos Barras juntas')
  plt.xlabel('Eje X')
  plt.ylabel('Eje Y')
  plt.legend()
  plt.grid()
  plt.show()
# ejemplo2()


# Histograma
def ejemplo3():
  #Histogramas
  Datos = [20,22,21,20,23,25,28,40,22,23,22,15,16,18,18,19,21,22,24,4,12,17,17,22,30,]
  Rangobin=[0,10,20,30,40]
  plt.hist(Datos, Rangobin, histtype='bar',rwidth=0.8, color='lightgreen')

  plt.title('Histograma')
  plt.xlabel('Eje X')
  plt.ylabel('Eje Y')
  #plt.grid()  #la grid no es necesaria (lineas horizontales y verticales)
  plt.show()
# ejemplo3()


def ejemplo4():
  # grupo A
  x1=[2,5,6,14] 
  y1= [11,22,33,44]

  #Scatter
  plt.scatter(x1,y1, color="red",  label = 'Puntos 1')

  plt.title('Dos Graficas juntas')
  plt.xlabel('Eje X')
  plt.ylabel('Eje Y')
  plt.legend()
  plt.grid()
  plt.show()
# ejemplo4()

# https://matplotlib.org/stable/gallery/color/named_colors.html


def ejemplo5():
  #Pie
  valores =[20,40,60,80]

  plt.pie(valores, labels=['Prekinder', 'kinder', 'primaria', 'secundaria'], colors=['red','purple','blue','orange']
          , startangle=90,shadow=True, explode=(0.1,0,0,0),autopct='%1.1f%%')
  plt.title('Grafico circular')
  plt.show()
# ejemplo5()

def ejemplo6():
  # Carga dataset del Titanic
  import pandas as pd 
  df = pd.read_csv('titanic3.csv')
  cantidades=df.survived.value_counts()
  plt.figure(figsize=(30,20))  #tamaño en pixeles? pulgadas? o una proporción?

  plt.subplot2grid((2,2),(0,0))
  plt.subplot2grid((2,2),(1,0))
  plt.subplot2grid((2,2),(0,1))
  plt.subplot2grid((2,2),(1,1))


  print(cantidades[0],cantidades[1])
  plt.figure(figsize=(30,20))  #tamaño en pixeles? pulgadas? o una proporción?

  plt.subplot2grid((2,2),(0,0))  #Grid de 2x2. primer grafico en la posicion (0,0)
  df.survived.value_counts().plot(kind='bar', alpha=0.5)  #seriexxxx.plot()
  plt.title('Sobrevivieron - Cantidad')

  plt.subplot2grid((2,2),(0,1))
  df.survived.value_counts(normalize=True).plot(kind='bar', alpha=0.5)
  plt.title('Sobrevivieron- Porcentaje')

  plt.subplot2grid((2,2),(1,0))
  df.survived.value_counts().plot(kind='bar', alpha=0.5)
  plt.title('Sobrevivieron - Cantidad')

  plt.subplot2grid((2,2),(1,1))
  plt.bar(cantidades[0],cantidades[1], color="blue", alpha=0.5, linewidth = 3, label = 'Barra 1')

  plt.title('Dos Barras juntas')
  plt.xlabel('Eje X')
  plt.ylabel('Eje Y')
  plt.legend()
  plt.grid()
ejemplo6()