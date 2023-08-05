from datetime import date # Se importa la libreria datetime para generar las fechas de los tickets.
from time import sleep # Se importa sleep para que la lectura del programa por consola sea más amena. 
from random import randint # Se importa para generar los números aleatorios.
from clases import Apuesta # Importamos la clase Apuesta con sus atributos y métodos.


# Se crea la función "Datos_Apostador" para que se encargue de pedir los datos personales al cliente en las funciones Jugar_Quiniela y Jugar_Quini 6, con el fin de returilizar código. Se utiliza la librería DateTime para registrar la fecha automáticamente, y la función len para otorgar un nro al ticket.
def Datos_Apostador():
  nombre_completo = input('\nIngrese su nombre completo: ')
  dni = input('\nIngrese su número de DNI sin puntos ni guiones: ')
  fecha = date.today()
  nro_tiket = len(apuestas)+1
  agencia = 'Quiniela LA SUERTE'
  return nombre_completo, dni, fecha, nro_tiket, agencia


# Esta función es llamada desde "Jugar_Quiniela" se encarga de validar que el nro ingresado sea de 2, 3 o 4 cifras, con un bucle while que no le deja salir hasta que el cliente ingrese una número correcto. También se pide el monto a apostar a dicho número.
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


# Esta función es llamada desde "Jugar_Quini6" y se encarga de pedirle al usuario los 6 nros a jugar. Cuenta con una validación para que el usuario no ingrese numeros negativos o mayores a 35, como así también, no te deja ingresar dos veces el mismo valor. Es por eso, que se utilizó un while en vez de un for. El monto no lo solicita, sino que la asigna un valor fijo. Antes de terminar, ordena los valores en una lista con la función sort, lo que va a servir para comparar luego con la lista de nros sorteados.
def Numeros_Quini6():
  nros_quini6 = []
  i = 0
  while i < 6:
    num = int(input(f'\nIngrese {i+1}º número: '))
    if -1 < num < 36:
      if num in nros_quini6:
        print('\n    NUMERO YA INGRESADO   \n')
        sleep(2)
      else:
        nros_quini6.append(num)
        i += 1
    else:
      print('\n    NUMERO INCORRECTO   \n')
      sleep(2)
  nros_quini6.sort()
  return nros_quini6


# Se accede a esta función desde el diccionario "menú" cuando el usuario ingresa la opción 1. Recopila la info del jugador en una lista datos_apostador, el número y monto en la variable nro_y_monto y luego genera el objeto Apuesta en la variable apuesta_quiniela, para lugo agregarlo a la colección apuestas del programa principal. Antes de finalzar, llama al método "imprimir_ticket" y lo muestra en consola.
def Jugar_Quiniela():
  datos_apostador = Datos_Apostador()
  nro_y_monto = Numero_Monto_Quiniela()
  apuesta_quiniela = Apuesta(datos_apostador[0], datos_apostador[1], datos_apostador[2], datos_apostador[3], datos_apostador[4], 'Quiniela', nro_y_monto[0], nro_y_monto[1])
  print(apuesta_quiniela.Imprimir_ticket())
  apuestas.append(apuesta_quiniela)
  sleep(3)
  return 


# Se accede a esta función desde el diccionario "menú" cuando el usuario ingresa la opción 2. Recopila la info del jugador en una lista datos_apostador, el número y monto en la variable numeros y luego genera el objeto Apuesta en la variable apuesta_quini6, para lugo agregarlo a la colección apuestas del programa principal. Antes de finalzar, llama al método "imprimir_ticket" y lo muestra en consola.
def Jugar_Quini6():
  datos_apostador = Datos_Apostador()
  numeros = Numeros_Quini6()
  apuesta_quini6 = Apuesta(datos_apostador[0], datos_apostador[1], datos_apostador[2], datos_apostador[3], datos_apostador[4], 'Quini 6', numeros, 400)
  print(apuesta_quini6.Imprimir_ticket())
  apuestas.append(apuesta_quini6)
  sleep(3)
  return


