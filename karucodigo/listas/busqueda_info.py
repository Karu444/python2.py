def buscarElem(lst, elem):
    for i in range(len(lst)):
        if lst[i] == elem:
            return i
    return None

def encontrarElem(lst, elem):
    for e in lst:
        if e == elem:
            return True 
    return False

lst = [1, 3, 4, 65, 54]
pos = buscarElem(lst, 68)
if pos != None:
    print(pos)
else:
    print("NO EXISTE en la lista.")
