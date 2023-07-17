while True:
    clave = input("Ingrese contraseña: ")
    if clave.strip() == "":
        print("Error. Ingrese contraseña correcta.")
        continue
    break

if len(clave) >= 8:
    isMay = False
    isMin = False
    isNum = False
    isSim = False
    for c in clave:
        ascii = ord(c)
        # validar si hay Mayuscula
        if ascii >= 65 and ascii <= 90 or ascii == 165:
            isMay = True
        # validar si hay Minuscula
        elif ascii >= 97 and ascii <= 122 or ascii == 164:
            isMin = True
        # validar si es numerico
        elif c.isdigit():
            isNum = True
        elif c in "%^&":
            isSim = True
        
        if isMay and isMin and isNum and isSim:
            break

    if isMay and isMin and isNum and isSim:
        print("Contraseña válida")
    else:
        print("Contraseña Inválida")
        
else:
    print("Contraseña Inválida")