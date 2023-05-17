import os 
from peewee import *
from funciones import *

continuar= True

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
    ╚══════════════════════════════════════════════╝ """)
    select= input('Digite las opcion que necesite: ')
    
    if select == '1':
        Agregar()
    elif select == '2':
        Modificar()
    elif select == '3':
        Exportar()
    elif select == '4':
        Mapa()   
    elif select == '5':
        continuar= False
        print('Adios....')
    else:
        input('DATOS ERRONEOS... Intenten escoger una opcion valida: ')
