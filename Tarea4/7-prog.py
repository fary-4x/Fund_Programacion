import os
os.system('cls')

Frase= str(input("Ingrese su frase: "))


V= {'a':0,'e':0,'i':0,'o':0,'u':0,}

a=0
e=0
i=0
o=0
u=0

for let in Frase:
    if let in V:
        V[let] +=1
        print(let)

print(V)
