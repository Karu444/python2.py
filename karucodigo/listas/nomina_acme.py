ids = []
noms = []
horasTs = []
valorHs = []
indic = 0

def nomEmpleado():
    pass

def leerInt(msg):
    while True:
        try:
            print("_" * 75)
            iNum = int(input(msg))
            return iNum
        except ValueError:
            print("_" * 75)
            print("Ingrese un numero entero valido")

def leerString(msg):
    while True:
        try:
            sNom = input(msg)
            if sNom.strip() == "":
                print("\nPor favor ingrese un nombre valido")
                continue
            return sNom
        except Exception as e:
            print("\nError al ingresar un nombre" , e.message)

def menu():
    while True:
        print("_" * 75)
        print("\nMENU")
        print("_" * 75)
        print("\n1. Agregar empleado")
        print("2. Modificar empleado")
        print("3. Buscar empleado")
        print("4. Eliminar empleado")
        print("5. Lista empleados")
        print("6. Listar nomina de un empleado")
        print("7. Listar nomina de todos los empleados")
        print("8. Salir")
        opc = leerInt("\nSeleccione una opción de 1 a 8: ")
        if opc < 1 or opc > 8:
            print("Ingrese una opción valida")
            continue
        return opc

def agregar(id, nom, horasT, valorH):
    ids.append(id)
    noms.append(nom)
    horasTs.append(horasT)
    valorHs.append(valorH)
    
def modificar():   
    try:
        id = leerInt("Ingrese el id del empleado: ")
        e = ids.index(id)
    except ValueError:
        print("El empleando no existe.")
        input("Presione cualqueir tecla para volver al menu...")
        return
    
    print("\nMENU DE MODIFICACION")
    print("\n1. Nombre")
    print("\n2. Horas trabajadas")
    print("\n3. Valor de la hora")
    while True:
        op = leerInt("Seleccione el que quiere modificar: ")
        if op < 1 or op > 3:
            print("Ingrese un valor valido")
            continue
        break
    if op == 1:
        print("Modificar nombre")
        nueNom = leerString("Ingrese el nuevo nombre: ")
        # noms.insert(e, nueNom)
        noms[e] = nueNom
    elif op == 2:
        print("Modificar horas trabajadas")
        while True:
            nueHor = leerInt("Ingrese el nuevo numero de horas trabajadas del empleado: ")
            if nueHor < 1 or nueHor > 160:
                print("El numero de horas tiene que estar entre 1 y 160")
                continue
            break
        horasTs.insert(e, nueHor)
    elif op == 3:
        print("Modificar valor de la hora")
        while True:
            nueValor = leerInt("Ingrese el valor unitario de la hora: ")
            if nueValor < 8000 or nueValor > 150000:
                print("El nuevo valor de la horas tiene que estar entre 8.000 y 150.000")
                continue
            break              
        valorHs.insert(e, nueValor)
  
def buscar():  
        id = leerInt("Ingrese el id del empleado: ")
        e = ids.index(id)
  
while True:
    iOpc = menu()
    if iOpc == 1:
        id = leerInt("Ingrese el numero de id: ")
        nom = leerString("Ingrese el nombre del empleado: ")
        while True:
            horasT = leerInt("Ingrese el numero de horas trabajadas del empleado: ")
            if horasT < 1 or horasT > 160:
                print("El numero de horas tiene que estar entre 1 y 160")
                continue
            break
        while True:
            valorH = leerInt("Ingrese el valor unitario de la hora: ")
            if valorH < 8000 or valorH > 150000:
                print("El valor de la horas tiene que estar entre 8.000 y 150.000")
                continue
            break   
        agregar(id, nom, horasT, valorH)
        print("Los datos fueron agregados")
    elif iOpc == 2:
        modificar()  
    elif iOpc == 3:
        buscar()
    elif iOpc == 4:
        # eliminar()
        pass
    elif iOpc == 5:
        # listEmpleados()
        pass
    elif iOpc == 6:
        nomEmpleado()
    elif iOpc == 7:
        nomEmpleado()        
    elif iOpc == 8:
        print("_" * 75)
        print("\nFin del programa")
        break