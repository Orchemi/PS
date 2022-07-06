import sys
input = sys.stdin.readline
from heapq import heappop, heappush

n, m = map(int, input().split())
h = []
for a in list(map(int, input().split())):
    heappush(h, a)

for _ in range(m):
    a = heappop(h)
    b = heappop(h)
    heappush(h, a+b)
    heappush(h, a+b)

print(sum(h))