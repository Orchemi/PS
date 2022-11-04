import sys
sys.setrecursionlimit(250000)
input = sys.stdin.readline

def check_around(i, j):
    global dp, N, visit
    if dp[i][j]: return dp[i][j]
    visit[i][j] = 1

    cur, flag = 0, 0
    for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
        si, sj = i+di, j+dj
        if not (0<=si<N and 0<=sj<N): continue
        if mat[i][j] >= mat[si][sj]: continue
        if dp[si][sj]:
            flag = 1
            if cur < dp[si][sj]:
                cur = dp[si][sj]
            continue

        if visit[si][sj]: continue

        check_cnt = check_around(si, sj)
        if check_cnt: flag = 1
        if cur < check_cnt:
            cur = check_cnt
    dp[i][j] = cur+1 if (cur or flag) else -1
    return dp[i][j]

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
visit = [[0]*N for _ in range(N)]

maxx = 0
for i in range(N):
    for j in range(N):
        ret = check_around(i, j)
        if maxx < ret:
            maxx = ret

print(maxx+1)