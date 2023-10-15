def main():
    def bfs(i, j):
        S = {(i, j)}
        while S:
            ni, nj = S.pop()
            if visit[ni][nj]: continue
            visit[ni][nj] = 1

            for di in range(-1, 2):
                si = ni+di
                if not (0<=si<I): continue
                for dj in range(-1, 2):
                    sj = nj+dj
                    if not (0<=sj<J): continue
                    if not mat[si][sj]: continue
                    S.add((si, sj))


    I, J = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(I)]
    visit = [[0]*J for _ in range(I)]

    cnt = 0
    for i in range(I):
        for j in range(J):
            if not mat[i][j]: continue
            if visit[i][j]: continue
            cnt += 1
            bfs(i, j)

    return cnt

print(main())