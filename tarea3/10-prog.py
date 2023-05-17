import os
os.system('cls')

import requests
import json

Nombre= input('Ingrese su nombre: ')
Apellido= input('Ingrese su Apellido: ')
Telefono= input('Ingrese su numero de telefono: ')
Email= input('Ingrese su direccion de correo eletronico: ')

print('Nombre:',Nombre)
print('Apellido:',Apellido)
print('telefono:',Telefono)
print('Email: ',Email)

html= f"""
<html>
    <head>
     <body style="background:#FFEBCD">
          <center>
          <ul>
          <div><li><b><h1>Datos Personales</h1></div></li>
          <div><li><b><h4>Nombre:</b> {Nombre}</h4></div></li>
          <div><li><b><h4>Apellido:</b> {Apellido}</h4></div></li>
          <div><li><b><h4>telefono:</b> {Telefono}</h4></div></li>
          <div><li><b><h4>email:</b> {Email}</h4></div></li>
          </ul>   
          </center>
   </head>
</html>
"""
archivo= open('html.html', 'w')
archivo.write(html)
archivo.close()