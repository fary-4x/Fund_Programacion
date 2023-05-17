import os
from funciones import *

continuar= True

while continuar:
    os.system('cls')
    print("""
    ╔══════════════════════════════════════════════╗
    ║    ¡BIENVENIDO AL REGISTRO DE ANIME!         ║
    ║══════════════════════════════════════════════║
    ║              A-Gestionar                     ║
    ║              B-Reportes                      ║
    ║              C-Configuracion                 ║
    ║              D-Acerca De                     ║
    ║              E-Salir                         ║ 
    ╚══════════════════════════════════════════════╝
    """)
    op= input('Digite la opcion que necesite: ')   
    if op == 'A' or op == 'a':
        Gestionar()
    elif op =='B'or op == 'b':
        Reportes()
    elif op =='C'or op == 'c':
        Configuracion()
    elif op == 'D'or op == 'd':
        AcercaD()
    elif op == 'E'or op == 'e':
        continuar= False
        print('Gracias por utilizar este programa...')
    else:
        input('Datos erroneos ingrese opciones validas, pulse enter para continuar... ')
