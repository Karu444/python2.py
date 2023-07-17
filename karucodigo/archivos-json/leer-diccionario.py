# Leer un archivo json para recuperar la estructura de datos diccionario

import json

with open("Ciclo 1/codigo/archivos-json/diccionario.json", "r") as archivo:
    midic = json.load(archivo)
    
if not archivo.closed:
    print("Cerrando archivo")
    archivo.close()

print("Diccionario:", midic)
print("\nDiccionario[3]:", midic["3"])