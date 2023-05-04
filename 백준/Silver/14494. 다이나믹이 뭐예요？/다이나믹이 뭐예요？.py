I, J = map(int, input().split())
M = 1e9+7
dp = [[0]*(J+1) for _ in range(I+1)]

for i in range(I+1): dp[i][1] = 1
for j in range(J+1): dp[1][j] = 1

for i in range(2, I+1):
    for j in range(2, J+1):
        dp[i][j] = (dp[i-1][j-1]+dp[i-1][j]+dp[i][j-1])%M
print(int(dp[I][J]))