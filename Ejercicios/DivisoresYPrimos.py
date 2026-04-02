# Hallar todos los divisores de N en complejidad O(sqrt(N))
# Formas de sacar la raiz en python: sqrt(n), n ** 0.5
# d, n/d <-> n = d*(n/d)

n = int(input())
divisores = []

for i in range(1, int(n ** 0.5) + 1): # se verifica hasta la raiz(n)
    if n % i == 0: # sí es divisor
        divisores.append(i)
        if (i != (n/i)): # para que no repita el último divisor
            divisores.append(int(n / i))
            # para que me dé las parejas de los divisores (así da todos los divisores)

divisores.sort() # para ordenar la lista (menor a mayor)
print(divisores)

# Verificando si es primo
if len(divisores) == 1:
    print(f"N: {n} no es primo ni compuesto")
elif len(divisores) <= 2:
    print(f"N: {n} es primo")
else:
    print(f"N: {n} es compuesto")
