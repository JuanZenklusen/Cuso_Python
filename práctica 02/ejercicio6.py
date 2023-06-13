print('Consigna 6:\n')

#entradas:
kilo_w = float(input('Ingrese la cantidad de Kw consumidos: '))
precio_kilow = float(input('Ingrese el precio del Kw/h: '))

#proceso
if kilo_w > 700:
  precio_kilow_700 = precio_kilow * 1.05
  precio_final = (700*precio_kilow)+((kilo_w-700)*precio_kilow_700)
else:
  precio_final = kilo_w*precio_kilow

#Salida
print('El valor a pagar es: $', precio_final)