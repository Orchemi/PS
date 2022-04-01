import sys
input = sys.stdin.readline

def dfs(i, u):
    global visited
    if i==V:
        return 1

    for v in rel[u]:
        if visited[v]: continue
        visited[v] = 1
        stack.append(v)
        if dfs(i+1, v):
            return 1
    return 0

def bfs():
    Q = []
    Q.append(S)
    f, r = -1, 0
    visited = [0]*(V+1)
    visited[S] = 1

    while f < r:
        f += 1
        u = Q[f]
        for v in rel[u]:
            if visited[v]: continue
            visited[v] = 1
            Q.append(v)
            r += 1
    return Q


V, E, S = map(int, input().split())
rel = [[] for _ in range(V+1)]
for _ in range(E):
    u, v = map(int, input().split())
    rel[u].append(v)
    rel[v].append(u)
rel = [sorted(i) for i in rel]

stack = [S]
visited = [0]*(V+1)
visited[S] = 1
dfs(0, S)
print(*stack)
print(*bfs())