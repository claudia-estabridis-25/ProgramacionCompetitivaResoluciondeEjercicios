n = int(input())
rating_casas = list(map(int, input().split()))
# input().split() lee toda la línea de ratings de una sola vez, así que NO se necesita un bucle for para leer los ratings

visitas_trineo = 0
cont_entregas = 0

entregadas = []
for i in range(n):    
    entregadas.append(False)

while cont_entregas < n:
    mayor = max(rating_casas)
    pos_actual = rating_casas.index(mayor) # .index() elige el índice más a la izquierda
    
    # Contador para las visitas del trineo
    visitas_trineo += 1

    # Validamos que la posición actual (la casa) no haya recibido regalos, para recién marcarla como entregada True
    if entregadas[pos_actual] == False:
        entregadas[pos_actual] = True
        cont_entregas += 1 # Para poder terminar el bucle while
    rating_casas[pos_actual] = -1
    
    # Antes de verificar si las casas adyacentes ya recibieron regalos, primero verificamos que exista la posición contigua, para evitar
    # desbordar los rangos
    if pos_actual - 1 >= 0:
        if entregadas[pos_actual - 1] == False:
            entregadas[pos_actual - 1] = True
            cont_entregas += 1
        rating_casas[pos_actual - 1] = -1
    
    if pos_actual + 1 < n:
        if entregadas[pos_actual + 1] == False:
            entregadas[pos_actual + 1] = True
            cont_entregas += 1
        rating_casas[pos_actual + 1] = -1

print(visitas_trineo)

"""
Notas:
- Se asigna -1 a las casas que ya tienen regalos entregados para que la función max() las ignore, así, hallará la siguiente casa con mayor rating
que no haya sido visitada.
- El método .index(valor) busca en la lista de izquierda a derecha, y devuelve la primera posición donde encuentra dicho valor.
"""
