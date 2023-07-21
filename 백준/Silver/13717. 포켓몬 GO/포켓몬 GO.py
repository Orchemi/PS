def main():
    N = int(input())
    D = {}
    names = []
    for _ in range(N):
        name = input()
        names.append(name)
        K, M = map(int, input().split())
        D[name] = 0
        while M >= K:
            m, n = M//K, M%K
            D[name] += m
            M = n + 2*m

    cnts = D.values()
    ssum, maxx = sum(cnts), max(cnts)
    for name in names:
        if D[name] == maxx:
            return ssum, name

print(*main(), sep='\n')