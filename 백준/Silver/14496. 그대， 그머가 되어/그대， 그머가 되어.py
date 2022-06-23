import sys
input = sys.stdin.readline
from collections import deque

def main():
    a, b = map(int, input().split())
    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e = map(int, input().split())
        G[s].append(e)
        G[e].append(s)

    Q = deque([[a, 0]])
    visit = [0]*(N+1)
    ret = 1e9
    while Q:
        u, d = Q.popleft()
        if u == b:
            ret = min(ret, d)
        for v in G[u]:
            if visit[v]: continue
            visit[v] = 1
            Q.append([v, d+1])

    return -1 if ret == 1e9 else ret

print(main())