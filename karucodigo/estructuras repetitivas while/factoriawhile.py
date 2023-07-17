n = int(input("Ingrese el valor de N: "))
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i = i + 1
print(f"El factorial de {n} es: {fact}")