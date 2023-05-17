import os
import webbrowser
import folium
import peewee
from db import *
from peewee import *
from prettytable import PrettyTable

tabla= PrettyTable()


def fecha(m):
    print(m)
    d= int(input('🢚Ingrese el dia de nacimiento'))
    ms= int(input('🢚Ingrese el mes de nacimiento'))
    a= int(input('🢚Ingrese el año de nacimiento'))
    return date(a, ms, d)

def Agregar():
    os.system('cls')
    p = Personajes()
    print('Ingrese los datos requeridos acontinuacion...')
    p.serie= input('Ingrese a que serie pertenece su personajes: ' )
    p.nombre= input('Ingrese el nombre del personaje a registrar: ' )
    p.apellido= input('Ingrese el apellido del anime a registrar:' )
    p.pronunc= input('Ingrese la pronunciacion del nombre del personaje: ' )
    p.estado= input('Ingrese el estado de vida del personaje: ' )
    p.sexo= input('Ingrese el sexo del personaje: ' )
    p.fecha = fecha('Ingrese la fecha de nacimiento del personaje: ' )
    p.zodiaco= input('Ingrese el signo zodiacal del personaje: ' )
    p.edad=int(input('Ingrese la edad del personaje: '))
    p.poder= input('Ingrese el poder del personaje: ' )
    p.frase= input('Ingrese la frase favortita del personaje: ' )
    p.vestimenta= input('Ingrese descripcion de la vestimenta del personaje: ' )
    p.altura=input('Ingrese la altura del personaje:' )
    p.foto= input('Ingrese el URL de la foto del personaje: ' )
    p.direccion=input('Ingrese donde vive el personaje: ')
    p.lat=input('Ingrese la latitud de donde vive el personaje:' )
    p.long= input('Ingrese la longitud de donde vive el personaje: ' )
    p.save()
    
    input('Los datos han sido guardados, pulse enter para continuar...')

def confirmar(campo, valor):
    os.system('cls')
    print(" El Campo "+campo+" posee el valor "+valor)
 
    dat= input(" Digite un valor nuevo o dejelo en blanco para continuar: ")
    print("")
    if dat =="":
        return valor
    else:
        return dat

def mostrarest():
    os.system('cls')
    tabla.field_names =["ID","serie", "nombre", "apellido", "pronunc", "estado", "sexo", "fecha", "zodiaco", "edad", "poder", "frase", "vestimenta", "altura", "foto", "direccion", "lat", "long"]

    for p in Personajes.select():
        
        tabla.add_row([p.id, p.serie, p.nombre, p.apellido, p.pronunc,p.estado, p.sexo, p.fecha, p.zodiaco, p.edad, p.poder, p.frase, p.vestimenta, p.altura, p.foto, p.direccion, p.lat, p.long])
    
    return tabla
    

def Modificar():
    os.system('cls')
    print("Acontinuacion modificara un personaje")
    print("")
    print(mostrarest())
    
    idx=input("Digite el ID a Editar o pulse X para Cancelar: ")
    print("")
 
    if idx=="x" or idx=="X":
        return False
    else:
        mod=input(f"Se va a modificar todo lo que contiene el ID {idx}, presio Si o No para continuar: ")
       
        if mod=="no"or mod=="No" or mod=="":
            return False
        elif mod=="Si" or mod=="si":
            p=Personajes.select().where(Personajes.id==idx).get()
            print("")
            p.serie= confirmar('serie', p.serie)
            print("")
            p.nombre = confirmar('nombre', p.nombre)
            print("")
            p.apellido = confirmar('apellido', p.apellido)
            print("")
            p.pronunc = confirmar('pronunc', p.pronunc)
            print("")
            p.estado = confirmar('estado',p.estado)
            print("")
            p.sexo = confirmar('sexo', p.sexo)
            print("")
            p.fecha = str(confirmar('fecha', str(p.fecha)))
            print("")
            p.zodiaco = confirmar('zodiaco', p.zodiaco)
            print("")
            p.edad = int(confirmar('edad', str(p.edad)))
            print("")
            p.poder = confirmar('poder', p.poder)
            print("")
            p.frase = confirmar('frase', p.frase)
            print("")
            p.vestimenta =confirmar('vestimenta', p.vestimenta)
            print("")
            p.altura = str(confirmar('altura', str(p.altura)))
            print("")
            p.foto = confirmar('foto', p.foto)
            print("")
            p.direccion = confirmar('direccion', p.direccion)
            print("")
            p.lat = str(confirmar('lat', str(p.lat)))
            print("")
            p.long = str(confirmar('long', str(p.long)))
            print("")
            p.save()
           
            input(" Modificacion exitosa")
    
   
