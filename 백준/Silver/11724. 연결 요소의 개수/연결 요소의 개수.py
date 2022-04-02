import sys
input = sys.stdin.readline
from collections import deque

def bfs(s):
    global visited
    Q = deque()
    Q.append(s)

    while Q:
        u = Q.popleft()
        for v in links[u]:
            if visited[v]: continue
            visited[v] = 1
            Q.append(v)


V, E = map(int, input().split())
links = [[] for _ in range(V)]
for _ in range(E):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    links[u].append(v)
    links[v].append(u)

visited = [0]*V
cnt = 0
for i in range(V):
    if not visited[i]:
        cnt += 1
        bfs(i)
print(cnt)