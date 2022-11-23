import sys
input = sys.stdin.readline
from heapq import heappop, heappush
from math import gcd

def find_s(x, y):
    g = gcd(x, y)
    if not x: return (0, 0, 1) if y > 0 else (0, 0, 5)
    if not y: return (0, 0, 3) if x > 0 else (0, 0, 7)

    if x > 0: d = 2 if y > 0 else 4
    else: d = 8 if y > 0 else 6
    return (x/g, y/g, d)


N, M = map(int, input().split())
D = {}
for _ in range(N):
    x, y, d = map(int, input().split())
    s = find_s(x, y)
    if not D.get(s, ''):
        D[s] = [0, []]
    heappush(D[s][1], d)

for _ in range(M):
    x, y, d = map(int, input().split())
    s = find_s(x, y)
    if not D.get(s, ''):
        print(N)
        continue
    D[s][0] += d
    while D[s][1]:
        if D[s][1][0] > D[s][0]: break
        heappop(D[s][1])
        N -= 1

    print(N)