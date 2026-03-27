a, b, x = map(int, input().split())

if ((x-a) % b == 0) and (x >= (a+b)):
    print("SI")
else:
    print("NO")
