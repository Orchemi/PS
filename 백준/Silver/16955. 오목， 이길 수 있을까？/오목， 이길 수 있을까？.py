def main():
    def check():
        for i in range(N):
            for j in range(N):
                if mat[i][j]!='X': continue
                if check_around(i, j): return 1
        return 0

    def check_around(i, j):
        for oi, oj in ((1,0),(0,1),(1,1),(-1,1)):
            for di, dj in ((oi,oj), (-oi,-oj)):
                if not (0<=i+4*di<N and 0<=j+4*dj<N): continue
                lst = [mat[i+k*di][j+k*dj] for k in range(5)]
                if check_list(lst): return 1
        return 0

    def check_list(lst):
        cnt_X = cnt_B = 0
        for v in lst:
            if v=='X': cnt_X += 1
            elif v=='.': cnt_B += 1
        return cnt_X==4 and cnt_B==1

    N = 10
    mat = [list(input()) for _ in range(N)]
    return check()

print(main())