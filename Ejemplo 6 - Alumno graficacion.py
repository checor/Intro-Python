import pandas as pd
import matplotlib.pyplot as plt

alumnos = pd.read_csv("alumnos.csv")

alumnos['Promedio'] = (alumnos['Calificacion 2'] + alumnos['Calificacion 2'] + alumnos['Calificacion 3']) / 3
alumnos['Promedio'].plot(x='Promedio', title="Promedio por numero de lista", use_index=False)

print(alumnos['Promedio'])
