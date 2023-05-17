import os
from peewee import *
from funciones import *


continuar = True

while continuar:
    os.system('cls')
    print("""
             ╔══════════════════════════════════════════════╗
             ║    ¡BIENVENIDO AL REGISTRO DE ROBOS!         ║
             ║══════════════════════════════════════════════║
             ║              1-Agregar                       ║
             ║              2-Modificar                     ║
             ║              3-Exportar                      ║
             ║              4-Mapa                          ║
             ║              5-Salir                         ║ 
             ╚══════════════════════════════════════════════╝ 
             """)

    selectt= input('Digite la opcion que necesite del recuadro: ' )

    if selectt == '1':
        Agregar()
    elif selectt == '2':
        Modificar()
    elif selectt == '3':
        Exportar()
    elif selectt == '4':
        Mapa()
    elif selectt == '5':
        continuar= False
        print('Fin...')
    else:
        input('Datos erroneos, intente nuevamente ingresando una opcion valida')