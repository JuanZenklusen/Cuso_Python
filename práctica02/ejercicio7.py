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