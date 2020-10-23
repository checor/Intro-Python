# Reto 2: Condicion de falla
# Si el porcentaje de falla es mayor a 3%
# Alertar de un problema en la línea

piezas_correctas = 67
piezas_fallidas = 7

# Solucion
# Calculamos el porcentaje de falla como el reto anterior
total_piezas = piezas_correctas + piezas_fallidas
porcentaje_falla = (piezas_fallidas / total_piezas) * 100
porcentaje_falla = round(porcentaje_falla * 100, 2)

print("Porcentaje de falla", porcentaje_falla, "%")

# Revisamos el porcentaje sea menor o igual a 3%
if porcentaje_falla >= 3:
    print("Problema en la línea")
else:
    print("Línea OK")