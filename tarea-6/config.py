import datetime
import db
from peewee import *
import os
from prettytable import from_db_cursor
import sqlite3

def configuracion(main, funciones):
          os.system('cls')
          print("""
            ╔═════════════════════════════════════════════════════════════════════════════╗
            ║               Introduce un numero para hacer dicha accion.                  ║
            ║                                                                             ║
            ║                                1 = Provincias                               ║
            ║                                2 = Vacunas                                  ║
            ║                                3 = Inicio                                   ║
            ║                                                                             ║
            ╚═════════════════════════════════════════════════════════════════════════════╝ 
           """)
          selector = funciones.verificarDatos(": ", 1)
          if (selector == 1):
              Provincias(main, funciones)
          elif (selector == 2):
              Vacunas(main, funciones)
          elif (selector == 3):
              main()
          else: 
              input("Estos digitos no son aceptados presione enter y escoga una opcion valida")
              configuracion(main, funciones)



def Provincias(main, funciones):           
    os.system('cls')
    connection = sqlite3.connect("vacunacion.db") 
    cursor = connection.cursor()
    cursor.execute(f"SELECT id, nombreProvincia FROM Provincias")
    mytable = from_db_cursor(cursor)
    print(mytable)
    do = funciones.verificarDatos("Pulse 1 para volver al inicio o 2 para agregar una vacunacion: ", 1)
    if(do == 1):
        main()
    elif(do == 2):
        funciones.vacunacion(main, db.Paciente)
    else:
        input("Pulse 1 , 2 o enter para volver al inicio")
        main()

def Vacunas(main, funciones):
    os.system('cls')
    connection = sqlite3.connect("vacunacion.db") 
    cursor = connection.cursor()
    cursor.execute(f"SELECT id, nombreVacuna, cantidadRestante FROM Vacuna")
    mytable = from_db_cursor(cursor)
    print(mytable)
    do = funciones.verificarDatos("Pulse 1 volver al inicio o 2 para modificar o agregar vacunas: ", 1)
    if(do == 1):
        main()
    elif(do == 2):
        ModificarVacuna(main, funciones, Vacunas)
    else:
        input("Pulse 1, 2 o enter para volver al inicio")
        main()
        
def ModificarVacuna(main, funciones, Vacunas):
    os.system('cls')
    find = 0
    id = 0
    selector = funciones.verificarDatos("Pulse 1 si quiere alguna vacuna, 2 si llegaron nuevas cantidades de vacunas, 3 si quiere añadir un tipo de vacuna, 4 si quiere eliminar alguna: ", 1)
    if(selector == 1):
        connection = sqlite3.connect("vacunacion.db") 
        cursor = connection.cursor()
        cursor.execute(f"SELECT id, nombreVacuna, cantidadRestante FROM Vacuna")
        mytable = from_db_cursor(cursor)
        print(mytable)
        id = funciones.verificarDatos("Ingrese el ID de la vacuna a modificar", 1)
        
        for i in db.Vacuna.select():
            if (int(i.id) == int(id)):
                    find = 1
        if(find == 1):
            dbEdit = db.Vacuna.select().where(db.Vacuna.id == id).get()
            nombreNew = funciones.verificarDatos("Ingrese el nuevo nombre: ", 2)
            cantidadNew = funciones.verificarDatos("Cuantas vacunas hay?: ", 1)
            print(f"""
                   Estos seran los cambios aplicados:
                  {dbEdit.nombreVacuna} ---> {nombreNew}
                  {dbEdit.cantidadRestante} ---> {cantidadNew}
                  Digite Si para aplicar los cambios
                  """)
            confirm = str(input())
            if(confirm == "Si"):
                dbEdit.nombreVacuna = nombreNew
                dbEdit.cantidadRestante = cantidadNew
                dbEdit.save()
                input("Pulse enter para volver al inicio")
                main()
            else:
                input("No fueron aplicado los cambios, pulse enter para volver al inicio")
                main()
        else:
            input("Vacuna inexistente, pulse enter para volver al inicio")
            main()
    elif(selector == 2):
        connection = sqlite3.connect("vacunacion.db") 
        cursor = connection.cursor()
        cursor.execute(f"SELECT id, nombreVacuna, cantidadRestante FROM Vacuna")
        mytable = from_db_cursor(cursor)
        print(mytable)
        id = funciones.verificarDatos("Introduce el ID de la vacuna a modificar: ", 1)
        
        for lista in db.Vacuna.select():
            if (int(lista.id) == int(id)):
                    find = 1
        
        if(find == 1):
            dbEdit = db.Vacuna.select().where(db.Vacuna.id == id).get()
            cantidadNew = funciones.verificarDatos("Cuantas vacunas llegaron?: ", 1)
            print(f"""
                  Estos seran los cambios aplicados:
                  {dbEdit.cantidadRestante} ---> {dbEdit.cantidadRestante+cantidadNew}
                  Digite Si para aplicar los cambios
                  """)
            confirm = str(input())
            if(confirm == "Si"):
                dbEdit.cantidadRestante = dbEdit.cantidadRestante+cantidadNew
                dbEdit.save()
            else:
                input("No fueron aplicado los cambios, pulse enter para volver al inicio: ")
                main()
        else:
            input("Inexistente, pulse enter para volver al inicio")
            main()
    elif(selector == 3):
        datab = db.Vacuna()
        datab.nombreVacuna = funciones.verificarDatos("Ingrese el nombre de la vacuna: ", 2)
        datab.cantidadRestante = funciones.verificarDatos("Ingrese la cantidad de vacunas disponible: ", 1)
        datab.save()
        input("Vacuna agregada con exito, pulse enter para volver al inicio: ")
        main()
    
    elif(selector == 4):
        connection = sqlite3.connect("vacunacion.db") 
        cursor = connection.cursor()
        cursor.execute(f"SELECT id, nombreVacuna, cantidadRestante FROM Vacuna")
        mytable = from_db_cursor(cursor)
        print(mytable)
        id = funciones.verificarDatos("Ingrese el ID de la vacuna a modificar: ", 1)
        
        for i in db.Vacuna.select():
            if (int(i.id) == int(id)):
                    find = 1
        if(find == 1):
            dbEdit = db.Vacuna.select().where(db.Vacuna.id == id).get()
            txt = str(dbEdit.nombreVacuna)
            texto = f" Escriba ELiminar para confirmar su eleccion : "
            selecto = funciones.verificarDatos(texto, 2)
            if(selecto == "Eliminar"):
                dbEdit.delete_instance()
            else:
                input("Datos declinados pulse enter para volver al inicio")
                main()
        else:
            input("Datos declinados, pulse enter para al inicio")
            main()
    else:
        input("Datos declinados, pulse enter para ir al inicio")
        main()   