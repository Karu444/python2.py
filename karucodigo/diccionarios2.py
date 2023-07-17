num_estudiantes_ingles = int(input())
estudiantes_ingles = set(map(int, input().split()))
num_estudiantes_frances = int(input())
estudiantes_frances = set(map(int, input().split()))

estudiantes_ingles_exclusivos = estudiantes_ingles - estudiantes_frances

total_estudiantes_ingles_exclusivos = len(estudiantes_ingles_exclusivos)

print(total_estudiantes_ingles_exclusivos)