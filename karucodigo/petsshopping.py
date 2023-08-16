import json, os
os.system("clear")

def menu():
    os.system("clear")
    print("=" *40)
    print("========== Bienvenido al menu ==========")
    print("============= PetShopping ==============")
    print("1.                     Mostrar mascotas.")
    print("2.                     Agregar mascotas.")
    print("3.               Buscar tipo de mascota.")
    print("4.                     Actualizar datos.")
    print("5.                     Eliminar mascota.")
    print("0.                                Salir.")
    print("=" *40)
    print(" ")
    print("=" *40)
    print(" ")
    print("           / \  w  / \ ")
    print("       \ \   >     <  / /")
    print("       =    n  >º<  n   =")
    print("          =          = ")
    print("               ===         ==>>>")
    print("             (  v  )     //")
    print("            (  vvv  ) ==//  ")
    print("            \  / \  /")
    print("         ^  nnn   nnn  ^")
    print("      ^^^^^^^^^^^^^^^^^^^  ")
    print("=" *40)

def opcion_1():
    print("Has elegido la Opción 1.")
    print("Estas son nuestras mascotas disponibles: ")
    with open("petshopping.json", "r") as file:
        mascotas = json.load(file)  
        print("{:<3} {:<1} {:<10} {:<1} {:<15} {:<1} {:<10} {:<1} {:<35} {:<1}".format(" ", "|", "TIPO", "|", "RAZA", "|", "PRECIO", "|", "SERVICIOS", "|"))
        counter = 1
    for x in mascotas["pets"]:
        services = ""
        for y in x["servicios"]:
                services = str(services) + str(y) + ", " 
        services = services
        print("{:<3} {:<1} {:<10} {:<1} {:<15} {:<1} {:<10} {:<1} {:<35} {:<1}".format(str(counter), "|", x["tipo"], "|", x["raza"], "|", x["precio"], "|", services.title().rstrip(", "), "|"))
        counter += 1
    input()
        

def opcion_2():
    print("Has elegido la Opción 2")
    print("Por favor llena los datos correspondientes para agregar la nueva mascota.")
    
    tipo = input("Digite el tipo de mascota que deseas agregar: ")
    raza = input("Digite las razas de la nueva mascota: ")
    precio = int(input("Digite el precio de la nueva mascota: "))
    servicios = input("Digite los servicios asociados a la nueva mascota (separados por comas): ").split(',')
    
    nueva_mascota = {
        "tipo": tipo,
        "raza": raza,
        "precio": precio,
        "servicios": servicios
    }
    
    with open("petshopping.json", "r+") as file:
        data = json.load(file)
        data["pets"].append(nueva_mascota)
        file.seek(0)
        json.dump(data, file, indent=4)
    
    print("Mascota agregada con éxito.")
    input()

    
def opcion_3():
    print("Has elegido la Opción 3")
    tipo_elegido = input("Digite el tipo de mascota que desea buscar: ")
    with open("petshopping.json", "r") as file:
        mascotas = json.load(file)
        print("{:<3} {:<1} {:<10} {:<1} {:<15} {:<1} {:<10} {:<1} {:<35} {:<1}".format(" ", "|", "TIPO", "|", "RAZA", "|", "PRECIO", "|", "SERVICIOS", "|"))
        counter = 1
        for x in mascotas["pets"]:
            if x["tipo"] == tipo_elegido:
                services = ", ".join(x["servicios"])
                print("{:<3} {:<1} {:<10} {:<1} {:<15} {:<1} {:<10} {:<1} {:<35} {:<1}".format(str(counter), "|", x["tipo"], "|", x["raza"], "|", x["precio"], "|", services.title(), "|"))
                counter += 1
        input()

def opcion_4():
    print("Has elegido la Opción 4")
    with open("petshopping.json", "r+") as file:
        data = json.load(file)
        print("Estas son nuestras mascotas disponibles: ")
        for idx, mascota in enumerate(data["pets"]):
            print(f"{idx + 1}: {mascota['tipo']} - {mascota['raza']}")
        indice = int(input("Elije el índice de la mascota a actualizar: ")) - 1
        if 0 <= indice < len(data["pets"]):
            mascota_actualizada = data["pets"][indice]
            print(f"Actualizando datos para {mascota_actualizada['tipo']} - {mascota_actualizada['raza']}")
            
            tipo = input("Digite el tipo de mascota actualizado: ")
            raza = input("Digite las razas de la mascota actualizada: ")
            precio = int(input("Digite el precio de la mascota actualizado: "))
            servicios = input("Digite los servicios actualizados (separados por comas): ").split(',')

            mascota_actualizada["tipo"] = tipo
            mascota_actualizada["raza"] = raza
            mascota_actualizada["precio"] = precio
            mascota_actualizada["servicios"] = servicios
            
            data["pets"][indice] = mascota_actualizada

            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()  
            
            print("Mascota actualizada con éxito.")
        else:
            print("Índice inválido.")
        input()




def opcion_5():
    print("Has elegido la Opción 5")
    with open("petshopping.json", "r") as file:
        data = json.load(file)
        print("Estas son nuestras mascotas disponibles: ")
        for idx, mascota in enumerate(data["pets"]):
            print(f"{idx + 1}: {mascota['tipo']} - {mascota['raza']}")
        indice = int(input("Elije el índice de la mascota a eliminar: ")) - 1
        if 0 <= indice < len(data["pets"]):
            mascota_eliminada = data["pets"].pop(indice)
            print(f"Eliminando {mascota_eliminada['tipo']} - {mascota_eliminada['raza']}")
            with open("petshopping.json", "w") as file:
                json.dump(data, file, indent=4)
            print("Mascota eliminada con éxito.")
        else:
            print("Índice inválido.")
        input()

while True:
    menu()
    opcion = input("Elige una opción (1-4): ")

    if opcion == '1':
        opcion_1()
    elif opcion == '2':
        opcion_2()
    elif opcion == '3':
        opcion_3()
    elif opcion == '4':
        opcion_4()
    elif opcion == '5':
        opcion_5() 
    elif opcion == '0':
        print("=" *40)
        print("===== Gracias por usar el programa =====")
        print("============= PetShopping ==============")
        print("============ ¡Hasta luego! =============")
        break
    else:
        print("Opción inválida. Por favor, elige una opción válida.")

menu()