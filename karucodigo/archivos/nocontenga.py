import io

fd = open("codigo/archivos/mbox-short.txt", "r", encoding="utf-8")
for linea in fd:
    line = linea.rstrip()
    if not "@uct.ac.za" in line :
        continue
    print(line)

fd.close()
