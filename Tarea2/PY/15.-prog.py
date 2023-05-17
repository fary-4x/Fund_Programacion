import os
os.system("cls")

kmPorGalon = int(input("Introduce la cantidad de km por galon que da tu automovil: "))
distancia = int(input("Introduce la distancia en Km que piensas recorrer: "))
kmPorGalon = kmPorGalon*distancia
print("La gasolina regular esta a 239.30 entonces debes comprar ", kmPorGalon*239.30, " pesos en gasolina para hacer dicho viaje")