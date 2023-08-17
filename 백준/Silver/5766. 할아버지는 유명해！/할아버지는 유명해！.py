def main():
    D = {}
    for _ in range(N):
        arr = list(map(int, input().split()))
        for a in arr:
            D[a] = D.get(a, 0) + 1

    maxxs = [0, 0]
    players = [[], []]
    for k, v in D.items():
        if v < maxxs[1]: continue
        elif v > maxxs[0]:
            maxxs = [v, maxxs[0]]
            players = [[k], players[0]]
        elif v == maxxs[0]:
            players[0].append(k)
        elif v > maxxs[1]:
            maxxs[1] = v
            players[1] = [k]
        elif v == maxxs[1]:
            players[1].append(k)

    return sorted(players[1])


while True:
    N, M = map(int, input().split())
    if N == M == 0: break
    print(*main())