a, b, c = map(int, input().split())
d = int(input())

# Combinaciones:
# a + b
# a + c
# b + c

if (a + b) == d:
    print(a, b)
elif (a + c) == d:
    print(a, c)
elif (b + c) == d:
    print(b, c)
