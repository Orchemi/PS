def main():
    def make_mat():
        mat = [['.']*JJ for _ in range(II)]
        for i in range(II):
            for j in range(i%2, JJ, 2):
                mat[i][j] = '#'
        return mat

    def paint_core():
        for i in range(I):
            for j in range(J):
                mat[i+u][j+l] = core[i][j]

    I, J = map(int, input().split())
    u, l, r, d = map(int, input().split())
    II, JJ = I+u+d, J+l+r
    core = [list(input()) for _ in range(I)]
    mat = make_mat()
    paint_core()
    for l in mat:
        print(*l, sep='')

main()