numeros = [10, 20, 30, 20, 40, 10, 50, 30]
conjunto = set()
for element in numeros:
  conjunto.add(element) #hasta aquí elimino los duplicados con un conjunto, para luego poder recorrerlo y que se puede imprimir una sola vez cuántas veces aparece cada número en la lista original.

print(conjunto)

for element in conjunto:
  print(f'El número {element} aparece en la lista con una frecuencia de: {numeros.count(element)}')