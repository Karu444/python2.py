"""
Ejercicio 3
Determinar e imprimir si un número es primo o no
"""

while True:
    try:
        n = int(input("\nNumero? "))
        if n < 2:
            print("Ingrese un numero entero mayor que 1")
            continue
        break
    except ValueError:
        print("Ingrese un numero valido.")

primo = True
divisor = 0
for i in range(2, n):
    if n % i == 0:
        primo = False
        divisor = i
        break
        
if primo:
    print("El numero es primo")
else:
    print("El numero no es primo. lo divide", divisor)