def make_mat():
    mat = [[0]*N for _ in range(N)]
    C = N//2
    mat[C][C] = 1

    for k in range(C+1):
        n = 2*k+1
        m = n**2
        ni = nj = C-k
        mat[ni][ni] = m

        n -= 1
        for _ in range(n):
            m -= 1
            ni += 1
            mat[ni][nj] = m

        for _ in range(n):
            m -= 1
            nj += 1
            mat[ni][nj] = m

        for _ in range(n):
            m -= 1
            ni -= 1
            mat[ni][nj] = m

        for _ in range(n-1):
            m -= 1
            nj -= 1
            mat[ni][nj] = m

    return mat

def draw_mat():
    for l in mat:
        print(*l)

def find_point():
    for i in range(N):
        for j in range(N):
            if mat[i][j] == K: return i+1, j+1


N = int(input())
K = int(input())

mat = make_mat()
draw_mat()
point = find_point()
print(*point)