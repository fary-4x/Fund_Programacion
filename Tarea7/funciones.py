import os
from prettytable import from_db_cursor
from peewee import *
import sqlite3


db= SqliteDatabase('LICENCIA.db')

class Motocicleta(Model):
    cedula= CharField()
    nombre=CharField()
    marca=CharField()
    modelo=CharField()
    placa=CharField()
    chasis=CharField()
    telefono=CharField()
    direccion=TextField()
    lat=CharField()
    long=CharField()
    actividad=CharField()
    descripcion=CharField()

    class Meta:
        Database = db

db.connect()
db.create_tables([Motocicleta])

def Agregar(main):
    os.system('cls') 
    base= Motocicleta()
    base.cedula = int(input("Ingrese su cedula "))
    base.nombre =str(input("Ingrese su nombre "))
    base.marca =str(input("Ingrese la marca del motor "))
    base.modelo = int(input("Ingrese el modelo del motor "))
    base.placa = int(input("Ingrese la placa del motor "))
    base.chasis = int(input("Ingrese el chasis del motor "))
    base.telefono = int(input("Ingrese su numero telefonico "))
    base.direccion= int(input("Ingrese su direccion "))
    base.lat= int(input("Ingrese la latitud"))
    base.long= int(input("Ingrese la longitud "))
    base.long= int(input("Ingrese la actividad del motor "))
    base.long= int(input("Ingrese la descripcion del motor "))
    
    base.save()
    ingre= int(input("Pulse 0 para ir al inicio o 1 para salir"))
    if ingre == 0: main()
    else: input("Presiona enter para salir")

def Mostrar_Datos(main):   
    os.system('cls')
    connection = sqlite3.connect("LICENCIA.db")
    cursor = connection.cursor() 
    cursor.execute("SELECT cedula, nombre, marca, modelo, placa, chasis, telefono, direccion, lat, long, actividad, descripcion FROM Motocicleta ")
    mytable = from_db_cursor(cursor)
    print(mytable)
    ingre= int(input("Pulse 0 para ir al inicio o 1 para salir"))
    if ingre == 0: main()
    else: input("Presiona enter para salir")



def Modificar(main):    
    os.system('cls')
    connection = sqlite3.connect("LICENCIA.db")
    cursor = connection.cursor() 
    cursor.execute("SELECT cedula, nombre, marca, modelo, placa, chasis, telefono, direccion, lat, long, actividad, descripcion FROM Motocicleta ")
    mytable = from_db_cursor(cursor)
    
    print(mytable)
    pedir = int(input("Ingrese la cedula que desea modificar"))

    tabla = Motocicleta.select().where(Motocicleta.cedula == pedir).get()
    print('Ingrese los nuevos datos o pulse 0 para mantener los datos')
    
    Nuevacedula = int(input('Ingrese la nueva cedula '))
    Nuevonombre = str(input('Ingrese el nuevo nombre '))
    Nuevamarca = str(input('Ingrese la nueva marca'))
    Nuevomodelo = int(input('Ingrese el nuevo modelo'))
    Nuevaplaca = int(input('Ingrese la nueva placa'))
    Nuevochasis = int(input('Ingrese el nuevo chasis'))
    Nuevotele = int(input('Ingrese el nuevo telefono'))
    Nuevadire = int(input('Ingrese la nueva direccion'))
    Nuevalat = int(input('Ingrese la nueva latitud'))
    Nuevalong = int(input('Ingrese la nueva longitud'))
    Nuevaactividad = int(input('Ingrese la nueva actividad'))
    Nuevadesc= int(input('Ingrese la nueva descripcion'))
    
    