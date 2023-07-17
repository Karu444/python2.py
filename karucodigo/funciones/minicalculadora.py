def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print("Error!. Ingrese un numero entero válido.")

def msgError(msg):
    print("--> !ERROR!", msg)
    input("--> Presione cualquier tecla para continuar ...")

def menu():
    while True:
        print("\n\n******")
        print(" MENU ")
        print("******\n")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Potencia")
        print("6. Factorial")
        print("7. Salir")
        op = leerInt("\n>> Opción (1 a 7)? ")
        if op < 1 or op > 7:
            msgError("Opcion no valida")
            continue
        return op

def sumar():
    print("\n" * 3, "*** 1. SUMAR ***")
    n1 = leerInt("Ingrese un número: ")
    n2 = leerInt("Ingrese otro número: ")
    print("\n==> El resultado de la suma es: ", n1 + n2)
    input("--> Presione cualquier tecla para vover al menu ...")

def restar():
    pass

def multiplicar():
    pass

def dividir():
    pass

def potencia():
    pass

def factorial():
    print("\n" * 3, "*** 6. FACTORIAL ***")
    n1 = leerInt("Ingrese un número: ")
    f = 1
    for i in range(1, n1+1):
        f *= i
    print("\n==> El resultado del factorial es: ", f)
    input("--> Presione cualquier tecla para vover al menu ...")



# PROGRAMA GENERAL
while True:
    opcion = menu()
    
    if opcion == 1:
        sumar()
    elif opcion == 2:
        restar()
    elif opcion == 3:
        multiplicar()
    elif opcion == 4:
        dividir()
    elif opcion == 5:
        potencia()
    elif opcion == 6:
        factorial()
    elif opcion == 7:
        print("\n** Gracias por usar la MiniCalculadora **")
        break
    else:
        msgError("Opcion inválida.")