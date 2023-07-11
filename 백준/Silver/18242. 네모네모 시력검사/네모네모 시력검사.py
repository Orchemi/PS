def main():
    def find_walls():
        walls = set()
        for i in range(I):
            for j in range(J):
                if mat[i][j]=='#':
                    walls.add((i, j))
        return walls

    def find_mnx():
        wis = [i for i, j in walls]
        wjs = [j for i, j in walls]
        return min(wis), min(wjs), max(wis), max(wjs)

    def find_around():
        def check(S): return '.' in S
        dirs = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        wu = {mat[mni][j] for j in range(mnj, mxj+1)}
        if check(wu): return 'UP'

        wd = {mat[mxi][j] for j in range(mnj, mxj+1)}
        if check(wd): return 'DOWN'

        wl = {mat[i][mnj] for i in range(mni, mxi+1)}
        if check(wl): return 'LEFT'

        wr = {mat[i][mxj] for i in range(mni, mxi+1)}
        if check(wr): return 'RIGHT'

    I, J = map(int, input().split())
    mat = [list(input()) for _ in range(I)]
    walls = find_walls()
    mni, mnj, mxi, mxj = find_mnx()
    return find_around()

print(main())