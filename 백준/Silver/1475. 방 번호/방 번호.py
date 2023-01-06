N = input()
D = {}
for n in N:
    n = int(n)
    if n==9:
        D[6] = D.get(6, 0)+1
    else:
        D[n] = D.get(n, 0)+1

six = D.get(6, 0)
D[6] = six//2+1 if six%2 else six//2

print(max(D.values()))