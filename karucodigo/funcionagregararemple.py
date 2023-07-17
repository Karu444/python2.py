def agregar_empleado(empleados, ide, nombre, sueldo):
    empleado = {
        'id': ide,
        'nombre': nombre,
        'sueldo': sueldo
    }
    empleados.append(empleado)

def buscar_empleado_por_id(empleados, ide):
    for empleado in empleados:
        if empleado['id'] == ide:
            return empleado
    return None

def editar_empleado_por_id(empleados, ide, nuevo_nombre, nuevo_sueldo):
    for empleado in empleados:
        if empleado['id'] == ide:
            empleado['nombre'] = nuevo_nombre
            empleado['sueldo'] = nuevo_sueldo
            return True
    return False

# Lista para almacenar los empleados
lista_empleados = []

# Función para ingresar un nuevo empleado por el usuario
def ingresar_empleado_por_usuario():
    try:
        ide = int(input("Ingrese el ID del empleado: "))
        nombre = input("Ingrese el nombre del empleado: ")
        sueldo = float(input("Ingrese el sueldo del empleado: "))
        agregar_empleado(lista_empleados, ide, nombre, sueldo)
        print("Empleado agregado exitosamente.")
    except ValueError:
        print("Error: Ingrese un ID válido y un sueldo numérico.")

# Ejemplo de uso para ingresar un nuevo empleado
ingresar_empleado_por_usuario()

# Mostrar la lista de empleados agregados
print("\nLista de empleados:")
for empleado in lista_empleados:
    print(f"ID: {empleado['id']}, Nombre: {empleado['nombre']}, Sueldo: {empleado['sueldo']}")

# Función para editar un empleado por el usuario
def editar_empleado_por_usuario():
    try:
        ide = int(input("Ingrese el ID del empleado que desea editar: "))
        empleado_encontrado = buscar_empleado_por_id(lista_empleados, ide)
        if empleado_encontrado:
            nuevo_nombre = input("Ingrese el nuevo nombre del empleado: ")
            nuevo_sueldo = float(input("Ingrese el nuevo sueldo del empleado: "))
            editar_empleado_por_id(lista_empleados, ide, nuevo_nombre, nuevo_sueldo)
            print(f"Empleado con ID {ide} editado exitosamente.")
        else:
            print(f"No se encontró ningún empleado con ID {ide}.")
    except ValueError:
        print("Error: Ingrese un ID válido y un sueldo numérico.")

# Ejemplo de uso para editar un empleado existente
editar_empleado_por_usuario()

# Mostrar la lista de empleados después de la edición
print("\nLista de empleados después de la edición:")
for empleado in lista_empleados:
    print(f"ID: {empleado['id']}, Nombre: {empleado['nombre']}, Sueldo: {empleado['sueldo']}")



#