import sys
input = sys.stdin.readline


def dfs(i, j, d, N):
    if i==ti and j==tj:
        global ans
        ans += 1
        return

    global mat
    # 현재 방향이 대각선
    if d=='di':
        # 대각으로 가자
        if 0<=i+1<N and 0<=j+1<N:
            if not (mat[i+1][j] or mat[i][j+1] or mat[i+1][j+1]):
                dfs(i+1, j+1, 'di', N)
        # 가로로 가자
        if 0<=j+1<N:
            if not mat[i][j+1]:
                dfs(i, j+1, 'hr', N)
        # 세로로 가자
        if 0<=i+1<N:
            if not mat[i+1][j]:
                dfs(i+1, j, 've', N)

    # 현재 방향이 가로
    elif d=='hr':
        # 대각으로 가자
        if 0<=i+1<N and 0<=j+1<N:
            if not (mat[i+1][j] or mat[i][j+1] or mat[i+1][j+1]):
                dfs(i+1, j+1, 'di', N)
        # 가로로 가자
        if 0<=j+1<N:
            if not mat[i][j+1]:
                dfs(i, j+1, 'hr', N)

    # 현재 방향이 세로
    elif d == 've':
        # 대각으로 가자
        if 0 <= i + 1 < N and 0 <= j + 1 < N:
            if not (mat[i + 1][j] or mat[i][j + 1] or mat[i + 1][j + 1]):
                dfs(i + 1, j + 1, 'di', N)
        # 세로로 가자
        if 0 <= i + 1 < N:
            if not mat[i + 1][j]:
                dfs(i + 1, j, 've', N)


N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]

ni, nj, nd = 0, 1, 'hr'
ti, tj = N-1, N-1
ans = 0
dfs(ni, nj, nd, N)
print(ans)