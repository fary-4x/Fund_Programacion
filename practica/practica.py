#Farinel Rosa Reyes (2021-1042)

import os
os.system('cls')
  
import re
import requests
import json
import webbrowser

cedula = input( " Ingrese una cedula " )
cedula = re.sub('[-]', '', cedula)
url = f"https://api.adamix.net/apec/cedula/{cedula}"
datos = requests.get(url).json()


foto = (datos['foto'])
nombre = (datos['Nombres'])
apellido = (datos['Apellido1'])+" "+(datos['Apellido2'])
fnacimiento = (datos['FechaNacimiento'])
edad = (2021 - int(fnacimiento[:4]))
sexo = (datos['IdSexo'])

if sexo == 'M':
    sexo = 'Masculino'
else: 
    sexo = 'Femenino'

dia = fnacimiento[8:10]
mes = fnacimiento[5:7]
dia = int(dia)
mes = int(mes)

zodiaco =['CAPRICORNIO', 'PISCIS', 'ARIES', 'TAURO', 'GEMINIS','CANCER', 'LEO', 'VIRGO', 'LIBRA', 'ESCORPIO', 'SAGITARIO' ]

fechas=[20, 19, 20, 20, 21, 22, 22, 22, 22, 22, 21]

mes = mes - 1

if dia > fechas[mes]:
    mes = mes + 1

if mes == 12: 
    mes = 0

zodiacos = zodiaco[mes]

c = open('parcial.html', 'w')
c.write(f"""

<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>Parcial</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <link rel='stylesheet' type='text/css' media='screen' href='style.css'>
    <script src='main.js'></script>
</head>

<center>
 <br>
 <br>
 <img src= "{foto}"
</center>


<body>
  <br>
  <br>
  <font size = 6>
     <b>Nombres: </b>{nombre}<br>
     <b>Apellidos: </b>{apellido}<br>
     <b>Fecha De Nacimiento: </b>{fnacimiento}<br>
     <b>Edad: </b>{edad}<br>
     <b>Sexo: </b>{sexo}<br>
     <b>Signo Zodiacal: </b>{zodiacos}<br>
  </font>
</body>

</html>

""")
c.close()
webbrowser.open('parcial.html')
