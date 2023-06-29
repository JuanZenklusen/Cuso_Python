#Una manera de resolverlo sería la que desarrollamos en el ejercicio 5.abs

numeros = [10, 20, 30, 20, 40, 10, 50, 30]
sin_duplicados = []
for element in numeros:
  if numeros.count(element) == 1:
    sin_duplicados.append(element)
  elif sin_duplicados.count(element) == 0:
    sin_duplicados.append(element)
numeros = sin_duplicados
print(numeros)