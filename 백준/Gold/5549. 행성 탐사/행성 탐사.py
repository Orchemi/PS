import sys
input = sys.stdin.readline

D = {'J':0, 'O':1, 'I':2}
I, J = map(int, input().split())
K = int(input())
mat = [list(input()) for _ in range(I)]
dp = [[[0]*3 for _ in range(J+1)] for _ in range(I+1)]

for i in range(1, I+1):
    for j in range(1, J+1):
        v = mat[i-1][j-1]
        dp[i][j][D[v]] += 1
        for v1, v2, v3 in (dp[i-1][j], dp[i][j-1], [-k for k in dp[i-1][j-1]]):
            dp[i][j][0] += v1
            dp[i][j][1] += v2
            dp[i][j][2] += v3

for _ in range(K):
    i1, j1, i2, j2 = map(int, input().split())
    ans = [0]*3
    for v1, v2, v3 in (dp[i2][j2], dp[i1-1][j1-1]):
        ans[0] += v1
        ans[1] += v2
        ans[2] += v3
    for v1, v2, v3 in (dp[i1-1][j2], dp[i2][j1-1]):
        ans[0] -= v1
        ans[1] -= v2
        ans[2] -= v3

    print(*ans)