n, m = map(int, input().split())
stilles = [0] * (n+1)
capturas = [0] * (n+1)

for _ in range (m):
    evento = input().split()
    tipo_evento = evento[0] # Guardo CAPTURA o ROBO

    if tipo_evento == "CAPTURA":
        p = int(evento[1]) # participante
        k = int(evento[2]) # cantidad Stille capturada
        stilles[p] += k
        capturas[p] += 1

    if tipo_evento == "ROBO":
        p = int(evento[1]) # participante ratero
        q = int(evento[2]) # participante robado
        k = int(evento[3]) # cantidad Stille robada
        robo = min(k, stilles[q])
        stilles[q] -= robo
        stilles[p] += robo

ganador = 1

# El bucle empieza en 2 porque si empezara en 1, estaría comparando al participante 1 contra sí mismo (ganador ya empieza con 1)
for i in range(2, n + 1):
    if stilles[i] > stilles[ganador]:
        ganador = i
    elif stilles[i] == stilles[ganador]:
        if capturas[i] > capturas[ganador]:
            ganador = i
# ¿Qué pasa si capturas[i] == capturas[ganador]? NO HACEMOS NADA. Como ganador ya tiene un número menor (porque el bucle for va de menor a mayor),
# al no entrar en el IF, conservamos al de menor número.

print(ganador)

"""
La función min(k, stilles[q]) compara cuánto se quiere robar (k), contra cuánto hay realmente disponibles (stilles[q]), de esa forma se valida que
no se robe más de lo que hay porque el resultado saldría negativo.
"""
