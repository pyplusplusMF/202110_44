# Clase del dia jueves 10 de junio
# definición de una clase llamada circulo
# calcularemos el área y el perimetro
import math
class Circulo:
    # constructor
    def __init__ (self, radio = 1):
        self.radio = radio # atributo radio
    
    # Metodos
    # Establecer un radio
    def setRadio (self, radio):
        self.radio = radio
    # Obtener el area del circulo
    def getArea (self):
        a = math.pi * (self.radio * self.radio)
        return a
    # Obtener el perimetro del circulo
    def getPerimetro (self):
        p = 2 * math.pi * self.radio
        return p

circuloA = Circulo()
print ('radio = ', circuloA.radio)
print ('perimetro = ', circuloA.getPerimetro())
print ('area = ', circuloA.getArea())

# radio =  1
# perimetro =  6.283185307179586
# area =  3.141592653589793   

circuloB = Circulo(5)
print ('radio = ', circuloB.radio)
print ('perimetro = ', circuloB.getPerimetro())
print ('area = ', circuloB.getArea())

# radio =  5
# perimetro =  31.41592653589793
# area =  78.53981633974483

circuloC = Circulo()
circuloC.setRadio(5)
print ('radio = ', circuloC.radio)
print ('perimetro = ', circuloC.getPerimetro())
print ('area = ', circuloC.getArea())

# radio =  5
# perimetro =  31.41592653589793
# area =  78.53981633974483