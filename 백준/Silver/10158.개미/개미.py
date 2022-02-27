import sys; input = sys.stdin.readline

I, J = map(int, input().split())
ni, nj = map(int, input().split())
di, dj = 1, 1
ai, aj = -1, -1
To = int(input())

# 세로
T = To % (2*I)
if T==0:
    ai = ni

if ai==-1:
    if T >= I-ni:
        T -= (I-ni)
        ni = I
    else:
        ai = ni + T

if ai==-1:
    if T >= I:
        T -= I
        ai = T
    else:
        ai = ni - T

# 가로
T = To % (2*J)
if T==0:
    aj = nj

if aj==-1:
    if T >= J-nj:
        T -= (J-nj)
        nj = J
    else:
        aj = nj + T

if aj==-1:
    if T >= J:
        T -= J
        aj = T
    else:
        aj = nj - T

print(ai, aj)