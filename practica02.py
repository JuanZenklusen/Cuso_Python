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
