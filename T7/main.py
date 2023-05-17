import os
from funciones import *
from dbx import *

continuar = True

while continuar:
    os.system('cls')
    print("""
             ╔══════════════════════════════════════════════╗
             ║    ¡BIENVENIDO AL REGISTRO DE LICENCIA!      ║
             ║══════════════════════════════════════════════║
             ║              1-Agregar                       ║
             ║              2-Modificar                     ║
             ║              3-Imprimir Licencia             ║
             ║              4-Mapa                          ║
             ║              5-Salir                         ║ 
             ╚══════════════════════════════════════════════╝ 
             """)

    tmp= input('Digite la opcion que necesite del recuadro: ' )

    if tmp == '1':
        Agregar()
    elif tmp == '2':
        Modificar()
    elif tmp == '3':
        Imprimir()
    elif tmp == '4':
        Mapa()
    elif tmp == '5':
        continuar= False
        print('Fin...')
    else:
        Mostrar('Datos erroneos, intente nuevamente ingresando una opcion valida')