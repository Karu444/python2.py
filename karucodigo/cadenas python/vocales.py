while True:
    frase = input("Ingrese frase: ")
    if frase.strip() == "":
        print("Error. Ingrese frase correcta.")
        continue
    break

cont = 0
for f in frase:
    if f.lower() in "aeiou":
        cont += 1
    elif f.lower() == "q":
        break

print("Cantidad de vocales: ", cont)