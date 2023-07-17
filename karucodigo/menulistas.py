empleados = []

def agregar_empleado():
    id_empleado = input("Ingrese el ID del empleado: ")
    nombre = input("Ingrese el nombre del empleado: ")
    horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
    valor_hora = float(input("Ingrese el valor de la hora: "))

    if 1 <= horas_trabajadas <= 160 and 8000 <= valor_hora <= 150000:
        empleado = {
            'id': id_empleado,
            'nombre': nombre,
            'horas_trabajadas': horas_trabajadas,
            'valor_hora': valor_hora
        }
        empleados.append(empleado)
        print("Empleado agregado exitosamente.")
    else:
        print("Error: Las horas trabajadas deben estar entre 1 y 160, y el valor de la hora entre $8,000 y $150,000.")

def modificar_empleado():
    id_empleado = input("Ingrese el ID del empleado que desea modificar: ")

    for empleado in empleados:
        if empleado['id'] == id_empleado:
            print("Datos actuales del empleado:")
            print("ID:", empleado['id'])
            print("Nombre:", empleado['nombre'])
            print("Horas trabajadas:", empleado['horas_trabajadas'])
            print("Valor de la hora:", empleado['valor_hora'])
            
            nombre = input("Ingrese el nuevo nombre del empleado: ")
            horas_trabajadas = int(input("Ingrese las nuevas horas trabajadas: "))
            valor_hora = float(input("Ingrese el nuevo valor de la hora: "))

            if 1 <= horas_trabajadas <= 160 and 8000 <= valor_hora <= 150000:
                empleado['nombre'] = nombre
                empleado['horas_trabajadas'] = horas_trabajadas
                empleado['valor_hora'] = valor_hora
                print("Empleado modificado exitosamente.")
            else:
                print("Error: Las horas trabajadas deben estar entre 1 y 160, y el valor de la hora entre $8,000 y $150,000.")
            break
    else:
        print("Empleado no encontrado.")

def buscar_empleado():
    id_empleado = input("Ingrese el ID del empleado que desea buscar: ")

    for empleado in empleados:
        if empleado['id'] == id_empleado:
            print("Información del empleado:")
            print("ID:", empleado['id'])
            print("Nombre:", empleado['nombre'])
            print("Horas trabajadas:", empleado['horas_trabajadas'])
            print("Valor de la hora:", empleado['valor_hora'])
            break
    else:
        print("Empleado no encontrado.")

def eliminar_empleado():
    id_empleado = input("Ingrese el ID del empleado que desea eliminar: ")

    for empleado in empleados:
        if empleado['id'] == id_empleado:
            empleados.remove(empleado)
            print("Empleado eliminado exitosamente.")
            break
    else:
        print("No se encontró ningún empleado con ese ID.")

def listar_empleados():
    if len(empleados) == 0:
        print("No hay empleados registrados.")
        return

    pagina = 1
    empleados_por_pagina = 5
    total_paginas = (len(empleados) + empleados_por_pagina - 1) // empleados_por_pagina

    while pagina <= total_paginas:
        print("=== Página", pagina, "===")
        inicio = (pagina - 1) * empleados_por_pagina
        fin = inicio + empleados_por_pagina
        for empleado in empleados[inicio:fin]:
            print("ID:", empleado['id'])
            print("Nombre:", empleado['nombre'])
            print("Horas trabajadas:", empleado['horas_trabajadas'])
            print("Valor de la hora:", empleado['valor_hora'])
            print("-------------------------")

        if pagina < total_paginas:
            opcion = input("Presione Enter para ver la siguiente página o 'M' para volver al menú principal: ")
            if opcion.upper() == 'M':
                break
        else:
            print("No hay más empleados para mostrar.")

        pagina += 1

def listar_nomina_empleado():
    id_empleado = input("Ingrese el ID del empleado: ")

    for empleado in empleados:
        if empleado['id'] == id_empleado:
            salario_bruto = empleado['horas_trabajadas'] * empleado['valor_hora']
            subsidio_transporte = 0
            salario_minimo = 1000000
            if salario_bruto < salario_minimo:
                subsidio_transporte = 106454

            descuento_eps = salario_bruto * 0.04
            descuento_pension = salario_bruto * 0.04
            salario_neto = salario_bruto + subsidio_transporte - descuento_eps - descuento_pension

            print("=== Nómina del empleado ===")
            print("ID:", empleado['id'])
            print("Nombre:", empleado['nombre'])
            print("Salario bruto:", salario_bruto)
            print("Subsidio de transporte:", subsidio_transporte)
            print("Descuento EPS:", descuento_eps)
            print("Descuento pensión:", descuento_pension)
            print("Salario neto:", salario_neto)
            break
    else:
        print("Empleado no encontrado.")

def listar_nomina_todos():
    if len(empleados) == 0:
        print("No hay empleados registrados.")
        return

    pagina = 1
    empleados_por_pagina = 5
    total_paginas = (len(empleados) + empleados_por_pagina - 1) // empleados_por_pagina

    while pagina <= total_paginas:
        print("=== Página", pagina, "===")
        inicio = (pagina - 1) * empleados_por_pagina
        fin = inicio + empleados_por_pagina
        for empleado in empleados[inicio:fin]:
            salario_bruto = empleado['horas_trabajadas'] * empleado['valor_hora']
            subsidiotransporte = 0
            salario_minimo = 1000000 
            if salario_bruto < salario_minimo:
                subsidio_transporte = 106454

            descuento_eps = salario_bruto * 0.04
            descuento_pension = salario_bruto * 0.04
            salario_neto = salario_bruto + subsidio_transporte - descuento_eps - descuento_pension

            print("ID:", empleado['id'])
            print("Nombre:", empleado['nombre'])
            print("Salario bruto:", salario_bruto)
            print("Subsidio de transporte:", subsidio_transporte)
            print("Descuento EPS:", descuento_eps)
            print("Descuento pensión:", descuento_pension)
            print("Salario neto:", salario_neto)
            print("-------------------------")

        if pagina < total_paginas:
            opcion = input("Presione Enter para ver la siguiente página o 'M' para volver al menú principal: ")
            if opcion.upper() == 'M':
                break
        else:
            print("No hay más empleados para mostrar.")

        pagina += 1

def mostrar_menu():
    while True:
        print("\n*** NOMINA ACME ***")
        print(" MENU")
        print("1- Agregar empleado")
        print("2- Modificar empleado")
        print("3- Buscar empleado")
        print("4- Eliminar empleado")
        print("5- Listar empleados")
        print("6- Listar nómina de un empleado")
        print("7- Listar nómina de todos los empleados")
        print("8- Salir")

        opcion = input(">> Escoja una opción (1-8): ")
        print()

        if opcion == '1':
            agregar_empleado()
        elif opcion == '2':
            modificar_empleado()
        elif opcion == '3':
            buscar_empleado()
        elif opcion == '4':
            eliminar_empleado()
        elif opcion == '5':
            listar_empleados()
        elif opcion == '6':
            listar_nomina_empleado()
        elif opcion == '7':
            listar_nomina_todos()
        elif opcion == '8':
            confirmacion = input("¿Está seguro/a de que desea salir? (S/N): ")
            if confirmacion.upper() == 'S':
                print("¡Gracias por usar el programa! ¡Hasta luego!")
                break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida (1-8).")

mostrar_menu()