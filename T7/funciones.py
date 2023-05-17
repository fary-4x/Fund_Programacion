from logging import exception
import dbx
import folium
import webbrowser

def Mostrar(txtt):
    input(f"{txtt} Pulse enter para continuar...")

def entrada (txt, tipo='str'):
    tpm = input(f"{txt}: ")
    if (len(tpm) == 0):
        tpm = entrada(txt, tipo)

    if (tpm == 'number'):
        try:
            tpm = float(tpm)
        except Exception:
            Mostrar('Ingrese un numero valido')
            tpm = entrada(txt, tipo)
   
    return tpm



def Agregar():

    dat= dbx.Motocicleta()
    dat.cedula = entrada("Ingrese su cedula ")
    dat.nombre =entrada("Ingrese su nombre ")
    dat.marca =entrada("Ingrese la marca del motor ")
    dat.modelo = entrada("Ingrese el modelo del motor ")
    dat.placa =entrada ("Ingrese la placa del motor ")
    dat.chasis = entrada("Ingrese el chasis del motor ")
    dat.tel = entrada("Ingrese su numero telefonico ")
    dat.direcc= entrada("Ingrese su direccion ")
    dat.lat= entrada("Ingrese la latitud", tipo='number')
    dat.long= entrada("Ingrese la longitud ",tipo='number')
    dat.desc= entrada("Ingrese la actividad del motor ")
    dat.actividad= entrada("Ingrese la descripcion del motor ")
    dat.save()
    Mostrar('Motor agregado')

def Mapa():
    Mostrar('A continuacion se mostrara el Mapa con todos los motores registrados')

    m = folium.Map(location=[18.9649, -70.2956], zoom_start=10)

    tooltip = "Click para ver mas!"
    
    for dat in dbx.Motocicleta.select():
        folium.Marker([dat.lat, dat.long  ], popup= f"{dat.marca} {dat.modelo}", ).add_to(m)

    m.save("Mapa.html")
    
    webbrowser.open('Mapa.html')



