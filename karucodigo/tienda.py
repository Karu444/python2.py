import json
import datetime

# Función para obtener la fecha actual en formato YYYY-MM-DD
def obtener_fecha_actual():
    fecha_actual = datetime.datetime.now()
    return fecha_actual.strftime('%Y-%m-%d')

# Función para guardar los datos en un archivo JSON
def guardar_datos_en_json(datos, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        json.dump(datos, archivo)

# Función para cargar los datos desde un archivo JSON
def cargar_datos_desde_json(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

# Crear o cargar el archivo JSON para los registros del día
nombre_archivo_registros = 'registros.json'
registros_diarios = cargar_datos_desde_json(nombre_archivo_registros)

# Función para agregar un cliente
def agregar_cliente():
    cedula = input("Ingrese el número de cédula del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    clientes[cedula] = nombre
    print("Cliente agregado exitosamente.")

# Función para agregar un producto
def agregar_producto():
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    valor_unitario = float(input("Ingrese el valor unitario del producto: "))
    iva = float(input("Ingrese el IVA del producto (%): "))
    productos[codigo] = {
        'nombre': nombre,
        'valor_unitario': valor_unitario,
        'iva': iva
    }
    print("Producto agregado exitosamente.")

# Función para realizar una venta
def realizar_venta():
    cedula = input("Ingrese el número de cédula del cliente: ")
    if cedula not in clientes:
        print("Cliente no registrado.")
        return

    total_venta = 0
    lista_productos_vendidos = []

    while True:
        codigo_producto = input("Ingrese el código del producto (o '0' para finalizar la venta): ")
        if codigo_producto == '0':
            break

        if codigo_producto not in productos:
            print("Producto no registrado.")
            continue

        cantidad = int(input("Ingrese la cantidad vendida: "))

        producto = productos[codigo_producto]
        subtotal = producto['valor_unitario'] * cantidad
        iva_producto = subtotal * (producto['iva'] / 100)
        total_producto = subtotal + iva_producto

        lista_productos_vendidos.append({
            'codigo': codigo_producto,
            'nombre': producto['nombre'],
            'cantidad': cantidad,
            'subtotal': subtotal,
            'iva': iva_producto,
            'total': total_producto
        })

        total_venta += total_producto

    registros_diarios[cedula] = registros_diarios.get(cedula, []) + lista_productos_vendidos

    # Imprimir tirilla de pago
    imprimir_tirilla_pago(clientes[cedula], lista_productos_vendidos, total_venta)

    print(f"Venta realizada exitosamente. Total venta: {total_venta}")

# Función para imprimir la tirilla de pago
def imprimir_tirilla_pago(nombre_cliente, productos_vendidos, total_venta):
    print("----- Tirilla de Pago -----")
    print(f"Cliente: {nombre_cliente}")
    print("Productos:")
    for producto in productos_vendidos:
        print(f"  - {producto['nombre']}: {producto['cantidad']} x ${producto['subtotal']:.2f}")
    print(f"Total a pagar: ${total_venta:.2f}")
    print("---------------------------")

# Menú principal del programa
clientes = {}
productos = {}

while True:
    print("\n----- Menú -----")
    print("1. Agregar cliente")
    print("2. Agregar producto")
    print("3. Realizar venta")
    print("4. Salir")

    opcion = input("Seleccione una opción (1/2/3/4): ")

    if opcion == '1':
        agregar_cliente()
    elif opcion == '2':
        agregar_producto()
    elif opcion == '3':
        realizar_venta()
    elif opcion == '4':
        # Reiniciar registros diarios y guardar los datos en el archivo JSON
        fecha_actual = obtener_fecha_actual()
        guardar_datos_en_json(registros_diarios, f"{nombre_archivo_registros}_{fecha_actual}.json")
        registros_diarios = {}
        print("Gracias por usar el programa. Registros diarios guardados.")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida (1/2/3/4).")
        
        
        
#Entendido. Para imprimir la tirilla de pago después de cada venta, podemos agregar una función llamada imprimir_tirilla_pago() que tome los detalles de la venta y genere el formato de la tirilla. Luego, llamaremos a esta función dentro de la función realizar_venta() para imprimir la tirilla después de finalizar la venta.

#Vamos a modificar el código anterior para incluir la función imprimir_tirilla_pago() y realizar algunas otras mejoras. Utilizaremos una cadena de formato (f-string) para generar la tirilla con los detalles de la venta.


#Con este código, después de cada venta, se imprimirá una tirilla con los detalles de la venta, incluyendo el nombre del cliente, los productos vendidos con sus cantidades y subtotales, y el total a pagar. Si deseas modificar el formato de la tirilla o agregar más detalles, puedes hacerlo en la función imprimir_tirilla_pago().

#Recuerda que este es solo un ejemplo básico, y puedes ajustar y mejorar el código según las necesidades específicas de tu micromercado. Si tienes alguna pregunta o necesitas más ayuda, no dudes en preguntar. ¡Buena suerte!