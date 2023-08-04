import time
from menu import Encabezado, menu
from apostador import *

apostadores = []
apuestas = []
salir = True

while salir:
    if salir == False:
        break
    else:
        Encabezado()
        accion = input()

        if accion in menu:
            menu[accion]()
        else:
            print("Opción inválida.")
            time.sleep(3)
        
        print(apostadores)
        print(apuestas)

        time.sleep(3)