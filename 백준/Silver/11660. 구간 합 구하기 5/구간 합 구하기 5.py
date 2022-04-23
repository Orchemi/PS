import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

def S(i, j):
    if not memo[i][j]:
        memo[i][j] = mat[i][j]
        if not i:
            memo[i][j] += S(i, j-1)
        elif not j:
            memo[i][j] += S(i-1, j)
        else:
            memo[i][j] += S(i-1, j) + S(i, j-1) - S(i-1, j-1)

    return memo[i][j]

N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
memo = [[0]*N for _ in range(N)]
memo[0][0] = mat[0][0]

for _ in range(M):
    i1, j1, i2, j2 = map(lambda x: (int(x)-1), input().split())
    S1 = S(i2, j2)
    S2 = S(i1-1, j2) if i1 else 0
    S3 = S(i2, j1-1) if j1 else 0
    S4 = S(i1-1, j1-1) if (i1 and j1) else 0
    print(S1 - S2 - S3 + S4)