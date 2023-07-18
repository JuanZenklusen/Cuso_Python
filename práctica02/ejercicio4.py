print('Consigna 4:\n')

#entrada
n2cifras = int(input('Ingrese un número de 2 cifras: '))
while n2cifras <10 or n2cifras >=100:
  n2cifras = int(input('\nNo ha realizado un ingreso válido, por favor, introduzca un número de dos cifras: '))

#proceso
cifra1 = n2cifras // 10
cifra2 = n2cifras % 10
suma_cifras = cifra1 + cifra2
if suma_cifras % 2 == 1:
  criterio = 'impar'
else:
  criterio = 'par'

#Salida
print('El primer dígito es', cifra1,'y el segundo es', cifra2,'y la suma entre ambos es igual a', suma_cifras, 'que es un número', criterio)
