i=1
a=1
for a in range(1,10):
  print('\nTabla del', a)
  for i in range(1, 11):
    print(i,'x', a, '=',i*a)



''' Resolución del profe
for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print("")'''