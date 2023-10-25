def main():
    N = int(input())
    E = int(input())
    D = {}
    for a in range(1, N+1):
        D[a] = set()

    for e in range(E):
        K, *arr = map(int, input().split())
        if 1 in arr:
            for a in arr:
                D[a].add(e)
        else:
            ssum = set()
            for a in arr:
                ssum = ssum | D[a]

            for a in arr:
                D[a] = ssum | set()

    ret = []
    for k in D.keys():
        if D[1]-D[k]: continue
        ret.append(k)

    for k in sorted(ret):
        print(k)

main()