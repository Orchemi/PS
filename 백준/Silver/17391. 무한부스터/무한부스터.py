import sys
input = sys.stdin.readline
from collections import deque

def main():
    I, J = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(I)]
    visit = [[0]*J for _ in range(I)]
    visit[0][0] = 1
    Q = deque([(0, 0)])
    while Q:
        ni, nj = Q.popleft()
        nb = mat[ni][nj]
        for k in range(1, nb+1):
            for di, dj in ((1, 0), (0, 1)):
                si, sj = ni+di*k, nj+dj*k
                if not (0<=si<I and 0<=sj<J): continue
                if visit[si][sj]: continue
                if si==I-1 and sj==J-1: return visit[ni][nj]

                visit[si][sj] = visit[ni][nj]+1
                Q.append((si, sj))

print(main())