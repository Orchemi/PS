def main():
    def find_count(l):
        ret = 1
        for i in range(3):
            ret *= Ls[i]//l
        return ret

    N, *Ls = map(int, input().split())
    prev_K, K = -1, min(Ls)
    if find_count(K) >= N: return K
    s, e = 0, min(Ls)

    while K != prev_K:
        m = (s+e)/2
        cnt = find_count(m)
        if cnt >= N: s = m
        else: e = m
        prev_K, K = K, m
    return K

print(main())