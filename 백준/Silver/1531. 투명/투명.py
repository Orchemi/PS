import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mat = [[0]*101 for _ in range(101)]
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2+1):
        for j in range(x1, x2+1):
            mat[i][j] += 1

ret = 0
for i in range(1, 101):
    for j in range(1, 101):
        if mat[i][j] > M:
            ret += 1

print(ret)