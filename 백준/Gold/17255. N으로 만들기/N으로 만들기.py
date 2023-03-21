def main():
    def dfs(S, l):
        if l == 1: return 1
        if D.get(S, 0): return D[S]

        left_S, right_S = S[1:], S[:-1]
        D[S] = dfs(left_S, l-1)
        if left_S == right_S: return D[S]
        D[S] += dfs(right_S, l-1)
        return D[S]

    S = input()
    l = len(S)
    if l==1: return 1
    D = {}
    dfs(S, l)
    return D[S]

print(main())