class Apostador:
    def __init__(self, nombre_y_apellido, dni):
        self.nombre_y_apellido = nombre_y_apellido
        self.dni = dni
    
    def apostar_quiniela(self, numero_a_apostar, valor_apuesta, fecha, juego):
        pass

class ApuestaQuiniela:
    def __init__(self, numero_a_apostar, valor_apuesta, fecha, juego):
        self.numero_a_apostar = numero_a_apostar
        self.valor_apuesta = valor_apuesta
        self.fecha = fecha
        self.juego = juego