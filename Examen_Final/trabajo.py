from datetime import date
from time import sleep

class Apuesta:
  def __init__(self, nombre_completo, dni, fecha, nro_tiket, agencia, juego, nro, monto_apuesta):
    self.nombre_completo = nombre_completo
    self.dni = dni
    self.fecha = fecha
    self.nro_tiket = nro_tiket
    self.agencia = agencia
    self.juego = juego
    self.nro = nro
    self.monto_apuesta = monto_apuesta


def Datos_Apostador():
  nombre_completo = input('Ingrese su nombre completo: ')
  dni = input('Ingrese su número de DNI sin puntos ni guiones: ')
  fecha = date.today()
  nro_tiket = len(apuestas)+1
  agencia = 'Quiniela LA SUERTE'
  return nombre_completo, dni, fecha, nro_tiket, agencia


def Numero_Monto_Quiniela():
  ciclo_while = True
  numero_apostado = 0
  while ciclo_while:
    nro = int(input('\nIngrese el nro a apostar desde 10 a 9999: '))
    if nro>9999:
      print('Ingresó un número mayor s los permitidos.')
      sleep(2)
    elif nro<10:
      print('Ingresó un número menor a los permitidos.')
      sleep(2)
    else:
      print(f'Ha seleccionado el número {nro} correctamente')
      numero_apostado = nro
      ciclo_while = False
  monto = float(input(f'¿Cuánto dinero quiere apostar al Nº {numero_apostado}? $ '))
  return numero_apostado, monto
    

def Jugar_Quiniela():
  datos_apostador = Datos_Apostador()

  nro_y_monto = Numero_Monto_Quiniela()

  apuesta_quiniela = Apuesta(datos_apostador[0], datos_apostador[1], datos_apostador[2], datos_apostador[3], datos_apostador[4], 'Quiniela', nro_y_monto[0], nro_y_monto[1])

  print(f'''
  Apuesta correctamente ingresada al Nº {apuesta_quiniela.nro} con un monto de $ {apuesta_quiniela.monto_apuesta}. 
  Datos del jugador:  
   - Nombre: {apuesta_quiniela.nombre_completo}
   - DNI: {apuesta_quiniela.dni}
   - Fecha: {apuesta_quiniela.fecha}
   - Nro de ticket: {apuesta_quiniela.nro_tiket}
   - Agencia: {apuesta_quiniela.agencia}
   - Juego: {apuesta_quiniela.juego}''')
  
  apuestas.append(apuesta_quiniela)
  
  sleep(3)


menu = {
  '1': Jugar_Quiniela,
}

apuestas = []
ciclo = True

while ciclo:
  print('menu')
  print('1 - Quiniela')
  print('2 - Quini 6')
  print('3 - Arqueo')
  print('4 - Sortear')
  print('5 - Salir')

  opcion = input("\nSelecciona una opción: ")

  if opcion in menu:
      menu[opcion]()
  else:
      print("Opción inválida.\n")
      sleep(2)
