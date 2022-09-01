A, B = input(), input()
al, bl = len(A), len(B)

mat = [[0]*(bl+1) for _ in range(al+1)]
for i in range(1, al+1):
    a = A[i-1]
    for j in range(1, bl+1):
        b = B[j-1]
        mat[i][j] = max(mat[i][j-1], mat[i-1][j])
        if a == b:
            mat[i][j] = max(mat[i-1][j-1]+1, mat[i][j])

print(mat[al][bl])