import sys
input = sys.stdin.readline
from heapq import heappop, heappush

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    H = []
    for a in arr:
        heappush(H, a)

    ret = 1
    while N > 1:
        a, b = heappop(H), heappop(H)
        ret = (ret*a*b) % 1000000007
        heappush(H, a*b)
        N -= 1
    print(ret)