didj = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]


def f(ni, nj):
    for di, dj in didj:
        if 0 <= ni + di < L and 0 <= nj + dj < L:
            if mat[ni+di][nj+dj] != -1:
                continue

            mat[ni+di][nj+dj] = mat[ni][nj]+1
            queue.append((ni+di, nj+dj))
    return


T = int(input())
for _ in range(T):
    L = int(input())
    mat = [[-1]*L for _ in range(L)]
    ni, nj = map(int, input().split())
    ti, tj = map(int, input().split())

    mat[ni][nj] = 0
    queue = [(ni, nj)]
    start = -1
    while mat[ti][tj] == -1:
        start += 1
        ni, nj = queue[start]
        f(ni, nj)
    print(mat[ti][tj])