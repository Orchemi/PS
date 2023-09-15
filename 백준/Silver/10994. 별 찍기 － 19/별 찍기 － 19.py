N = int(input())
M = 4*(N-1)+1
mat = [[' ']*M for _ in range(M)]
for k in range(N):
    ni = nj = 2*k
    L = M - 4*k - 1
    if not L:
        mat[ni][nj] = '*'
        for l in mat:
            print(*l, sep='')

    for _ in range(L):
        mat[ni][nj] = '*'
        ni += 1
    for _ in range(L):
        mat[ni][nj] = '*'
        nj += 1
    for _ in range(L):
        mat[ni][nj] = '*'
        ni -= 1
    for _ in range(L):
        mat[ni][nj] = '*'
        nj -= 1