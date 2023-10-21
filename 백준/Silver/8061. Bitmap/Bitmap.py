def main():
    def find_init_starts():
        starts = set()
        for i in range(I):
            for j in range(J):
                if mat[i][j]:
                    starts.add((i, j))
        return starts

    I, J = map(int, input().split())
    mat = [list(map(int, input())) for _ in range(I)]
    visit = [[-1]*J for _ in range(I)]

    starts = find_init_starts()
    flag = 0
    while starts:
        for i, j in starts:
            visit[i][j] = flag

        new_starts = set()
        while starts:
            i, j = starts.pop()
            for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                si, sj = i+di, j+dj
                if not (0<=si<I and 0<=sj<J): continue
                if not visit[si][sj]==-1: continue
                new_starts.add((si, sj))
        flag += 1
        starts = new_starts

    for l in visit:
        print(*l)

main()