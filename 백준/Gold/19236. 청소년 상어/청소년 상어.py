def main():
    def copy_mat(mat):
        new_mat = [[[] for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                new_mat[i][j] = mat[i][j][:]
        return new_mat

    def make_init_mat():
        mat = [[[] for _ in range(4)] for _ in range(4)]
        for i in range(4):
            lst = list(map(int, input().split()))
            for j in range(4):
                mat[i][j] = [lst[2*j], lst[2*j+1]]
        return mat


    def move_shark(i, j, di, dj, acc, mat):
        mat = move_fishes(mat)
        si, sj = i, j
        maxx = acc
        while True:
            si, sj = si+di, sj+dj
            if not (0<=si<4 and 0<=sj<4): break
            if not mat[si][sj]: continue
            fish_score = mat[si][sj][0]
            nsi, nsj = dirs[mat[si][sj][1]]
            new_mat = copy_mat(mat)
            new_mat[i][j] = []
            new_mat[si][sj][0] = 17
            maxx = max(maxx, move_shark(si, sj, nsi, nsj, acc+fish_score, new_mat))
        return maxx


    def move_fishes(mat):
        def move_fish(k):
            fi, fj = positions[k]
            fd = mat[fi][fj][1]
            for d in range(fd, 9):
                di, dj = dirs[d]
                si, sj = fi+di, fj+dj
                if not (0<=si<4 and 0<=sj<4): continue
                if not mat[si][sj]:
                    mat[si][sj] = [k, d]
                    mat[fi][fj] = []
                    return
                if mat[si][sj][0]==17: continue
                else:
                    tk, td = mat[si][sj]
                    positions[tk] = (fi, fj)
                    positions[k] = (k, d)
                    mat[si][sj] = [k, d]
                    mat[fi][fj] = [tk, td]
                    return

            for d in range(1, fd):
                di, dj = dirs[d]
                si, sj = fi+di, fj+dj
                if not (0<=si<4 and 0<=sj<4): continue
                if not mat[si][sj]:
                    mat[si][sj] = [k, d]
                    mat[fi][fj] = []
                    return
                if mat[si][sj][0]==17: continue
                else:
                    tk, td = mat[si][sj]
                    positions[tk] = (fi, fj)
                    positions[k] = (k, d)
                    mat[si][sj] = [k, d]
                    mat[fi][fj] = [tk, td]
                    return

        positions = {}
        for i in range(4):
            for j in range(4):
                if not mat[i][j]: continue
                if mat[i][j][0] == 17: continue
                positions[mat[i][j][0]] = (i, j)

        for k in sorted(positions.keys()):
            move_fish(k)

        return mat


    dirs = ((),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1))
    mat = make_init_mat()
    init_score = mat[0][0][0]
    mat[0][0][0] = 17
    return move_shark(0, 0, *dirs[mat[0][0][1]], init_score, copy_mat(mat))

print(main())