import sys
input = sys.stdin.readline

N = int(input())
it, nt, tt = 0, 0, 0
for _ in range(N):
    ml, md = map(int, input().split())
    nt += md
    if nt > tt:
        it += nt-tt
        tt = nt
    tt += ml

print(it)