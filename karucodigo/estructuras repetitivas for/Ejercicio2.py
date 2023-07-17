"""
Ejercicio 2:
Hacer un programa que calcule el factorial de un numero.

factoria 5 = 1 * 2 * 3 * 4 * 5 = 120
Factorial N = 1 * 2 * 3 * ... * N
"""

n = int(input("Ingrese el valor de N: "))

fact = 1
for i in range(1, n+1):
    fact = fact * i
    
print(f"El factorial de {n} es: {fact}")