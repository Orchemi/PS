import sys
input = sys.stdin.readline

I, J = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(I)]
dp = [[0]*(J+1) for _ in range(I+1)]
for i in range(1, I+1):
    for j in range(1, J+1):
        dp[i][j] = mat[i-1][j-1] + max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

print(dp[I][J])