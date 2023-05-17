import os
import sqlite3
import webbrowser
import folium
from prettytable import from_db_cursor, prettytable
from db import *



def fecha(m):
    print(m)
    d= int(input('🢚 Ingrese el dia del asalto: ' ))
    ms= int(input('🢚 Ingrese el mes del asalto: ' ))
    a= int(input('🢚 Ingrese el año del asalto: ' ))
    
    return date(a,ms,d)


def Agregar():
    os.system('cls')
    r= Robos()
    print('Ingrese los datos que se le pide a continuacion: ' )
    r.cedula= input('Ingrese su cedula: ' )
    r.nombre= input ('Ingrese su nombre: ' )
    r.fecha= fecha ('Ingrese la fecha del asalto 🢛: ' )
    r.objeto= input('Ingrese el objeto robado: ' )
    r.monto= input('Ingrese el valor en RD$: ' )
    r.ubicacion= input('Ingrese el lugar donde ocurrio el asalto: ' )
    r.latitud= input('Ingrese la latitud de la ubicacion del asalto: ' )
    r.longitud= input('Ingrese la longitud de la ubicacion del asalto: ' )
    r.save()
    
    input('Los datos han sido guardados con exito, pulse enter para continuar... ')

def Modificar():
    connection = sqlite3.connect("Registro.db")
    cursor = connection.cursor()
    cursor.execute("SELECT id, cedula, nombre, fecha, objeto, monto, ubicacion, latitud, longitud FROM Robos")
    mytable = from_db_cursor(cursor) 
    print(mytable) 


def Exportar():
  for r in Robos.select():
    print(r.id, r.nombre)
  v= input('Digite el ID : ')
  r= Robos.select().where(Robos.id == v).get()
  html= f""" 
            <!DOCTYPE html>
    <html>
        <head>
   
         <title>DATOS</title>
        </head>
        <body>
            <div>
            <center>
             <h1>DATOS DEL ASALTADO</h1>
            </center>
            <br>
            <center>
                <h2>Cedula: <b>{r.cedula}</b></h2>
                <h2>Nombre: <b>{r.nombre}</b></h2>
                <h2>Fecha del robo: <b>{r.fecha}</b></h2>
                <h2>Objeto robado: <b>{r.objeto}</b></h2>
                <h2>Valor en RD$: <b>{r.monto}</b></h2>
                <h2>Ubicacion del asalto: <b>{r.ubicacion}</b></h2>
                <h2>Latitud: <b>{r.latitud}</b></h2>
                <h2>Longitud: <b>{r.longitud}</b></h2>
            </center>
            </div>
        </body>
    </html>"""

  f = open('Robos.html', 'w')
  f.write(html)
  f.close()
  webbrowser.open('Robos.html')

def Mapa():
  for r in Robos.select():
    print(r.id, r.nombre)
  v= input('Digite el ID : ')
  r= Robos.select().where(Robos.id == v).get()
  tooltip ='Pulse aca'
  robos= Robos.select()
  m = folium.Map(location=[18.5236, -69.6750], zoomstart=10)
  
  for r in robos:
      folium.Marker([r.latitud, r.longitud], popup=f"<b>{r.nombre} <hr> <b>Objeto Robado: </b>{r.objeto} <hr> <b>Fecha del asalto:</b> {r.fecha} <hr> <b>Valor RD$:</b>{r.monto} ",tooltip=tooltip).add_to(m)
  
  m.save('Mapa.html')
  webbrowser.open('Mapa.html')
  

