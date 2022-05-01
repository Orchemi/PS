import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input())
arr = list(map(int, input().split()))
ret = [0]*N
i = N-1
Q = []
while i >= 0:
    nowh = arr[i]
    heappush(Q, (arr[i], i))
    minh, mini = heappop(Q)
    while nowh > minh:
        ret[mini] = i+1
        minh, mini = heappop(Q)
    heappush(Q, (minh, mini))
    i -= 1

print(*ret)