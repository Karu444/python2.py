#Funciones
def prodMayVtasSem(mat):
    vsumprod = []
    for f in range(len(mat)):
        sum = 0
        for c in range(len(mat[f])):
            sum += mat[f][c]
        vsumprod.append(sum)

    print(vsumprod)
    return vsumprod.index(max(vsumprod)) + 1


def prodMayVtasSem2(mat):
    # se modifica la funcion para aprovechar el recorrido e ir encontrando la respuesta

    # prod con mayor ventas.
    # Inicia en 0 para darle un valor de arranque que luego cambiara en el algoritmo
    prodmayvta = 0

    # Venta semanal mayor.
    # Inicia con un valor menor posible. Cualquier producto tendra ventas mayores a -1
    vtasemmay = -1
    for f in range(len(mat)):
        sum = 0
        for c in range(len(mat[f])):
            sum += mat[f][c]

        if sum > vtasemmay:
            # Si las ventas de las semana superan a las ventas que se tenian como mayores
            # entonces esa semana se vendió más y el producto es el de la fila f
            vtasemmay = sum
            prodmayvta = f + 1
    return prodmayvta

# Programa Principal
mventas = [[100, 88, 92, 94, 85, 110, 118],
           [30, 42, 31, 32, 38, 40, 37],
           [23, 35, 39, 45, 55, 60, 61],
           [45, 50, 56, 65, 45, 57, 68],
           [18, 25, 33, 21, 22, 28, 32]]

pmyVtasSem = prodMayVtasSem2(mventas)
print("El producto que mas vende a la semana es:", pmyVtasSem)
