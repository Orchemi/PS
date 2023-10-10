def main():
    def find_keys_count():
        A = list(map(int, input().split()))
        S = set(A)
        D = {}
        for k in S:
            D[k] = 0

        for a in A:
            D[a] += 1

        return S, D


    N = int(input())
    S1, D1 = find_keys_count()
    S2, D2 = find_keys_count()

    ret = 0
    for s in S1|S2:
        ret += abs(D1.get(s, 0) - D2.get(s, 0))
    return ret // 2

print(main())