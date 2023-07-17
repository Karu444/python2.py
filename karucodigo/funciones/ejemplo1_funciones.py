# SINTAXIS GENERAL
# def nombre_funcion([param1, param2, .., paramN]):
#     cuerpo_funcion

def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print("Error!. Ingrese un numero entero válido.")
    
# funcion que sume dos numeros
def sumar(num1, num2):
    s = num1 + num2
    return s

a = leerInt("Ingrese un numero: ")
b = leerInt("Ingrese otro numero: ")
print(f"El resultado de la suma es: {sumar(a, b)}")

