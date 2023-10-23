def main():
    def find_all_C(c):
        ret = []
        for i in range(N):
            for j in range(N):
                if mat[i][j] == c:
                    ret.append((i, j))
        return ret

    def check_Ws():
        def check_around(i, j):
            def check_one_direction(i, di, j, dj):
                cnt = 0
                si = i+di
                sj = j+dj
                while True:
                    if not (0<=si<N and 0<=sj<N): return 0
                    if mat[si][sj] == '.': return 0
                    if mat[si][sj] == 'B': return cnt
                    if mat[si][sj] == 'W':
                        cnt += 1
                        si += di
                        sj += dj

            cnts = 0
            for di, dj in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
                cnts += check_one_direction(i, di, j, dj)
            return cnts

        max_cnt = 0
        mi, mj = 0, 0
        for wi, wj in Ws:
            for di in range(-1, 2):
                si = wi+di
                if not (0<=si<N): continue
                for dj in range(-1, 2):
                    sj = wj+dj
                    if not (0<=sj<N): continue
                    if mat[si][sj] != '.': continue
                    if visited[si][sj]: continue
                    visited[si][sj] = 1
                    cur_cnt = check_around(si, sj)
                    if max_cnt < cur_cnt:
                        max_cnt = cur_cnt
                        mi, mj = si, sj

        if max_cnt:
            print(mj, mi)
            print(max_cnt)
        else:
            print('PASS')


    N = int(input())
    mat = [list(input()) for _ in range(N)]
    Ws = find_all_C('W')
    visited = [[0]*N for _ in range(N)]
    check_Ws()

main()