import sys
input = sys.stdin.readline
from collections import deque

def SM(mat):
    for l in mat:
        print(*l)
    print()

def main():
    global mat, I, J

    # N번동안 차 확인
    for _ in range(N):
        if not check_main(): return False

    # BFS
    Q = deque([(0,0)])
    mat[0][0] = 1
    while Q:
        ni, nj = Q.popleft()
        for di, dj in ((1,0),(0,1),(-1,0),(0,-1)):
            si, sj = ni+di, nj+dj
            if not (0<=si<I and 0<=sj<J): continue
            if mat[si][sj]: continue

            mat[si][sj] = mat[ni][nj]+1
            if si==I-1 and sj==J-1: return True
            Q.append((si, sj))
    return False


def check_main():
    i, j, r = map(int, input().split())
    if i+j <= r: return False
    i, j = i-1, j-1
    check_diamond(i, j, r)
    return True

def check_diamond(ci, cj, cr):
    std_step = ((0,-1),(-1,0),(0,1),(1,0))
    std_didj = ((-1,1),(1,1),(1,-1),(-1,-1))
    for idx in range(4):
        k = 0
        si, sj = std_step[idx]
        i, j = ci+si*cr, cj+sj*cr
        di, dj = std_didj[idx]
        while k <= cr:
            check_diamond_unit(i, j)
            i, j, k = i+di, j+dj, k+1


def check_diamond_unit(i, j):
    global mat, I, J
    if not (0<=i<I and 0<=j<J): return
    mat[i][j] = '*'

# 입력
I, J = map(int, input().split())
N = int(input())
mat = [[0] * J for _ in range(I)]
ret = main()
print('YES' if ret else 'NO')
if ret: print(mat[I-1][J-1]-1)