maxCnt = 0
I, J = map(int, input().split())
mat = [list(input()) for _ in range(I)]
visits = [[[] for _ in range(J)] for _ in range(I)]
visits[0][0].append((1, 0^(1<<(ord(mat[0][0])-65))))

cntSet = set()
Q = set()
Q.add((0, 0))

while Q:
    ni, nj = Q.pop()
    while visits[ni][nj]:
        cntNow, visit = visits[ni][nj].pop()
        needCnt = 1
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            si, sj = ni+di, nj+dj
            if not (0<=si<I and 0<=sj<J): continue
            if visit&(1<<(ord(mat[si][sj])-65)): continue
            needCnt = 0
            visits[si][sj].append((cntNow+1, visit|(1<<(ord(mat[si][sj])-65))))
            Q.add((si, sj))

        if needCnt:
            maxCnt = max(maxCnt, cntNow)
print(maxCnt)