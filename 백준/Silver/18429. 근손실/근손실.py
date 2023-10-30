def dfs(i, ssum, S):
    if ssum < i*K: return 0
    if not S: return 1
    ret = 0
    for ii in range(N-i):
        ret += dfs(i+1, ssum+S[ii], S[:ii]+S[ii+1:])
    return ret

N, K = map(int, input().split())
S = list(map(int, input().split()))
print(dfs(0, 0, S))