import os
os.system('cls')

import requests 
import webbrowser

cant = input("Ingrese la cantidad de usuarios que desea ver : ")
Dts = requests.get("https://randomuser.me/api/?results="+cant).json()
 
rose= []
hombres = 0 
mujeres = 0

for persona in Dts ["results"]: 
    if persona ['gender'] == 'male':
        hombres = hombres + 1

    else: 
        mujeres = mujeres + 1
    fila = f"""
        <div class="col-md-2 text-center">
            <div>
                <img class="img-fluid" src="{persona['picture']['large']}"/>"
            </div>
            {persona['name']['first']}
            {persona['name']['last']}
            ({persona['gender']})
        </div>
    """
    rose.append(fila)

Total_per = "".join(rose)

html = """
<html> 
    <head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" integrity="undefined" crossorigin="anonymous">
    </head>
    <body class="container">
        <div class="row">
            #personas
        </div>
            mujeres: #mujeres hombre: #hombres total: #total
        <div>
        </div>
    </body>
</html>
"""
html = html.replace('#personas', Total_per)
html = html.replace('#mujeres', str(mujeres))
html = html.replace('#hombres', str(hombres))
html = html.replace('#total', str(hombres + mujeres))

f = open ('Fary.html', 'w', encoding="utf-8")
f.write(html)
f.close()

webbrowser.open('Fary.html')