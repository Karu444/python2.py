# Leer un archivo json para recuperar la estructura de datos lista

import json

with open("Ciclo 1/codigo/archivos-json/lista.json", "r") as archivo:
    lista = json.load(archivo)
    
if not archivo.closed:
    print("Cerrando archivo")
    archivo.close()

for elem in lista:
    print(elem, end=", ")