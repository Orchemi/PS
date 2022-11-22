import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input())
H = []
for _ in range(N):
    d, t = map(int, input().split())
    heappush(H, (-t, -d))

k = heappop(H)
t, d = -k[0], -k[1]
cur = t-d+1
while H:
    k = heappop(H)
    t, d = -k[0], -k[1]
    cur = min(cur-1, t)
    cur -= d-1

print(cur-1)