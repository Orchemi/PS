I, J = map(int, input().split())
mat = [list(map(int, input())) for _ in range(I)]

# 가로 연속 1
h_mat = [[0]*J for _ in range(I)]
for i in range(I):
    h_mat[i][0] = mat[i][0]
for i in range(I):
    for j in range(1, J):
        if not mat[i][j]: continue
        h_mat[i][j] = h_mat[i][j-1]+1

# 세로 연속 1
v_mat = [[0]*J for _ in range(I)]
for j in range(J):
    v_mat[0][j] = mat[0][j]
for i in range(1, I):
    for j in range(J):
        if not mat[i][j]: continue
        v_mat[i][j] = v_mat[i-1][j]+1

dp = [[0]*(J+1) for _ in range(I+1)]
for i in range(1, I+1):
    for j in range(1, J+1):
        if not mat[i-1][j-1]: continue
        l = dp[i-1][j-1]
        if not l:
            dp[i][j] = 1
            continue

        if v_mat[i-1][j-1] > l and h_mat[i-1][j-1] > l:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = min(v_mat[i-1][j-1], h_mat[i-1][j-1], l+1)

maxx = 0
for i in range(I+1):
    for j in range(J+1):
        if maxx < dp[i][j]:
            maxx = dp[i][j]
print(maxx**2)