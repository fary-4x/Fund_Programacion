import os 
os.system('cls')
from peewee import *
from datetime import*


db= SqliteDatabase('Registro.db')

class Robos(Model):
    cedula= IntegerField()
    nombre= CharField(50)
    fecha= DateField()
    objeto= CharField()
    monto= IntegerField()
    ubicacion= CharField(50)
    latitud= FloatField()
    longitud= FloatField()
    
    class Meta:
        database= db

db.connect()
db.create_tables([Robos])