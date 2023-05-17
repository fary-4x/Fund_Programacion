from tkinter import *
import os
os.system('cls')
import tkinter 
import webbrowser

datos = Tk()
datos.title("Datos")
datos.geometry("350x200")


nombre= Entry(datos)
nombre.grid(row=2, column=1, columnspan=12, sticky=W+E)

apellido= Entry(datos)
apellido.grid(row=4, column=1,columnspan=12, sticky=W+E)

tel= Entry(datos)
tel.grid(row=6, column=1,columnspan=12, sticky=W+E)

correo= Entry(datos)
correo.grid(row=8, column=1,columnspan=12, sticky=W+E)

text1= Label(datos, text= 'Ingrese su nombre')
text1.grid(row=1, column=1)

text2= Label(datos, text= 'Ingrese su apellido')
text2.grid(row=3, column=1)

text3= Label(datos, text= 'Ingrese su numero telefonico')
text3.grid(row=5, column=1)

text4= Label(datos, text= 'Ingrese su correo eletronico')
text4.grid(row=7, column=1)



def ingresar():
    n= str(nombre.get())
    a= str(apellido.get())
    t= int(tel.get())
    c= str(correo.get())

    html= open('html.html', 'w')
    html.write(f"""
    <html>
        <head>
           <body style="background:#FFEBCD">
                 <center>
                    <ul>
                    <div><li><b><h1>Datos Personales</h1></div></li>
                    <div><li><b><h4>Nombre:</b> {n}</h4></div></li>
                    <div><li><b><h4>Apellido:</b> {a}</h4></div></li>
                    <div><li><b><h4>Telefono:</b> {t}</h4></div></li>
                    <div><li><b><h4>Email:</b> {c}</h4></div></li>
                    </ul>   
                 </center>
           <body>    
        </head>
    </html> """)
    
    html.close()
    webbrowser.open('html.html')



boton1= Button(datos, text= 'Aceptar', command= ingresar)
boton1.grid (row=9,column=1 )


datos.mainloop()