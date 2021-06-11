# Clase del dia jueves 10 de junio
# definición de una clase llamada Television

class Television:
    
    # constructor
    def __init__(self):
        self.canal = 1 # canal por defecto es 1
        self.volumen = 1 # volumen por defecto es 1
        self.on = False # por defecto está apagado
    # metodos
    def encenderTV (self):
        self.on = True
    def apagarTV (self):
        self.on = False
    def getCanal (self):
        return self.canal
    def setCanal (self, canal):
        if (self.on == True and self.canal >= 1 and self.canal <= 120):
            self.canal = canal
    def setVolumen (self, volumen):
        if (self.on == True and self.volumen >= 1 and self.volumen <= 7):
            self.volumen = volumen
    def getVolumen (self):
        return self.volumen
    def subirCanal (self):
        if (self.on == True and self.canal <= 120):
            self.canal += 1
    def bajarCanal (self):
        if (self.on == True and self.canal <= 120):
            self.canal -= 1
    def subirVolumen (self):
        if (self.on == True and self.volumen <= 7):
            self.volumen += 1
    def bajarVolumen (self):
        if (self.on == True and self.volumen <= 7):
            self.volumen -= 1

tv1 = Television()
print ('canal: ', tv1.canal)
print ('volumen: ', tv1.volumen)
print ('estado: ', tv1.on)

tv1.encenderTV()
print ('estado: ', tv1.on)
tv1.setCanal (30)
print ('canal: ', tv1.canal)
tv1.subirVolumen()
tv1.subirVolumen()
tv1.subirVolumen()
tv1.subirVolumen()
tv1.subirVolumen()
print ('volumen: ', tv1.volumen)

tv1.subirCanal()
tv1.subirCanal()
tv1.subirCanal()

print ('En resumen tv1 se encuentra en el siguiente estado: ')
print ('canal = ', tv1.getCanal())
print ('volumen = ',tv1.getVolumen())
print ('estado = ', tv1.on)