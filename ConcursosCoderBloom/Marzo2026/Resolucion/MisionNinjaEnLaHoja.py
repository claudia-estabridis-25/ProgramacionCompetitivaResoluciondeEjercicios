rangos = list(map(int, input().split()))
dificultades = list(map(int, input().split()))

def calcula_cobro(rango, dif):
    if rango == 1 and dif <= 2:
        return rango*dif
    elif rango == 2 and dif <= 3:
        return rango*dif
    elif rango == 3:
        return rango*dif
    else:
        return 0

ganancia_max = 0

# Combinaciones
for i in range(3):
    for j in range(3):
        for k in range(3):
            if i != j and i != k and j != k:
                cobro1 = calcula_cobro(rangos[0], dificultades[i])
                cobro2 = calcula_cobro(rangos[1], dificultades[j])
                cobro3 = calcula_cobro(rangos[2], dificultades[k])

                ganancia_actual = cobro1 + cobro2 + cobro3

                if ganancia_actual > ganancia_max:
                    ganancia_max = ganancia_actual

print(ganancia_max)
