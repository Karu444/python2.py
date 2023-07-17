diccionario_categoria = {1: 25000, 2: 30000, 3: 40000, 4: 45000, 5: 60000}

totHonor = 0
docentes = {}
while True:
    cedula = int(input("Cédula del docente: "))
    nombre = input("Nombre del docente: ")
    categoria = int(input("Categoria del docente: "))
    horas = int(input("Horas laboradas en el mes por el docente: "))
    docentes[cedula] = {}
    docentes[cedula]["nombre"] = nombre
    docentes[cedula]["categoria"] = categoria
    docentes[cedula]["horas"] = horas

    opc = input("Desea agregar otro docente (S/N)?")
    if opc.lower() == "n":
        break
    print("")

print("\n\n *** INFORME ***")
print("=" * 30)
for k in docentes.keys():
    h = docentes[k]["horas"] * diccionario_categoria[docentes[k]["categoria"]]
    totHonor += h
    print(docentes[k]["nombre"], f" -- ${h:,}")

print("=" * 30)
print(f"Total honorarios de los docentes: ${totHonor:,}")
