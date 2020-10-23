# Reto 5: Analisis de datos
# Lee el archivo bosch y calcula el porcentaje
# de falla de cada línea así como si la linea
# presenta riesgo
import pandas as pd

produccion = pd.read_csv("bosch.csv")

# Solución
# Utilizar el dataframe creado y agregar nuevos campos
# para calcular el porcentaje de falla
produccion['total_piezas'] = produccion['piezas_ok'] + produccion['piezas_falla']
produccion['pocentaje_fallo'] = (produccion['piezas_falla'] / produccion['total_piezas']) * 100
# Podemos usar expresiones booleanas sin problema
produccion['alerta_linea'] = produccion['pocentaje_fallo'] > 3

# Opcional: Ordenar por procentaje de fallo
produccion = produccion.sort_values('pocentaje_fallo', ascending=False)

# Guardamos resultados en nuevo archivo
produccion.to_csv("bosch_resultados.csv")
