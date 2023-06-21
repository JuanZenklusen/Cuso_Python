nro = int(input('Ingrese nro entero y positivo: '))
i=1
while nro < 0:
  print('No es un número valido.')
  nro = int(input('Ingrese nro entero y positivo: '))
while i <= nro:
  print(i, end=", ")
  i=i+2
