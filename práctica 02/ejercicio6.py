print('Consigna 6:\n')

#entradas:
kilo_w = float(input('Ingrese la cantidad de Kw consumidos: '))
precio_kilow = float(input('Ingrese el precio del Kw/h: '))

#proceso
if kilo_w > 700:
  precio_kilow = precio_kilow * 1.05

#Salida
print('El valor a pagar es: $', (kilo_w * precio_kilow))