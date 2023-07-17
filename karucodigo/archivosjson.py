import json

archivo_empleados = "emplacme.json"

def cargar_empleados():
    try:
        with open(archivo_empleados, "r") as file:
            empleados = json.load(file)
    except FileNotFoundError:
        empleados = []
    return empleados

def guardar_empleados(empleados):
    with open(archivo_empleados, "w") as file:
        json.dump(empleados, file)

def agregar_empleado():
    empleados = cargar_empleados()

    id_empleado = input("Ingrese el ID del empleado: ")
    nombre = input("Ingrese el nombre del empleado: ")
    horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
    valor_hora = float(input("Ingrese el valor de la hora: "))

    empleado = {
        "id": id_empleado,
        "nombre": nombre,
        "horas_trabajadas": horas_trabajadas,
        "valor_hora": valor_hora
    }

    empleados.append(empleado)
    guardar_empleados(empleados)
    print("Empleado agregado correctamente.")

def modificar_empleado():
    id_empleado = input("Ingrese el ID del empleado a modificar: ")

    empleados = cargar_empleados()
    empleado_encontrado = False

    for empleado in empleados:
        if empleado["id"] == id_empleado:
            empleado_encontrado = True

            nombre = input("Ingrese el nuevo nombre del empleado: ")
            horas_trabajadas = int(input("Ingrese las nuevas horas trabajadas: "))
            valor_hora = float(input("Ingrese el nuevo valor de la hora: "))

            empleado["nombre"] = nombre
            empleado["horas_trabajadas"] = horas_trabajadas
            empleado["valor_hora"] = valor_hora

            break

    if empleado_encontrado:
        guardar_empleados(empleados)
        print("Empleado modificado correctamente.")
    else:
        print("No se encontró un empleado con ese ID.")

def buscar_empleado():
    id_empleado = input("Ingrese el ID del empleado a buscar: ")

    empleados = cargar_empleados()
    empleado_encontrado = False

    for empleado in empleados:
        if empleado["id"] == id_empleado:
            empleado_encontrado = True
            print("Información del empleado:")
            print(f"ID: {empleado['id']}")
            print(f"Nombre: {empleado['nombre']}")
            print(f"Horas trabajadas: {empleado['horas_trabajadas']}")
            print(f"Valor de la hora: {empleado['valor_hora']}")
            break

    if not empleado_encontrado:
        print("No se encontró un empleado con ese ID.")

def eliminar_empleado():
    id_empleado = input("Ingrese el ID del empleado a eliminar: ")

    empleados = cargar_empleados()
    empleado_encontrado = False

    for empleado in empleados:
        if empleado["id"] == id_empleado:
            empleado_encontrado = True
            empleados.remove(empleado)
            break

    if empleado_encontrado:
        guardar_empleados(empleados)
        print("Empleado eliminado correctamente.")
    else:
        print("No se encontró un empleado con ese ID.")

def listar_empleados():
    empleados = cargar_empleados()

    if len(empleados) == 0:
        print("No hay empleados registrados.")
        return

    print("Lista de empleados:")
    for empleado in empleados:
        print(f"ID: {empleado['id']}")
        print(f"Nombre: {empleado['nombre']}")
        print(f"Horas trabajadas: {empleado['horas_trabajadas']}")
        print(f"Valor de la hora: {empleado['valor_hora']}")
        print("-------------------")

def calcular_nomina_empleado():
    id_empleado = input("Ingrese el ID del empleado para calcular la nómina: ")

    empleados = cargar_empleados()
    empleado_encontrado = False

    for empleado in empleados:
        if empleado["id"] == id_empleado:
            empleado_encontrado = True
            salario_bruto = empleado["horas_trabajadas"] * empleado["valor_hora"]

            if salario_bruto < 1000000:
                subsidio_transporte = 106454
            else:
                subsidio_transporte = 0

            descuento_eps = salario_bruto * 0.04
            descuento_pension = salario_bruto * 0.04

            salario_neto = salario_bruto + subsidio_transporte - descuento_eps - descuento_pension

            print("Nómina del empleado:")
            print(f"ID: {empleado['id']}")
            print(f"Nombre: {empleado['nombre']}")
            print(f"Salario bruto: {salario_bruto}")
            print(f"Subsidio de transporte: {subsidio_transporte}")
            print(f"Descuento EPS: {descuento_eps}")
            print(f"Descuento pensión: {descuento_pension}")
            print(f"Salario neto: {salario_neto}")
            break

    if not empleado_encontrado:
        print("No se encontró un empleado con ese ID.")

def listar_nomina_empleados():
    empleados = cargar_empleados()

    if len(empleados) == 0:
        print("No hay empleados registrados.")
        return

    print("Nómina de todos los empleados:")
    for empleado in empleados:
        salario_bruto = empleado["horas_trabajadas"] * empleado["valor_hora"]

        if salario_bruto < 1000000:
            subsidio_transporte = 106454
        else:
            subsidio_transporte = 0

        descuento_eps = salario_bruto * 0.04
        descuento_pension = salario_bruto * 0.04

        salario_neto = salario_bruto + subsidio_transporte - descuento_eps - descuento_pension

        print(f"ID: {empleado['id']}")
        print(f"Nombre: {empleado['nombre']}")
        print(f"Salario bruto: {salario_bruto}")
        print(f"Subsidio de transporte: {subsidio_transporte}")
        print(f"Descuento EPS: {descuento_eps}")
        print(f"Descuento pensión: {descuento_pension}")
        print(f"Salario neto: {salario_neto}")
        print("-------------------")

# Función principal del programa
def main():
    while True:
        print("*** NOMINA ACME ***")
        print("MENU")
        print("1- Agregar empleado")
        print("2- Modificar empleado")
        print("3- Buscar empleado")
        print("4- Eliminar empleado")
        print("5- Listar empleados")
        print("6- Listar nómina de un empleado")
        print("7- Listar nómina de todos los empleados")
        print("8- Salir")

        opcion = input("Escoja una opción (1-8): ")

        if opcion == "1":
            agregar_empleado()
        elif opcion == "2":
            modificar_empleado()
        elif opcion == "3":
            buscar_empleado()
        elif opcion == "4":
            eliminar_empleado()
        elif opcion == "5":
            listar_empleados()
        elif opcion == "6":
            calcular_nomina_empleado()
        elif opcion == "7":
            listar_nomina_empleados()
        elif opcion == "8":
            confirmacion = input("¿Está seguro de que desea salir? (s/n): ")
            if confirmacion.lower() == "s":
                print("¡Hasta luego!")
                break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()