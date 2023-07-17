articulos = {1: "Lapiz", 2: "Cuadernos", 3: "Borrador", 4: "Calculadora", 5: "Escuadra"}
valores = {1: 2500, 2: 3800, 3: 1200, 4: 35000, 5: 3700}

N = int(input("Ingrese la cantidad de artículos diferentes que desea comprar: "))

compra = {}

for i in range(N):
    codigo = int(input("Ingrese el código del artículo: "))
    cantidad = int(input("Ingrese la cantidad comprada: "))
    
    if codigo in valores:
        nombre = articulos[codigo]
        valor_unitario = valores[codigo]
        valor_total = valor_unitario * cantidad
        compra[codigo] = {"Nombre": nombre, "Cantidad": cantidad, "Valor Unitario": valor_unitario, "Valor Total": valor_total}
    else:
        print("Código de artículo inválido. Inténtelo nuevamente.")
        continue

valor_total_compra = sum(item["Valor Total"] for item in compra.values())

for codigo, info in compra.items():
    print(f"Código: {codigo}")
    print(f"Nombre: {info['Nombre']}")
    print(f"Cantidad: {info['Cantidad']}")
    print(f"Valor Unitario: {info['Valor Unitario']}")
    print(f"Valor Total: {info['Valor Total']}")
    print("")

print(f"Valor Total de la Compra: {valor_total_compra}")

