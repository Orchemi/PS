import sys
input = sys.stdin.readline
from collections import deque

def bfs(ni, nj, nc):
    global mat, wCnt, bCnt
    cnt = 0
    Q = deque()
    Q.append((ni, nj))

    while Q:
        ni, nj = Q.popleft()
        if not mat[ni][nj]: continue
        mat[ni][nj] = ''
        cnt += 1
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            si, sj = ni+di, nj+dj
            if not (0<=si<I and 0<=sj<J): continue
            if not mat[si][sj]==nc: continue
            Q.append((si, sj))
    
    if nc=='W':
        wCnt += cnt**2
    else:
        bCnt += cnt**2

J, I = map(int, input().split())
mat = [list(input()) for _ in range(I)]

wCnt = bCnt = 0
for i in range(I):
    for j in range(J):
        if mat[i][j]:
            bfs(i, j, mat[i][j])

print(wCnt, bCnt)