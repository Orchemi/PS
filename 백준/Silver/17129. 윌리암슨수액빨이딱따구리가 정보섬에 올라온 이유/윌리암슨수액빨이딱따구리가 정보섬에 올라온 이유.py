import sys
input = sys.stdin.readline
from collections import deque

def find_start_pos():
    for i in range(I):
        for j in range(J):
            if mat[i][j]==2: return i, j

def bfs(bi, bj):
    Q = deque([(bi, bj)])
    while Q:
        i, j = Q.popleft()
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            si, sj = i+di, j+dj
            if not (0<=si<I and 0<=sj<J): continue
            if visit[si][sj]: continue
            if mat[si][sj]==1: continue
            if mat[si][sj]: return visit[i][j]
            visit[si][sj] = visit[i][j] + 1
            Q.append((si, sj))
    return 0

I, J = map(int, input().split())
mat = [list(map(int, input().strip())) for _ in range(I)]
bi, bj = find_start_pos()
visit=[[0]*J for _ in range(I)]
visit[bi][bj] = 1
ret = bfs(bi, bj)
if ret:
    print('TAK')
    print(ret)
else:
    print('NIE')