# Esta función es llamada desde "Comprobar_Apuesta" para generar aleatoriamente el sorteo del Quini 6. Se utiliza una función while y no una función for, ya que puede que se genere dos veces el mismo número, y para esto utiliza una validación antes de sumarlo a la colección.
def Sortear_Quini6():
  res_quini6 = []
  while len(res_quini6) < 7: 
    num = randint(0, 35)
    if num in res_quini6:
      continue
    else:
      res_quini6.append(num)
  res_quini6.sort()
  return res_quini6


# Se accede a esta función desde el diccionario "menú" cuando el usuario ingresa la opción 3. Primero genera un numero al azar de entre 2 y 4 cifras y lo almacena en resultado_quiniela. Luego llama a la función "Sortear_Quini6" y sus valores los almacena en resultado_quini6. Imprime en consola los resultados y comprueba si existen ganadores.
def Comprobar_Apuesta():
  resultado_quiniela = randint(10, 9999)
  resultado_quini6 = Sortear_Quini6()
  print('\nSorteando quiniela...')
  sleep(1)
  print(f'\nResultado del sorteo a cabeza ----->>   {resultado_quiniela}   <<-----')
  sleep(2)
  print('\nSorteando Quini 6...')
  sleep(1)
  print(f'\nResultado del sorteo a cabeza ----->>   {resultado_quini6}   <<-----')
  sleep(2)
  print('\nComprobando ganadores...')
  sleep(1)
  ganador = 0
  for apuesta in apuestas:
    if apuesta.nro == resultado_quiniela:
      print(f'\nTENEMOS GANADOR -> Ticket Nº: {apuesta.nro_tiket} - {apuesta.nombre_completo}')
      ganador += 1
      sleep(2)
    if apuesta.nro == resultado_quini6:
      print(f'\nTENEMOS GANADOR -> Ticket Nº: {apuesta.nro_tiket} - {apuesta.nombre_completo}')
      ganador += 1
      sleep(2)
  if ganador > 0:
    return print(f'\nTenemos {ganador} ganador(es)')
  else:
    return print('\nNingun Ganador')


# Se accede a esta función desde el diccionario "menú" cuando el usuario ingresa la opción 4. Se encarga de recorrer los montos apostados utilizando unn bucle for y lo va sumando al acumulador ingresos_netos. Luego calcula el 45% y lo destina a impuestos, y los ingresos brutos resulta de la diferencia entre ingresos netos y los impuestos. Luego imprime en consola el arqueo de caja correspondiente.
def Arqueo_Caja():
  ingresos_netos = 0 # el total de los pagos de los apostadores
  for monto in apuestas:
    ingresos_netos += monto.monto_apuesta
  impuestos = ingresos_netos * 0.47 # dinero que corresponde a impuestos 47% de las apuestas
  ingresos_brutos = ingresos_netos - impuestos # dinero que corresponde a la agencia
  print(f'''
        --------  Arqueo de caja: Quiniela LA SUERTE  ---------
        
        Ingreso total por apuestas........... $ {ingresos_netos}
          - Imp. Nacionales.................. $ {impuestos}
        
        Ingresos brutos...................... $ {ingresos_brutos}
        -------------------------------------------------------
        ''')
  sleep(2)
  

# Genera el encabezado.
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


# Diccionario que dispara las funciones correspondientes según lo que ingrese el usuario
menu = {
  '1': Jugar_Quiniela,
  '2': Jugar_Quini6,
  '3': Comprobar_Apuesta,
  '4': Arqueo_Caja,
}


# Aquí comienza el programa principal.
apuestas = []

while True:
  Encabezado()
  opcion = input()
  sleep(0.5)
  if opcion == '5':
    break
  else:
    if opcion in menu:
        menu[opcion]()
    else:
        print("Opción inválida.\n")
        sleep(2)
  sleep(0.5)

print('Fin del programa')