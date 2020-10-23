# Reto 6: Graficacion
# Graficar el porcentaje de fallo de las líneas
import pandas as pd
import matplotlib.pyplot as plt

produccion = pd.read_csv("bosch.csv")

# Solución:
# Calcular el porcentaje como el reto anterior y usar pd.plot()
produccion['total_piezas'] = produccion['piezas_ok'] + produccion['piezas_falla']
produccion['pocentaje_fallo'] = (produccion['piezas_falla'] / produccion['total_piezas']) * 100
produccion['alerta_linea'] = produccion['pocentaje_fallo'] > 3

# Usaremos las opciones de plot para graficar sólo la línea y el porcentaje de fallo
produccion.plot(x="linea", y="pocentaje_fallo", title="Porcentaje de fallo por línea")
plt.show()
