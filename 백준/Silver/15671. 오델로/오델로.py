def main():
    def make_init_mat():
        mat = [['.']*6 for _ in range(6)]
        mat[2][3] = 'B'
        mat[3][2] = 'B'
        mat[2][2] = 'W'
        mat[3][3] = 'W'
        return mat

    def flip_all(ni, nj, C):
        def check_valid(di, dj, C):
            si, sj = ni+di, nj+dj
            while True:
                if not (0<=si<6): return False
                if not (0<=sj<6): return False
                if mat[si][sj]==C: return True
                if mat[si][sj]=='.': return False
                si += di
                sj += dj

        def flip(di, dj, C):
            si, sj = ni+di, nj+dj
            while True:
                if not (0<=si<6): return
                if not (0<=sj<6): return
                if mat[si][sj]==C: return
                mat[si][sj] = C
                si += di
                sj += dj

        mat[ni][nj] = C
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if not check_valid(di, dj, C): continue
                flip(di, dj, C)


    def count(C):
        cnt = 0
        for i in range(6):
            for j in range(6):
                if mat[i][j] == C:
                    cnt += 1
        return cnt


    def show_mat(mat):
        for l in mat:
            print(*l, sep='')


    R = {'W': 'B', 'B': 'W'}
    N = int(input())
    mat = make_init_mat()
    K = 'B'
    for _ in range(N):
        ni, nj = map(int, input().split())
        flip_all(ni-1, nj-1, K)
        K = R[K]

    show_mat(mat)
    return 'White' if count('W') > count('B') else 'Black'

print(main())