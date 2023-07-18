'''
1. Escribe un programa que solicite al usuario una palabra y luego cuente cuántas letras contiene.

palabra=input('Ingrese una palabra: ')
print('Contine ', len(palabra), 'letras la palabra infresada')

'''
'''
2. Escribe un programa que solicite al usuario una frase y luego muestre la frase invertida.

#Hay dos maneras de resolver: 
palabra=input('Ingrese una palabra: ')
print(palabra[::-1])

#o usando un for
palabra=input('Ingrese una palabra o frase: ')
for i in range(1,len(palabra)+1):
  print(palabra[-i], end="")

'''
'''
3. Escribe un programa que verifique si una palabra ingresada por el usuario es un palíndromo (se lee igual de izquierda a derecha y de derecha a izquierda).

palabra=input('Ingrese una palabra: ')
if palabra[::-1] == palabra:
  print('La palabra es palíndromo')
else:
  print('la palabra no es palíndromo')

'''
'''
4. Escribe un programa que solicite al usuario una frase y cuente cuántas palabras contiene.

frase=input('Ingrese una frase: ')
frase.count(" ")
print(frase.count(" ")+1)
#no se si es válido esto, yo conté cuántas veces había espacios y le sume uno. Preguntar al profe

'''
'''
5. Escribe un programa que solicite al usuario su nombre y luego muestre el nombre con la primera letra en mayúscula y las demás en minúsculas.

nombre = input('Ingrese su nombre: ')
print(nombre.title())

'''
'''
6. Escribe un programa que solicite al usuario una palabra y cuente cuántas vocales (a, e, i, o, u) contiene.

palabra = input('Ingrese una palabra: ')
palabra = palabra.lower() #Convierto todo a minúsculas, porque si pone una palabra con mayúscula que inicia con A no la contaría
print(palabra.count('a')+palabra.count('e')+palabra.count('i')+palabra.count('o')+palabra.count('u'))

'''
'''
7. Escribe un programa que solicite al usuario una palabra y luego muestre la palabra sin los caracteres repetidos.
'''




'''
8. Escribe un programa que solicite al usuario una frase y una longitud, y luego cuente cuántas palabras de esa longitud hay en la frase.

9. Escribe un programa que solicite al usuario una frase y una subcadena, y luego cuente cuántas veces aparece esa subcadena en la frase.

'''
