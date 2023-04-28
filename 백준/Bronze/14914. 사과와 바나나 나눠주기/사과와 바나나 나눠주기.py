a, b = map(int, input().split())
maxx = max(a, b)

for n in range(1, maxx+1):
    if a%n or b%n: continue
    print(n, a//n, b//n)