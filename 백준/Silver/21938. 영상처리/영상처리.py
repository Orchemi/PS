def main():
    def make_new_mat():
        new_mat = [[0]*J for _ in range(I)]
        for i in range(I):
            for j in range(J):
                tj = j*3
                ssum = mat[i][tj] + mat[i][tj+1] + mat[i][tj+2]
                if ssum >= T: new_mat[i][j] = 1
        return new_mat

    def bfs(i, j):
        S = {(i, j)}
        while S:
            i, j = S.pop()
            for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
                si, sj = i+di, j+dj
                if not (0<=si<I and 0<=sj<J): continue
                if not new_mat[si][sj]: continue
                if visit[si][sj]: continue
                visit[si][sj] = 1
                S.add((si, sj))


    I, J = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(I)]
    T = int(input())*3
    new_mat = make_new_mat()

    visit = [[0]*J for _ in range(I)]
    ret = 0
    for i in range(I):
        for j in range(J):
            if not new_mat[i][j]: continue
            if visit[i][j]: continue
            visit[i][j] = 1
            bfs(i, j)
            ret += 1
    return ret

print(main())