import sys
input = sys.stdin.readline
from heapq import heappop, heappush
from math import inf

n = int(input())
m = int(input())
visit = [0]*(n+1)
G = [[] for _ in range(n+1)]
D = [[inf, []] for _ in range(n+1)]

while m > 0:
    s, e, w = map(int, input().split())
    m -= 1
    G[s].append((e, w))

S, E = map(int, input().split())
D[S][0] = 0
D[S][1] = [S]

Q = [(D[S][0], S)]
while Q:
    val, u = heappop(Q)
    if visit[u]: continue
    visit[u] = 1

    for v, w in G[u]:
        if not visit[v] and D[v][0] > D[u][0]+w:
            D[v][0] = D[u][0]+w
            D[v][1] = D[u][1]+[v]
            heappush(Q, (D[v][0], v))

print(D[E][0])
print(len(D[E][1]))
print(*D[E][1])