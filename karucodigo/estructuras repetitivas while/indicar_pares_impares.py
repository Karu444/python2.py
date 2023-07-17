"""
Dada unos  números enteros, que se ingresan uno a uno se pide calcular e imprimir:

Cuáles y cuántos números son pares
Cuáles y cuántos números son impares

El ingreso de números se termina cuando el número ingresado es -1 (Bandera o testigo)

"""

canPares = 0
canImpares = 0

# Se lee el primer numero
num = int(input("Numero entero: "))
while num != -1:
    # Si es diferente a -1 HAGA
    if num % 2 == 0:
        print("--> El numero es PAR.")
        canPares += 1
    else:
        print("--> El numero es IMPAR.")
        canImpares = +1
    
    # Leer el siguiente numero
    num = int(input("\nNumero entero: "))

print("\n", "-" * 30)
print("Cantidad de numero PARES:", canPares)
print("Cantidad de numero IMPARES:", canImpares)
print("-" * 30, "\n")
