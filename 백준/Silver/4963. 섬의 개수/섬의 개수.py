import sys
input = sys.stdin.readline
from collections import deque


def check(i, j):
    global visit
    Q = deque()
    Q.append((i, j))

    area = (-1, 0, 1)
    while Q:
        ni, nj = Q.popleft()
        if visit[ni][nj]: continue
        visit[ni][nj] = 1

        for di in area:
            for dj in area:
                si, sj = ni+di, nj+dj
                if not (0<=si<I and 0<=sj<J): continue
                if visit[si][sj]: continue
                if not mat[si][sj]: continue
                Q.append((si, sj))


while True:
    J, I = map(int, input().split())
    if J == I == 0: break

    mat = [list(map(int, input().split())) for _ in range(I)]
    visit = [[0]*J for _ in range(I)]
    cnt = 0
    for i in range(I):
        for j in range(J):
            if mat[i][j] and not visit[i][j]:
                cnt += 1
                check(i, j)
    print(cnt)