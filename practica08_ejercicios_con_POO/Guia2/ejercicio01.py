'''Supongamos que queremos modelar diferentes tipos de vehículos. Podemos crear
una clase base llamada "Vehiculo" y luego derivar clases específicas como
"Automovil", "Motocicleta", etc.'''

class Vehiculos:
    def __init__(self, modelo):
        self.modelo = modelo

    def Arrancar(self):
        print('Ha arrancado')
    
    def Acelerar(self):
        print('Está acelerando')

    def Frenar(self):
        print('Ha frenado')
    
    def Apagar(self):
        print('Está apagado')

class Automovil(Vehiculos):
    def __init__(self, marca, color, caballos_de_fuerza):
        self.marca = marca
        self.color = color
        self.caballos_de_fuerza = caballos_de_fuerza

class Motocicleta(Vehiculos):
    def __init__(self, marca, color, cilindrada):
        self.marca = marca
        self.color = color
        self.cilindrada = cilindrada