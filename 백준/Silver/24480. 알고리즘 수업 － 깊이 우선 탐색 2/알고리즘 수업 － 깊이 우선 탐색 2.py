import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)

N, M, R = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

for point in G:
    point.sort(reverse=True)

check = [0]*(N+1)
check[R] = 1
cnt = 1
def dfs(u):
    global check, cnt
    for v in G[u]:
        if check[v]: continue
        cnt += 1
        check[v] = cnt
        dfs(v)
dfs(R)
for i in range(1, N+1):
    print(check[i])