def main():
    def move(ci, cj, a):
        di, dj = ds[cd]
        ci += a*di
        cj += a*dj
        poss.add((ci, cj))
        return ci, cj

    ci, cj, cd = 0, 0, 0
    poss = {(0, 0)}
    moves = input()
    for m in moves:
        if m == 'F':
            ci, cj = move(ci, cj, 1)
        elif m == 'B':
            ci, cj = move(ci, cj, -1)
        elif m == 'L':
            cd = (cd-1)%4
        elif m == 'R':
            cd = (cd+1)%4

    mni, mxi, mnj, mxj = [0]*4
    for pi, pj in poss:
        if mni > pi: mni = pi
        if mxi < pi: mxi = pi
        if mnj > pj: mnj = pj
        if mxj < pj : mxj = pj

    return (mxi-mni)*(mxj-mnj) 


N = int(input())
ds = [(-1,0),(0,1),(1,0),(0,-1)]
for _ in range(N):
    print(main())