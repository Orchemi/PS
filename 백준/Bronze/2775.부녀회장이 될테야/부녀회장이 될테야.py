tcs = int(input())

for tc in range(tcs):
    row = int(input())
    col = int(input())
    mat = []

    for r in range(row+1):
        mat.append([])

        for c in range(col+1):
            if r == 0:
                mat[r].append(c)
            else:
                if (c == 0) or (c == 1):
                    mat[r].append(c)
                else:
                    sum_i = 0
                    for i in range(1, c+1):
                        sum_i += mat[r-1][i]

                    mat[r].append(sum_i)

    print(mat[row][col])