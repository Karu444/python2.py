"""
Dado el nombre y salario de un empleado, calcular el 
subsidio de transporte, teniendo en cuenta que si el 
salario es menor o igual a $1.200.000 entonces tiene 
derecho a un subsidio de transporte por valor de $120.000, 
de lo contrario no tiene derecho al subsidio de 
transporte.  Se debe visualizar el nombre, salario y 
subsidio de transporte 
"""

nom = input("Ingrese el nombre: ")
sal = int(input("Ingrese el salario: "))


if sal <= 1_200_000:
    subtrans = 120_000
else:
    subtrans = 0

print("\n", "-" * 30)
print("Nombre:", nom)
print("Salario:", sal)
print("Subsidio:", subtrans)
print("-" * 30, "\n")
