print('Consigna 10:\n')

#emtradas
l1 = float(input('Ingrese longitud de lado 1 del triángulo: '))
l2 = float(input('Ingrese longitud de lado 2 del triángulo: '))
l3 = float(input('Ingrese longitud de lado 3 del triángulo: '))

#proceso y salida
if l1 == l2 and l1 == l3:
  print('El triángulo formado es equilatero.')
else:
  if l1 != l2 and l1 != l3 and l2 != l3:
    print('El tirángulo formado es escaleno.')
  else:
    print('El triángulo formado es isóseles.')