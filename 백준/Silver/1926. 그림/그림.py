import sys
input = sys.stdin.readline
from collections import deque

def bfs(ni, nj):
    global maxArea, mat

    Q = deque()
    Q.append((ni, nj))
    cnt = 0
    while Q:
        ni, nj = Q.popleft()
        if not mat[ni][nj]: continue
        mat[ni][nj] = 0
        cnt += 1
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            si, sj = ni+di, nj+dj
            if not (0<=si<I and 0<=sj<J): continue
            if not mat[si][sj]: continue
            Q.append((si, sj))

    maxArea = max(maxArea, cnt)


I, J = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(I)]
total = 0
maxArea = 0
for i in range(I):
    for j in range(J):
        if mat[i][j]:
            total += 1
            bfs(i, j)

print(total)
print(maxArea)