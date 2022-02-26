N = 101
mat = [[0]*N for _ in range(N)]

mni = mnj = N
mxi = mxj = 0

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    mni = min(mni, y1, y2)
    mxi = max(mxi, y1, y2)
    mnj = min(mnj, x1, x2)
    mxj = max(mxj, x1, x2)

    for i in range(y1, y2):
        for j in range(x1, x2):
            mat[i][j] += 1

sum_v = 0
for i in range(mni, mxi+1):
    for j in range(mnj, mxj+1):
        if mat[i][j]:
            sum_v += 1

print(sum_v)