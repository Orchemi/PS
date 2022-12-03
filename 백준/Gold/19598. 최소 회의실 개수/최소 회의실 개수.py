import sys
input = sys.stdin.readline
from heapq import heappop, heappush

def main():
    def make_H():
        H = []
        for _ in range(N):
            s, e = map(int, input().split())
            heappush(H, (s, e))
        return H

    def count_place():
        cnt = 1
        K = []
        s, e = heappop(H)
        heappush(K, e)
        while H:
            s, e = heappop(H)
            if K[0] > s:
                cnt += 1
            else:
                heappop(K)
            heappush(K, e)

        return cnt

    N = int(input())
    H = make_H()
    return count_place()

print(main())