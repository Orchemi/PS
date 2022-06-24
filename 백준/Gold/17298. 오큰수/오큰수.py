import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input())
arr = list(map(int, input().split()))

Q = []
ret = [-1]*N
for i in range(N):
    heappush(Q, [arr[i], i])
    while Q:
        val, idx = heappop(Q)
        if arr[i] > val:
            ret[idx] = arr[i]
        else:
            heappush(Q, [val, idx])
            break

print(*ret)