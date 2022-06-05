import sys
input = sys.stdin.readline

N = int(input())
Ls = list(map(int, input().split()))
Rs = list(map(int, input().split()))
dp = [[0]*(N+1) for _ in range(N+1)]

for l in range(N-1, -1, -1):
    for r in range(N-1, -1, -1):
        if Rs[r] < Ls[l]:
            dp[l][r] = max(dp[l+1][r+1], dp[l+1][r], dp[l][r+1]+Rs[r])
        else:
            dp[l][r] = max(dp[l+1][r+1], dp[l+1][r])

print(dp[0][0])