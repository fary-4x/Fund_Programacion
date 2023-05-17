import os
os.system('cls')
import requests
import json


Ciu_pais = str(input("Ingrese el nombre de la ciudad o pais que guste para identificar su clima :" ))

Api=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={Ciu_pais}&appid=0a507ba4a506456cbbd40b0c8b19fc65").json()


temp = float(Api['main']['temp'])
tempMax = float(Api['main']['temp_max'])
tempMin = float(Api['main']['temp_min'])


print("*************************************")

print("Temperatura: ",int(temp-273.15 ),"°C")
print("Temperatura maxima: ",int(tempMax-273.15),"°C" )
print("Temperatura minima: ",int(tempMin-273.15),"°C" )

print("*************************************")