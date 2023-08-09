def main():
    D = {}
    for _ in range(N):
        n, v = input().split()
        v = float(v)
        if not D.get(v, []): D[v] = []
        D[v].append(n)
    print(*D[max(D.keys())])

while True:
    N = int(input())
    if not N: break
    main()