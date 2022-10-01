import sys
input = sys.stdin.readline

def calc_time(n):
    global time, dp, first
    if dp[n]: return dp[n]

    if not first[n]:
        dp[n] = time[n]
        return dp[n]

    maxx = 0
    while first[n]:
        nn = first[n].pop()
        ret = calc_time(nn)
        if maxx < ret:
            maxx = ret

    dp[n] = time[n] + maxx
    return dp[n]


N = int(input())
dp = [0]*(N+1)
time = [0]*(N+1)
first = [set() for _ in range(N+1)]
for i in range(1, N+1):
    t, n, *arr = map(int, input().split())
    time[i] = t
    first[i] = set(arr)

for i in range(1, N+1):
    dp[i] = calc_time(i)

print(max(dp))