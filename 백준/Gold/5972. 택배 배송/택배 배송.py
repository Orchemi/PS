import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
rels = [[] for _ in range(N+1)]
minns = [1e8]*(N+1)
minns[1] = 0
Q = deque([1])
for _ in range(M):
    u, v, k = map(int, input().split())
    rels[u].append((v, k))
    rels[v].append((u, k))

while Q:
    u = Q.popleft()
    for v, k in rels[u]:
        if minns[u]+k < minns[v]:
            minns[v] = minns[u]+k
            Q.append(v)

print(minns[N])