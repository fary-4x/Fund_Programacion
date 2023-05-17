import os
os.system("cls")
import math

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingreses el valor de b: "))
c = int(input("Ingrese el valor de c: "))

x1 = (-b+math.sqrt(b**2-(4*a*c)))/(2*a)
x2 = (-b-math.sqrt(b**2-(4*a*c)))/(2*a)
print("x1 = ", x1)
print("x2 = ", x2)