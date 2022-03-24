from collections import deque

def bfs():
    global mat
    Q = deque()
    Q.append((0,0))
    mat[0][0]=2

    didj = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    ti, tj = I-1, J-1
    while Q and mat[ti][tj]==1:
        ni, nj = Q.popleft()
        for di, dj in didj:
            si, sj = ni+di, nj+dj
            if not (0<=si<I and 0<=sj<J): continue
            if not mat[si][sj]==1: continue
            mat[si][sj] = mat[ni][nj]+1
            Q.append((si,sj))
    return mat[ti][tj] - 1

I, J = map(int, input().split())
mat = [list(map(int, input())) for _ in range(I)]
print(bfs())
