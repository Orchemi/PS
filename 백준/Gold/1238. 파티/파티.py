import sys
input = sys.stdin.readline
from heapq import heappop, heappush

def dijk(S, T):
    visit = [0]*N
    D = [0xffffff]*N
    D[S] = 0
    Q = [(D[S], S)]

    while Q:
        val, u = heappop(Q)
        if visit[u]: continue
        visit[u] = 1

        for v, w in G[u]:
            if not visit[v] and D[v] > D[u]+w:
                D[v] = D[u]+w
                heappush(Q, (D[v], v))
    return D[T]

N, M, X = map(int, input().split())
X = X-1
G = [[] for _ in range(N)]
for _ in range(M):
    s, e, w = map(int, input().split())
    G[s-1].append((e-1, w))
    
maxDis = 0
for S in range(N):
    maxDis = max(maxDis, dijk(S, X) + dijk(X, S))
print(maxDis)