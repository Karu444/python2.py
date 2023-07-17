# Crear archivo json con una estructura de datos lista


import json

lista = [10, 20, 30, 40, 60]

with open("Ciclo 1/codigo/archivos-json/lista.json", "w") as archivo:
    json.dump(lista, archivo)
    
if not archivo.closed:
    print("Cerrando archivo")
    archivo.close()