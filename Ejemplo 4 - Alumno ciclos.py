alumno = {
    "nombre": "Sergio Urbina",
    "edad": 28,
    "semestre": 20,
    "calificaciones": [10, 5, 8, 7, 10]
}

print("Nombre de alumno:", alumno['nombre'])
print("Edad:",  alumno['edad'], "años")

for calificacion in alumno['calificaciones']:
    if calificacion < 7:
        print("No aplica para la beca")
        quit()
        
print("Si aplica para la beca")