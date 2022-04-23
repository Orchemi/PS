import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
S = [[0]*N for _ in range(N)]
S[0][0] = mat[0][0]

# S 채우기
# 첫 줄 채우기
j = 1
while j < N:
    S[0][j] = S[0][j-1] + mat[0][j]
    j += 1

i = 1
while i < N:
    S[i][0] = S[i-1][0] + mat[i][0]
    i += 1

# 전체 채우기
i = 1
while i < N:
    j = 1
    jsum = mat[i][0]
    while j < N:
        jsum += mat[i][j]
        S[i][j] = S[i-1][j] + jsum
        j += 1
    i += 1

for _ in range(M):
    i1, j1, i2, j2 = map(lambda x: (int(x)-1), input().split())
    S1 = S[i2][j2]
    S2 = S[i1-1][j2] if i1 else 0
    S3 = S[i2][j1-1] if j1 else 0
    S4 = S[i1-1][j1-1] if (i1 and j1) else 0
    print(S1 - S2 - S3 + S4)