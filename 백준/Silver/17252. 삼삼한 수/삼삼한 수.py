def dfs(i, ssum):
    global N
    if ssum+(3**i) > N: return 0
    if ssum+(3**i) == N: return 1
    if dfs(i+1, ssum+3**i): return 1
    if dfs(i+1, ssum): return 1

N = int(input())
print('YES' if dfs(0, 0) else 'NO')