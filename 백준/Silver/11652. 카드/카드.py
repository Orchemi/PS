import sys
input = sys.stdin.readline

N = int(input())
D = {}
for _ in range(N):
    n = int(input())
    D[n] = D.get(n, 0) + 1

ret, maxx = '', 0
for k in D.keys():
    if maxx > D[k]: continue
    elif maxx < D[k]:
        maxx = D[k]
        ret = k
    elif ret > k:
        ret = k

print(ret)