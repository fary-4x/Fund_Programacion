import os
os.system("cls")

import datetime


hoy = datetime.date.today()
dia = int(input("Ingresa el dia que naciste: "))
mes = int(input("Ingresa tu mes de nacimiento en formato numero: "))
age = int(input("Ingresa tu año de nacimiento: "))

age = hoy.year - age

if (mes < int(hoy.strftime("%m"))):
    print("Tienes ", age, " años")
    
elif(dia <= int(hoy.strftime("%d")) and mes == int(hoy.strftime("%m"))):
    print("Tienes ", age, " años")    

else:
    print("Tienes ", age-1, " años")    
