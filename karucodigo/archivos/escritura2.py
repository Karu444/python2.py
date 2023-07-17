fd = open("codigo/archivos/prueba2.txt", "w")
lst = ["Primera linea\n", "Segunda linea\n"]
fd.writelines(lst)
fd.close()