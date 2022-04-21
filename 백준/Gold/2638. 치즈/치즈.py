import sys
input = sys.stdin.readline
from collections import deque

def bfs(ni, nj):
    global removeQ, space
    Q = deque()
    Q.append((ni, nj))
    while Q:
        ni, nj = Q.popleft()
        if visit[ni][nj]: continue
        visit[ni][nj] = 1

        for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
            si, sj = ni+di, nj+dj
            if not (0<=si<I and 0<=sj<J): continue
            if mat[si][sj]:
                space[si][sj] += 1
                if space[si][sj] == 2:
                    removeQ.append((si, sj))
            else:
                Q.append((si, sj))


I, J = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(I)]
space = [[0]*J for _ in range(I)]
visit = [[0]*J for _ in range(I)]

removeQ = deque()
bfs(0, 0)
time = 0
while removeQ:
    for _ in range(len(removeQ)):
        ni, nj = removeQ.popleft()
        bfs(ni, nj)
    time += 1

print(time)