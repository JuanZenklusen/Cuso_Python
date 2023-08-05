from datetime import date
from time import sleep
from random import randint
from clases import Apuesta


def Datos_Apostador():
  nombre_completo = input('\nIngrese su nombre completo: ')
  dni = input('\nIngrese su número de DNI sin puntos ni guiones: ')
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
      print('\n  --  Ingresó un número mayor a los permitidos.  --')
      sleep(2)
    elif nro<10:
      print('\n  --  Ingresó un número menor a los permitidos.  --')
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
    num = int(input(f'\nIngrese {i+1}º número: '))
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


def Sortear_Quini6():
  res_quini6 = []
  while len(res_quini6) < 7: #utilizo un while, porque por ahi el randint le genera dos numeros iguales y quizás sean más de 6 iteraciones
    num = randint(0, 36)
    if num in res_quini6:
      continue
    else:
      res_quini6.append(num)
  res_quini6.sort()
  return res_quini6


def Comprobar_Apuesta():
  '''resultado_quiniela = randint(10, 9999)'''
  '''resultado_quini6 = Sortear_Quini6()'''
  resultado_quiniela = 1234
  resultado_quini6 = [1, 2, 3, 4, 5, 6]
  ganador = 0
  for apuesta in apuestas:
    if apuesta.nro == resultado_quiniela:
      print(f'\nTENEMOS GANADOR -> Ticket Nº: {apuesta.nro_tiket} - {apuesta.nombre_completo}')
      ganador += 1
    if apuesta.nro == resultado_quini6:
      print(f'\nTENEMOS GANADOR -> Ticket Nº: {apuesta.nro_tiket} - {apuesta.nombre_completo}')
      ganador += 1
  if ganador > 0:
    return print(f'\nTenemos {ganador} ganador(es)')
  else:
    return print('\nNingun Ganador')


def Encabezado():
    nombre_quiniela = "* Quiniela | 'L A S U E R T E' *"
    encabezado_menu = '|Escoja la opción deseada:|'
    print('\n')
    for i in range(len(nombre_quiniela)):
        print('*', end="")
    print(f'\n{nombre_quiniela}')
    for i in range(len(nombre_quiniela)+1):
        print('*', end="")
    print()
    for i in range(len(encabezado_menu)):
        print('-', end="")
    print(f'\n{encabezado_menu}')
    for i in range(len(encabezado_menu)):
        print('-', end="")
    print('\n1 - Quiniela\n2 - Quini 6\n3 - Comprobar apuesta\n4 - Arqueo de caja\n5 - Salir\n')


menu = {
  '1': Jugar_Quiniela,
  '2': Jugar_Quini6,
  '3': Comprobar_Apuesta,
}

apuestas = []

while True:
  Encabezado()

  opcion = input("\nSelecciona una opción: ")
  if opcion == '5':
    break
  else:
    if opcion in menu:
        menu[opcion]()
    else:
        print("Opción inválida.\n")
        sleep(2)

print('saliste del main')