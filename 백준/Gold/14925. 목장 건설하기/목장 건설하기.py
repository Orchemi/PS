import sys
input = sys.stdin.readline

I, J = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(I)]
mat_h = [[0]*(J+1) for _ in range(I+1)]
mat_v = [[0]*(J+1) for _ in range(I+1)]

for i in range(1, I+1):
    for j in range(1, J+1):
        if mat[i-1][j-1]: continue
        mat_h[i][j] = mat_h[i][j-1] + 1

for j in range(1, J+1):
    for i in range(1, I+1):
        if mat[i-1][j-1]: continue
        mat_v[i][j] = mat_v[i-1][j] + 1

dp = [[0]*(J+1) for _ in range(I+1)]
for i in range(1, I+1):
    for j in range(1, J+1):
        if mat[i-1][j-1]: continue
        dp[i][j] = min(mat_v[i][j], mat_h[i][j], dp[i-1][j-1]+1)

maxx = 0
for i in range(1, I+1):
    for j in range(1, J+1):
        if maxx < dp[i][j]:
            maxx = dp[i][j]
print(maxx)