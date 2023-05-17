import os
os.system("cls")


pan = int(input("¿Con cuantos panes cueta? ")) #1
carne = int(input("¿Con cuantas carnes cuenta? ")) #2
tocineta = str(input("¿Con cuantas libras de tocineta cuenta? ")) #1/5
cantidadTotal = pan
if(tocineta.count('/') == 1):
    counter = tocineta.index('/')
    tocineta1 = int(tocineta[:counter].replace(' ', ''))
    tocineta2 = int(tocineta[counter+1:].replace(' ', ''))
    tocineta = tocineta1/tocineta2
else:
    tocineta = int(tocineta)

tocineta = int(tocineta/0.2)

if(cantidadTotal > carne):
    cantidadTotal = carne
elif(cantidadTotal > tocineta):
    cantidadTotal = tocineta
    
print("Con esos ingredientes puedes hacer ", cantidadTotal, " hamburguesas")