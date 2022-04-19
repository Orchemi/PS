import sys
input = sys.stdin.readline
from heapq import heappop, heappush
from math import inf

def dijk(S, E):
    global G

    visit = [0]*(V+1)
    D = [inf]*(V+1)
    D[S] = 0
    Q = [(D[S], S)]
    while Q:
        val, u = heappop(Q)
        if visit[u]: continue
        visit[u] = 1

        for v, w in G[u]:
            if not visit[v] and D[v] > D[u] + w:
                D[v] = D[u] + w
                heappush(Q, (D[v], v))
    return -1 if D[E] == inf else D[E]


def main(S, A, B, T):
    R1 = dijk(S, A)
    if R1==-1: return -1
    R2 = dijk(A, B)
    if R2==-1: return -1
    R3 = dijk(B, T)
    if R3==-1: return -1
    return R1+R2+R3


V, E = map(int, input().split())
G = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))

C1, C2 = map(int, input().split())
ret1 = main(1, C1, C2, V)
ret2 = main(1, C2, C1, V)
ret3 = {ret1, ret2} - {-1}
print(min(ret3) if ret3 else -1)