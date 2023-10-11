def main():
    def bfs(i, j):
        Q = {(i, j)}
        v, k = 0, 0
        while Q:
            ni, nj = Q.pop()
            if visit[ni][nj]: continue
            visit[ni][nj] = 1

            if mat[ni][nj]=='v':
                v += 1
            elif mat[ni][nj]=='k':
                k += 1

            for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                si, sj = ni+di, nj+dj
                if not (0<=si<I and 0<=sj<J): continue
                if mat[si][sj]=='#': continue
                Q.add((si, sj))
        return (k, 0) if k > v else (0, v)


    I, J = map(int, input().split())
    mat = [list(input()) for _ in range(I)]
    visit = [[0]*J for _ in range(I)]

    sheep, wolf = 0, 0
    for i in range(I):
        for j in range(J):
            if mat[i][j]=='#': continue
            if visit[i][j]: continue
            ns, nw = bfs(i, j)
            sheep += ns
            wolf += nw
    return sheep, wolf

print(*main())