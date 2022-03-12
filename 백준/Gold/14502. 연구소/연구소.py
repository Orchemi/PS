import sys
input = sys.stdin.readline

def wallsPick(i, start):
    global spaces, walls
    global cntZero

    if i == 3:
        mat2 = makeWalls(walls)
        runVirus(mat2)
        return

    for k in range(start, cntZero):
        if not visited[k]:
            visited[k] = 1
            walls.append(spaces[k])
            wallsPick(i+1, k+1)
            visited[k] = 0
            walls.pop()

def makeWalls(walls):
    mat2 = [lst[::] for lst in mat]
    for wall in walls:
        wi, wj = wall
        mat2[wi][wj] = 1
    return mat2

def runVirus(mat2):
    global viruses, H, W
    global cntZero, ans

    didj = [(-1,0), (1,0), (0,-1), (0,1)]
    virusesQ = viruses[::]
    cntZero2 = cntZero - 3
    start = -1
    end = len(virusesQ)

    while start < end - 1:
        start += 1
        vi, vj = virusesQ[start]

        for di, dj in didj:
            if 0<=vi+di<H and 0<=vj+dj<W:
                if not mat2[vi+di][vj+dj]:
                    mat2[vi+di][vj+dj] = 2
                    cntZero2 -= 1
                    virusesQ.append((vi+di, vj+dj))
                    end += 1
    ans = max(cntZero2, ans)

H, W = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(H)]

viruses = []
spaces = []
cntZero = 0
for i in range(H):
    for j in range(W):
        if mat[i][j]==2:
            viruses.append((i, j))
        elif not mat[i][j]:
            spaces.append((i, j))
            cntZero += 1

walls = []
visited = [0]*cntZero
ans = 0

wallsPick(0, 0)
print(ans)
