"""INTRODUCCIÓN
Resuelva los siguientes enunciados en Python validando la entrada del usuario y usando diccionarios.

ENUNCIADO
La empresa ACME desea que le construya un programa para gestionar la nómina de sus empleados. Después
de recoger los requerimientos se llegó a la decisión de gestionar los empleados y sus nóminas a través del
siguiente menú.

*** NOMINA ACME ***
MENU
1- Agregar empleado
2- Modificar empleado
3- Buscar empleado
4- Eliminar empleado
5- Listar empleados
6- Listar nómina de un empleado
7- Listar nómina de todos los empleados
8- Salir
>> Escoja una opción (1-8)?

1. Agregar empleado: Esta opción permite adicionar un empleado con su id, nombre, horas trabajadas y
valor de la hora. Los empleados pueden trabajar entre 1 a 160 Horas. Y el valor de la hora puede estar
entre $8,000 y $150,000 pesos la hora.
2. Modificar empleado: Esta opción permite cambiar cualquiera de los datos del empleado, menos el id de
empleado.
3. Buscar empleado: Esta opción permite buscar un empleado por su id, si lo encuentra, muestra la
información de este y si no, muestra un mensaje de que el empleado no ha sido ingresado
4. Eliminar empleado: Esta opción permite eliminar a un empleado por su id. Si borra al empleado, muestra
un mensaje que ha sido eliminado y si no, muestra un mensaje de que no se eliminó el empleado.
5. Listar Empleados: Esta opción permite mostrar los empleados con su información (id, nombre, horas y
valor de la hora trabajada), debe permitir paginación, esto es, se muestran los primeros 5 empleados,
luego para y muestra un mensaje para que el usuario decida si desea seguir viendo o volver al menú. Si
desea seguir viendo, le muestra los siguientes 5 empleados y así sucesivamente hasta que no haya más
empleados o la persona no desee seguir viendo.
Estructura de datos - Diccionarios Trainer Ing.
Carlos H. Rueda C.
6. Listar la nómina de un empleado: Esta opción permite mostrar la nómina de un empleado buscado por
su ID. El salario bruto se calcula como el valor de la hora por la cantidad de horas trabajadas. Si gana
menos del salario mínimo legal vigente en Colombia 2023 (por favor consulte el dato) se le debe da
subsidio de transporte. Se le debe descontar el valor de la eps y pensión correspondiente al 4% cada uno
y el salario Neto es la suma del salario bruto, el auxilio menos los descuentos.
El menú debe mostrar los datos del empleado y los datos de la nómina.
7. Listar nómina de todos los empleados: Esta opción permite mostrar la nómina de todos los empleados.
El listado debe estar paginado cada 5 empleados. El calculo de la nómina de cada empleado es el mismo
que en la opción 6.
8. Salir: Esta opción sale del programa, pero antes le pregunta al usuario si desea salir de la aplicación.
Sino no desea, vuelve al menú. Si desea salir de la aplicación muestra un mensaje de despedida y termina
el programa."""
nominacme = {}
agregarempleado = {}
# PROGRAMA GENERAL


def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 1:
                print("Error! El codigo debe ser entero postivo.")
                input("Digite cualquier tecla para continuar...")
                continue
            return n
        except ValueError:
            print("Error! Ingrese un numero valido")


def msgError(msg):
    print("----> ¡ERROR!" + msg)
    input("---> Presione ENTER para continuar")

# MENU ELEGIR PROGRANA


def menu():
    print("\n---------------")
    print(" NOMINA ACME MENU: ")
    print("----------------\n")
    print("1.Agregar empleado ")
    print("2.Modificar empleado ")
    print("3.Buscar empleado ")
    print("4.Eliminar empleado ")
    print("5.Listar empleados ")
    print("6.Listar nomina de un empleado ")
    print("7.Listar nomina de todos los empleados")
    print("8.Salir ")
    print(">> Escoja una opcion (1-8)?")
    elegirop = leerInt("\n>> Opcion (1 a 8)? ")
    if elegirop < 1 or elegirop > 8:
        msgError("Ingrese una opcion valida")
    return elegirop


def Agregar_empleado(ruta):
    """1. Agregar empleado: Esta opción permite adicionar un empleado con su id, nombre, horas trabajadas y
valor de la hora. Los empleados pueden trabajar entre 1 a 160 Horas. Y el valor de la hora puede estar
entre $8,000 y $150,000 pesos la hora."""

    id = input("Ingrese el id del empleado: ")
    nominacme[id] = {}
    print(f"Id empleado: {id}")

    nombre = input("Ingrese el nombre de empleado: ")
    nominacme[id]["nombre"] = nombre
    print(f"Nombre empleado: {nombre}")

    horas = int(input("Ingrese horas trabajadas: "))
    nominacme[id]["Horas trabajadas"] = horas
    while True:
        if horas < 1 or horas > 160:
            print("Ingrese una hora valida")
            return horas
        else:
            break
    print(f"Horas trabajadas: {horas}")

    while True:
        valorhora = int(input("Ingrese el valor de la hora trabajada: "))

        if valorhora < 8000 or valorhora > 150000:
            print("Ingrese un valor de hora adecuado")

        else:
            nominacme[id]["Valor hora"] = valorhora
            break
    print(f"Valor horas trabajadas {valorhora}")
    print("LOS VALORES DEL NUEVO EMPLEADO SON: ")
    nominacme.items()
    # print(nominacme)

    # Guardar en el disco
    lstempl = [id, nombre, str(horas), str(valorhora)]
    strempl = "\n" + ";".join(lstempl)
    fd = open(ruta, "a+")
    fd.write(strempl)
    fd.close()

    input("---> Presione ENTER para continuar")


