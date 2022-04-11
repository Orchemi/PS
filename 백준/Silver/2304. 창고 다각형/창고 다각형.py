import sys
input = sys.stdin.readline

N = int(input())
hs = [0]*1010
maxh = 0
for _ in range(N):
    i, h = map(int, input().split())
    maxh = max(maxh, h)
    hs[i] = h

sumL = sumC = sumR = 0

li = 0
lh = 0
while not hs[li]==maxh:
    lh = max(lh, hs[li])
    sumL += lh
    li += 1


ri = 1009
rh = 0
while not hs[ri-1]==maxh:
    rh = max(rh, hs[ri-1])
    sumR += rh
    ri -= 1

sumC = (ri-li)*maxh
print(sumL + sumR + sumC)