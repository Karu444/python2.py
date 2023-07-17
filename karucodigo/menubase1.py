def mostrar_menu():
    print("Bienvenido al Menú Predeterminado")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")

def opcion_1():
    print("Has elegido la Opción 1")
    # Agrega aquí la lógica para la opción 1

def opcion_2():
    print("Has elegido la Opción 2")
    # Agrega aquí la lógica para la opción 2

def opcion_3():
    print("Has elegido la Opción 3")
    # Agrega aquí la lógica para la opción 3

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-4): ")

    if opcion == '1':
        opcion_1()
    elif opcion == '2':
        opcion_2()
    elif opcion == '3':
        opcion_3()
    elif opcion == '4':
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, elige una opción válida.")


#Este código define una función mostrar_menu() que muestra las opciones disponibles y luego utiliza un bucle while para mantener el menú en funcionamiento hasta que el usuario elija la opción "4" para salir.

#Cada opción del menú se implementa en una función separada (opcion_1(), opcion_2(), opcion_3()). Puedes agregar la lógica específica que deseas ejecutar para cada opción dentro de estas funciones.

#recuerda que este código base es simple y se puede adaptar y expandir según las necesidades específicas del proyecto. ¡Espero que te sea útil!