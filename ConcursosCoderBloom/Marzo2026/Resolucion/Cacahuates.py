n = int(input())
cacahuates = list(map(int, input().split()))

maximo = max(cacahuates)
cont = 0

for bolsa in cacahuates:
    if bolsa == maximo:
        cont += 1
        # pos_max = cacahuates.index(maximo)

print(maximo, cont)
