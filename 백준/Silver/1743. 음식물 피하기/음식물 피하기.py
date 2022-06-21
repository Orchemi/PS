import sys
input = sys.stdin.readline

def bfs(i, j):
    global maxx, mat, I, J
    Q = set()
    Q.add((i, j))
    cnt = 1
    mat[i][j] = 0
    while Q:
        ni, nj = Q.pop()
        for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
            si, sj = ni+di, nj+dj
            if not (0<=si<I and 0<=sj<J): continue
            if mat[si][sj]:
                Q.add((si, sj))
                cnt += 1
                mat[si][sj] = 0

    maxx = max(maxx, cnt)



I, J, N = map(int, input().split())
mat = [[0]*J for _ in range(I)]
for _ in range(N):
    r, c = map(int, input().split())
    mat[r-1][c-1] = 1

maxx = 0
for i in range(I):
    for j in range(J):
        if mat[i][j]:
            bfs(i, j)

print(maxx)