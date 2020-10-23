# Ejemplo 6: Graficación con Pandas
# Pandas puede graficar con ayuda de la librería Matplotlib
# Se recomienda revisar su documentación para conocer todas sus funciones
# https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html
import pandas as pd
# Necesitamos importar pyplot para mostrar gráficas
import matplotlib.pyplot as plt

# Leemos el CSV como en el ejemplo anterior
alumnos = pd.read_csv("alumnos.csv")

# Calculamos el promedio
alumnos['Promedio'] = (alumnos['Calificacion 2'] + alumnos['Calificacion 2'] + alumnos['Calificacion 3']) / 3

# Preparamos la grafica
# title: Coloca titulo a la gráfica
# kind: Indica el tipo (barras, lineal...)
alumnos['Promedio'].plot(title="Promedio del salon", kind='bar')

# Mostramos la grafica
plt.show()
