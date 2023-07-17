# Crear archivo json con una estructura de datos diccionario


import json

midic = {1:"Lapiz", 2:"Borrador", 3:"Cuaderno", 4:"Lapicero"}

with open("Ciclo 1/codigo/archivos-json/diccionario.json", "w") as archivo:
    json.dump(midic, archivo)
    
if not archivo.closed:
    print("Cerrando archivo")
    archivo.close()