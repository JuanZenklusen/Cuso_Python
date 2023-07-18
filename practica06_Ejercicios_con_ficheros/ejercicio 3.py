'''Enunciado
Crear un programa que permita al usuario registrar y analizar las ventas de un negocio.
Las ventas se registrarán en un archivo de texto y se podrán realizar operaciones como
calcular el total de ventas, el promedio de ventas y encontrar las ventas más altas y más
bajas.'''

#Leer todas las ventas
def Leer_ventas():
    with open('practica06_Ejercicios_con_ficheros\\ejercicio3.txt',encoding='UTF-8') as archivo:
        print(f'Las ventas registradas son: \n\n{archivo.read()}\n')
    
#Obtener una lista con todas las lineas del archivo
def Obtener_lista_ventas():
    with open('practica06_Ejercicios_con_ficheros\\ejercicio3.txt',encoding='UTF-8') as archivo:
        lineas = archivo.readlines() #creo una lista con el contenido de las lineas
        return lineas #retorno la lista
    
#Retornar lista de todas las lineas del archivo y lista de los precios
def Obtener_precios():
    lista = Obtener_lista_ventas()
    precios = []
    for elemento in lista:
        posicion = elemento.find('$')
        precio = int(elemento[posicion+1:])
        precios.append(precio)
    return lista,precios
 
#Permite agregar las ventas por parametro texto y precio de venta, genera la linea y agrega la venta al archivo
def Agregar_venta(texto,precio_venta):
    lista_actual_vetas = Obtener_lista_ventas()
    nueva_venta = f'\n{texto} ${precio_venta}'
    lista_actual_vetas.append(nueva_venta)
    with open('practica06_Ejercicios_con_ficheros\\ejercicio3.txt','w',encoding='UTF-8') as archivo:
        archivo.writelines(lista_actual_vetas)
    return 'Archivo actualizado', Leer_ventas()

#Imprime la mayor o mayores ventas en caso de que dos ventas tengan el mismo monto
def Buscar_vta_mayor():
    lista,precios = Obtener_precios()
    mayor_monto = max(precios)
    lineas_con_monto = []
    for elemento2 in lista:
        if str(mayor_monto) in elemento2:
            lineas_con_monto.append(elemento2)
        else:
            continue
    print('\nMayor/es venta/s: ')
    for linea_con_monto in lineas_con_monto:
        print(f'\t{linea_con_monto}')
        
#Imprime la menor o menores ventas en caso de que dos ventas tengan el mismo monto
def Buscar_vta_menor():
    lista,precios = Obtener_precios()
    menor_monto = min(precios)
    lineas_con_monto = []
    for elemento2 in lista:
        if str(menor_monto) in elemento2:
            lineas_con_monto.append(elemento2)
        else:
            continue
    print('\nMenor/es venta/s: ')
    for linea_con_monto in lineas_con_monto:
        print(f'\t{linea_con_monto}')
        
#Impreime el promedio de ventas
def Promedio_vtas():
    lista,precios = Obtener_precios()
    print(f'Promedio de ventas: ${round(sum(precios)/len(precios),2)}')


menu = {
    '1': lambda: Agregar_venta(input('Ingrese cantidad y articulo vendido: '), input('Ingrese precio a pagar: ')),
    '2': Leer_ventas,
    '3': Buscar_vta_mayor,
    '4': Buscar_vta_menor,
    '5': Promedio_vtas
}

print('Bienvenido al gestor VENDOTODO S.A.')
print("MENU DE OPCIONES:")
print("   1. Agregar una venta")
print("   2. Leer todas las ventas")
print("   3. Obtener venta mayor")
print("   4. Obtener venta menor")
print("   5. Promedio de ventas")

opcion = input("\nSelecciona una opción: ")

if opcion in menu:
    menu[opcion]()
else:
    print("Opción inválida.")