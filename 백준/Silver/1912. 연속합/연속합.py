N = int(input())
dp = list(map(int, input().split()))
i = 1
maxV = dp[0]
while i < N:
    dp[i] = max(dp[i-1]+dp[i], dp[i])
    maxV = max(maxV, dp[i])
    i += 1

print(maxV)