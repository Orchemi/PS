import sys
input = sys.stdin.readline

def main():
    def rotate():
        for i in range(0, TL, SL):
            for j in range(0, TL, SL):
                rotate_square(i, j)

    def rotate_square(si, sj):
        square_new = [[0]*SL for _ in range(SL)]
        for i in range(SL):
            for j in range(SL):
                square_new[i][j] = mat[si+SL-1-j][sj+i]

        for i in range(SL):
            for j in range(SL):
                mat[si+i][sj+j] = square_new[i][j]

    def remove_ice():
        del_arr = []
        for i in range(TL):
            for j in range(TL):
                if not mat[i][j]: continue
                ice_cnt = 0
                for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
                    si, sj = i+di, j+dj
                    if not (0<=si<TL and 0<=sj<TL): continue
                    if not mat[si][sj]: continue
                    ice_cnt += 1

                if ice_cnt < 3:
                    del_arr.append((i, j))

        for ki, kj in del_arr:
            mat[ki][kj] -= 1

    # 전체 얼음 양 계산
    def calc_sum_ice():
        sum_ice = 0
        for i in range(TL):
            for j in range(TL):
                sum_ice += mat[i][j]
        return sum_ice

    # 최대 얼음 크기 계산
    def calc_max_ice():
        def calc_ice(i, j):
            Q = set()
            Q.add((i, j))
            cur_ice = 0
            while Q:
                i, j = Q.pop()
                if not (0<=i<TL and 0<=j<TL): continue
                if visit[i][j] or not mat[i][j]: continue
                visit[i][j] = 1
                cur_ice += 1
                for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
                    Q.add((i+di, j+dj))
            return cur_ice

        visit = [[0]*TL for _ in range(TL)]
        max_ice = 0
        for i in range(TL):
            for j in range(TL):
                if not mat[i][j]: continue
                cur_ice = calc_ice(i, j)
                if max_ice < cur_ice:
                    max_ice = cur_ice
        return max_ice

    N, Q = map(int, input().split())
    TL = 2**N
    mat = [list(map(int, input().split())) for _ in range(TL)]
    qs = list(map(int, input().split()))
    for q in qs:
        SL = 2**q
        if q: rotate()
        remove_ice()

    print(calc_sum_ice())
    print(calc_max_ice())

main()