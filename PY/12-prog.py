import os
os.system("cls")

kWh = int(input("Cuantos  kWh consumes mensual? "))

if (kWh > 700):
    print("Debes pagar ", kWh*11.10)
elif (kWh > 301):
    print("Debes pagar ", kWh*10.86)
elif (kWh > 201):
    print("Debes pagar ", kWh*6.97)
else:
    print("Debes pagar ", kWh*4.44)
    