def escribirMemDisco(ruta, dicempl):
    fd = open(ruta, "w")
    fd.write("ID;NOMBRE;HORASTRAB;VALHORA")

    for id in dicempl.keys():
        nombre = dicempl[id]["nombre"]
        horastrab = dicempl[id]["Horas trabajadas"]
        valhora = dicempl[id]["Valor hora"]

        lstempl = [id, nombre, str(horastrab), str(valhora)]
        strempl = "\n" + ";".join(lstempl)
        fd.write(strempl)

    fd.close()


def Modificar_empleado(ruta):
    """2. Modificar empleado: Esta opción permite cambiar cualquiera de los datos del empleado, menos el id de empleado."""
    print("Modificar empleado: ")
    print("----Seleccione el numero de lo que quiere modificar---- ")
    print("\n 1.Modificar nombre \n 2.Modificar horas \n 3.Modicar valor hora")

    while True:
        buscarid = input("Ingrese el id del empleado que desea modificar: ")
        if buscarid in nominacme:
            print("ID ENCONTRADO")
            modificar = int(input("Ingrese un numero: "))
            if modificar == 1:
                nombrenuevo = input("Ingrese el nuevo nombre: ")
                nominacme[buscarid]["nombre"] = nombrenuevo
                break
            elif modificar == 2:
                nuevahora = int(input("Ingrese las nuevas horas trabajadas: "))
                nominacme[buscarid]["Horas trabajadas"] = nuevahora
                break
            elif modificar == 3:
                nuevovalorh = int(input("Ingrese nuevo valor trabajadas: "))
                nominacme[buscarid]["Valor hora"] = nuevovalorh
                break
            else:
                print("Ingrese un numero valido")
        else:
            ("ID NO ENCONTRADO")

    # Modificar el archivo
    escribirMemDisco(ruta, nominacme)
    input("---> Presione ENTER para continuar")


def Buscar_empleado():
    """3. Buscar empleado: Esta opción permite buscar un empleado por su id, si lo encuentra, muestra la información de este y si no, muestra un mensaje de que el empleado no ha sido ingresado"""
    while True:
        buscarid = input("Ingrese el id del empleado que desea modificar: ")
        if buscarid in nominacme:
            print("ID ENCONTRADO")
            nombre = nominacme[buscarid]["nombre"]
            htrabjadas = nominacme[buscarid]["Horas trabajadas"]
            vlhora = nominacme[buscarid]["Valor hora"]

            print("-----EMPLEADO----")
            print("Los datos del empleado son: ")
            print(f"ID empleado: {buscarid}")
            print(f"Nombre empleado: {nombre}")
            print(f"Horas trabajadas: {htrabjadas}")
            print(f"Valor hora: {vlhora}")
            print(nominacme)
            break
        else:
            ("Empleado no encontrado")
    input("---> Presione ENTER para continuar")


def Eliminar_empleado(ruta):
    """4. Eliminar empleado: Esta opción permite eliminar a un empleado por su id. Si borra al empleado, muestra
    un mensaje que ha sido eliminado y si no, muestra un mensaje de que no se eliminó el empleado."""
    while True:
        buscarid = input("Ingrese el id del empleado que desea eliminar : ")
        if buscarid in nominacme:
            nominacme.pop(buscarid)
            print(f"ID ELIMINADO,se elimino el id : {buscarid}")
            break
        print("El id ingresado no existe ingrese de nuevo ")

    escribirMemDisco(ruta, nominacme)
    input("---> Presione ENTER para continuar")

def Listar_empleados():
    """5. Listar Empleados: Esta opción permite mostrar los empleados con su información (id, nombre, horas y
valor de la hora trabajada), debe permitir paginación, esto es, se muestran los primeros 5 empleados,
luego para y muestra un mensaje para que el usuario decida si desea seguir viendo o volver al menú. Si
desea seguir viendo, le muestra los siguientes 5 empleados y así sucesivamente hasta que no haya más
empleados o la persona no desee seguir viendo.
Estructura de datos - Diccionarios Trainer Ing.
Carlos H. Rueda C."""
    contador = 4
    indicador = 0
    for empleado in nominacme.keys():
        print("#"*40)
        print("LISTA EMPLEADOS ")
        print("#"*40)

        idencontrado = empleado
        nombre = nominacme[empleado]["nombre"]
        htrabjadas = nominacme[empleado]["Horas trabajadas"]
        vlhora = nominacme[empleado]["Valor hora"]

        print("-----EMPLEADO----")
        print("Los datos del empleado son: ")
        print(f"ID empleado: {idencontrado}")
        print(f"Nombre empleado: {nombre}")
        print(f"Horas trabajadas: {htrabjadas}")
        print(f"Valor hora: {vlhora}")
        print(nominacme)

        if indicador == contador:
            print("Quieres ver otros 5 empleados? ")
            print("Presiona 1 si deseas continuar o Presiona 2 si deseas salir")
            opcion = int(input("OPCION: "))
            if opcion == 1:
                contador += 5
                continue
            elif opcion == 2:
                break
        indicador += 1
    input("---> Presione ENTER para continuar")


