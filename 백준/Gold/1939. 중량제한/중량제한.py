import sys
input = sys.stdin.readline

V, E = map(int, input().split())
G = [[] for _ in range(V+1)]
D = [0]*(V+1)
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))

S, T = map(int, input().split())
Q = set()
D[S] = 0xffffffff
Q.add(S)

while Q:
    u = Q.pop()
    for v, w in G[u]:
        minV = min(D[u], w)
        if D[v] >= minV: continue
        D[v] = minV
        Q.add(v)

print(D[T])