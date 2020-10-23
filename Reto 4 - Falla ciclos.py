# Reto 4: Ciclos
# Indicar cuantas piezas incompletas hay
# así como piezas rotas
piezas = {
    'correctas': ['OK', 'OK', 'OK', 'OK', 'OK', ],
    'fallidas': ['Incompleta', 'Rota', 'Incompleta']
}

# Solución
# Una manera es usar dos contadores como variables
# Y utilizar un for para revisar todas las piezas
piezas_rotas = 0
piezas_incompletas = 0

for pieza in piezas['fallidas']:
    if pieza == 'Incompleta':
        piezas_incompletas += 1
    if pieza == 'Rota':
        piezas_rotas += 1

print("Piezas rotas", piezas_rotas)
print("Piezas incompleta", piezas_incompletas)
