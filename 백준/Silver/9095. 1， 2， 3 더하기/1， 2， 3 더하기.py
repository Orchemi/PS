def dp(n):
    if not memo[n]:
        a = dp(n-1) + dp(n-2) + dp(n-3)
        memo[n] = a
    return memo[n]

memo = [0]*12
memo[:2] = 1, 1, 2

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp(n))