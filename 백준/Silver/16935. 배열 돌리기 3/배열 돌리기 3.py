def main():
    def calc1(): return mat[::-1]
    def calc2(): return [lst[::-1] for lst in mat]
    def turn(r):
        new_mat = [[0]*I for _ in range(J)]
        if r==3:
            for i in range(I):
                for j in range(J):
                    new_mat[j][I-i-1] = mat[i][j]
        elif r==4:
            for j in range(J):
                for i in range(I):
                    new_mat[J-j-1][i] = mat[i][j]
        return new_mat

    def rotate(r):
        new_mat = [[0]*J for _ in range(I)]
        II, JJ = I//2, J//2
        pos1 = [(0,0),(II,0),(II,JJ),(0,JJ)]
        if r==5:
            pos2 = [(0,JJ),(0,0),(II,0),(II,JJ)]
        if r==6:
            pos2 = [(II,0),(II,JJ),(0,JJ),(0,0)]

        for k in range(4):
            ai, aj = pos1[k]
            bi, bj = pos2[k]
            for i in range(II):
                for j in range(JJ):
                    new_mat[bi+i][bj+j] = mat[ai+i][aj+j]
        return new_mat


    I, J, R = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(I)]
    Rs = list(map(int, input().split()))
    for r in Rs:
        if r==1: mat=calc1()
        elif r==2: mat=calc2()
        elif r==3 or r==4:
            mat=turn(r)
            I, J = J, I
        else:
            mat=rotate(r)

    for l in mat:
        print(*l)

main()