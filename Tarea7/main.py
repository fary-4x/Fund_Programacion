from peewee import *
import funciones
import os

def main():
      os.system('cls')
      print("""
            ╔══════════════════════════════════════════════╗
            ║    ¡BIENVENIDO AL REGISTRO DE LICENCIA!      ║
            ║══════════════════════════════════════════════║
            ║        Digite la opcion que necesite:        ║
            ║                                              ║
            ║              1-Agregar                       ║
            ║              2-Ver datos                     ║
            ║              3-Modificar                     ║
            ║              4-Imprimir Licencia             ║
            ║              5-Mapa                          ║
            ║              6-Salir                         ║ 
            ╚══════════════════════════════════════════════╝ 
           """)
      
      seleccion = int(input())
      if (seleccion == 1):
            funciones.Agregar(main)
      elif (seleccion == 2):
            funciones.Mostrar_Datos(main)
      elif (seleccion == 3):
            funciones.Modificar(main)    
      elif (seleccion == 4):
           funciones.Exportar()
      elif (seleccion == 5):
            funciones.Mapa(main)
      elif (seleccion == 6): 
            input('Pulse Enter para salir ')
      else: print('Su opcion no es aplicable, Ingrese un numero valido')
      
main()