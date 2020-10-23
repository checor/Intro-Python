# Ejemplo 4: Estructuras de datos
# Las listas y diccionarios
# permiten organizar valores para evitar
# tener muchas variables individuales
alumno = {
    "nombre": "Sergio Urbina",
    "edad": 28,
    "semestre": 20,
    "calificaciones": [10, 9, 8, 7, 10]
}

# Tanto listas como diccionarios
# se acceden con []
print("Mi nombre es", alumno['nombre'])
print("Tengo",  alumno['edad'], "años")
print("Mi ultima calficación es:", alumno['calificaciones'][-1])

if alumno['edad']:
    print("Eres mayor de edad")
else:
    print("Aun no puedes tomar :(")
print("Adios")
