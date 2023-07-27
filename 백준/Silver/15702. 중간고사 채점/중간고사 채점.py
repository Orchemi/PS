def main():
    N, M = map(int, input().split())
    scores = list(map(int, input().split()))
    D = {}
    for _ in range(M):
        t, *rets = input().split()
        ts_score = 0
        for i in range(N):
            if rets[i] == 'X': continue
            ts_score += scores[i]
        D[int(t)] = ts_score

    max_score = 0
    min_num = 1e5
    for k, v in D.items():
        if v > max_score:
            min_num = k
            max_score = v
        elif v == max_score:
            min_num = min(min_num, k)

    return min_num, max_score

print(*main())