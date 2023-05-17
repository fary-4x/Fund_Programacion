import os
os.system('cls')

n1 = int (input("Ingrese su primer numero: "))
n2 = int(input("Ingrese su segundo numero: "))
n3 = int(input("Ingrese su tercer numero: "))

M = n1 

if n2 > M: 
    M = n2
if n3 > M: 
    M = n3
print("El numero mayor ingresado es: ",M)
