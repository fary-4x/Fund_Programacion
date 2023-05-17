import os
os.system("cls")

import math


cateto1 = int(input("Ingrese el cateto 1: "))
hipotenusa = int(input("Ingrese la hipotenusa: "))

print("El cateto ausente es: ",  math.sqrt(hipotenusa**2 - cateto1**2))