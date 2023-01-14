def main():
    I, J = map(int, input().split())
    mat = [list(input()) for _ in range(I)]
    visit = [[0]*J for _ in range(I)]

    def dfs(i, j, v):
        if not (0<=i<I and 0<=j<J): return
        if visit[i][j]: return

        vv = mat[i][j]
        if vv != v: return

        visit[i][j] = 1
        if vv=='|':
            dfs(i-1, j, vv)
            dfs(i+1, j, vv)
        else:
            dfs(i, j-1, vv)
            dfs(i, j+1, vv)
        return

    cnt = 0
    for i in range(I):
        for j in range(J):
            if visit[i][j]: continue
            dfs(i, j, mat[i][j])
            cnt += 1

    return cnt

print(main())