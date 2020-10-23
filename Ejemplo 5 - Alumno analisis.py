# Ejemplo 5: Analisis de datos
# Pandas es una librería para el análisis de datos
# Necesitamos instalarla e importarla
# Mas información: https://pandas.pydata.org/docs/
import pandas as pd

# Pandas read_csv toma un archivo csv y lo convierte en un DataFrame
alumnos = pd.read_csv("alumnos.csv")

# Agregamos una nueva columna, el promedio calculado
alumnos['Promedio'] = (alumnos['Calificacion 2'] + alumnos['Calificacion 2'] + alumnos['Calificacion 3']) / 3

# Opcionalmente, podemos orndarlos por promedio
alumnos = alumnos.sort_values('Promedio', ascending=False)

# Podemos imprimir o guardar los resultados
# En este caso, vamos a guardarlos en un nuevo csv
alumnos[['Nombre', 'Promedio']].to_csv("alumnos_resultados.csv")
