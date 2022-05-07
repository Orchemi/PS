import sys
input = sys.stdin.readline

def find_x(x):
    if x!= p[x]:
        x = find_x(p[x])
    return x

V, E = map(int, input().split())
G = [''] + list(input().split())
p = [i for i in range(V+1)]
Q = []
for _ in range(E):
    u, v, w = map(int, input().split())
    Q.append((w, u, v))

Q.sort(reverse=True)
cnt = 0
ssum = 0
while cnt < V-1 and Q:
    w, u, v = Q.pop()
    if G[u] == G[v]: continue

    a, b = find_x(u), find_x(v)
    if a == b: continue

    p[a] = b
    cnt += 1
    ssum += w

ret = ssum if cnt == V-1 else -1
print(ret)