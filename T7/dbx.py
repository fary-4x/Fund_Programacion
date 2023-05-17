from peewee import *
import peewee

databasee = SqliteDatabase('LISENCIA.db')

class Motocicleta(Model):
   cedula = IntegerField()
   nombre = CharField(50)
   marca = CharField(50)
   modelo = CharField(50)
   placa = CharField(50)
   chasis = CharField(50)
   tel = IntegerField()
   direcc= CharField(50)
   lat = DoubleField()
   long = DoubleField()
   desc = CharField(50)
   actividad = CharField(50)
   class Meta:
       database = databasee
       
databasee.connect()
databasee.create_tables([Motocicleta])
