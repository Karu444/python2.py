def calcular_promedio(calificaciones):
    total_calificaciones = sum(calificaciones)
    promedio = total_calificaciones / len(calificaciones)
    return promedio

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

# Lista para almacenar los datos de los estudiantes
lista_estudiantes = []

# Función para ingresar los datos de un estudiante por el usuario
def ingresar_datos_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    calificaciones = []
    for asignatura in ['Matemáticas', 'Ciencias', 'Historia']:
        calificacion = float(input(f"Ingrese la calificación de {asignatura}: "))
        calificaciones.append(calificacion)

    estudiante = {
        'nombre': nombre,
        'calificaciones': calificaciones
    }
    lista_estudiantes.append(estudiante)
    print("Datos del estudiante ingresados exitosamente.")

# Ejemplo de uso para ingresar datos de un estudiante
ingresar_datos_estudiante()

# Calcular promedio y asignar calificación final para cada estudiante
for estudiante in lista_estudiantes:
    promedio = calcular_promedio(estudiante['calificaciones'])
    calificacion_final = asignar_calificacion_final(promedio)
    estudiante['promedio'] = promedio
    estudiante['calificacion_final'] = calificacion_final

# Mostrar los datos de los estudiantes y sus calificaciones
print("\nDatos de los estudiantes y sus calificaciones:")
for estudiante in lista_estudiantes:
    print(f"Nombre: {estudiante['nombre']}")
    print(f"Calificaciones: {estudiante['calificaciones']}")
    print(f"Promedio: {estudiante['promedio']}")
    print(f"Calificación final: {estudiante['calificacion_final']}")
    print("--------------------")
