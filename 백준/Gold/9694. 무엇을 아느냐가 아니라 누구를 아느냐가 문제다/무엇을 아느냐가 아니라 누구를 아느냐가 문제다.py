import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    G = [[] for _ in range(M+1)]
    for _ in range(N):
        u, v, w = map(int, input().split())
        G[u].append((v, w))
        G[v].append((u, w))

    check = [[1e5, []] for _ in range(M+1)]
    check[0] = [0, [0]]
    Q = deque()
    Q.append((0, 0))
    while Q:
        u, cost = Q.popleft()
        for v, w in G[u]:
            if not (cost + w < check[v][0]): continue
            check[v] = [cost + w, check[u][1]+[v]]
            Q.append((v, cost+w))

    ret = [-1] if check[M-1][0] == 1e5 else check[M-1][1]
    print(f'Case #{t+1}:', end=' ')
    print(*ret)