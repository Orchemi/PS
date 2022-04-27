import sys
input = sys.stdin.readline
from collections import deque

def bfs(i):
    global v
    Q = deque()
    Q.append(i)

    minMuch = much[i]
    while Q:
        u = Q.popleft()
        minMuch = min(minMuch, much[u])
        if v[u]: continue
        v[u] = 1

        for e in G[u]:
            Q.append(e)

    return minMuch

N, M, k = map(int, input().split())
much = [0]
much += list(map(int, input().split()))
G = [[] for _ in range(N+1)]
v = [0]*(N+1)
for _ in range(M):
    s, e = map(int, input().split())
    G[s].append(e)
    G[e].append(s)

minSsum = 0
for i in range(1, N+1):
    if not v[i]:
        minSsum += bfs(i)

ans = minSsum if minSsum <= k else 'Oh no'
print(ans)