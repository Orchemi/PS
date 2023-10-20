def main():
    def dfs(i, j):
        cnt = 1
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            si, sj = i+di, j+dj
            if not (0<=si<3 and 0<=sj<3): continue
            if mat[si][sj]=='X': continue
            if visit[si][sj]: continue
            visit[si][sj] = 1
            cnt += dfs(si, sj)
        return cnt

    mat = [list(input()) for _ in range(3)]
    n, *arr = map(int, input().split())
    visit = [[0]*3 for _ in range(3)]
    visit[1][1] = 1

    compare = []
    for i in range(3):
        for j in range(3):
            if visit[i][j]: continue
            if mat[i][j]=='X': continue
            visit[i][j] = 1
            compare.append(dfs(i, j))
    compare.sort()
    return 1 if arr == compare else 0


T = int(input())
for _ in range(T):
    print(main())