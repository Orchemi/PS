import sys
input = sys.stdin.readline

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
dictC = {0:(1,2), 1:(0,2), 2:(0,1)}

i = 1
while i<N:
    for j in range(3):
        c1, c2 = dictC[j]
        v = min(mat[i-1][c1], mat[i-1][c2])
        mat[i][j] = mat[i][j] + v
    i += 1

print(min(mat[N-1]))