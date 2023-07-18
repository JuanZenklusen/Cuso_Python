print('Consigna 11:\n')

#emtradas
aaaa = int(input('Ingrese el año: '))

#proceso y salida
if aaaa % 400 == 0:
  print('El año es biciesto.')
else:
  if aaaa % 4 == 0 and aaaa % 100 != 0:
    print('El año es biciesto.')
  else:
    print ('El año no es biciesto.')

print('----------------------\n')
print('Consigna 12:\n')

#emtradas
n1 = int(input('Ingrese un número entre 0 y 10: '))
while n1 < 0 or n1 > 10:
  n1 = int(input('ERROR. Ingrese un número entre 0 y 10: '))

#proceso y salida
if n1 % 2 == 0:
  print('El numero es par')
else:
  print('El numero es impar')