n = int(input("Numero: "))
mayor = n
menor = n
while n >= 0:
    if n > mayor:
        mayor = n
    elif n < menor:
        menor = n
        
    n = int(input("Numero: "))

print("El numero menor es: ", menor)
print("El numero mayor es: ",  mayor)  