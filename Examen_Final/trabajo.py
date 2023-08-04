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

  def Imprimir_ticket(self):
    return f'''
    --------- Detalle de la apuesta --------- 
        Agencia: {(self.agencia).upper()}
        Tipo de Sorteo: {self.juego}
    
    Nombre:............... {(self.nombre_completo).upper()}
    DNI:.................. {self.dni}
    Fecha:................ {self.fecha}
    Nro. Ticket:.......... {self.nro_tiket}
    Numero/s apostado/s:.. {self.nro}
    Valor ticket:......... $ {self.monto_apuesta}
    -----------------------------------------\n\n'''

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
      print('\nIngresó un número mayor s los permitidos.')
      sleep(2)
    elif nro<10:
      print('\nIngresó un número menor a los permitidos.')
      sleep(2)
    else:
      print(f'\nHa seleccionado el número {nro} correctamente')
      numero_apostado = nro
      ciclo_while = False
  monto = float(input(f'\n¿Cuánto dinero quiere apostar al Nº {numero_apostado}? $ '))
  return numero_apostado, monto


def Numeros_Quini6():
  nros_quini6 = []
  i = 0
  while i < 6:
    num = int(input(f'Ingrese {i+1}º número: '))
    if -1 < num < 36:
      if num in nros_quini6:
        print('\n    NUMERO YA INGRESADO   \n')
      else:
        nros_quini6.append(num)
        i += 1
    else:
      print('\n    NUMERO INCORRECTO   \n')
  nros_quini6.sort()
  return nros_quini6


def Jugar_Quiniela():
  datos_apostador = Datos_Apostador()

  nro_y_monto = Numero_Monto_Quiniela()

  apuesta_quiniela = Apuesta(datos_apostador[0], datos_apostador[1], datos_apostador[2], datos_apostador[3], datos_apostador[4], 'Quiniela', nro_y_monto[0], nro_y_monto[1])

  print(apuesta_quiniela.Imprimir_ticket())
  apuestas.append(apuesta_quiniela)
  sleep(3)
  return 


def Jugar_Quini6():
  datos_apostador = Datos_Apostador()

  numeros = Numeros_Quini6()

  apuesta_quini6 = Apuesta(datos_apostador[0], datos_apostador[1], datos_apostador[2], datos_apostador[3], datos_apostador[4], 'Quini 6', numeros, 400)
  print(apuesta_quini6.Imprimir_ticket())
  apuestas.append(apuesta_quini6)
  return

menu = {
  '1': Jugar_Quiniela,
  '2': Jugar_Quini6
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



  # esto de abajo es por si quiero iterar todas las apuestas
  '''for apuesta in apuestas:
    print(apuesta.Imprimir())'''
