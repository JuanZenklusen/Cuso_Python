mylist5 = [1,2,3,15,5,8,7,6,5,5,5,3]
myconjunto5 = set()
for element in mylist5:
  myconjunto5.add(element)
print(myconjunto5)
#hasta aquí elimino duplicados creando un conjunto... pero si el ejercicio pide que se genere una nueva lista, debería hacer lo que está debajo, que crea una nueva lista e itera cada elemento del conjunto:

mynewlist5 = []
for element in myconjunto5:
  mynewlist5.append(element)
print(mynewlist5)