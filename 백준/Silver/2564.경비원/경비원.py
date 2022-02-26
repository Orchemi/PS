def pos23(W, H, d, x):
    if d == 1:
        return x, H
    elif d == 2:
        return x, 0
    elif d == 3:
        return 0, H-x
    elif d == 4:
        return W, H-x

def dfs(cnt, ni, nj, ti, tj):
    if ni==ti and nj==tj:
        return cnt

    global mat
    mat[ni][nj] = 0
    didj = [(-1,0), (1,0), (0,1), (0,-1)]

    for di, dj in didj:
        if 0<=ni+di<(W+1) and 0<=nj+dj<(H+1):
            if mat[ni+di][nj+dj]:
                return dfs(cnt+1, ni+di, nj+dj, ti, tj)

W, H = map(int, input().split())
L = 2*(W+H)
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
nd, nx = map(int, input().split())

mat = [[1]*(H+1)]
mat += [[1]+[0]*(H-1)+[1] for _ in range(W-1)]
mat += [[1]*(H+1)]

sum_v = 0
for d, x in lst:
    mat = [[1]*(H+1)]
    mat += [[1]+[0]*(H-1)+[1] for _ in range(W-1)]
    mat += [[1]*(H+1)]

    ni, nj = pos23(W, H, nd, nx)
    ti, tj = pos23(W, H, d, x)

    k = dfs(0, ni, nj, ti, tj)
    ans = k if L > 2*k else L-k
    sum_v += ans
print(sum_v)