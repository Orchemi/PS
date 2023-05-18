def main():
    def find_direction():
        D = {}
        for t in g1: D[t] = -1
        for t in g2: D[t] = 1
        return D

    N1, N2 = map(int, input().split())
    N = N1+N2
    g1 = input()
    g2 = input()
    T = int(input())
    D = find_direction()
    ret = [*list(g1)[::-1], *list(g2)]

    now = 0
    while now < T:
        move_set = set()
        for i in range(N):
            j = i-D[ret[i]]
            if not (0<=j<N): continue
            if D[ret[i]]==D[ret[j]]: continue
            if (i, j) in move_set: continue
            if (j, i) in move_set: continue
            move_set.add((i, j))

        for i, j in move_set:
            ret[i], ret[j] = ret[j], ret[i]
        now += 1
    return ret

print(*main(), sep="")