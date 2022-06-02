import sys
input = sys.stdin.readline

V, E = map(int, input().split())
hs = [0] + list(map(int, input().split()))
hs2 = []
for i, h in enumerate(hs):
    hs2.append([h, i])
hs2.sort(reverse=True)


cnts = [0]*(V+1)
G = [set() for _ in range(V+1)]
for _ in range(E):
    u, v = map(int, input().split())
    if hs[u] > hs[v]:
        u, v = v, u
    G[u].add(v)


for i in range(V):
    s = hs2[i][1]
    max_cnt = 0
    for k in G[s]:
        max_cnt = max(max_cnt, cnts[k])
    cnts[s] = max_cnt + 1

for i in range(1, V+1):
    print(cnts[i])