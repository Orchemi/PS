import sys
input = sys.stdin.readline
from heapq import heappop, heappush

def check(s):
    visit = [0]*(V+1)
    Q = [(0, s)]
    nowFarm = 0

    while Q:
        dis, u = heappop(Q)
        if dis > M: continue
        if visit[u]: continue
        visit[u] = 1
        nowFarm += arr[u]

        for v, w in G[u]:
            heappush(Q, (dis+w, v))

    return nowFarm


V, M, E = map(int, input().split())
arr = [0] + list(map(int, input().split()))
G = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))

maxFarm = 0
for s in range(1, V+1):
    maxFarm = max(maxFarm, check(s))

print(maxFarm)