def nómina_empleado():
    """6. Listar la nómina de un empleado: Esta opción permite mostrar la nómina de un empleado buscado por
    su ID. El salario bruto se calcula como el valor de la hora por la cantidad de horas trabajadas. Si gana
    menos del salario mínimo legal vigente en Colombia 2023 (por favor consulte el dato) se le debe da
    subsidio de transporte. Se le debe descontar el valor de la eps y pensión correspondiente al 4% cada uno
    y el salario Neto es la suma del salario bruto, el auxilio menos los descuentos."""
    while True:
        buscarid = input("Ingrese el id del empleado que desea modificar: ")
        if buscarid in nominacme:
            print("ID ENCONTRADO")
            break
        else:
            print("ID NO ENCONTRADO")

    sueldobruto = nominacme[buscarid]["Horas trabajadas"] * \
        nominacme[buscarid]["Valor hora"]
    eps = sueldobruto * 0.04
    pension = sueldobruto * 0.04
    descuento = (eps + pension)
    auxilio = 0
    nombre = nominacme[buscarid]["nombre"]
    if sueldobruto <= 1160000:
        print("Merecedor subsidio de transporte")
        auxilio = 140606
    sueldoneto = (sueldobruto + auxilio) - descuento
    print(f"La nomina del empleado {nombre}")
    print(f"Sueldo bruto: {sueldobruto}")
    print(f"Valor eps: {eps}")
    print(f"Valor pension: {pension}")
    print(f"Valor auxilio: {auxilio}")
    print(f"Sueldo neto: {sueldoneto}")
    input("---> Presione ENTER para continuar")


def nómina_todos():
    contador = 4
    indicador = 0
    for empleado in nominacme.keys():
        print("#"*40)
        print("NOMINAS EMPLEADOS ")
        print("#"*40)

        sueldobruto = nominacme[empleado]["Horas trabajadas"] * \
            nominacme[empleado]["Valor hora"]
        eps = sueldobruto * 0.04
        pension = sueldobruto * 0.04
        descuento = (eps + pension)
        auxilio = 0
        nombre = nominacme[empleado]["nombre"]
        if sueldobruto <= 1160000:
            print("Merecedor subsidio de transporte")
            auxilio = 140606
        sueldoneto = (sueldobruto + auxilio) - descuento
        print(f"La nomina del empleado {nombre}")
        print(f"Sueldo bruto: {sueldobruto}")
        print(f"Valor eps: {eps}")
        print(f"Valor pension: {pension}")
        print(f"Valor auxilio: {auxilio}")
        print(f"Sueldo neto: {sueldoneto}")

        if indicador == contador:
            print("Quieres ver otros 5 empleados? ")
            print("Presiona 1 si deseas continuar o Presiona 2 si deseas salir")
            opcion = int(input("OPCION: "))
            if opcion == 1:
                contador += 5
                continue
            elif opcion == 2:
                break
        indicador += 1
    input("---> Presione ENTER para continuar")


def cargarArch(ruta):
    fd = open(ruta, "a+")

    cont = 0
    dicempl = {}
    fd.seek(0)
    for linea in fd:
        cont += 1
        if cont > 1:
            lin = linea.rstrip()
            lstempl = lin.split(";")
            dicempl[lstempl[0]] = {}
            dicempl[lstempl[0]]["nombre"] = lstempl[1]
            dicempl[lstempl[0]]["Horas trabajadas"] = int(lstempl[2])
            dicempl[lstempl[0]]["Valor hora"] = int(lstempl[3])

    fd.close()

    if cont < 2:
        dicempl = {}

    return dicempl


# Validacion menu:
ruta = "Campus Lab/Ciclo 1/Pruebas/codigo/diccionarios/emplacme.dat"
while True:
    nominacme = cargarArch(ruta)

    elegirop = menu()

    if elegirop == 1:
        Agregar_empleado(ruta)
    elif elegirop == 2:
        Modificar_empleado(ruta)
    elif elegirop == 3:
        Buscar_empleado()
    elif elegirop == 4:
        Eliminar_empleado(ruta)
    elif elegirop == 5:
        Listar_empleados()
    elif elegirop == 6:
        nómina_empleado()
    elif elegirop == 7:
        nómina_todos()
    elif elegirop == 8:
        print("Se ha cerrado el programa")
        break

# print(nominacme)