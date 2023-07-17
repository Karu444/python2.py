def mostrar_menu(menu_items):
    print("Bienvenido al Menú Predeterminado")
    for index, item in enumerate(menu_items, start=1):
        print(f"{index}. {item['opcion']}")

def opcion_1():
    print("Has elegido la Opción 1")
    # Agrega aquí la lógica para la opción 1

def opcion_2():
    print("Has elegido la Opción 2")
    # Agrega aquí la lógica para la opción 2

def opcion_3():
    print("Has elegido la Opción 3")
    # Agrega aquí la lógica para la opción 3

# Lista de opciones del menú en un diccionario
menu = [
    {"opcion": "Opción 1", "accion": opcion_1},
    {"opcion": "Opción 2", "accion": opcion_2},
    {"opcion": "Opción 3", "accion": opcion_3},
    {"opcion": "Salir", "accion": None}
]

while True:
    mostrar_menu(menu)
    opcion = input("Elige una opción (1-4): ")

    try:
        opcion = int(opcion)
        if 1 <= opcion <= len(menu):
            if menu[opcion - 1]["accion"] is not None:
                menu[opcion - 1]["accion"]()
            else:
                print("¡Hasta luego!")
                break
        else:
            print("Opción inválida. Por favor, elige una opción válida.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número válido.")


#En esta versión, hemos definido cada opción del menú como un diccionario en la lista menu. Cada diccionario tiene dos claves: "opcion" y "accion". "opcion" almacena el texto de la opción del menú que se mostrará, y "accion" contiene la función que se ejecutará cuando el usuario elija esa opción.

#El bucle while sigue siendo el mismo, pero ahora, cuando el usuario elige una opción, buscamos en la lista menu el diccionario correspondiente y ejecutamos la función asociada a través de la clave "accion".

#Este enfoque permite una mayor flexibilidad, ya que puedes agregar fácilmente más opciones al menú agregando diccionarios adicionales en la lista menu con sus respectivas funciones.