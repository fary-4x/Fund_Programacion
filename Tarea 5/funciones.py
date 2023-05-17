import os
from prettytable import from_db_cursor
from peewee import *
import sqlite3
import webbrowser

db = SqliteDatabase('Base_Estudiantil.db')

class Base_Estudiantil(Model):
   MatriEstu = IntegerField()
   NombreEstu = CharField(50)
   ApellidosEstu = CharField(50)
   N1 = IntegerField()
   N2 = IntegerField()
   Calificacion = CharField(1)
   class Meta:
       database = db
       
db.connect()
db.create_tables([Base_Estudiantil])

def Ingresar(main):
    os.system('cls')
    base =Base_Estudiantil()
    base.MatriEstu = int(input("Ingrese la matricula estudiantil "))
    base.NombreEstu =str(input("Ingrese el nombre del estudiante "))
    base.ApellidosEstu =str(input("Ingrese el apellido del estudiante "))
    base.N1 = int(input("Ingrese la primera nota "))
    base.N2 = int(input("Ingrese la segunda nota "))
    
    if  base.N1 + base.N2/2 >90 : base.Calificacion = 'A'
    elif base.N1 + base.N2/2 >80 : base.Calificacion = 'B'
    elif base.N1 + base.N2/2 >70 : base.Calificacion = 'C'
    else: base.Calificacion = 'F'
    base.save()
    ingre= int(input("Pulse 0 para ir al inicio o 1 para salir"))
    if ingre == 0: main()
    else: input("Presiona enter para salir")

def Mostrar_Datos(main):   
    os.system('cls')
    connection = sqlite3.connect("Base_Estudiantil.db")
    cursor = connection.cursor() 
    cursor.execute("SELECT MatriEstu, NombreEstu, ApellidosEstu, N1, N2, Calificacion FROM Base_Estudiantil ")
    mytable = from_db_cursor(cursor)
    print(mytable)
    ingre= int(input("Pulse 0 para ir al inicio o 1 para salir"))
    if ingre == 0: main()
    else: input("Presiona enter para salir")


def Modificar(main):    
    os.system('cls')
    connection = sqlite3.connect("Base_Estudiantil.db")
    cursor = connection.cursor() 
    cursor.execute("SELECT MatriEstu, NombreEstu, ApellidosEstu, N1, N2, Calificacion FROM Base_Estudiantil ")
    mytable = from_db_cursor(cursor)
    
    print(mytable)
    pedir = int(input("Ingrese la matricula que desea modificar"))

    tabla = Base_Estudiantil.select().where(Base_Estudiantil.MatriEstu == pedir).get()
    print('Ingrese los nuevos datos o pulse 0 para mantener los datos')
    
    NuevoMatricula = int(input('Ingrese la nueva matricula '))
    NuevoNombre = str(input('Ingrese el nuevo nombre '))
    NuevoApellido = str(input('Ingrese los nuevos apellidos '))
    NuevoN1 = int(input('Ingrese la nueva primer nota'))
    NuevoN2 = int(input('Ingrese la nueva segunda nota'))
    NotaFinal = ""
    
    if NuevoMatricula == 0: NuevoMatricula = tabla.MatriEstu
    if NuevoNombre == '0': NuevoNombre = tabla.NombreEstu
    if NuevoApellido == '0': NuevoApellido = tabla.ApellidosEstu
    if NuevoN1 == 0: NuevoN1 = tabla.N1
    if NuevoN2 == 0: NuevoN2 = tabla.N2
    
    if   NuevoN1+NuevoN2/2 >90 : NotaFinal= 'A'
    elif NuevoN1+NuevoN2/2 >80 : NotaFinal= 'B'
    elif NuevoN1+NuevoN2/2 >70 : NotaFinal= 'C'
    else:NotaFinal= 'F'
    
   
    print(f"""
                Para cambiar los datos pulse 0 para confirmar
              
                            Matricula: {tabla.MatriEstu} ---> {NuevoMatricula}
                            Nombre: {tabla.NombreEstu} ---> {NuevoNombre}
                            Apellido: {tabla.ApellidosEstu} ---> {NuevoApellido}
                            Calificacion 1: {tabla.N1} ---> {NuevoN1}
                            Calificacion 2: {tabla.N2} ---> {NuevoN2}
                            Calificacion Final: {tabla.Calificacion} ----> {NotaFinal}
                            
              """)
    confirmar = int(input())
    if confirmar == 0:  
        tabla.MatriculaEstu = NuevoMatricula
        tabla.NombreEstu = NuevoNombre
        tabla.ApellidosEstu = NuevoApellido
        tabla.N1 = NuevoN1
        tabla.N2= NuevoN2
        tabla.Calificacion = NotaFinal
        tabla.save()
        ingre= int(input("Pulse 0 para ir al inicio o 1 para salir"))
        if ingre == 0: main()
        else: input("Presiona enter para salir")
    else: 
        input("Cambios descartados, presiona enter para ir al inicio")
        main()

def Eliminar(main):
    os.system('cls')
    connection = sqlite3.connect("Base_Estudiantil.db")
    cursor = connection.cursor() 
    cursor.execute("SELECT MatriEstu, NombreEstu, ApellidosEstu, N1, N2, Calificacion FROM Base_Estudiantil ")
    mytable = from_db_cursor(cursor)
    print(mytable)
    pedir = int(input("Ingrese la matricula que desea eliminar"))
    tabla = Base_Estudiantil.select().where(Base_Estudiantil.MatriEstu == pedir).get()
    confirmar= int(input('Pulse 0 para confirmar'))
   
    if confirmar == 0:
        tabla.delete_instance()
        input("Eliminacion Exitosa, presiona enter para ir al inicio")
        main()
    else: 
        input("Eliminacion Descartada, presiona enter para ir al inicio")
        main()
    


def Exportar():
    os.system('cls')
    connection = sqlite3.connect("Base_Estudiantil.db")
    cursor = connection.cursor()
    cursor.execute("SELECT MatriEstu, NombreEstu, ApellidosEstu, N1, N2, Calificacion FROM Base_Estudiantil")
    databaseForHTML = from_db_cursor(cursor)
    databaseForHTML = databaseForHTML.get_html_string()
    databaseForHTML = databaseForHTML.replace('<table>', '<table class="table table-bordered>"')
    html = f"""
    
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <title>Database</title>
</head>
<body>
    <div class = 'container'>
        {databaseForHTML}
    </dib>
</body>
</html>
    """
    name = str(input("Con que nombre quieres exportar la tabla? "))
    file = open(name+'.html', 'x')
    file.write(html)
    file.close()
    webbrowser.open(name+'.html')