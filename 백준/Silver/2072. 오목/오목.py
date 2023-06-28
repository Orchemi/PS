def main():
    def SM():
        for l in mat:
            print(*l)
        print()

    def check_around(ci, cj):
        def check_dir(di, dj):
            ni, nj = ci+di, cj+dj
            cnt = 0
            while True:
                if not (0<=ni<20 and 0<=nj<20): return cnt
                if not mat[ni][nj] == mat[ci][cj]: return cnt
                cnt += 1
                ni, nj = ni+di, nj+dj


        def check_double_dir(di, dj):
            cnt = 0
            for k in (-1, 1):
                cnt += check_dir(di*k, dj*k)
            return cnt == 4

        if check_double_dir(1, 0): return True
        if check_double_dir(0, 1): return True
        if check_double_dir(1, 1): return True
        if check_double_dir(1, -1): return True
        return False

    N = int(input())
    mat = [['.']*20 for _ in range(20)]
    for n in range(1, N+1):
        i, j = map(int, input().split())
        mat[i][j] = n%2
        if check_around(i, j): return n
    return -1

print(main())