import sys
input = sys.stdin.readline
from collections import deque

def pathcheck(s, e):
    visit = [0]*(V+1)
    Q = deque()
    Q.append((s, [s]))

    while Q:
        u, path = Q.popleft()
        if u == e: return path
        if visit[u]: continue
        visit[u] = 1

        for v in G[u]:
            if visit[v]: continue
            Q.append((v, path+[v]))
            

V, Q = map(int, input().split())
doors = ['0'] + list(input().split())
G = [[] for _ in range(V+1)]
for _ in range(V-1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

for _ in range(Q):
    s, e = map(int, input().split())
    path = pathcheck(s, e)
    txt = ''
    for p in path:
        txt += doors[p]
        txt = str(int(txt) % 1000000007)
    print(txt)