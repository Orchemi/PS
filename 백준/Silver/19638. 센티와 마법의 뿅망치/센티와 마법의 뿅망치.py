import sys
input = sys.stdin.readline
from heapq import heappop, heappush

def main():
    N, C, T = map(int, input().split())
    H = []
    for _ in range(N):
        heappush(H, -int(input()))

    cnt = 0
    while True:
        tallest = -heappop(H)
        if tallest == 1:
            return ('YES', cnt) if C>1 else ('NO', 1)
        if tallest < C: return 'YES', cnt

        if cnt == T: return 'NO', tallest
        heappush(H, -(tallest//2))
        cnt += 1

print(*main(), sep='\n')