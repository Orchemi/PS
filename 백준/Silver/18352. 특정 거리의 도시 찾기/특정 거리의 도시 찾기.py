import sys
input = sys.stdin.readline
from collections import deque

V, M, K, X = map(int, input().split())
G = [[] for _ in range(V+1)]
ok = [1]*(V+1)


for _ in range(M):
    s, e = map(int, input().split())
    G[s].append(e)

Q = deque()
Q.append(X)
ok[X] = 0
i = 0
while i < K and Q:
    for _ in range(len(Q)):
        u = Q.popleft()

        for v in G[u]:
            if not ok[v]: continue
            ok[v] = 0
            Q.append(v)
    i += 1

if not Q:
    print(-1)
    quit()

Q2 = sorted(Q)
for i in range(len(Q2)):
    print(Q2[i])