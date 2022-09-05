N = int(input())
mat = [[0]*(N+5) for _ in range(2)]
mat[0][1] = 1
mat[1][4] = 1

for j in range(2, N+1):
    k = 3 if j % 2 else 4
    mat[1][j + k] += mat[0][j-1]
    mat[0][j] = mat[0][j-1]*2 - mat[1][j]

print(mat[0][N])