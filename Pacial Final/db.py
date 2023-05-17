from peewee import SqliteDatabase
from datetime import *
from peewee import *

db = SqliteDatabase('ANIME.db')



class Personajes(Model): 
    serie = CharField()
    nombre= CharField()
    apellido= CharField()
    pronunc= CharField()
    estado= CharField()
    sexo= CharField()
    fecha= DateField()
    zodiaco= CharField()
    edad= IntegerField()
    poder= CharField()
    frase= CharField()
    vestimenta= CharField()
    altura= IntegerField()
    foto= CharField()
    direccion= CharField()
    lat= FloatField()
    long= FloatField()
     
    class Meta:
        database= db

class Series(Model):
    serie= CharField()
    CantidaPersonajes= CharField()
    class Meta:
        database = db

db.connect() 
db.create_tables([Personajes, Series])       
