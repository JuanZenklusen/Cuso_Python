from datetime import date
from apostador import Apostador, ApuestaQuiniela
from main import apostadores, apuestas

#Se instacia una funcion quiniela para que pida todos los parámetros
def Quiniela():
    nombre_y_apellido = input('Ingrese su Nombre y Apellido completo: ')
    dni = int(input('ingrese su DNI: '))
    apostadores.append(Apostador(nombre_y_apellido, dni))
    numero_a_apostar = int(input('Ingrese número a apostar: '))
    if numero_a_apostar > 9999:
        return print('-- NUMERO NO VALIDO -- Volviendo al menu principal')
    valor_apuesta = float(input(f'¿Cuánto dinero quiere apostar al N° {numero_a_apostar}: $'))
    fecha = date.today()
    juego = 'Quiniela'
    apuestas.append(ApuestaQuiniela(numero_a_apostar, valor_apuesta, fecha, juego))

