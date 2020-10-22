import pandas as pd
import matplotlib.pyplot as plt

alumnos = pd.read_csv("alumnos.csv")

alumnos['Promedio'] = (alumnos['Calificacion 2'] + alumnos['Calificacion 2'] + alumnos['Calificacion 3']) / 3

alumnos = alumnos.sort_values('Promedio', ascending=False)

print(alumnos[['Nombre', 'Promedio']])
