def pado(n):
    if not memo[n]:
        memo[n] = pado(n-2) + pado(n-3)
    return memo[n]


memo = [0]*101
for i in range(1, 4):
    memo[i] = 1

T = int(input())
for _ in range(T):
    N = int(input())
    print(pado(N))