nro=int(input('Ingrese un numero: '))
i=1
j=1
for i in range(0,nro+1):
  for j in range(0,i):
    print('*', end='')
    j=j+1
  print('')
  i=i+1

''' Resolución del profe
n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("")'''