import sys
input = sys.stdin.readline
from heapq import heappop, heappush

Q = []
N = int(input())
for _ in range(N):
    heappush(Q, -int(input()))

while Q:
    print(-heappop(Q))