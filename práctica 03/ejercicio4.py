nro = int(input('Ingrese nro entero y positivo: '))
while nro < 0:
  print('No es un número valido.')
  nro = int(input('Ingrese nro entero y positivo: '))
while nro != -1:
  print(nro, end=", ")
  nro = nro - 1
