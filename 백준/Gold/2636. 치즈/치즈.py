import sys
input = sys.stdin.readline

I, J = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(I)]
space = [[0]*J for _ in range(I)]
RemoveSet = set()
RemoveSet.add((0, 0))

time = 0
lastcnt = 0
while RemoveSet:
    lastcnt = len(RemoveSet)
    Q = RemoveSet
    for i, j in RemoveSet:
        mat[i][j] = 0

    RemoveSet = set()
    while Q:
        ni, nj = Q.pop()
        if space[ni][nj]: continue
        space[ni][nj] = 1

        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            si, sj = ni+di, nj+dj
            if not (0<=si<I and 0<=sj<J): continue
            if space[si][sj]: continue
            if mat[si][sj]:
                RemoveSet.add((si, sj))
                continue
            Q.add((si, sj))
    time += 1

print(time-1)
print(0 if time==1 else lastcnt)