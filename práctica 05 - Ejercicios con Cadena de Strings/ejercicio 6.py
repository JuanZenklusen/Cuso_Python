palabra = input('Ingrese una palabra: ')
palabra = palabra.lower() #Convierto todo a minúsculas, porque si pone una palabra con mayúscula que inicia con A no la contaría
print(palabra.count('a')+palabra.count('e')+palabra.count('i')+palabra.count('o')+palabra.count('u'))