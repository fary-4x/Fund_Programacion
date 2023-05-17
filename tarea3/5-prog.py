import os
os.system('cls')

import requests
import json

search = str(input("Ingresa lo que quieres buscar: "))
url = requests.get(f'https://es.wikipedia.org/w/api.php?action=query&list=search&srprop=snippet&format=json&origin=*&utf8=&srsearch={search}').json()

print("__________________________________________________________________________________________")

for info in url['query']['search']:
    print("Titulo", info['title'])
    descp = info['snippet']
    print("Descripcion:", descp.replace('span class=\"searchmatch\">','').replace('<','').replace('/span>',''))
   
print("___________________________________________________________________________________________")



