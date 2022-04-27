import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dp = [[0]*(N+1) for _ in range(M+1)]

for i in range(1, M+1):
    days, pages = map(int, input().split())
    for j in range(1, N+1):
        if j >= days:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-days] + pages)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[M][N])