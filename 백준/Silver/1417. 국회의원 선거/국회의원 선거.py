from heapq import heappop, heappush

def main():
    N = int(input())
    if N==1: return 0
    a = int(input())
    os = []
    for _ in range(N-1):
        heappush(os, -int(input()))

    cnt = 0
    while True:
        k = -heappop(os)
        if a > k: return cnt
        cnt += 1
        a += 1
        heappush(os, 1-k)

print(main())