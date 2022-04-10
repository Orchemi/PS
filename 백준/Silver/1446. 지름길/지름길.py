from heapq import heappop, heappush

def dijk(s):
    global D
    visit = [0]*(L+1)
    D[s] = 0
    Q = [[0, s]]

    while Q:
        d, u = heappop(Q)
        if visit[u]: continue
        visit[u] = 1

        for v, w in G[u]:
            if not visit[v] and D[v] > D[u]+w:
                D[v] = D[u]+w
                heappush(Q, [D[v], v])


N, L = map(int, input().split())
D = [L+1]*(L+1)
G = [[] for _ in range(L+1)]
for _ in range(N):
    s, e, w = map(int, input().split())
    if e > L: continue
    G[s].append([e, w])

for i in range(L):
    G[i].append([i+1, 1])

dijk(0)
print(D[L])