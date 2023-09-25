def main():
    def show_cube(cube):
        for mat in cube:
            for l in mat:
                print(*l, sep='')

    def find_bombs():
        bombs = []
        for h in range(H):
            for i in range(I):
                for j in range(J):
                    if cube[h][i][j] == '*':
                        bombs.append((h, i, j))
        return bombs

    def check_around():
        bomb_counts = [[[0]*J for _ in range(I)] for _ in range(H)]
        for bh, bi, bj in bombs:
            for dh in range(-1, 2):
                sh = bh+dh
                if not (0<=sh<H): continue
                for di in range(-1, 2):
                    si = bi+di
                    if not (0<=si<I): continue
                    for dj in range(-1, 2):
                        sj = bj+dj
                        if not (0<=sj<J): continue
                        bomb_counts[sh][si][sj] += 1

        for h in range(H):
            for i in range(I):
                for j in range(J):
                    bomb_counts[h][i][j] %= 10

        for bh, bi, bj in bombs:
            bomb_counts[bh][bi][bj] = '*'

        return bomb_counts


    I, J, H = map(int, input().split())
    cube = [[list(input()) for _ in range(I)] for _ in range(H)]
    bombs = find_bombs()
    bomb_counts = check_around()
    show_cube(bomb_counts)

main()