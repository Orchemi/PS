from itertools import combinations
from collections import deque

def check_around(i, j):
    global I, J, origin_mat
    for di in range(-1, 2):
        for dj in range(-1, 2):
            si, sj = i+di, j+dj
            if not (0<=si<I and 0<=sj<J): continue
            if origin_mat[si][sj]==2: return 1
    return 0

def main(mat, tu1, tu2):
    global I, J, origin_mat
    now_cnt = 0
    Q = set()
    for ti, tj in (tu1, tu2):
        mat[ti][tj] = 1

    for ti, tj in (tu1, tu2):
        for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
            si, sj = ti+di, tj+dj
            if not (0<=si<I and 0<=sj<J): continue
            if mat[si][sj]==2:
                Q.add((si, sj))
    while Q:
        i, j = Q.pop()
        ret = check2(i, j)
        now_cnt += ret
    return now_cnt


def check2(i, j):
    global I, J, check, new_mat
    Q = deque([(i, j)])
    ret, pos = 0, 1
    while Q:
        ti, tj = Q.popleft()
        if check[ti][tj]: continue
        check[ti][tj] = 1
        ret += 1
        for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
            si, sj = ti+di, tj+dj
            if not (0<=si<I and 0<=sj<J): continue

            sv = new_mat[si][sj]
            if not sv: pos = 0
            if sv == 1: continue
            elif sv == 2:
                if check[si][sj]: continue
                Q.append((si, sj))

    return ret if pos else 0


I, J = map(int, input().split())
origin_mat = [list(map(int, input().split())) for _ in range(I)]
blanks = []
for i in range(I):
    for j in range(J):
        if origin_mat[i][j]: continue
        if check_around(i, j): blanks.append((i, j))

maxx = 0
for tu1, tu2 in combinations(blanks, 2):
    check = [[0]*J for _ in range(I)]
    new_mat = [l[:] for l in origin_mat]
    ret = main(new_mat, tu1, tu2)
    if maxx < ret: maxx = ret

print(maxx)