def main():
    def draw():
        for si in range(ii, ii+II):
            mat[si][jj] = '*'
            mat[si][jj+JJ-1] = '*'

        for sj in range(jj, jj+JJ):
            mat[ii][sj] = '*'
            mat[ii+II-1][sj] = '*'

        mat[ii+1][jj+JJ-1] = ' '
        mat[ii+2][jj+JJ-2] = '*'

    N = int(input())
    if N==1:
        print("*")
        return
    
    I, J = 4*N-1, 4*N-3
    mat = [[' ']*J for _ in range(I)]

    for i in range(N-1):
        ii, jj = 2*i, 2*i
        II, JJ = I-2*ii, J-2*jj
        draw()

    for k in range(3):
        mat[2*N-2+k][2*N-2] = '*'

    for lst in mat:
        print(''.join(lst).rstrip())

main()