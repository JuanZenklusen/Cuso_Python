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
