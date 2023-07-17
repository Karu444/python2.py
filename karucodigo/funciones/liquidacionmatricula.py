## PROGRAMA GENERAL
cod = leerInt("Ingrese el código del estudiante: ")
nom = leerString("Ingrese el nombre del estudiante: ")
progAcad = leerProgramaAcademico()
beca = leerIndBeca()

valNetoPagar = calMatricula(progAcad, beca)

print("\n", "-" * 40)
print("Estudiante: ", nom)
print(f"El valor neto a pagar es: f{valNetoPagar:,.0f}")
