import os 
import funciones
from peewee import SqliteDatabase, AutoField, CharField, DateField, ForeignKeyField, Model, IntegerField


def main():
      os.system('cls')
      print("""
            ╔═══════════════════════════════════════════════╗
            ║                    MENÚ                       ║
            ║═══════════════════════════════════════════════║
            ║  Introduce un numero para hacer dicha accion. ║
            ║                                               ║
            ║                  1 = Ver datos                ║
            ║                  2 = Ingresar                 ║
            ║                  3 = Modificar                ║
            ║                  4 = Eliminar                 ║
            ║                  5 = Exportar                 ║ 
            ║                  6 = Salir                    ║  
            ╚═══════════════════════════════════════════════╝ 
           """)


      seleccion = int(input())
      if (seleccion == 1):
            funciones.Mostrar_Datos(main)
      elif (seleccion == 2):
            funciones.Ingresar(main)
      elif (seleccion == 3):
           funciones.Modificar(main)
      elif (seleccion == 4):
            funciones.Eliminar(main)
      elif (seleccion == 5):
           funciones.Exportar()
      elif (seleccion == 6):
            input('Pulse Enter para salir ')
      else: print('Su opcion no es aplicable, Ingrese un numero valido')
      
main()