import sys
from math import ceil
input = sys.stdin.readline

N, L = map(int, input().split())
AA = 1000000000
trees = list(map(int, input().split()))
TD = {}
for t in trees:
    TD[t] = TD.get(t, 0) + 1

TL = sorted(list(TD.keys()))
TLL = len(TL)

i = 0
for i in range(-1, -TLL, -1):
    if L >= (TL[i]-TL[i-1])*TD[TL[i]]:
        L -= (TL[i]-TL[i-1])*TD[TL[i]]
        TD[TL[i-1]] = TD[TL[i-1]] + TD[TL[i]]
        TD.pop(TL[i])
        i -= 1
    else:
        break

print(TL[i] - ceil(L/TD[TL[i]]))