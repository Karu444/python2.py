#caputarar el nombre
while True:
    nom = input("Nombre: ")
    if nom == "" or nom.strip() == "":
        print("Ingrese un nombre válido")
        continue
    break
    
#capturar la nota
while True:
    try: 
        nota = round(float(input("Nota (0.0 a 5.0): ")), 2)
        if nota < 0 or nota > 5:
            print("Ingrese una nota entre 0.0 y 5.0")
            continue
        break
    except ValueError:
        print("Ingrese una nota válida.")

sum = 0
ce = 0
prom = 0
mayor = nota
nommayor = nom
menor = nota
nommenor = nom
while nom.upper() != "FIN":
    sum += nota # sum = sum + nota
    ce += 1 # ce = ce + 1
    
    if nota > mayor:
        mayor = nota
        nommayor = nom
    elif nota < menor:
        menor = nota
        nommenor = nom
    
    #caputarar el nombre
    while True:
        nom = input("Nombre: ")
        if nom == "" or nom.strip() == "":
            print("Ingrese un nombre válido")
            continue
        break
        
    #capturar la nota
    while True:
        try: 
            nota = float(input("Nota (0.0 a 5.0): "))
            if nota < 0 or nota > 5:
                print("Ingrese una nota entre 0.0 y 5.0")
                continue
            break
        except ValueError:
            print("Ingrese una nota válida.")
            

prom = sum / ce
print(f"El promedio de las notas es: {prom:.2f}")
print(f"El estudiante con mayor nota es {nommayor} ({mayor})")
print(f"El estudiante con menor nota es {nommenor} ({menor})")
        

