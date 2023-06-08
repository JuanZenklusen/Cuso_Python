from math import pi

print('----------------------\n')
print('Consigna 1:\n')

# definir entradas
radio = float(input('Ingrese rádio de la superficie: '))
altura = float(input('Ingrese altura del cilindro: '))

# proceso
if altura > radio:
    volumen = (pi*(radio**2))*altura
    print('El volumen del cilindro es:', volumen)
    print('\n')
else:
    #area = pi*(radio**2)
    area = 2 * pi * radio * (radio + altura)
    print('El área del cilindro es:', area)
    print('\n')

print('----------------------\n')
print('Consigna 2:\n')

# definir entradas
radio = float(input('Ingrese rádio de la superficie: '))
altura = float(input('Ingrese altura del cilindro: '))

# proceso
if altura > radio:
    volumen = (pi*(radio**2))*altura
    print('El volumen del cilindro es:', volumen)
    print('\n')
else:
    #area = pi*(radio**2)
    print('error')
    print('\n')

print('----------------------\n')
print('Consigna 3:\n')

#entradas

l1 = float(input('Ingrese dimensión de lado 1: '))
l2 = float(input('Ingrese dimensión de lado 2: '))
l3 = float(input('Ingrese dimensión de lado 3: '))

#cálculo diagonales
d1 = ((l1**2) + (l2**2))**0.5
d2 = ((l1**2) + (l3**2))**0.5
d3 = ((l2**2) + (l3**2))**0.5
d_mayor = max(d1, d2, d3)

#salida
if d_mayor == d1:
  print('La diagonal mayor es compuesta por el lado 1 y el lado 2')
else:
  if d_mayor == d2:
    print('La diagonall mayor es compuesta por el lado 1 y lado 3')
  else:
    print('La diagonal mayor es la compuesta por el lado 2 y el lado 3')    

print('Mide: ', d_mayor)


print('----------------------\n')
print('Consigna 4:\n')
#entradas

l1 = float(input('Ingrese dimensión de lado 1: '))
l2 = float(input('Ingrese dimensión de lado 2: '))
l3 = float(input('Ingrese dimensión de lado 3: '))

#cálculo diagonales
d1 = ( (l1**2) + (l2**2) )**0.5
d2 = ( (l1**2) + (l3**2) )**0.5
d3 = ( (l2**2) + (l3**2) )**0.5
d_mayor = max(d1, d2, d3)

#salida
if d_mayor == d1:
  print('La diagonal mayor es compuesta por el lado 1 y el lado 2')
else:
  if d_mayor == d2:
    print('La diagonall mayor es compuesta por el lado 1 y lado 3')
  else:
    print('La diagonal mayor es la compuesta por el lado 2 y el lado 3')    

print('Mide: ', d_mayor)


print('----------------------\n')
print('Consigna 4:\n')

#entrada
n2cifras = int(input('Ingrese un número de 2 cifras: '))
while n2cifras <10 or n2cifras >=100:
  n2cifras = int(input('\nNo ha realizado un ingreso válido, por favor, introduzca un número de dos cifras: '))

#proceso
cifra1 = n2cifras // 10
cifra2 = n2cifras % 10
suma_cifras = cifra1 + cifra2
if suma_cifras % 2 == 1:
  criterio = 'impar'
else:
  criterio = 'par'

#Salida
print('El primer dígito es', cifra1,'y el segundo es', cifra2,'y la suma entre ambos es igual a', suma_cifras, 'que es un número', criterio)

print('----------------------\n')
print('Consigna 5:\n')

#entradas
entero_multiplo = float(input('Ingrese un número: '))

#proceso y salida
if (entero_multiplo % 1) == 0:
  print ('El número es entero')
else:
  print('El número no es entero')

if (entero_multiplo % 7) == 0:
  print('El número es múltiplo de 7')
else:
  print('El número no es múltiplo de 7')

print('----------------------\n')
print('Consigna 6:\n')

#entradas:
kilo_w = float(input('Ingrese la cantidad de Kw consumidos: '))
precio_kilow = float(input('Ingrese el precio del Kw/h: '))

#proceso
if kilo_w > 700:
  precio_kilow = precio_kilow * 1.05

#Salida
print('El valor a pagar es: $', (kilo_w * precio_kilow))

print('----------------------\n')
print('Consigna 7:\n')

#entradas:
t = float(input('Ingrese temperatura: '))
p = int(input('Ingrese 1 para convertir de ºF a ºC o 2 para convertir de ºC a ºF: '))
while p != 1 and p != 2:
  p = int(input('No ha ingresado una opción correcta! Ingrese 1 para convertir de ºF a ºC o 2 para convertir de ºC a ºF: '))

if p == 1:
  c = 5/9*(t-32)
  print('Convirtiendo de ºF a ºC.... Resultado:', c, 'ºC')
else:
  c = 32+(9*t/5)
  print('Convirtiendo de ºC a ºF.... Resultado:', c, 'ºF')

print('----------------------\n')
print('Consigna 8:\n')

"""Dadas las tres calificaciones de dos estudiantes. La calificación final de cada uno
es la suma de sus dos mejores calificaciones. Muestre un mensaje que indique cual
estudiante (1 o 2) tiene la mayor calificación final."""

#entradas:
cal_a_1 = float(input('Ingrese primer calificacion del estudiante 1: '))
cal_b_1 = float(input('Ingrese segunda calificacion del estudiante 1: '))
cal_c_1 = float(input('Ingrese tercera calificacion del estudiante 1: '))
cal_a_2 = float(input('Ingrese primer calificacion del estudiante 2: '))
cal_b_2 = float(input('Ingrese segunda calificacion del estudiante 2: '))
cal_c_2 = float(input('Ingrese tercera calificacion del estudiante 2: '))

#proceso
cal_final_1 = (cal_a_1 + cal_b_1 + cal_c_1) - min(cal_a_1, cal_b_1, cal_c_1)
cal_final_2 = (cal_a_2 + cal_b_2 + cal_c_2) - min(cal_a_2, cal_b_2, cal_c_2)

#salida
if cal_final_1 == cal_final_2:
  print('Ambos tienen la misma calificación')
else:
  if cal_final_1 > cal_final_2:
    print('El alumno 1 tiene una mayor calificacion con: ', cal_final_1)
  else:
    print('El alumno 2 tiene una mayor calificacion con: ', cal_final_2)
