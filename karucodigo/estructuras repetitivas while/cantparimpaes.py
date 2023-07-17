canPares = 0
canImpares = 0

num = int(input("Numero entero: "))
while num != -1:
    if num % 2 == 0:
        print("--> El numero es PAR")
        canPares = canPares + 1
    else:
        print("--> El numero es IMPAR")
        canImpares = canImpares + 1
    
    num = int(input("\nNumero entero: "))
    
print("\n", "-" * 30)
print("Cantidad de numeros PARES:", canPares)
print("Cantidad de numeros IMPARES:", canImpares)