'''Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla todos los números impares desde 1 hasta ese número separados por comas.
def Nros_impares(nro):
    lista = []
    for i in range(1, nro+1, 2):
        lista.append(str(i))
    resultado = ", ".join(lista)
    return resultado

n = int(input('Ingrese nro entero y positivo: '))
print('Los numeros impares en el rango especificado son: ', Nros_impares(n))'''



'''n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("")'''


