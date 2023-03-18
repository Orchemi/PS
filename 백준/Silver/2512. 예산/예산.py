def main():
    N = int(input())
    arr = list(map(int, input().split()))
    S = sum(arr)
    M = int(input())
    D = {}
    for a in arr:
        D[a] = D.get(a, 0)+1
    ks = sorted(D.keys(), reverse=True)
    kl = len(ks)
    if S <= M: return ks[0]
    if M <= ks[-1]*N: return M//N

    i = 0
    while i < kl:
        gap = ks[i]-ks[i+1]
        if gap*D[ks[i]] <= S-M:
            S -= gap*D[ks[i]]
            D[ks[i+1]] += D[ks[i]]
            D[ks[i]] = 0
        else:
            cnt = D[ks[i]]
            minus = (S-M)//cnt
            return ks[i] - (minus+1 if (S-M)%cnt else minus)
        i += 1

print(main())