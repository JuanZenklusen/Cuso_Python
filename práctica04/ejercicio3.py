import random

mylist3 = []
mynewlist3 = []
for i in range(10): #aquí llena la lista con 10 numeros al azar del 0 al 100
  mylist3.append(random.randint(0, 100))
for element in mylist3:
  if element % 2 != 0:
    mynewlist3.append(element)
print(mylist3)
print(mynewlist3)