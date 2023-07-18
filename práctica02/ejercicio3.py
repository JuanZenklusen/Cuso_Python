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