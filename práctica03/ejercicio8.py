nro=int(input('Ingrese un numero: '))
i=1
j=1
a=1
b=1
for i in range(0,nro+1):
  for j in range(0,i):
    a=a-2
    print(a, end=' ')
    j=j+1
  print('')
  a=b+2
  b=b+2
  i=i+1

''' Resolución del profe
n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")
'''