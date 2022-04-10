import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input())
M = int(input())
D = [0xfffffff]*N
visit = [0]*N
G = [[] for _ in range(N)]
for _ in range(M):
    s, e, w = map(int, input().split())
    s, e = s-1, e-1
    G[s].append((e, w))

S, E = map(int, input().split())
S, E = S-1, E-1
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

print(D[E])