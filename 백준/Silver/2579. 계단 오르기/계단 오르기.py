N = int(input())
arr = [int(input()) for _ in range(N)]
dp = [[0]*(N+1) for _ in range(2)]
dp[0][1] = arr[0]
for j in range(2, N+1):
    dp[0][j] = max(dp[0][j-2], dp[1][j-2]) + arr[j-1]
    dp[1][j] = dp[0][j-1] + arr[j-1]

print(max(dp[0][N], dp[1][N]))