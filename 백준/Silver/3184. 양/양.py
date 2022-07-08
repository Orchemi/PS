import sys
input = sys.stdin.readline

def SM(mat):
    for l in mat:
        print(*l)
    print()

def bfs(i, j):
    global co, cv, I, J, mat, visit
    Q = set()
    Q.add((i, j))
    while Q:
        ni, nj = Q.pop()
        if visit[ni][nj]: continue
        if mat[ni][nj]=='o':
            co += 1
        elif mat[ni][nj]=='v':
            cv += 1
        visit[ni][nj] = 1
        for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
            si, sj = ni+di, nj+dj
            if not (0<=si<I and 0<=sj<J): continue
            if mat[si][sj] == '#': continue
            Q.add((si, sj))

I, J = map(int, input().split())
mat = [list(input()) for _ in range(I)]
visit = [[0]*J for _ in range(I)]
to, tv = 0, 0
for i in range(I):
    for j in range(J):
        if mat[i][j]=='#': continue
        if visit[i][j]: continue
        co, cv = 0, 0
        bfs(i, j)

        if co > cv:
            to += co
        else:
            tv += cv

print(to, tv)