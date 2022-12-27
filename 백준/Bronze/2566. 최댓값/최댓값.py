mv, mi, mj = 0, 0, 0
mat = [list(map(int, input().split())) for _ in range(9)]
for i in range(9):
    for j in range(9):
        if mv < mat[i][j]:
            mv = mat[i][j]
            mi, mj = i, j

print(mv)
print(mi+1, mj+1)