import os
os.system("cls")


frase = str(input("Ingrese su frase: "))


print("Tiene ",len(frase.replace(' ', '')), " caracteres sin contar espacios")
print("Tiene ",len(frase), " caracteres contando los espacios")

