import sys
limit_number = 10000
sys.setrecursionlimit(limit_number)
input = sys.stdin.readline

def func(mat, C, ni, nj):
    global N

    if 0<=ni<N and 0<=nj<N:
        if mat[ni][nj]==C:
            mat[ni][nj] = 'N'
            func(mat, C, ni+1, nj)
            func(mat, C, ni-1, nj)
            func(mat, C, ni, nj+1)
            func(mat, C, ni, nj-1)
    return

N = int(input())
mat1 = [list(input()) for _ in range(N)]

mat2 = []
for lst in mat1:
    mat2.append([])
    for i in lst:
        k = 'B' if i=='B' else 'R'
        mat2[-1].append(k)

cnt1 = cnt2 = 0
for i in range(N):
    for j in range(N):
        if not mat1[i][j]=='N':
            func(mat1, mat1[i][j], i, j)
            cnt1 += 1

        if not mat2[i][j]=='N':
            func(mat2, mat2[i][j], i, j)
            cnt2 += 1

print(cnt1, cnt2)