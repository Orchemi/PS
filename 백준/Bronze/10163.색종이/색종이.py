import sys; input = sys.stdin.readline

T = 1001
mat = [[0]*T for _ in range(T)]
dictR = {}

mni = mnj = T
mxi = mxj = 0

N = int(input())
for k in range(1,N+1):
    ni, nj, di, dj = map(int, input().split())

    mni = min(ni, mni)
    mnj = min(nj, mnj)
    mxi = max(ni+di, mxi)
    mxj = max(nj+dj, mxj)

    for i in range(ni, ni+di):
        for j in range(nj, nj+dj):
            mat[i][j] = k

for i in range(mni, mxi):
    for j in range(mnj, mxj):
        if mat[i][j]:
            dictR[mat[i][j]] = dictR.get(mat[i][j], 0) + 1

for k in range(1, N+1):
    print(dictR.get(k, 0))