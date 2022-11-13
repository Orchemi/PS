import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

maxH = []
minH = []
for a in arr:
    heappush(maxH, -a)
    heappush(minH, a)

diff = float('inf')
mx, mn = -heappop(maxH), heappop(minH)
while mx > mn:
    if diff > abs(mn+mx):
        diff = abs(mn+mx)
        rmn, rmx = mn, mx
    if not diff: break
    if mx+mn < 0:
        mn = heappop(minH)
    else :
        mx = -heappop(maxH)

print(rmn, rmx)