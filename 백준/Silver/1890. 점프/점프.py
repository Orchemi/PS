N = int(input())
steps = [list(map(int, input().split())) for _ in range(N)]
cnts = [[0]*N for _ in range(N)]
cnts[0][0] = 1

for i in range(N):
    for j in range(N):
        cnt = cnts[i][j]
        if not cnt: continue
        step = steps[i][j]
        if i+step < N: cnts[i+step][j] += cnt
        if j+step < N: cnts[i][j+step] += cnt

print(cnts[N-1][N-1] // 3)