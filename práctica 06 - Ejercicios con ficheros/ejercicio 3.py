'''Enunciado
Crear un programa que permita al usuario registrar y analizar las ventas de un negocio.
Las ventas se registrarán en un archivo de texto y se podrán realizar operaciones como
calcular el total de ventas, el promedio de ventas y encontrar las ventas más altas y más
bajas.'''

def agregar_venta(linea):
    pass

def menu():
    print('Qué desea realizar??\n')
    print('\t- Escriba 1 para agregar una nueva venta:')
    print('\t- Escriba 2 para segunda opción.')
    print('\t- Escriba 3 para tercer opción.')
    print('\n')
    print('\t-Si desea terminar el programa escriba "salir"\n')

#main
desea_salir=True
print('Bienvenido al gestor de ventas de VENDEMETODO.COM\n')
while desea_salir:
    menu()
    instruccion = input('Ingrese: ')
    if instruccion == "salir":
        desea_salir=False
    elif instruccion == 1:
        venta = input('Escriba articulo vendido: ')
        monto = input('Indique a que precio lo vendió: $')
        
    else:
        print('\n\nNo ha elengido una opción válida\n\n')

print('Ha finalizado el programa. Hasta Luego\n\n')