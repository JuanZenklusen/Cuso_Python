palabra=input('Ingrese una palabra: ')
if palabra[::-1] == palabra:
  print('La palabra es palíndromo')
else:
  print('la palabra no es palíndromo')