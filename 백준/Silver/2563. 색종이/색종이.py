N = int(input())
mat = [[0]*101 for _ in range(101)]
for _ in range(N):
    x, y = map(int, input().split())
    for xx in range(x, x+10):
        for yy in range(y, y+10):
            mat[xx][yy] = 1

cnt = 0
for i in range(101):
    for j in range(101):
        if mat[i][j]: cnt += 1

print(cnt)