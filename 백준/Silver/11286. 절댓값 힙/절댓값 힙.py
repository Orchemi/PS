import sys
input = sys.stdin.readline
from heapq import heappop, heappush

Q = []
N = int(input())
for _ in range(N):
    n = int(input())
    if not n:
        if not Q:
            print(0)
        else:
            n, op = heappop(Q)
            print(n*op)
    else:
        if n < 0:
            heappush(Q, (-n, -1))
        else:
            heappush(Q, (n, 1))