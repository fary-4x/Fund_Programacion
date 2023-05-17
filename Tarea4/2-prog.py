import os
os.system('cls')

A = int(input("Ingrese el primer angulo: "))
B = int(input("Ingrese el segundo angulo: "))
C = int(input("Ingrese el tercer angulo: "))
print("")
S_Angulos = (A+B+C)
if (S_Angulos > 180 or S_Angulos < 180):
     print("Su figura no es un triangulo"); exit(0)

if A==90 and B<90 and C<90 or A<90 and B==90 and C<90 or A<90 and B<90 and C==90:
    print ("Su figura es un triangulo")
elif A<90 and B<90 and C<90:
    print ("Su figura es un acutangulo")
else: 
    print ("Su figura es un obtusangulo")



