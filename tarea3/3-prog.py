import os
os.system('cls')

import requests 
import json 



url = "https://randomuser.me/api/?results=1"
Inf = requests.get(url).json()

print("______________________________________________________")
print("Titulo: ", Inf['results'][0]['name']['title'])
print("Nombre: ",Inf['results'][0]['name']['first'])
print("Apellido: ", Inf['results'][0]['name']['last'])
print("Fecha Nacimiento: ",Inf['results'][0]['dob']['date'])
print("Edad: ",Inf['results'][0]['dob']['age'])
print("______________________________________________________")
print("")





