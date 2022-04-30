import sys
input = sys.stdin.readline

N, M = map(int, input().split())
D = [0]+[int(input()) for _ in range(N)]
T = [0]+[int(input()) for _ in range(M)]
memo = [[0]*(N+1) for _ in range(M+1)]
for k in range(1, N+1):
    memo[k][k] = memo[k-1][k-1] + T[k]*D[k]

for j in range(1, N+1):
    for i in range(j+1, M+1):
        memo[i][j] = min(memo[i-1][j-1]+D[j]*T[i], memo[i-1][j])

print(memo[M][N])