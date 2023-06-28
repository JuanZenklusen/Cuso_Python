'''
Escribe un algoritmo que tome una lista de números como parámetro y devuelva la suma de todos los elementos de la lista.

mylist1=[1,2,3,4,5,6,7]
a=0
for element in mylist1:
  a=a+element
print(a)'''


'''
Escribe un algoritmo que tome una lista de números como parámetro y devuelva una nueva lista que contenga solo los números pares.


mylist2=[1,2,3,4,5,6,7,8,9,10]
mynewlist2=[]
for element in mylist2:
  if element % 2 == 0:
    mynewlist2.append(element)
print(mynewlist2)'''


'''
Escribe un algoritmo que tome una lista de números al azar como parámetro y devuelva una nueva lista que contenga solo los números impares.


import random

mylist3 = []
mynewlist3 = []
for i in range(10): #aquí llena la lista con 10 numeros al azar del 0 al 100
  mylist3.append(random.randint(0, 100))
for element in mylist3:
  if element % 2 != 0:
    mynewlist3.append(element)
print(mylist3)
print(mynewlist3)'''


'''
Escribe un algoritmo que tome una lista como parámetro y devuelva una nueva
lista con los elementos en orden inverso.


mylist4 = [1,5,8,45,31,2,18,67,195423,0]
mylist4.sort()
mylist4.reverse()
print(mylist4)'''


'''
Escribe un algoritmo que tome una lista como parámetro y devuelva una nueva
lista que elimine los elementos duplicados.


mylist5 = [1,2,3,15,5,8,7,6,5,5,5,3]
myconjunto5 = set()
for element in mylist5:
  myconjunto5.add(element)
print(myconjunto5)
#hasta aquí elimino duplicados creando un conjunto... pero si el ejercicio pide que se genere una nueva lista, debería hacer lo que está debajo, que crea una nueva lista e itera cada elemento del conjunto:

mynewlist5 = []
for element in myconjunto5:
  mynewlist5.append(element)
print(mynewlist5)'''


'''
Escribe un programa que encuentre el número más grande en una lista de números.
numeros = [10, 5, 25, 30, 15]

numeros = [10, 5, 25, 30, 15]
numeros.sort()
print(numeros[-1])'''


'''
Escribe un programa que elimine los elementos duplicados de una lista. (Busca
dos maneras diferentes de resolverlo). numeros = [10, 20, 30, 20, 40, 10, 50, 30]

#Una manera de resolverlo sería la que desarrollamos en el ejercicio 5.abs

numeros = [10, 20, 30, 20, 40, 10, 50, 30]
sin_duplicados = []
for element in numeros:
  if numeros.count(element) == 1:
    sin_duplicados.append(element)
  elif sin_duplicados.count(element) == 0:
    sin_duplicados.append(element)
numeros = sin_duplicados
print(numeros)'''


'''
Escribe un programa que cuente la frecuencia de cada elemento en una lista y
muestre los resultados. numeros = [10, 20, 30, 20, 40, 10, 50, 30]


numeros = [10, 20, 30, 20, 40, 10, 50, 30]
conjunto = set()
for element in numeros:
  conjunto.add(element) #hasta aquí elimino los duplicados con un conjunto, para luego poder recorrerlo y que se puede imprimir una sola vez cuántas veces aparece cada número en la lista original.

print(conjunto)

for element in conjunto:
  print(f'El número {element} aparece en la lista con una frecuencia de: {numeros.count(element)}')'''
