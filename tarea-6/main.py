import os
import funciones
import db
import config 


def main():
      os.system('cls')
      print("""
            ╔══════════════════════════════════════════════╗
            ║    ¡BIENVENIDO AL REGISTRO DE VACUNACION!    ║
            ║══════════════════════════════════════════════║
            ║        Digite la opcion que necesite         ║
            ║                1-Registro                    ║
            ║                2-Vacunacion                  ║
            ║                3-Exportar                    ║
            ║                4-Configuracion               ║
            ║                5-Salir                       ║
            ║                                              ║ 
            ╚══════════════════════════════════════════════╝ 
           """)
      
      selectt = int(input('Ingrese la opcion que desee elegir '))
      if (selectt == 1):
          funciones.Registro(main)
      elif (selectt == 2):
          funciones.vacunacion(main, db.Paciente)
      elif (selectt == 3):
          funciones.Exportar(main)
      elif (selectt == 4):
          config.configuracion(main, funciones)
      else: input("Pulse enter para salir")
      

main()