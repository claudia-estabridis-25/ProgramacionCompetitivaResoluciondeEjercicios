import math

r, a = map(int, input().split())

mcd = math.gcd(r, a) # función para calcular el MCD
mcm = (r*a)//mcd

print(mcm)

"""
MCD: Busca el número más grande que divide a otros (se usa para repartir cosas en grupos iguales).

MCM: Busca el número más pequeño que es múltiplo de otros (se usa para saber cuándo coinciden eventos que se repiten).

$$MCM(a, b) = \frac{|a \times b|}{MCD(a, b)}$$
"""
