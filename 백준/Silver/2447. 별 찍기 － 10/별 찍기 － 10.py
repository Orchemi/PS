def foo(ni, nj, nl):
    if nl==3:
        global mat
        for i in range(3):
            for j in range(3):
                if i==1 and j==1: continue
                mat[ni+i][nj+j]='*'
        return

    tl = nl//3
    for i in range(ni, ni+3*tl, tl):
        for j in range(nj, nj+3*tl, tl):
            if i==ni+tl and j==nj+tl: continue
            foo(i, j, tl)
    return


L = int(input())
mat = [[' ']*L for _ in range(L)]

foo(0, 0, L)

for lst in mat:
    print(*lst, sep='')