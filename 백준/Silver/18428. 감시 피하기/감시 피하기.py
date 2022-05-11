import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations


def B_crossCheck(bi, bj):
    for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
        k = 1
        while True:
            si, sj = bi+di*k, bj+dj*k
            if not (0<=si<N and 0<=sj<N): break
            if mat[si][sj]=='T': return 1
            k += 1
    return 0

def T_crossCheckMain():
    global Ts
    for ti, tj in Ts:
        if T_crossCheck(ti, tj): return 0
    return 1

def T_crossCheck(ti, tj):
    global mat2
    for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
        k = 1
        while True:
            si, sj = ti+di*k, tj+dj*k
            if not (0<=si<N and 0<=sj<N): break
            if mat2[si][sj]=='T': break
            if mat2[si][sj]=='S':
                return 1
            k += 1
    return 0

N = int(input())
mat = [list(input().split()) for _ in range(N)]

# 1. 각 위치 리스트에 넣기
Ss = []
Ts = []
Bs = deque()
for i in range(N):
    for j in range(N):
        if mat[i][j] == 'S':
            Ss.append((i, j))
        elif mat[i][j] == 'T':
            Ts.append((i, j))
        else:
            Bs.append((i, j))

# 2. Bs에서 유효하지 않은 좌표 제거
for _ in range(len(Bs)):
    bi, bj = Bs.popleft()
    if B_crossCheck(bi, bj):
        Bs.append((bi, bj))

# 3. Bs에서 3개 뽑는 모든 경우의 수
ret = 'NO'
for comb in combinations(Bs, 3):
    mat2 = [lst[::] for lst in mat]
    for ci, cj in comb:
        mat2[ci][cj] = 'T'

    if T_crossCheckMain():
        ret = 'YES'
        break

print(ret)