def Eliminar():
    os.system('cls')
    for p in Personajes.select():
        print(f"{p.id} {p.serie}, {p.nombre}, {p.apellido}")
    idx= input('Ingrese ID del perosnaje a eliminar o pulse x para cancelar: ' )
    if idx =="x":
        return False  
    p=Personajes.select().where(Personajes.id==idx).get() 
    p.delete_instance()
    input(" Eliminacion exitosa")

 

def Gestionar():
        os.system('cls')
        print("""
        ╔══════════════════════════════════════════════╗
        ║              ¡ELIGE TU OPCION!               ║
        ║══════════════════════════════════════════════║
        ║                1-Agregar                     ║
        ║                2-Modificar                   ║
        ║                3-Eliminar                    ║
        ╚══════════════════════════════════════════════╝
        """)
        op= input('Digite la opcion que necesite: ')   
        if op == '1':
            Agregar()
        elif op =='2':
            Modificar()
        elif op =='3':
            Eliminar()
        else:
            input('Digite una opcion valida...')

#---------------------------------------------------------------------------#

def Agregar1():
    os.system('cls')
    s= Series()
    print('Ingrese los datos requeridos acontinuacion...')
    s.serie= input('Ingrese el nombre de la serie animada: ' )
    s.CantidaPersonajes=input('ingrese la cantidad de personajes: ' )
    s.save()
    input('Datos registrados exitosamente, pulse enter para continuar...')

def confirmar1(campo, valor):
    os.system('cls')
    print(" El Campo "+campo+" posee el valor "+valor)
 
    dat= input(" Digite un valor nuevo o dejelo en blanco para continuar: ")
    print("")
    if dat =="":
        return valor
    else:
        return dat

def mostrar():
    os.system('cls')
    tabla.field_names =["ID", "serie", "CantidaPersonajes"]

    for s in Series.select():
        
        tabla.add_row([s.id, s.serie, s.CantidaPersonajes])
    
    return tabla
    
def Modificar2():
    os.system('cls')
    print("Acontinuacion modificara un personaje")
    print("")
    print(mostrar())
    
    idx=input("Digite el ID a Editar o pulse X para Cancelar: ")
    print("")
 
    if idx=="x" or idx=="X":
        return False
    else:
        mod=input(f"Se va a modificar todo lo que contiene el ID {idx}, presio Si o No para continuar: ")
       
        if mod=="no"or mod=="No" or mod=="":
            return False
        elif mod=="Si" or mod=="si":
            s=Series.select().where(Series.id==idx).get()
            print("")
            s.serie = confirmar1('serie', s.serie)
            print("")
            s.CantidaPersonajes = confirmar1('CantidaPersonajes', s.CantidaPersonajes)
            print("")
            s.save()
           
            input(" Modificacion exitosa")

def Eliminar3():
    os.system('cls')
    for s in Series.select():
        print(f"{s.id}, {s.serie}")
    idx= input('Ingrese ID del perosnaje a eliminar o pulse x para cancelar: ' )
    if idx =="x":
        return False  
    p=Series.select().where(Series.id==idx).get() 
    p.delete_instance()
    input(" Eliminacion exitosa")

def Configuracion():
    os.system('cls')
    
    print("""          
    ╔══════════════════════════════════════════════╗
    ║              ¡ELIGE TU OPCION!               ║
    ║══════════════════════════════════════════════║
    ║                1-Agregar                     ║
    ║                2-Modificar                   ║
    ║                3-Eliminar                    ║
    ╚══════════════════════════════════════════════╝""")
    
    op= input('Digite la opcion que necesite: ')   
    if op == '1':
        Agregar1()
    elif op =='2':
        Modificar2()
    elif op =='3':
        Eliminar3()
    else:
        input('Digite una opcion valida...')


