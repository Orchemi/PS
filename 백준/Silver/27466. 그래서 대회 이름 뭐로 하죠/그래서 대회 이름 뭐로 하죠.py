def main():
    def find_as():
        ret = []
        for i in range(N):
            if S[i] == 'A': ret.append(i+1)
        return ret

    N, M = map(int, input().split())
    S = list(input())
    mu = set('AEIOU')
    while S and S[-1] in mu:
        S.pop()
        N -= 1
    if N < M: return 'NO'

    as_idxs = find_as()
    if len(as_idxs) < 2: return 'NO'

    a1, a2 = as_idxs[-2], as_idxs[-1]
    gap1, gap2 = a2-a1-1, N-a2-1

    if N - (gap1+gap2) < M: return 'NO'

    head, tail = '', S.pop()
    for _ in range(2):
        while S[-1] != 'A':
            S.pop()
        tail = S.pop() + tail

    print('YES')
    return ''.join(S[M-len(tail)-1:])+tail

print(main())