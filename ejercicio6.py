nro=int(input('Ingrese un numero: '))
i=1
j=1
for i in range(0,nro+1):
  for j in range(0,i):
    print('*', end='')
    j=j+1
  print('')
  i=i+1
