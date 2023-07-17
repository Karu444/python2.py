try:
    n = int(input("Numero: "))
    res = 10 / n
    print("El resultado de la operacion es:", res)
except ValueError:
    print("!Error!. Debes ingresar un numero válido.")
except ZeroDivisionError:
    print("!Error!. No se puede dividir entre cero.")
except Exception as e:
    print("!Error!. Ha ocurrido un error inesperado.", str(e))
    
print("FIN DE PROGRAMA")