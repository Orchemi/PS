import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N, K = map(int, input().split())
nums = list(map(int, input().split()))
Q = []

for n in nums:
    heappush(Q, n)

for _ in range(K):
    a = heappop(Q)

print(a)