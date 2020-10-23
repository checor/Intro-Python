# Reto 3: Estructuras
# Con la estructura de abajo, vuelve a calcular
# el porcentaje de falla y problema de línea

piezas = {
    'correctas': ['OK', 'OK', 'OK', 'OK', 'OK', ],
    'fallidas': ['Incompleta', 'Rota', 'Incompleta']
}

# Solución

# Calculamos el porcentaje de falla como el reto anterior
# pero ahora accediendo a los datos del diccionario
# y calculando el total en la lista con len
piezas_correctas = len(piezas['correctas'])
piezas_fallidas = len(piezas['fallidas'])

total_piezas = piezas_correctas + piezas_fallidas
porcentaje_falla = (piezas_fallidas / total_piezas) * 100
porcentaje_falla = round(porcentaje_falla * 100, 2)

print("Porcentaje de falla", porcentaje_falla, "%")

if porcentaje_falla >= 3:
    print("Problema en la línea")
else:
    print("Línea OK")