from tkinter import *
import os
os.system('cls')
import tkinter 

prom = Tk()
prom.title("Promedio")
prom.geometry("350x200")

nota1= Entry(prom)
nota1.grid(row=2, column=1, columnspan=12, sticky=W+E)

nota2= Entry(prom)
nota2.grid(row=4, column=1,columnspan=12, sticky=W+E)

nota3= Entry(prom)
nota3.grid(row=6, column=1,columnspan=12, sticky=W+E)

nota4= Entry(prom)
nota4.grid(row=8, column=1,columnspan=12, sticky=W+E)

text1= Label(prom, text= 'Ingrese la primer nota')
text1.grid(row=1, column=1)

text2= Label(prom, text= 'Ingrese la segunda nota')
text2.grid(row=3, column=1)

text3= Label(prom, text= 'Ingrese la tercera nota')
text3.grid(row=5, column=1)

text4= Label(prom, text= 'Ingrese la cuarta nota')
text4.grid(row=7, column=1)

promedio= Label(prom)
promedio.grid(row=11,column=1)

literal= Label(prom)
literal.grid(row=12,column=1 )

def Ingresar():
    n1= int(nota1.get())
    n2= int(nota2.get())
    n3= int(nota3.get())
    n4= int(nota4.get())
    finalp= (n1+n2+n3+n4)/4
    promedio.config(text=finalp)
    
    
    if  finalp >=90: eqiv= 'A'
    elif finalp >=80: eqiv= 'B'
    elif finalp >=70: eqiv= 'C'
    else: eqiv= 'F'
    literal.config(text= eqiv)


boton1= Button(prom, text= 'Aceptar', command= Ingresar)
boton1.grid (row=9,column=1 )



prom.mainloop()