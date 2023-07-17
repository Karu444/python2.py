# Función para calcular el promedio
def calcular_promedio(calificaciones):
    total_calificaciones = sum(calificaciones)
    promedio = total_calificaciones / len(calificaciones)
    return promedio

# Función para asignar una calificación final
def asignar_calificacion_final(promedio):
    if promedio >= 90:
        return 'A'
    elif promedio >= 80:
        return 'B'
    elif promedio >= 70:
        return 'C'
    elif promedio >= 60:
        return 'D'
    else:
        return 'F'

# Lista para almacenar los datos de los estudiantes en diferentes grados
grado1 = []
grado2 = []
grado3 = []

# Función para ingresar las notas de un estudiante por el usuario
def ingresar_notas_estudiante(grado):
    nombre = input("Ingrese el nombre del estudiante: ")
    sexo = input("Ingrese el sexo del estudiante (M/F): ")
    notas = []
    for i in range(3):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        notas.append(nota)

    # Calculamos la definitiva del estudiante
    definitiva = calcular_promedio(notas)

    estudiante = {
        'nombre': nombre,
        'sexo': sexo,
        'notas': notas,
        'definitiva': definitiva
    }
    grado.append(estudiante)
    print("Notas del estudiante ingresadas exitosamente.")

# Función para buscar un estudiante por su número de lista y grado
def buscar_estudiante_por_lista(grado, numero_lista):
    for estudiante in grado:
        if estudiante['numero_lista'] == numero_lista:
            return estudiante
    return None

# Función para mostrar los datos de un estudiante
def mostrar_estudiante(estudiante):
    print(f"Nombre: {estudiante['nombre']}")
    print(f"Sexo: {estudiante['sexo']}")
    print(f"Notas: {estudiante['notas']}")
    print(f"Definitiva: {estudiante['definitiva']}")
    calificacion_final = asignar_calificacion_final(estudiante['definitiva'])
    print(f"Calificación final: {calificacion_final}")
    print("--------------------")

# Función para editar las notas de un estudiante
def editar_notas_estudiante(grado, numero_lista):
    estudiante = buscar_estudiante_por_lista(grado, numero_lista)
    if estudiante:
        print(f"\nNotas actuales de {estudiante['nombre']}: {estudiante['notas']}")
        for i in range(3):
            nota_nueva = float(input(f"Ingrese la nueva nota {i+1}: "))
            estudiante['notas'][i] = nota_nueva

        # Recalculamos la definitiva del estudiante
        estudiante['definitiva'] = calcular_promedio(estudiante['notas'])

        print(f"\nNotas de {estudiante['nombre']} editadas exitosamente.")
    else:
        print(f"\nNo se encontró ningún estudiante con el número de lista {numero_lista}.")

# Menú principal del programa
while True:
    print("\n----- Menú -----")
    print("1. Ingresar notas de un estudiante")
    print("2. Ver datos de un estudiante")
    print("3. Editar notas de un estudiante")
    print("4. Salir")
    
    opcion = input("Seleccione una opción (1/2/3/4): ")

    if opcion == '1':
        grado = input("Ingrese el grado del estudiante (1/2/3): ")
        if grado == '1':
            ingresar_notas_estudiante(grado1)
        elif grado == '2':
            ingresar_notas_estudiante(grado2)
        elif grado == '3':
            ingresar_notas_estudiante(grado3)
        else:
            print("Grado inválido. Por favor, ingrese un grado válido (1/2/3).")
    elif opcion == '2':
        numero_lista_buscar = int(input("Ingrese el número de lista del estudiante que desea ver: "))
        grado_buscar = input("Ingrese el grado del estudiante (1/2/3): ")
        if grado_buscar == '1':
            estudiante_encontrado = buscar_estudiante_por_lista(grado1, numero_lista_buscar)
        elif grado_buscar == '2':
            estudiante_encontrado = buscar_estudiante_por_lista(grado2, numero_lista_buscar)
        elif grado_buscar == '3':
            estudiante_encontrado = buscar_estudiante_por_lista(grado3, numero_lista_buscar)
        else:
            print("Grado inválido. Por favor, ingrese un grado válido (1/2/3).")
            continue
        
        if estudiante_encontrado:
            mostrar_estudiante(estudiante_encontrado)
        else:
            print(f"No se encontró ningún estudiante con el número de lista {numero_lista_buscar} en el grado {grado_buscar}.")
    elif opcion == '3':
        numero_lista_editar = int(input("Ingrese el número de lista del estudiante cuyas notas desea editar: "))
        grado_editar = input("Ingrese el grado del estudiante (1/2/3): ")
        if grado_editar == '1':
            editar_notas_estudiante(grado1, numero_lista_editar)
        elif grado_editar == '2':
            editar_notas_estudiante(grado2, numero_lista_editar)
        elif grado_editar == '3':
            editar_notas_estudiante(grado3, numero_lista_editar)
        else:
            print("Grado inválido. Por favor, ingrese un grado válido (1/2/3).")
    elif opcion == '4':
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida (1/2/3/4).")

print("Gracias por usar el programa.")
