# Reto 1: Piezas fallidas
# Calcular el porcentaje de pieza fallidas
# utilizando las variables a continuación

piezas_correctas = 67
piezas_fallidas = 7

# Solución:
# Calculamos el total de piezas en un varaible
total_piezas = piezas_correctas + piezas_fallidas
# En otra variable, calculamos el porcentaje
porcentaje_falla = (piezas_fallidas / total_piezas) * 100
# Opcional: Redondear el resultado antes de mostrarlo
porcentaje_falla = round(porcentaje_falla * 100, 2)
# Mostramos el resultado:
print("Porcentaje de falla", porcentaje_falla, "%")
