# Diseñar una función que calcule la media de tres nú-
# meros leídos del teclado y poner un ejemplo de su 
# aplicación.

def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print("Error!. Ingrese un numero entero válido.")

def media(n1, n2, n3):
    m = (n1+n2+n3) / 3
    return m

a = leerInt("Ingrese el primer número: ")
b = leerInt("Ingrese el segundo número: ")
c = leerInt("Ingrese el tercer número: ")
prom = media(a, b, c)
print(f"La media de {a}, {b}, {c} es {prom:.3f}")
