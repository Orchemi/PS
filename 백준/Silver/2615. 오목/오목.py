def main():
    for j in range(19):
        for i in range(19):
            if mat[i][j]:
                nv = mat[i][j]
                ni, nj = i, j
                if check4(nv, ni, nj):
                    return nv, ni+1, nj+1
    return 0, 0, 0

def check4(nv, ni, nj):
    didj = [(0,1),(1,0),(1,1),(1,-1)]
    for di, dj in didj:
        if check(nv, ni, nj, di, dj) == 5:
            return 1
    return 0

def check(nv, ni, nj, di, dj):
    a = 1
    while (0<=ni-a*di<19) and (0<=nj-a*dj<19) and (mat[ni-a*di][nj-a*dj]==nv):
        a += 1
    b = 1
    while (0<=ni+b*di<19) and (0<=nj+b*dj<19) and (mat[ni+b*di][nj+b*dj]==nv):
        b += 1
    return a + b - 1

mat = [list(map(int, input().split())) for _ in range(19)]
v, i, j = main()
if v:
    print(v)
    print(i, j)
else:
    print(0)