#------------------------------------------------------------------------------#

def exportar():
    os.system('cls')
    for p in Personajes.select():
        print(p.id, p.nombre)
    v=input('Digite el ID que desea exportar: ' )
    p= Personajes.select().where(Personajes.id == v).get()
    html= f"""
    <!DOCTYPE html>
    <html>
        <head>

            <title>ANIME</title>
        </head>
        <body>
         <div>
                <center>
                    <h1>DATOS DEL ASALTADO</h1>
                </center>
                <br>
                <center>
                    <h2>Foto del personaje:<b><img src={p.foto}></b></h2>
                    <h2>Nombre del personaje:<b>{p.serie}</b></h2>
                    <h2>Nombre del personaje:<b>{p.nombre}</b></h2>
                    <h2>Apellido del personaje:<b>{p.apellido}</b></h2>
                    <h2>Pronunciacion:<b>{p.pronunc}</b></h2>
                    <h2>Estado de vida:<b>{p.estado}</b></h2>
                    <h2>Sexo:<b>{p.sexo}</b></h2>
                    <h2>Fecha de nacimiento:<b>{p.fecha}</b></h2>
                    <h2>Signo Zodiacal:<b>{p.zodiaco}</b></h2>
                    <h2>Edad :<b>{p.edad}</b></h2>
                    <h2>Poder del personaje:<b>{p.poder}</b></h2>
                    <h2>Descripcion de vestimenta:<b>{p.vestimenta}</b></h2>
                    <h2>Dirreccion:<b>{p.direccion}</b></h2>
                    <h2>Latitud:<b>{p.lat}</b></h2>
                    <h2>Longitud:<b>{p.long}</b></h2>
                    
                </center>
          </div>
        </body>
    </html>"""
    f = open('Personajes.html', 'w')
    f.write(html)
    f.close()
    webbrowser.open('Personajes.html')

def Mapa():
    os.system('cls')
    for p in Personajes.select():
        print(p.id, p.serie, p.nombre)
    v=input('Digite el ID que desea exportar: ' )
    p= Personajes.select().where(Personajes.id == v).get()
    
    m= folium.Map(location=[18.5236, -69.6750], zoomstart=10)
    tooltip='Pulse acá para mas inf.'
    folium.Marker(location=[p.lat, p.long], popup=f"<b>Nombre: {p.nombre} <hr> <b>Apellido: </b>{p.apellido} <hr> <b>Fecha de nacimiento:</b> {p.fecha}",tooltip=tooltip).add_to(m)
    
    m.save('Mapa.html')
    webbrowser.open('Mapa.html')


def Reportes():
    os.system('cls')
    print("""
        ╔══════════════════════════════════════════════╗
        ║              ¡ELIGE TU OPCION!               ║
        ║══════════════════════════════════════════════║
        ║       1-Mapa                                 ║
        ║       2-Exportar personaje                   ║
        ║       3-Listado de estado de vida            ║
        ╚══════════════════════════════════════════════╝ """)
    op= input('Ingrese la opcion que desee: ' )
    if op == '1':
        Mapa()
    elif op == '2':
        exportar()
    elif op == '3':
        print("")
        estados = [[0,"Vivo"],
                  [0, "Muerto"],
                  [0, "Indefinido"]]
        print("")
        for a in Personajes.select():
            for b in range(len(estados)):
                if (a.estado == estados[b][1]):
                    estados[b][0] += 1
        print("")            
        for a in range(len(estados)):
            if (estados[a][0] != 0):
                print(f"{estados[a][1]} Esta es su cantidad : {estados[a][0]}  de personajes")
        print("")
        for a in Personajes.select().order_by(Personajes.estado):
             print (f"{a.estado}")
#-----------------------------------------------------------------------------#
def AcercaD():
    os.system('cls')
    yt= (f"https://youtu.be/GODmA6ypAz4")
    webbrowser.open(yt)

