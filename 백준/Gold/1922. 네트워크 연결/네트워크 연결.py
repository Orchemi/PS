import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
from heapq import heappop, heappush

def find(x):
    if not x == p[x]:
        p[x] = find(p[x])
    return p[x]

V = int(input())
E = int(input())
p = [i for i in range(V+1)]
H = []
for _ in range(E):
    u, v, w = map(int, input().split())
    heappush(H, (w, u, v))

cnt = 0
ssum = 0
while cnt < V-1 and H:
    w, u, v = heappop(H)
    a = find(u)
    b = find(v)
    if not a==b:
        p[a] = b
        cnt += 1
        ssum += w

print(ssum)