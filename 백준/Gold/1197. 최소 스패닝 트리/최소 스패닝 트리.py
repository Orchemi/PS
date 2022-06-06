import sys
input = sys.stdin.readline
from heapq import heappop, heappush


def find_set(x):
    global p
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]


def union(u, v, w):
    global cnt, ret, p
    a, b = find_set(u), find_set(v)
    if a != b:
        p[a] = b
        ret += w
        cnt += 1


V, E = map(int, input().split())
Q = []
for _ in range(E):
    u, v, w = map(int, input().split())
    heappush(Q, (w, u, v))

p = [i for i in range(V+1)]
ret = 0
cnt = 0
while cnt < V-1:
    w, u, v = heappop(Q)
    union(u, v, w)

print(ret)