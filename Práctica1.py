import math

#Consiguna 1
print('Consigna 1:\n')

# Pedir al usuario la velocidad y el tiempo
velocidad = float(input("Ingrese la velocidad del móvil (m/s): "))
tiempo = float(input("Ingrese el tiempo transcurrido (s): "))

# Calcular la distancia recorrida
distancia = velocidad * tiempo

# Imprimir el resultado
print("La distancia recorrida es:", distancia, "metros.\n")

#Consiguna 2
print('Consigna 2:\n')

# Pedir al usuario las notas
n1 = float(input('Ingrese nota del primer parcial: '))
n2 = float(input('Ingrese nota del segundo parcial: '))
n3 = float(input('Ingrese nota del tercer parcial: '))

# Calcular promedio de notas
nota = (n1+n2+n3)/3

# imprimir en pantalla el resultado
print('La nota final es: ', nota,'\n')

#Consiguna 3
print('Consigna 3:\n')

# Pedir variables
correctas = int(input('Ingrese cantidad de respuestas correctas: '))
incorrectas = int(input('Ingrese cantidad de respuestas incorrectas: '))
blanco = int(input('Ingrese cantidad de respuestas en blanco: '))

# calculo de puntaje
resultado = (correctas*3)-(incorrectas*1)+(blanco*0)

# imprimir en pantalla el resultado
print('El puntaje final es: ', resultado,'\n')


#Consiguna 4
print('Consigna 4:\n')

# Pedir variables
ganados = int(input('Ingrese cantidad de partidos ganados: '))
empatados = int(input('Ingrese cantidad de partidos empatados: '))
perdidos = int(input('Ingrese cantidad de partidos perdidos: '))

# calcular
puntos = (ganados*3)+empatados

# imprimir en pantalla el resultado
print('El total de puntos obtenidos por el club ABC fue de: ', puntos,'\n')


#Consiguna 5
print('Consigna 5:\n')

# ingresar datos
tam_disco = float(input('¿Cuántos GB tiene tu disco? '))

# cálculo
cantidad_discos = math.ceil((tam_disco*1024)/1.44)

# resultados en pantalla
print('Se necesitan ', round(cantidad_discos), 'discos de 3.5\n')

#Consiguna 6
print('Consigna 6:\n')

# ingresar datos
x1 = int(input('Ingrese posición inicial en el eje "x": '))
y1 = int(input('Ingrese posición inicial en el eje "y": '))

x2 = int(input('Ingrese posición final en el eje "x": '))
y2 = int(input('Ingrese posición final en el eje "y": '))

# calculo
delta_x = abs(x1-x2)
delta_y = abs(y1-y2)

hipotenusa = math.sqrt((delta_x**2)+(delta_y**2))

# resultados en pantalla
print('la distancia recorrida es: ', hipotenusa,'\n')

#Consiguna 7
print('Consigna 7:\n')

# ingresar numero entero
num = int(input('Ingrese un número entero: '))

# calculo
cal = num % 2

if cal == 0:
  print('El número es par.\n')
else:
  print('El número es impar.\n')


#Consiguna 8
print('Consigna 8:\n')

# ingresar valores
v1 = float(input('Ingrese primer valor: '))
v2 = float(input('Ingrese segundo valor: '))
v3 = float(input('Ingrese tercer valor: '))

# determinar que valor es el más grande
print('El número más grande es: ', max(v1, v2, v3),'\n')


#Consiguna 9
print('Consigna 9:\n')

# Ingresar datos
nombre = input('Nombre y apellido del empleado: ')
dni = input('Número de D.N.I.: ')
sueldo_basico = float(input('Ingrese sueldo básico: '))
antig = int(input('¿Cuántos años hace que trabaja?: '))
estado_civil = int(input('Estado civil: [0 si es soltero / 1 si es casado]: '))
hijos = int(input('Ingrese cantidad de hijos: '))
presentismo = int(input('¿Corresponde presentismo?: [1 si corresponde cobrar / 0 si no corresponde]'))

# cálculos
SB = sueldo_basico
antiguedad = SB*0.012*antig
if presentismo == 1:
  MP = 3500
else:
  MP = 0
AJ = SB*.11
OS = SB*.03
AG = SB*.01
if estado_civil == 1:
  conyuge = 800
else:
  conyuge = 0
hjs = hijos*400

SN = SB+antiguedad+MP-AJ-OS-AG+conyuge+hjs

# resultado en pantalla
print('\nRecibo de haberes de:', nombre, 'DNI:', dni)
print('Sueldo básico: $ ', SB)
if antig > 0:
  print(' + Antigûedad: $ ', antiguedad)
if presentismo > 0:
  print(' + Presentismo: $', MP)
if conyuge > 0:
  print(' + Conyugue: $', conyuge)
if hjs > 0:
  print(' + Hijo(s): $', hjs)
print(' - Aporte Jubilatorio: $', AJ)
print(' - Obra Social: $', OS)
print(' - Aporte Gremial: $', AG)
print('-----------------------')
print('Sueldo Neto: $', SN)
