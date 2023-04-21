import sys
input = sys.stdin.readline
from heapq import heappop, heappush

def dijk(S):
    global D
    Q = [(D[S], S)]
    visit = [0]*(V+1)

    while Q:
        d, u = heappop(Q)
        if visit[u]: continue
        visit[u] = 1

        for v, w in G[u]:
            if not visit[v] and D[v] > D[u]+w:
                D[v] = D[u]+w
                heappush(Q, [D[v], v])


V, E = map(int, input().split())
S = int(input())-1
G = [[] for _ in range(V)]
D =  [0xffffff]*V
D[S] = 0
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u-1].append((v-1, w))

dijk(S)
for val in D:
    print('INF' if val == 0xffffff else val)