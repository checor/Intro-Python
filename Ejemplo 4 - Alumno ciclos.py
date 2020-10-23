# Ejemplo 4: Ciclos de control
# permiten realizar la misma accion hasta
# que cierta condición deje de ser verdadera
alumno = {
    "nombre": "Sergio Urbina",
    "edad": 28,
    "semestre": 20,
    "calificaciones": [10, 5, 8, 7, 10]
}

print("Nombre de alumno:", alumno['nombre'])
print("Edad:",  alumno['edad'], "años")

becado = True

for calificacion in alumno['calificaciones']:
    if calificacion < 7:
        becado = False
        break # Rompe el ciclo

if becado:
    print("Si aplica para la beca")
else:
    print("No aplica para la beca")