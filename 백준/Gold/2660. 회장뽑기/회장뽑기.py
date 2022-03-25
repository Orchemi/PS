from collections import deque

def BFS(i):
    Q = deque()
    Q.append(i)
    visited = [0]*(V+1)
    visited[i] = 1
    dis = -1

    while Q and (dis <= minV):
        for _ in range(len(Q)):
            s = Q.popleft()
            visited[s] = 1
            for v in rel[s]:
                if visited[v]: continue
                visited[v] = 1
                Q.append(v)
        dis += 1
    return dis


V = int(input())
rel = [[] for _ in range(V+1)]

while True:
    u, v = map(int, input().split())
    if u==v==-1: break
    rel[u].append(v)
    rel[v].append(u)


minV = 50
candis = []

for i in range(1, V+1):
    ret = BFS(i)
    if minV > ret:
        candis = [i]
        minV = ret

    elif minV==ret:
        candis.append(i)

print(minV, len(candis))
print(*sorted(candis))