#Importo pi
from math import pi

#Crear clase
class Circulo:
    #primero creo el constructos y los atributos
    def __init__(self, radio):
        self.radio = radio
    
    #Defino el metodo calcular area
    def calcular_area(self):
        return pi * self.radio ** 2
    
    #defino el metodo calcular perimetro
    def calcular_perimetro(self):
        return 2 * pi * self.radio

#Creo los objetos
circulo1=Circulo(20)
circulo2=Circulo(10)

#imprimo los resultados de los metodos
print(circulo1.calcular_area())
print(circulo2.calcular_area())
print(circulo1.calcular_perimetro())
print(circulo2.calcular_perimetro())