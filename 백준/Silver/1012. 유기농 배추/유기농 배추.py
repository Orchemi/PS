import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def func(ni, nj):
    global W
    global H
    global N
    global mat

    if 0<=ni<H and 0<=nj<W:
        if mat[ni][nj]:
            mat[ni][nj]=0
            func(ni+1, nj)
            func(ni-1, nj)
            func(ni, nj+1)
            func(ni, nj-1)
    return

T = int(input())
for _ in range(T):
    W, H, N = map(int, input().split())
    mat = [[0]*W for _ in range(H)]
    for _ in range(N):
        j, i = map(int, input().split())
        mat[i][j]=1

    cnt = 0
    for i in range(H):
        for j in range(W):
            if mat[i][j]:
                func(i, j)
                cnt += 1

    print(cnt)
