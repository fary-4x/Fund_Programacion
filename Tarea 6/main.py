from libs import *
import datos

def Configuracion():
    print("""
    ╔══════════════════════════════════════════════╗
    ║            Menu de Configuracion             ║
    ║══════════════════════════════════════════════║
    ║           1- Agregar Vacuna                  ║
    ║           2-Modificar Vacuna                 ║
    ║           3-Eliminar Vacuna                  ║
    ║           4-Agregar Provincia                ║
    ║           5-Modificar Provincia              ║
    ║           6-Eliminar Provincia               ║
    ║           0- Regresar al menu anterior       ║
    ╚══════════════════════════════════════════════╝ """)
   
    tmp = input('Ingrese la opcion que desee elegir')

menu_principal = True 

while (menu_principal):
   
    limpiar()       
    print("""
    ╔══════════════════════════════════════════════╗
    ║    ¡BIENVENIDO AL REGISTRO DE VACUNACION!    ║
    ║══════════════════════════════════════════════║
    ║                1- Registrar                  ║
    ║                2-Exportar                    ║
    ║                3-Configuracion               ║
    ║                0-Salir                       ║
    ║         Digite la opcion que necesite        ║
    ╚══════════════════════════════════════════════╝""")
 
    tmp = input ('Ingrese la opcion que desee elegir ')
   
    if tmp == '0': 
        print('Hasta la proxima....')
        menu_principal = False;
    elif tmp == '3':
        Configuracion()
    else:  
        input('Ingrese una opcion valida ')
