didj = [(-1,0),(0,1),(1,0),(0,-1)]
ci, cj = 0, 0
cd = 2
positions = [(ci, cj)]

N = int(input())
moves = input()
for m in moves:
    if m=='L':
        cd = (cd-1)%4
    elif m=='R':
        cd = (cd+1)%4
    else:
        ci, cj = ci+didj[cd][0], cj+didj[cd][1]
        positions.append((ci, cj))

mni, mnj = 0, 0
mxi, mxj = 0, 0
for pi, pj in positions:
    mni, mxi = min(mni, pi), max(mxi, pi)
    mnj, mxj = min(mnj, pj), max(mxj, pj)

I, J = mxi-mni+1, mxj-mnj+1
ret = [['#']*J for _ in range(I)]
for pi, pj in positions:
    ret[pi-mni][pj-mnj] = '.'

for lst in ret:
    print(*lst, sep='')