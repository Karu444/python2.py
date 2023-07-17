def crearMat(fils, cols):
    mat = []
    for f in range (fils):
        fila = []
        for c in range(cols):
            fila.append(0)
        mat.append(fila)
        
    return mat

def printMat(m):
    for f in range(len(m)):
        for c in range(len(m[f])):
            print(m[f][c], end="\t")
        print("")


fils = 3
cols = 4
m = crearMat(fils, cols)
print(m)
m[2][1] = 5
printMat(m)