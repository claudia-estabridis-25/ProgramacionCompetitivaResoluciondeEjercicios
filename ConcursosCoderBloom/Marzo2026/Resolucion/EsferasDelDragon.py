n = int(input())
estrellas = list(map(int, input().split()))
cont = 0

for i in range(n):
    if estrellas[i] >= 1 and estrellas[i] <= 7:
        cont += 1

print(cont)
