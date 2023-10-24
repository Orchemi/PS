def main():
    def check_around(i, j):
        S = {(i, j)}
        while S:
            i, j = S.pop()
            if visit[i][j]: continue
            visit[i][j] = 1
            for di, dj in ((1,0),(0,1)):
                si, sj = i+di, j+dj
                if not (0<=si<I and 0<=sj<J): continue
                if mat[si][sj]=='.': continue
                S.add((si, sj))

    I, J = map(int, input().split())
    mat = [list(input()) for _ in range(I)]
    visit = [[0]*J for _ in range(I)]
    cnt = 0

    for i in range(I):
        for j in range(J):
            if mat[i][j]=='.': continue
            if visit[i][j]: continue
            cnt += 1
            check_around(i, j)

    return cnt

print(main())